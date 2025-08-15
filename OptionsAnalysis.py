#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import json
import os
import time
import math
from collections import defaultdict
import numpy as np

class CompleteOptionsAnalyzer:
    def __init__(self):
        self.results_file = "options_results.json"
        self.watchlist_file = "watchlist.json"
        print("🚀 Complete Advanced Options Analyzer initialized")
        self.load_watchlist()
   
    def save_results(self, results):
        """Save results to JSON file with proper type conversion"""
        try:
            if os.path.exists(self.results_file):
                with open(self.results_file, 'r') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        print("⚠️  Corrupted JSON file, creating new one")
                        data = []
            else:
                data = []
           
            # Convert datetime and numpy types to JSON serializable formats
            results_copy = {}
            for key, value in results.items():
                if key == 'timestamp':
                    results_copy[key] = value.isoformat()
                elif hasattr(value, 'item'):  # numpy types
                    results_copy[key] = value.item()
                elif isinstance(value, (int, float, str, bool, type(None))):
                    results_copy[key] = value
                elif isinstance(value, list):
                    # Handle lists (like support/resistance levels)
                    results_copy[key] = [float(x) if hasattr(x, 'item') else x for x in value]
                else:
                    results_copy[key] = str(value)
           
            data.append(results_copy)
           
            # Keep only last 100 results to prevent file bloat
            if len(data) > 100:
                data = data[-100:]
           
            with open(self.results_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"💾 Results saved to {self.results_file}")
           
        except Exception as e:
            print(f"⚠️  Could not save results: {e}")
   
    def load_history(self):
        """Load historical analysis results"""
        if os.path.exists(self.results_file):
            try:
                with open(self.results_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
   
    def get_top_expirations(self, ticker, max_expirations=5):
        """Find the top expirations by total volume and open interest"""
        expiration_metrics = []
       
        print(f"  🔍 Scanning {len(ticker.options)} expirations for highest activity...")
       
        for exp_date in ticker.options[:15]:  # Check first 15 to avoid too much API load
            try:
                option_chain = ticker.option_chain(exp_date)
               
                if not option_chain.calls.empty and not option_chain.puts.empty:
                    total_volume = (option_chain.calls['volume'].fillna(0).sum() +
                                  option_chain.puts['volume'].fillna(0).sum())
                    total_oi = (option_chain.calls['openInterest'].fillna(0).sum() +
                              option_chain.puts['openInterest'].fillna(0).sum())
                   
                    # Calculate days to expiration
                    exp_datetime = pd.to_datetime(exp_date)
                    days_to_exp = (exp_datetime.date() - datetime.now().date()).days
                   
                    # Weighted score: volume * 2 + OI, but boost near-term expirations
                    time_weight = 1.5 if days_to_exp <= 7 else 1.2 if days_to_exp <= 30 else 1.0
                    activity_score = (total_volume * 2 + total_oi) * time_weight
                   
                    expiration_metrics.append({
                        'date': exp_date,
                        'volume': total_volume,
                        'oi': total_oi,
                        'days_to_exp': days_to_exp,
                        'activity_score': activity_score
                    })
               
                time.sleep(0.1)  # Small delay to avoid rate limiting
               
            except Exception as e:
                continue
       
        # Sort by activity score and return top expirations
        expiration_metrics.sort(key=lambda x: x['activity_score'], reverse=True)
        top_expirations = expiration_metrics[:max_expirations]
       
        if top_expirations:
            print(f"  📊 Top {len(top_expirations)} most active expirations identified")
            for i, exp in enumerate(top_expirations, 1):
                print(f"    {i}. {exp['date']} ({exp['days_to_exp']}d): {exp['volume']:,.0f} vol, {exp['oi']:,.0f} OI")
       
        return [exp['date'] for exp in top_expirations]
   
    def calculate_max_pain(self, option_chain, current_price):
        """Calculate max pain point where most options expire worthless"""
        try:
            strikes = set(option_chain.calls['strike'].tolist() + option_chain.puts['strike'].tolist())
            pain_values = {}
           
            for strike in strikes:
                total_pain = 0
               
                # Calculate pain for calls (ITM calls cause pain to writers)
                for _, call in option_chain.calls.iterrows():
                    if strike > call['strike']:
                        total_pain += call['openInterest'] * (strike - call['strike'])
               
                # Calculate pain for puts (ITM puts cause pain to writers)
                for _, put in option_chain.puts.iterrows():
                    if strike < put['strike']:
                        total_pain += put['openInterest'] * (put['strike'] - strike)
               
                pain_values[strike] = total_pain
           
            if pain_values:
                max_pain_strike = min(pain_values.keys(), key=lambda k: pain_values[k])
                return max_pain_strike, pain_values[max_pain_strike]
            return None, None
       
        except Exception as e:
            return None, None
   
    def find_unusual_activity(self, option_chain):
        """Identify unusual options activity based on volume vs OI"""
        unusual_calls = []
        unusual_puts = []
       
        try:
            # Find options with volume > 3x average open interest and minimum volume
            for _, call in option_chain.calls.iterrows():
                if call['volume'] and call['openInterest']:
                    ratio = call['volume'] / max(call['openInterest'], 1)
                    if call['volume'] > 500 and ratio > 3:  # Minimum 500 volume, 3x OI
                        unusual_calls.append({
                            'strike': call['strike'],
                            'volume': int(call['volume']),
                            'oi': int(call['openInterest']),
                            'ratio': round(ratio, 1)
                        })
           
            for _, put in option_chain.puts.iterrows():
                if put['volume'] and put['openInterest']:
                    ratio = put['volume'] / max(put['openInterest'], 1)
                    if put['volume'] > 500 and ratio > 3:
                        unusual_puts.append({
                            'strike': put['strike'],
                            'volume': int(put['volume']),
                            'oi': int(put['openInterest']),
                            'ratio': round(ratio, 1)
                        })
       
        except Exception as e:
            pass
       
        # Sort by volume and return top 5
        unusual_calls.sort(key=lambda x: x['volume'], reverse=True)
        unusual_puts.sort(key=lambda x: x['volume'], reverse=True)
       
        return unusual_calls[:5], unusual_puts[:5]
   
    def calculate_support_resistance(self, option_chain, current_price):
        """Find key support/resistance levels based on high open interest"""
        try:
            # Combine all strikes and their total OI
            strike_oi = defaultdict(int)
           
            for _, call in option_chain.calls.iterrows():
                if call['openInterest'] > 0:
                    strike_oi[call['strike']] += call['openInterest']
           
            for _, put in option_chain.puts.iterrows():
                if put['openInterest'] > 0:
                    strike_oi[put['strike']] += put['openInterest']
           
            # Filter strikes within 20% of current price
            relevant_strikes = {k: v for k, v in strike_oi.items()
                              if abs(k - current_price) / current_price <= 0.2 and v > 1000}
           
            if not relevant_strikes:
                return [], []
           
            # Sort by OI and get top strikes
            sorted_strikes = sorted(relevant_strikes.items(), key=lambda x: x[1], reverse=True)[:5]
           
            support = [strike for strike, oi in sorted_strikes if strike < current_price]
            resistance = [strike for strike, oi in sorted_strikes if strike > current_price]
           
            return support[:3], resistance[:3]
       
        except Exception as e:
            return [], []
   
    def analyze_earnings_impact(self, ticker_obj):
        """Check if earnings are coming up"""
        try:
            calendar = ticker_obj.calendar
            if calendar is not None and not calendar.empty:
                next_earnings = calendar.index[0]
                days_to_earnings = (next_earnings.date() - datetime.now().date()).days
               
                if days_to_earnings <= 45:  # Within 45 days
                    return {
                        'earnings_date': next_earnings.strftime('%Y-%m-%d'),
                        'days_until': days_to_earnings,
                        'pre_earnings': days_to_earnings > 0
                    }
        except Exception as e:
            pass
        return None
   
    def get_sector_info(self, symbol):
        """Get sector and industry information"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            return {
                'sector': info.get('sector', 'Unknown'),
                'industry': info.get('industry', 'Unknown'),
                'beta': info.get('beta', None),
                'market_cap': info.get('marketCap', 0)
            }
        except:
            return {'sector': 'Unknown', 'industry': 'Unknown', 'beta': None, 'market_cap': 0}
   
    def analyze_symbol(self, symbol, save_result=True, detailed=True):
        """Complete enhanced analysis with top 5 most active expirations"""
        print(f"\n🔍 Analyzing {symbol}...")
        print("=" * 50)
       
        try:
            ticker = yf.Ticker(symbol)
           
            # Get current price and historical data
            hist = ticker.history(period="10d")
            if hist.empty:
                print(f"❌ No price data for {symbol}")
                return None
           
            current_price = hist['Close'].iloc[-1]
            prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
            price_change = ((current_price - prev_close) / prev_close) * 100
           
            # Calculate realized volatility
            returns = hist['Close'].pct_change().dropna()
            realized_vol = returns.std() * math.sqrt(252) * 100 if len(returns) > 1 else 0
           
            print(f"💰 Current price: ${current_price:.2f} ({price_change:+.2f}%)")
            if realized_vol > 0:
                print(f"📊 10-day realized volatility: {realized_vol:.1f}%")
           
            # Get company information
            sector_info = self.get_sector_info(symbol)
            try:
                info = ticker.info
                company_name = info.get('longName', symbol)
                market_cap = sector_info['market_cap']
                if market_cap > 1e9:
                    market_cap_str = f"${market_cap/1e9:.1f}B"
                elif market_cap > 1e6:
                    market_cap_str = f"${market_cap/1e6:.1f}M"
                else:
                    market_cap_str = f"${market_cap:,.0f}"
                print(f"🏢 {company_name} (Market Cap: {market_cap_str})")
               
                if sector_info['sector'] != 'Unknown':
                    beta_str = f", Beta: {sector_info['beta']:.2f}" if sector_info['beta'] else ""
                    print(f"🏭 {sector_info['sector']} - {sector_info['industry']}{beta_str}")
            except:
                pass
           
            # Check for upcoming earnings (always check, but only display if detailed)
            earnings_info = self.analyze_earnings_impact(ticker)
            if detailed and earnings_info:
                days_str = f"{earnings_info['days_until']} days" if earnings_info['days_until'] > 0 else "TODAY"
                print(f"📈 Earnings: {earnings_info['earnings_date']} ({days_str})")
           
            # Check options availability
            if not hasattr(ticker, 'options') or not ticker.options:
                print(f"❌ No options available for {symbol}")
                return None
           
            print(f"📅 Available expirations: {len(ticker.options)}")
           
            # Get top 5 most active expirations
            top_expirations = self.get_top_expirations(ticker, 5)
           
            if not top_expirations:
                print("❌ No valid options data found")
                return None
           
            print(f"📅 Analyzing top {len(top_expirations)} most active expirations:")
           
            # Initialize variables for analysis
            total_call_volume = 0
            total_put_volume = 0
            total_call_oi = 0
            total_put_oi = 0
            all_unusual_calls = []
            all_unusual_puts = []
            all_support = []
            all_resistance = []
            weighted_iv = 0
            total_iv_weight = 0
            max_pain_price = None
           
            expirations_analyzed = 0
           
            # Analyze the most active expirations
            for i, exp_date in enumerate(top_expirations):
                try:
                    # Calculate days to expiration for context
                    exp_datetime = pd.to_datetime(exp_date)
                    days_to_exp = (exp_datetime.date() - datetime.now().date()).days
                   
                    print(f"  📊 Processing {exp_date} ({i+1}/{len(top_expirations)}) - {days_to_exp} days...")
                    option_chain = ticker.option_chain(exp_date)
                   
                    if not option_chain.calls.empty and not option_chain.puts.empty:
                        call_vol = option_chain.calls['volume'].fillna(0).sum()
                        put_vol = option_chain.puts['volume'].fillna(0).sum()
                        call_oi = option_chain.calls['openInterest'].fillna(0).sum()
                        put_oi = option_chain.puts['openInterest'].fillna(0).sum()
                       
                        total_call_volume += call_vol
                        total_put_volume += put_vol
                        total_call_oi += call_oi
                        total_put_oi += put_oi
                       
                        # Calculate average IV for this expiration
                        call_iv = option_chain.calls['impliedVolatility'].fillna(0).mean() * 100
                        put_iv = option_chain.puts['impliedVolatility'].fillna(0).mean() * 100
                        avg_iv = (call_iv + put_iv) / 2
                       
                        # Weight by total volume for overall IV calculation
                        total_vol = call_vol + put_vol
                        if total_vol > 0:
                            weighted_iv += avg_iv * total_vol
                            total_iv_weight += total_vol
                       
                        # Enhanced display with time to expiration context
                        exp_type = ""
                        if days_to_exp == 0:
                            exp_type = " [TODAY]"
                        elif days_to_exp <= 7:
                            exp_type = " [WEEKLY]"
                        elif days_to_exp <= 30:
                            exp_type = " [MONTHLY]"
                        elif days_to_exp <= 90:
                            exp_type = " [QUARTERLY]"
                       
                        print(f"    Calls: {call_vol:,.0f} vol, {call_oi:,.0f} OI, IV: {call_iv:.1f}%{exp_type}")
                        print(f"    Puts:  {put_vol:,.0f} vol, {put_oi:,.0f} OI, IV: {put_iv:.1f}%")
                       
                        # Enhanced analysis for top 3 most active expirations
                        if detailed and i < 3:
                            print(f"    📈 Enhanced analysis for top {i+1} expiration:")
                           
                            # Max pain calculation
                            max_pain, pain_value = self.calculate_max_pain(option_chain, current_price)
                            if max_pain:
                                max_pain_price = max_pain
                                distance = abs(current_price - max_pain)
                                direction = "above" if current_price > max_pain else "below"
                                print(f"      🎯 Max Pain: ${max_pain:.2f} (${distance:.2f} {direction} current)")
                           
                            # Unusual activity detection
                            unusual_calls, unusual_puts = self.find_unusual_activity(option_chain)
                            if unusual_calls:
                                print(f"      🚨 Unusual Call Activity: {len(unusual_calls)} strikes")
                                for uc in unusual_calls[:2]:
                                    print(f"        ${uc['strike']:.0f} - {uc['volume']:,} vol ({uc['ratio']:.1f}x OI)")
                           
                            if unusual_puts:
                                print(f"      🚨 Unusual Put Activity: {len(unusual_puts)} strikes")
                                for up in unusual_puts[:2]:
                                    print(f"        ${up['strike']:.0f} - {up['volume']:,} vol ({up['ratio']:.1f}x OI)")
                           
                            all_unusual_calls.extend(unusual_calls)
                            all_unusual_puts.extend(unusual_puts)
                           
                            # Support/Resistance levels
                            support, resistance = self.calculate_support_resistance(option_chain, current_price)
                            if support or resistance:
                                print(f"      📊 Key Levels from OI:")
                                if support:
                                    support_str = ", ".join([f"${s:.0f}" for s in support[:2]])
                                    print(f"        Support: {support_str}")
                                if resistance:
                                    resistance_str = ", ".join([f"${r:.0f}" for r in resistance[:2]])
                                    print(f"        Resistance: {resistance_str}")
                           
                            all_support.extend(support)
                            all_resistance.extend(resistance)
                           
                            # Volume concentration analysis
                            total_exp_volume = call_vol + put_vol
                            volume_concentration = total_exp_volume / (total_call_volume + total_put_volume) * 100 if (total_call_volume + total_put_volume) > 0 else 0
                            if volume_concentration > 30:
                                print(f"      ⚡ High Volume Concentration: {volume_concentration:.1f}% of total volume")
                       
                        expirations_analyzed += 1
               
                except Exception as e:
                    print(f"    ⚠️  Error processing {exp_date}: {e}")
                    continue
           
            if expirations_analyzed == 0:
                print("❌ No valid options data found")
                return None
           
            # Calculate final metrics
            pcr_volume = total_put_volume / total_call_volume if total_call_volume > 0 else 0
            pcr_oi = total_put_oi / total_call_oi if total_call_oi > 0 else 0
            avg_iv = weighted_iv / total_iv_weight if total_iv_weight > 0 else 0
            iv_rv_ratio = avg_iv / realized_vol if realized_vol > 0 else None
           
            # Enhanced sentiment analysis
            sentiment_score = 0
            sentiment_factors = []
           
            # Volume-based sentiment (primary factor)
            if pcr_volume > 1.5:
                sentiment_score -= 3
                sentiment_factors.append("Very high put volume")
            elif pcr_volume > 1.2:
                sentiment_score -= 2
                sentiment_factors.append("High put volume")
            elif pcr_volume < 0.6:
                sentiment_score += 3
                sentiment_factors.append("Very high call volume")
            elif pcr_volume < 0.8:
                sentiment_score += 2
                sentiment_factors.append("High call volume")
           
            # Open Interest positioning
            if pcr_oi > 1.3:
                sentiment_score -= 1
                sentiment_factors.append("Heavy put positioning")
            elif pcr_oi < 0.7:
                sentiment_score += 1
                sentiment_factors.append("Heavy call positioning")
           
            # Unusual activity impact
            unusual_call_vol = sum([uc['volume'] for uc in all_unusual_calls])
            unusual_put_vol = sum([up['volume'] for up in all_unusual_puts])
           
            if unusual_call_vol > unusual_put_vol * 2:
                sentiment_score += 1
                sentiment_factors.append("Unusual call buying")
            elif unusual_put_vol > unusual_call_vol * 2:
                sentiment_score -= 1
                sentiment_factors.append("Unusual put buying")
           
            # IV premium/discount
            if iv_rv_ratio:
                if iv_rv_ratio > 1.5:
                    sentiment_factors.append("High IV premium")
                elif iv_rv_ratio < 0.8:
                    sentiment_factors.append("Low IV discount")
           
            # Final sentiment classification
            if sentiment_score >= 4:
                sentiment = "🟢 EXTREMELY BULLISH"
            elif sentiment_score >= 3:
                sentiment = "🟢 VERY BULLISH"
            elif sentiment_score >= 2:
                sentiment = "🟢 STRONG BULLISH"
            elif sentiment_score >= 1:
                sentiment = "🟢 BULLISH"
            elif sentiment_score <= -4:
                sentiment = "🔴 EXTREMELY BEARISH"
            elif sentiment_score <= -3:
                sentiment = "🔴 VERY BEARISH"
            elif sentiment_score <= -2:
                sentiment = "🔴 STRONG BEARISH"
            elif sentiment_score <= -1:
                sentiment = "🔴 BEARISH"
            else:
                sentiment = "🟡 NEUTRAL"
           
            # Display comprehensive results
            print(f"\n📊 COMPREHENSIVE ANALYSIS:")
            print(f"=" * 50)
            print(f"Symbol: {symbol}")
            print(f"Current Price: ${current_price:.2f} ({price_change:+.2f}%)")
            if realized_vol > 0:
                print(f"Realized Vol (10d): {realized_vol:.1f}%")
            if avg_iv > 0:
                print(f"Implied Vol (avg): {avg_iv:.1f}%")
                if iv_rv_ratio:
                    print(f"IV/RV Ratio: {iv_rv_ratio:.2f}x")
            print(f"Expirations Analyzed: {expirations_analyzed} (most active)")
           
            if detailed and (all_support or all_resistance):
                print(f"")
                print(f"📈 KEY OPTION LEVELS (from top expirations):")
                if all_support:
                    # Remove duplicates and sort
                    unique_support = sorted(set(all_support), reverse=True)[:5]
                    support_str = ", ".join([f"${s:.0f}" for s in unique_support])
                    print(f"  Support: {support_str}")
                if all_resistance:
                    unique_resistance = sorted(set(all_resistance))[:5]
                    resistance_str = ", ".join([f"${r:.0f}" for r in unique_resistance])
                    print(f"  Resistance: {resistance_str}")
                if max_pain_price:
                    print(f"  Max Pain: ${max_pain_price:.2f}")
           
            print(f"")
            print(f"📊 VOLUME & POSITIONING:")
            print(f"  Call Volume: {total_call_volume:,.0f} | Put Volume: {total_put_volume:,.0f}")
            print(f"  Call OI: {total_call_oi:,.0f} | Put OI: {total_put_oi:,.0f}")
            print(f"  P/C Volume: {pcr_volume:.3f} | P/C OI: {pcr_oi:.3f}")
           
            print(f"")
            print(f"🎯 SENTIMENT: {sentiment} (Score: {sentiment_score})")
            if sentiment_factors:
                print(f"   Key Factors: {', '.join(sentiment_factors)}")
           
            # Special alerts
            alerts = []
           
            if earnings_info and earnings_info['days_until'] <= 7:
                alerts.append(f"⚠️  EARNINGS in {earnings_info['days_until']} days - expect volatility!")
           
            if len(all_unusual_calls) + len(all_unusual_puts) >= 3:
                alerts.append(f"🚨 HIGH UNUSUAL ACTIVITY - {len(all_unusual_calls)} calls, {len(all_unusual_puts)} puts")
           
            if pcr_volume > 2.0:
                alerts.append(f"🔴 EXTREME PUT VOLUME - P/C ratio {pcr_volume:.2f}")
            elif pcr_volume < 0.4:
                alerts.append(f"🟢 EXTREME CALL VOLUME - P/C ratio {pcr_volume:.2f}")
           
            if iv_rv_ratio and iv_rv_ratio > 2.0:
                alerts.append(f"💰 HIGH IV PREMIUM - {iv_rv_ratio:.1f}x realized vol")
            elif iv_rv_ratio and iv_rv_ratio < 0.6:
                alerts.append(f"💎 LOW IV DISCOUNT - {iv_rv_ratio:.1f}x realized vol")
           
            if detailed and alerts:
                print(f"")
                for alert in alerts:
                    print(f"   {alert}")
           
            # Prepare result dictionary
            result = {
                'symbol': symbol,
                'current_price': current_price,
                'price_change_pct': price_change,
                'realized_vol': realized_vol,
                'implied_vol': avg_iv,
                'iv_rv_ratio': iv_rv_ratio,
                'sentiment': sentiment,
                'sentiment_score': sentiment_score,
                'pcr_volume': pcr_volume,
                'pcr_oi': pcr_oi,
                'total_call_volume': total_call_volume,
                'total_put_volume': total_put_volume,
                'total_call_oi': total_call_oi,
                'total_put_oi': total_put_oi,
                'unusual_call_count': len(all_unusual_calls),
                'unusual_put_count': len(all_unusual_puts),
                'support_levels': list(set(all_support))[:3] if all_support else [],
                'resistance_levels': list(set(all_resistance))[:3] if all_resistance else [],
                'max_pain': max_pain_price,
                'earnings_days': earnings_info['days_until'] if earnings_info else None,
                'sector': sector_info['sector'],
                'beta': sector_info['beta'],
                'market_cap': sector_info['market_cap'],
                'expirations_analyzed': expirations_analyzed,
                'timestamp': datetime.now()
            }
           
            if save_result:
                self.save_results(result)
           
            return result
           
        except Exception as e:
            print(f"❌ Error analyzing {symbol}: {e}")
            return None
   
    def load_watchlist(self):
        """Load saved watchlist"""
        self.watchlist = []
        if os.path.exists(self.watchlist_file):
            try:
                with open(self.watchlist_file, 'r') as f:
                    self.watchlist = json.load(f)
            except:
                self.watchlist = []
   
    def save_watchlist(self):
        """Save watchlist to file"""
        try:
            with open(self.watchlist_file, 'w') as f:
                json.dump(self.watchlist, f, indent=2)
            print(f"💾 Watchlist saved with {len(self.watchlist)} symbols")
        except Exception as e:
            print(f"⚠️  Could not save watchlist: {e}")
   
    def add_to_watchlist(self, symbol):
        """Add symbol to watchlist"""
        symbol = symbol.upper()
        if symbol not in self.watchlist:
            self.watchlist.append(symbol)
            self.save_watchlist()
            print(f"✅ Added {symbol} to watchlist")
        else:
            print(f"⚠️  {symbol} already in watchlist")
   
    def remove_from_watchlist(self, symbol):
        """Remove symbol from watchlist"""
        symbol = symbol.upper()
        if symbol in self.watchlist:
            self.watchlist.remove(symbol)
            self.save_watchlist()
            print(f"❌ Removed {symbol} from watchlist")
        else:
            print(f"⚠️  {symbol} not in watchlist")
   
    def scan_watchlist(self):
        """Scan all watchlist symbols"""
        if not self.watchlist:
            print("📭 Watchlist is empty. Add symbols with 'add SYMBOL'")
            return
       
        print(f"\n🔄 SCANNING WATCHLIST ({len(self.watchlist)} symbols)")
        print("=" * 70)
       
        results = []
        for i, symbol in enumerate(self.watchlist, 1):
            print(f"\n[{i}/{len(self.watchlist)}] Processing {symbol}...")
            result = self.analyze_symbol(symbol, save_result=False, detailed=False)
            if result:
                results.append(result)
            time.sleep(1)  # Rate limiting to avoid overwhelming the API
       
        if not results:
            print("❌ No valid results from watchlist scan")
            return
       
        # Sort by sentiment score (highest first)
        results.sort(key=lambda x: x['sentiment_score'], reverse=True)
       
        print(f"\n📊 WATCHLIST SUMMARY:")
        print("=" * 90)
        print(f"{'Rank':<4} {'Symbol':<8} {'Price':<10} {'Change':<8} {'P/C Vol':<8} {'IV':<6} {'Sentiment':<20}")
        print("-" * 90)
       
        for i, result in enumerate(results, 1):
            iv_str = f"{result['implied_vol']:.0f}%" if result['implied_vol'] else "N/A"
            print(f"{i:<4} {result['symbol']:<8} ${result['current_price']:<9.2f} "
                  f"{result['price_change_pct']:+5.1f}%  {result['pcr_volume']:<8.3f} "
                  f"{iv_str:<6} {result['sentiment']}")
   
    def compare_symbols(self, symbols):
        """Compare multiple symbols side by side"""
        print(f"\n🔄 COMPARING {len(symbols)} SYMBOLS")
        print("=" * 80)
       
        results = []
        for i, symbol in enumerate(symbols, 1):
            print(f"\n[{i}/{len(symbols)}] Analyzing {symbol}...")
            result = self.analyze_symbol(symbol, save_result=False, detailed=False)
            if result:
                results.append(result)
            time.sleep(0.5)
       
        if not results:
            print("❌ No valid results to compare")
            return
       
        # Sort by sentiment score
        results.sort(key=lambda x: x['sentiment_score'], reverse=True)
       
        print(f"\n📊 COMPARISON SUMMARY:")
        print("=" * 100)
        print(f"{'Rank':<4} {'Symbol':<8} {'Price':<10} {'Change':<8} {'P/C Vol':<8} {'IV':<6} {'Sentiment':<20}")
        print("-" * 100)
       
        for i, result in enumerate(results, 1):
            iv_str = f"{result['implied_vol']:.0f}%" if result['implied_vol'] else "N/A"
            print(f"{i:<4} {result['symbol']:<8} ${result['current_price']:<9.2f} "
                  f"{result['price_change_pct']:+5.1f}%  {result['pcr_volume']:<8.3f} "
                  f"{iv_str:<6} {result['sentiment']}")
   
    def show_history(self, limit=15):
        """Display historical results with enhanced formatting"""
        history = self.load_history()
        if not history:
            print("📭 No historical data found")
            return
       
        print(f"\n📚 RECENT ANALYSIS HISTORY (last {min(limit, len(history))})")
        print("=" * 80)
       
        for i, result in enumerate(history[-limit:], 1):
            timestamp = datetime.fromisoformat(result['timestamp'])
            iv_str = f", IV: {result['implied_vol']:.0f}%" if result.get('implied_vol') else ""
            alerts = []
           
            if result.get('earnings_days') and result['earnings_days'] <= 7:
                alerts.append("📈 EARNINGS")
            if result.get('unusual_call_count', 0) + result.get('unusual_put_count', 0) >= 3:
                alerts.append("🚨 UNUSUAL")
            if result.get('pcr_volume', 0) > 1.5 or result.get('pcr_volume', 0) < 0.5:
                alerts.append("⚡ EXTREME")
           
            alert_str = f" [{', '.join(alerts)}]" if alerts else ""
           
            print(f"{i:2d}. {result['symbol']} - ${result['current_price']:.2f} - {result['sentiment']}{alert_str}")
            print(f"    {timestamp.strftime('%Y-%m-%d %H:%M')} - P/C: {result['pcr_volume']:.3f}{iv_str}")
   
    def export_data(self, format='csv'):
        """Export analysis data to file"""
        history = self.load_history()
        if not history:
            print("📭 No data to export")
            return
       
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
       
        if format.lower() == 'csv':
            try:
                df = pd.DataFrame(history)
                filename = f"options_analysis_{timestamp}.csv"
                df.to_csv(filename, index=False)
                print(f"📊 Exported {len(history)} records to {filename}")
            except Exception as e:
                print(f"❌ Error exporting CSV: {e}")
        else:
            try:
                filename = f"options_analysis_{timestamp}.json"
                with open(filename, 'w') as f:
                    json.dump(history, f, indent=2)
                print(f"📊 Exported {len(history)} records to {filename}")
            except Exception as e:
                print(f"❌ Error exporting JSON: {e}")

def main():
    print("🚀 Complete Advanced Options Analyzer v3.0")
    print("=" * 60)
    print("💡 Enhanced Commands:")
    print("  📈 SYMBOL: Detailed analysis of any stock symbol")
    print("  🔍 'quick SYMBOL': Fast analysis (less detail)")
    print("  ⚖️  'compare AAPL,MSFT,GOOGL': Compare multiple stocks")
    print("  ➕ 'add SYMBOL': Add to watchlist")
    print("  ➖ 'remove SYMBOL': Remove from watchlist")
    print("  📋 'watchlist': Show current watchlist")
    print("  🔄 'scan': Analyze all watchlist symbols")
    print("  📚 'history [N]': View last N analysis results")
    print("  💾 'export csv|json': Export all data")
    print("  🚪 'quit': Exit analyzer")
    print("=" * 60)
   
    analyzer = CompleteOptionsAnalyzer()
   
    while True:
        try:
            watchlist_count = len(analyzer.watchlist)
            watchlist_str = f" [{watchlist_count} symbols]" if watchlist_count > 0 else ""
            user_input = input(f"\n📝 Enter command{watchlist_str}: ").strip()
           
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Thanks for using the Advanced Options Analyzer!")
                break
           
            # History command
            if user_input.lower().startswith('history'):
                try:
                    parts = user_input.split()
                    limit = int(parts[1]) if len(parts) > 1 else 15
                    analyzer.show_history(limit)
                except (ValueError, IndexError):
                    analyzer.show_history()
                continue
           
            # Watchlist commands
            if user_input.lower() == 'watchlist':
                if analyzer.watchlist:
                    print(f"\n📋 CURRENT WATCHLIST ({len(analyzer.watchlist)} symbols):")
                    for i, symbol in enumerate(analyzer.watchlist, 1):
                        print(f"  {i:2d}. {symbol}")
                else:
                    print("📭 Watchlist is empty. Use 'add SYMBOL' to add stocks.")
                continue
           
            if user_input.lower() == 'scan':
                analyzer.scan_watchlist()
                continue
           
            if user_input.lower().startswith('add '):
                try:
                    symbol = user_input.split()[1].upper()
                    analyzer.add_to_watchlist(symbol)
                except IndexError:
                    print("❌ Usage: add SYMBOL (e.g., 'add AAPL')")
                continue
           
            if user_input.lower().startswith('remove '):
                try:
                    symbol = user_input.split()[1].upper()
                    analyzer.remove_from_watchlist(symbol)
                except IndexError:
                    print("❌ Usage: remove SYMBOL (e.g., 'remove AAPL')")
                continue
           
            # Export command
            if user_input.lower().startswith('export'):
                try:
                    parts = user_input.split()
                    format_type = parts[1].lower() if len(parts) > 1 else 'csv'
                    if format_type in ['csv', 'json']:
                        analyzer.export_data(format_type)
                    else:
                        print("❌ Supported formats: csv, json")
                except Exception as e:
                    analyzer.export_data()  # Default to CSV
                continue
           
            # Compare command
            if user_input.lower().startswith('compare'):
                try:
                    symbols_part = user_input.split(' ', 1)[1]
                    symbols = [s.strip().upper() for s in symbols_part.split(',')]
                    if len(symbols) < 2:
                        print("❌ Need at least 2 symbols to compare")
                    else:
                        analyzer.compare_symbols(symbols)
                except IndexError:
                    print("❌ Usage: compare AAPL,MSFT,GOOGL")
                continue
           
            # Quick analysis command
            if user_input.lower().startswith('quick '):
                try:
                    symbol = user_input.split()[1].upper()
                    print(f"🚀 Quick analysis mode for {symbol}")
                    result = analyzer.analyze_symbol(symbol, detailed=False)
                    if result:
                        print(f"\n✅ Quick analysis complete for {symbol}!")
                        print(f"💡 Use '{symbol}' for detailed analysis with all advanced metrics")
                    else:
                        print(f"❌ Failed to analyze {symbol}")
                except IndexError:
                    print("❌ Usage: quick SYMBOL (e.g., 'quick AAPL')")
                continue
           
            # Default case - analyze symbol
            if not user_input:
                user_input = "AAPL"
                print(f"📈 Using default symbol: {user_input}")
           
            # Clean symbol input (remove any extra characters)
            symbol = ''.join(c for c in user_input.upper() if c.isalpha())
           
            if len(symbol) < 1 or len(symbol) > 5:
                print("❌ Please enter a valid stock symbol (1-5 letters)")
                continue
           
            # Perform detailed analysis
            print(f"🔬 Performing detailed analysis for {symbol}...")
            result = analyzer.analyze_symbol(symbol, detailed=True)
           
            if result:
                print(f"\n✅ Complete analysis finished for {symbol}!")
                print(f"💡 Type 'add {symbol}' to add to watchlist")
            else:
                print(f"❌ Failed to analyze {symbol}")
                print("   • Check if the symbol is correct")
                print("   • Some stocks may not have options")
                print("   • Try again or try a different symbol")
               
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print("   Please try again or restart the analyzer")

if __name__ == "__main__":
    main()
