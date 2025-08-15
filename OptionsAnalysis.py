Last login: Thu Aug 14 23:38:38 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
MacBook-Pro-7:~ walterwoo$ #!/usr/bin/env python3
MacBook-Pro-7:~ walterwoo$ 
MacBook-Pro-7:~ walterwoo$ import yfinance as yf
-bash: import: command not found
MacBook-Pro-7:~ walterwoo$ import pandas as pd
-bash: import: command not found
MacBook-Pro-7:~ walterwoo$ from datetime import datetime, timedelta
-bash: from: command not found
MacBook-Pro-7:~ walterwoo$ import json
-bash: import: command not found
MacBook-Pro-7:~ walterwoo$ import os
-bash: import: command not found
MacBook-Pro-7:~ walterwoo$ import time
-bash: import: command not found
MacBook-Pro-7:~ walterwoo$ import math
-bash: import: command not found
MacBook-Pro-7:~ walterwoo$ from collections import defaultdict
-bash: from: command not found
MacBook-Pro-7:~ walterwoo$ import numpy as np
-bash: import: command not found
MacBook-Pro-7:~ walterwoo$ 
MacBook-Pro-7:~ walterwoo$ class AdvancedOptionsAnalyzer:
-bash: class: command not found
MacBook-Pro-7:~ walterwoo$     def __init__(self):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         self.results_file = "options_results.json"
-bash: self.results_file: command not found
MacBook-Pro-7:~ walterwoo$         self.watchlist_file = "watchlist.json"
-bash: self.watchlist_file: command not found
MacBook-Pro-7:~ walterwoo$         self.alerts_file = "alerts.json"
-bash: self.alerts_file: command not found
MacBook-Pro-7:~ walterwoo$         print("🚀 Advanced Options Analyzer initialized")
-bash: syntax error near unexpected token `"🚀 Advanced Options Analyzer initialized"'
MacBook-Pro-7:~ walterwoo$         self.load_watchlist()
>     
>     def save_results(self, results):
-bash: syntax error near unexpected token `def'
MacBook-Pro-7:~ walterwoo$         """Save results to JSON file with proper type conversion"""
-bash: Save results to JSON file with proper type conversion: command not found
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             if os.path.exists(self.results_file):
-bash: syntax error near unexpected token `self.results_file'
MacBook-Pro-7:~ walterwoo$                 with open(self.results_file, 'r') as f:
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                         data = json.load(f)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     except json.JSONDecodeError:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$                         print("⚠️  Corrupted JSON file, creating new one")
-bash: syntax error near unexpected token `"⚠️  Corrupted JSON file, creating new one"'
MacBook-Pro-7:~ walterwoo$                         data = []
-bash: data: command not found
MacBook-Pro-7:~ walterwoo$             else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$                 data = []
-bash: data: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Convert datetime and numpy types to JSON serializable formats
MacBook-Pro-7:~ walterwoo$             results_copy = {}
-bash: results_copy: command not found
MacBook-Pro-7:~ walterwoo$             for key, value in results.items():
-bash: syntax error near unexpected token `value'
MacBook-Pro-7:~ walterwoo$                 if key == 'timestamp':
>                     results_copy[key] = value.isoformat()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 elif hasattr(value, 'item'):  # numpy types
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                     results_copy[key] = value.item()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 elif isinstance(value, (int, float, str, bool, type(None))):
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                     results_copy[key] = value
-bash: results_copy[key]: command not found
MacBook-Pro-7:~ walterwoo$                 else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$                     results_copy[key] = str(value)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             data.append(results_copy)
-bash: syntax error near unexpected token `results_copy'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Keep only last 100 results to prevent file bloat
MacBook-Pro-7:~ walterwoo$             if len(data) > 100:
-bash: syntax error near unexpected token `data'
MacBook-Pro-7:~ walterwoo$                 data = data[-100:]
-bash: data: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             with open(self.results_file, 'w') as f:
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 json.dump(data, f, indent=2)
-bash: syntax error near unexpected token `data,'
MacBook-Pro-7:~ walterwoo$             print(f"💾 Results saved to {self.results_file}")
-bash: syntax error near unexpected token `f"💾 Results saved to {self.results_file}"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$         except Exception as e:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$             print(f"⚠️  Could not save results: {e}")
-bash: syntax error near unexpected token `f"⚠️  Could not save results: {e}"'
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def load_history(self):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Load historical analysis results"""
-bash: Load historical analysis results: command not found
MacBook-Pro-7:~ walterwoo$         if os.path.exists(self.results_file):
-bash: syntax error near unexpected token `self.results_file'
MacBook-Pro-7:~ walterwoo$             try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                 with open(self.results_file, 'r') as f:
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     return json.load(f)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$                 return []
-bash: return: []: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         return []
-bash: return: []: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def calculate_max_pain(self, option_chain, current_price):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Calculate max pain point"""
-bash: Calculate max pain point: command not found
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             strikes = set(option_chain.calls['strike'].tolist() + option_chain.puts['strike'].tolist())
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             pain_values = {}
-bash: pain_values: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             for strike in strikes:
>                 total_pain = 0
-bash: syntax error near unexpected token `total_pain'
MacBook-Pro-7:~ walterwoo$                 
MacBook-Pro-7:~ walterwoo$                 # Calculate pain for calls
MacBook-Pro-7:~ walterwoo$                 for _, call in option_chain.calls.iterrows():
-bash: syntax error near unexpected token `call'
MacBook-Pro-7:~ walterwoo$                     if strike > call['strike']:
>                         total_pain += call['openInterest'] * (strike - call['strike'])
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 
MacBook-Pro-7:~ walterwoo$                 # Calculate pain for puts
MacBook-Pro-7:~ walterwoo$                 for _, put in option_chain.puts.iterrows():
-bash: syntax error near unexpected token `put'
MacBook-Pro-7:~ walterwoo$                     if strike < put['strike']:
>                         total_pain += put['openInterest'] * (put['strike'] - strike)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 
MacBook-Pro-7:~ walterwoo$                 pain_values[strike] = total_pain
-bash: pain_values[strike]: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             max_pain_strike = min(pain_values.keys(), key=lambda k: pain_values[k])
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             return max_pain_strike, pain_values[max_pain_strike]
-bash: return: max_pain_strike,: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         except Exception as e:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$             return None, None
-bash: return: None,: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def calculate_gamma_exposure(self, option_chain, current_price):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Estimate gamma exposure levels"""
-bash: Estimate gamma exposure levels: command not found
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             total_call_gamma = 0
-bash: total_call_gamma: command not found
MacBook-Pro-7:~ walterwoo$             total_put_gamma = 0
-bash: total_put_gamma: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             for _, call in option_chain.calls.iterrows():
-bash: syntax error near unexpected token `call'
MacBook-Pro-7:~ walterwoo$                 if call['gamma'] and not pd.isna(call['gamma']):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     total_call_gamma += call['openInterest'] * call['gamma'] * 100
-bash: total_call_gamma: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             for _, put in option_chain.puts.iterrows():
-bash: syntax error near unexpected token `put'
MacBook-Pro-7:~ walterwoo$                 if put['gamma'] and not pd.isna(put['gamma']):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     total_put_gamma += put['openInterest'] * put['gamma'] * 100 * -1  # Puts are negative gamma
-bash: total_put_gamma: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             net_gamma = total_call_gamma + total_put_gamma
-bash: net_gamma: command not found
MacBook-Pro-7:~ walterwoo$             return total_call_gamma, total_put_gamma, net_gamma
-bash: return: total_call_gamma,: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$             return None, None, None
-bash: return: None,: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def find_unusual_activity(self, option_chain):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Identify unusual options activity"""
-bash: Identify unusual options activity: command not found
MacBook-Pro-7:~ walterwoo$         unusual_calls = []
-bash: unusual_calls: command not found
MacBook-Pro-7:~ walterwoo$         unusual_puts = []
-bash: unusual_puts: command not found
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             # Find options with volume > 5x average open interest
MacBook-Pro-7:~ walterwoo$             for _, call in option_chain.calls.iterrows():
-bash: syntax error near unexpected token `call'
MacBook-Pro-7:~ walterwoo$                 if call['volume'] and call['openInterest']:
>                     if call['volume'] > max(call['openInterest'] * 5, 1000):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         unusual_calls.append({
-bash: syntax error near unexpected token `{'
MacBook-Pro-7:~ walterwoo$                             'strike': call['strike'],
-bash: strike:: command not found
MacBook-Pro-7:~ walterwoo$                             'volume': call['volume'],
-bash: volume:: command not found
MacBook-Pro-7:~ walterwoo$                             'oi': call['openInterest'],
-bash: oi:: command not found
MacBook-Pro-7:~ walterwoo$                             'ratio': call['volume'] / max(call['openInterest'], 1)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         })
-bash: syntax error near unexpected token `}'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             for _, put in option_chain.puts.iterrows():
-bash: syntax error near unexpected token `put'
MacBook-Pro-7:~ walterwoo$                 if put['volume'] and put['openInterest']:
>                     if put['volume'] > max(put['openInterest'] * 5, 1000):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         unusual_puts.append({
-bash: syntax error near unexpected token `{'
MacBook-Pro-7:~ walterwoo$                             'strike': put['strike'],
-bash: strike:: command not found
MacBook-Pro-7:~ walterwoo$                             'volume': put['volume'],
-bash: volume:: command not found
MacBook-Pro-7:~ walterwoo$                             'oi': put['openInterest'],
-bash: oi:: command not found
MacBook-Pro-7:~ walterwoo$                             'ratio': put['volume'] / max(put['openInterest'], 1)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         })
-bash: syntax error near unexpected token `}'
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$             pass
-bash: pass: command not found
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         return unusual_calls[:5], unusual_puts[:5]  # Top 5 each
-bash: return: unusual_calls[:5],: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def calculate_support_resistance(self, option_chain, current_price):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Find key support/resistance levels based on OI"""
-bash: Find key support/resistance levels based on OI: No such file or directory
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             # Combine all strikes and their total OI
MacBook-Pro-7:~ walterwoo$             strike_oi = defaultdict(int)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             for _, call in option_chain.calls.iterrows():
-bash: syntax error near unexpected token `call'
MacBook-Pro-7:~ walterwoo$                 strike_oi[call['strike']] += call['openInterest']
-bash: strike_oi[call[strike]]: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             for _, put in option_chain.puts.iterrows():
-bash: syntax error near unexpected token `put'
MacBook-Pro-7:~ walterwoo$                 strike_oi[put['strike']] += put['openInterest']
-bash: strike_oi[put[strike]]: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Find top 3 strikes by OI near current price (within 20%)
MacBook-Pro-7:~ walterwoo$             relevant_strikes = {k: v for k, v in strike_oi.items() 
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                               if abs(k - current_price) / current_price <= 0.2}
-bash: syntax error near unexpected token `k'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if not relevant_strikes:
>                 return [], []
>             
>             sorted_strikes = sorted(relevant_strikes.items(), key=lambda x: x[1], reverse=True)[:3]
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             support = [strike for strike, oi in sorted_strikes if strike < current_price]
-bash: support: command not found
MacBook-Pro-7:~ walterwoo$             resistance = [strike for strike, oi in sorted_strikes if strike > current_price]
-bash: resistance: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             return support, resistance
-bash: return: support,: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$             return [], []
-bash: return: [],: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def analyze_earnings_impact(self, ticker_obj):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Analyze if earnings are coming up and impact on options"""
-bash: Analyze if earnings are coming up and impact on options: command not found
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             calendar = ticker_obj.calendar
usage: calendar [-A days] [-a] [-B days] [-D sun|moon] [-d]
		     [-F friday] [-f calendarfile] [-l longitude]
		     [-t dd[.mm[.year]]] [-U utcoffset] [-W days]
MacBook-Pro-7:~ walterwoo$             if calendar is not None and not calendar.empty:
>                 next_earnings = calendar.index[0]
>                 days_to_earnings = (next_earnings.date() - datetime.now().date()).days
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 
MacBook-Pro-7:~ walterwoo$                 if days_to_earnings <= 30:
>                     return {
>                         'earnings_date': next_earnings.strftime('%Y-%m-%d'),
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         'days_until': days_to_earnings,
-bash: days_until:: command not found
MacBook-Pro-7:~ walterwoo$                         'pre_earnings': days_to_earnings > 0
-bash: pre_earnings:: command not found
MacBook-Pro-7:~ walterwoo$                     }
-bash: syntax error near unexpected token `}'
MacBook-Pro-7:~ walterwoo$         except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$             pass
-bash: pass: command not found
MacBook-Pro-7:~ walterwoo$         return None
-bash: return: None: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def get_sector_comparison(self, symbol):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Get sector/industry info for context"""
-bash: Get sector/industry info for context: No such file or directory
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             ticker = yf.Ticker(symbol)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             info = ticker.info
-bash: info: command not found
MacBook-Pro-7:~ walterwoo$             return {
-bash: return: {: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$                 'sector': info.get('sector', 'Unknown'),
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 'industry': info.get('industry', 'Unknown'),
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 'beta': info.get('beta', None)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             }
-bash: syntax error near unexpected token `}'
MacBook-Pro-7:~ walterwoo$         except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$             return {'sector': 'Unknown', 'industry': 'Unknown', 'beta': None}
-bash: return: {sector:: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def analyze_symbol(self, symbol, save_result=True, detailed=True):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Enhanced analysis with advanced metrics"""
-bash: Enhanced analysis with advanced metrics: command not found
MacBook-Pro-7:~ walterwoo$         print(f"\n🔍 Analyzing {symbol}...")
-bash: syntax error near unexpected token `f"\n🔍 Analyzing {symbol}..."'
MacBook-Pro-7:~ walterwoo$         print("=" * 50)
-bash: syntax error near unexpected token `"="'
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             ticker = yf.Ticker(symbol)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Get current price and historical data
MacBook-Pro-7:~ walterwoo$             hist = ticker.history(period="5d")
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             if hist.empty:
>                 print(f"❌ No price data for {symbol}")
-bash: syntax error near unexpected token `f"❌ No price data for {symbol}"'
MacBook-Pro-7:~ walterwoo$                 return None
-bash: return: None: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             current_price = hist['Close'].iloc[-1]
-bash: current_price: command not found
MacBook-Pro-7:~ walterwoo$             prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             price_change = ((current_price - prev_close) / prev_close) * 100
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Calculate volatility
MacBook-Pro-7:~ walterwoo$             returns = hist['Close'].pct_change().dropna()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             realized_vol = returns.std() * math.sqrt(252) * 100
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             print(f"💰 Current price: ${current_price:.2f} ({price_change:+.2f}%)")
-bash: syntax error near unexpected token `f"💰 Current price: ${current_price:.2f} ({price_change:+.2f}%)"'
MacBook-Pro-7:~ walterwoo$             print(f"📊 5-day realized volatility: {realized_vol:.1f}%")
-bash: syntax error near unexpected token `f"📊 5-day realized volatility: {realized_vol:.1f}%"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Get company info
MacBook-Pro-7:~ walterwoo$             try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                 info = ticker.info
-bash: info: command not found
MacBook-Pro-7:~ walterwoo$                 company_name = info.get('longName', symbol)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 market_cap = info.get('marketCap', 0)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 if market_cap > 1e9:
>                     market_cap_str = f"${market_cap/1e9:.1f}B"
>                 elif market_cap > 1e6:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                     market_cap_str = f"${market_cap/1e6:.1f}M"
-bash: market_cap_str: command not found
MacBook-Pro-7:~ walterwoo$                 else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$                     market_cap_str = f"${market_cap:,.0f}"
-bash: market_cap_str: command not found
MacBook-Pro-7:~ walterwoo$                 print(f"🏢 {company_name} (Market Cap: {market_cap_str})")
-bash: syntax error near unexpected token `f"🏢 {company_name} (Market Cap: {market_cap_str})"'
MacBook-Pro-7:~ walterwoo$             except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$                 pass
-bash: pass: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Sector context
MacBook-Pro-7:~ walterwoo$             sector_info = self.get_sector_comparison(symbol)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             if sector_info['sector'] != 'Unknown':
>                 beta_str = f", Beta: {sector_info['beta']:.2f}" if sector_info['beta'] else ""
>                 print(f"🏭 {sector_info['sector']} - {sector_info['industry']}{beta_str}")
-bash: syntax error near unexpected token `f"🏭 {sector_info['sector']} - {sector_info['industry']}{beta_str}"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Earnings check
MacBook-Pro-7:~ walterwoo$             earnings_info = self.analyze_earnings_impact(ticker)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             if earnings_info:
>                 print(f"📈 Earnings: {earnings_info['earnings_date']} ({earnings_info['days_until']} days)")
-bash: syntax error near unexpected token `f"📈 Earnings: {earnings_info['earnings_date']} ({earnings_info['days_until']} days)"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Check options availability
MacBook-Pro-7:~ walterwoo$             if not hasattr(ticker, 'options') or not ticker.options:
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 print(f"❌ No options available for {symbol}")
-bash: syntax error near unexpected token `f"❌ No options available for {symbol}"'
MacBook-Pro-7:~ walterwoo$                 return None
-bash: return: None: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             print(f"📅 Available expirations: {len(ticker.options)}")
-bash: syntax error near unexpected token `f"📅 Available expirations: {len(ticker.options)}"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Enhanced analysis
MacBook-Pro-7:~ walterwoo$             total_call_volume = 0
-bash: total_call_volume: command not found
MacBook-Pro-7:~ walterwoo$             total_put_volume = 0
-bash: total_put_volume: command not found
MacBook-Pro-7:~ walterwoo$             total_call_oi = 0
-bash: total_call_oi: command not found
MacBook-Pro-7:~ walterwoo$             total_put_oi = 0
-bash: total_put_oi: command not found
MacBook-Pro-7:~ walterwoo$             all_unusual_calls = []
-bash: all_unusual_calls: command not found
MacBook-Pro-7:~ walterwoo$             all_unusual_puts = []
-bash: all_unusual_puts: command not found
MacBook-Pro-7:~ walterwoo$             all_support = []
-bash: all_support: command not found
MacBook-Pro-7:~ walterwoo$             all_resistance = []
-bash: all_resistance: command not found
MacBook-Pro-7:~ walterwoo$             total_call_gamma = 0
-bash: total_call_gamma: command not found
MacBook-Pro-7:~ walterwoo$             total_put_gamma = 0
-bash: total_put_gamma: command not found
MacBook-Pro-7:~ walterwoo$             weighted_iv = 0
-bash: weighted_iv: command not found
MacBook-Pro-7:~ walterwoo$             total_iv_weight = 0
-bash: total_iv_weight: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             expirations_analyzed = 0
-bash: expirations_analyzed: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             for i, exp_date in enumerate(ticker.options[:3]):
-bash: syntax error near unexpected token `exp_date'
MacBook-Pro-7:~ walterwoo$                 try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                     print(f"  📊 Processing {exp_date} ({i+1}/3)...")
-bash: syntax error near unexpected token `f"  📊 Processing {exp_date} ({i+1}/3)..."'
MacBook-Pro-7:~ walterwoo$                     option_chain = ticker.option_chain(exp_date)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     
MacBook-Pro-7:~ walterwoo$                     if not option_chain.calls.empty and not option_chain.puts.empty:
>                         call_vol = option_chain.calls['volume'].sum()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         put_vol = option_chain.puts['volume'].sum()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         call_oi = option_chain.calls['openInterest'].sum()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         put_oi = option_chain.puts['openInterest'].sum()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         
MacBook-Pro-7:~ walterwoo$                         total_call_volume += call_vol
-bash: total_call_volume: command not found
MacBook-Pro-7:~ walterwoo$                         total_put_volume += put_vol
-bash: total_put_volume: command not found
MacBook-Pro-7:~ walterwoo$                         total_call_oi += call_oi
-bash: total_call_oi: command not found
MacBook-Pro-7:~ walterwoo$                         total_put_oi += put_oi
-bash: total_put_oi: command not found
MacBook-Pro-7:~ walterwoo$                         
MacBook-Pro-7:~ walterwoo$                         # Advanced analysis for first expiration only
MacBook-Pro-7:~ walterwoo$                         if detailed and i == 0:
>                             # Max pain calculation
>                             max_pain, pain_value = self.calculate_max_pain(option_chain, current_price)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                             if max_pain:
>                                 print(f"    🎯 Max Pain: ${max_pain:.2f} (${abs(current_price - max_pain):.2f} from current)")
-bash: syntax error near unexpected token `f"    🎯 Max Pain: ${max_pain:.2f} (${abs(current_price - max_pain):.2f} from current)"'
MacBook-Pro-7:~ walterwoo$                             
MacBook-Pro-7:~ walterwoo$                             # Gamma exposure
MacBook-Pro-7:~ walterwoo$                             call_gamma, put_gamma, net_gamma = self.calculate_gamma_exposure(option_chain, current_price)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                             if net_gamma is not None:
>                                 total_call_gamma += call_gamma or 0
>                                 total_put_gamma += put_gamma or 0
>                                 gamma_direction = "🟢 Positive" if net_gamma > 0 else "🔴 Negative"
>                                 print(f"    ⚡ Net Gamma Exposure: {gamma_direction} ({net_gamma:,.0f})")
-bash: syntax error near unexpected token `f"    ⚡ Net Gamma Exposure: {gamma_direction} ({net_gamma:,.0f})"'
MacBook-Pro-7:~ walterwoo$                             
MacBook-Pro-7:~ walterwoo$                             # Unusual activity
MacBook-Pro-7:~ walterwoo$                             unusual_calls, unusual_puts = self.find_unusual_activity(option_chain)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                             if unusual_calls:
>                                 print(f"    🚨 Unusual Call Activity: {len(unusual_calls)} strikes")
-bash: syntax error near unexpected token `f"    🚨 Unusual Call Activity: {len(unusual_calls)} strikes"'
MacBook-Pro-7:~ walterwoo$                                 for uc in unusual_calls[:2]:
>                                     print(f"      ${uc['strike']:.0f} - {uc['volume']:,} vol ({uc['ratio']:.1f}x OI)")
-bash: syntax error near unexpected token `print'
MacBook-Pro-7:~ walterwoo$                             
MacBook-Pro-7:~ walterwoo$                             if unusual_puts:
>                                 print(f"    🚨 Unusual Put Activity: {len(unusual_puts)} strikes")
-bash: syntax error near unexpected token `f"    🚨 Unusual Put Activity: {len(unusual_puts)} strikes"'
MacBook-Pro-7:~ walterwoo$                                 for up in unusual_puts[:2]:
>                                     print(f"      ${up['strike']:.0f} - {up['volume']:,} vol ({up['ratio']:.1f}x OI)")
-bash: syntax error near unexpected token `print'
MacBook-Pro-7:~ walterwoo$                             
MacBook-Pro-7:~ walterwoo$                             all_unusual_calls.extend(unusual_calls)
-bash: syntax error near unexpected token `unusual_calls'
MacBook-Pro-7:~ walterwoo$                             all_unusual_puts.extend(unusual_puts)
-bash: syntax error near unexpected token `unusual_puts'
MacBook-Pro-7:~ walterwoo$                             
MacBook-Pro-7:~ walterwoo$                             # Support/Resistance
MacBook-Pro-7:~ walterwoo$                             support, resistance = self.calculate_support_resistance(option_chain, current_price)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                             all_support.extend(support)
-bash: syntax error near unexpected token `support'
MacBook-Pro-7:~ walterwoo$                             all_resistance.extend(resistance)
-bash: syntax error near unexpected token `resistance'
MacBook-Pro-7:~ walterwoo$                         
MacBook-Pro-7:~ walterwoo$                         # IV calculation
MacBook-Pro-7:~ walterwoo$                         call_iv_avg = option_chain.calls['impliedVolatility'].mean() * 100
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         put_iv_avg = option_chain.puts['impliedVolatility'].mean() * 100
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         
MacBook-Pro-7:~ walterwoo$                         # Weight by volume for overall IV
MacBook-Pro-7:~ walterwoo$                         weight = call_vol + put_vol
-bash: weight: command not found
MacBook-Pro-7:~ walterwoo$                         weighted_iv += (call_iv_avg + put_iv_avg) / 2 * weight
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                         total_iv_weight += weight
-bash: total_iv_weight: command not found
MacBook-Pro-7:~ walterwoo$                         
MacBook-Pro-7:~ walterwoo$                         expirations_analyzed += 1
-bash: expirations_analyzed: command not found
MacBook-Pro-7:~ walterwoo$                         
MacBook-Pro-7:~ walterwoo$                         print(f"    Calls: {call_vol:,} vol, {call_oi:,} OI, {call_iv_avg:.1f}% IV")
-bash: syntax error near unexpected token `f"    Calls: {call_vol:,} vol, {call_oi:,} OI, {call_iv_avg:.1f}% IV"'
MacBook-Pro-7:~ walterwoo$                         print(f"    Puts:  {put_vol:,} vol, {put_oi:,} OI, {put_iv_avg:.1f}% IV")
-bash: syntax error near unexpected token `f"    Puts:  {put_vol:,} vol, {put_oi:,} OI, {put_iv_avg:.1f}% IV"'
MacBook-Pro-7:~ walterwoo$                 
MacBook-Pro-7:~ walterwoo$                 except Exception as e:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$                     print(f"    ⚠️  Error processing {exp_date}: {e}")
-bash: syntax error near unexpected token `f"    ⚠️  Error processing {exp_date}: {e}"'
MacBook-Pro-7:~ walterwoo$                     continue
-bash: continue: only meaningful in a `for', `while', or `until' loop
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if expirations_analyzed == 0:
>                 print("❌ No valid options data found")
-bash: syntax error near unexpected token `"❌ No valid options data found"'
MacBook-Pro-7:~ walterwoo$                 return None
-bash: return: None: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Calculate final metrics
MacBook-Pro-7:~ walterwoo$             pcr_volume = total_put_volume / total_call_volume if total_call_volume > 0 else 0
-bash: pcr_volume: command not found
MacBook-Pro-7:~ walterwoo$             pcr_oi = total_put_oi / total_call_oi if total_call_oi > 0 else 0
-bash: pcr_oi: command not found
MacBook-Pro-7:~ walterwoo$             avg_iv = weighted_iv / total_iv_weight if total_iv_weight > 0 else 0
-bash: avg_iv: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Enhanced sentiment analysis
MacBook-Pro-7:~ walterwoo$             sentiment_score = 0
-bash: sentiment_score: command not found
MacBook-Pro-7:~ walterwoo$             sentiment_factors = []
-bash: sentiment_factors: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Volume-based sentiment (stronger weighting)
MacBook-Pro-7:~ walterwoo$             if pcr_volume > 1.5:
>                 sentiment_score -= 3
>                 sentiment_factors.append("Very high put volume")
-bash: syntax error near unexpected token `"Very high put volume"'
MacBook-Pro-7:~ walterwoo$             elif pcr_volume > 1.2:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment_score -= 2
-bash: sentiment_score: command not found
MacBook-Pro-7:~ walterwoo$                 sentiment_factors.append("High put volume")
-bash: syntax error near unexpected token `"High put volume"'
MacBook-Pro-7:~ walterwoo$             elif pcr_volume < 0.6:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment_score += 3
-bash: sentiment_score: command not found
MacBook-Pro-7:~ walterwoo$                 sentiment_factors.append("Very high call volume")
-bash: syntax error near unexpected token `"Very high call volume"'
MacBook-Pro-7:~ walterwoo$             elif pcr_volume < 0.8:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment_score += 2
-bash: sentiment_score: command not found
MacBook-Pro-7:~ walterwoo$                 sentiment_factors.append("High call volume")
-bash: syntax error near unexpected token `"High call volume"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # OI-based sentiment
MacBook-Pro-7:~ walterwoo$             if pcr_oi > 1.2:
>                 sentiment_score -= 1
>                 sentiment_factors.append("Put-heavy positioning")
-bash: syntax error near unexpected token `"Put-heavy positioning"'
MacBook-Pro-7:~ walterwoo$             elif pcr_oi < 0.8:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment_score += 1
-bash: sentiment_score: command not found
MacBook-Pro-7:~ walterwoo$                 sentiment_factors.append("Call-heavy positioning")
-bash: syntax error near unexpected token `"Call-heavy positioning"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Unusual activity impact
MacBook-Pro-7:~ walterwoo$             if len(all_unusual_calls) > len(all_unusual_puts) * 2:
-bash: syntax error near unexpected token `all_unusual_calls'
MacBook-Pro-7:~ walterwoo$                 sentiment_score += 1
-bash: sentiment_score: command not found
MacBook-Pro-7:~ walterwoo$                 sentiment_factors.append("Unusual call activity")
-bash: syntax error near unexpected token `"Unusual call activity"'
MacBook-Pro-7:~ walterwoo$             elif len(all_unusual_puts) > len(all_unusual_calls) * 2:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment_score -= 1
-bash: sentiment_score: command not found
MacBook-Pro-7:~ walterwoo$                 sentiment_factors.append("Unusual put activity")
-bash: syntax error near unexpected token `"Unusual put activity"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # IV vs realized vol
MacBook-Pro-7:~ walterwoo$             if avg_iv > realized_vol * 1.5:
>                 sentiment_factors.append("High IV premium")
-bash: syntax error near unexpected token `"High IV premium"'
MacBook-Pro-7:~ walterwoo$             elif avg_iv < realized_vol * 0.8:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment_factors.append("Low IV discount")
-bash: syntax error near unexpected token `"Low IV discount"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Final sentiment
MacBook-Pro-7:~ walterwoo$             if sentiment_score >= 3:
>                 sentiment = "🟢 VERY BULLISH"
>             elif sentiment_score >= 2:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment = "🟢 STRONG BULLISH"
-bash: sentiment: command not found
MacBook-Pro-7:~ walterwoo$             elif sentiment_score >= 1:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment = "🟢 BULLISH"
-bash: sentiment: command not found
MacBook-Pro-7:~ walterwoo$             elif sentiment_score <= -3:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment = "🔴 VERY BEARISH"
-bash: sentiment: command not found
MacBook-Pro-7:~ walterwoo$             elif sentiment_score <= -2:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment = "🔴 STRONG BEARISH"
-bash: sentiment: command not found
MacBook-Pro-7:~ walterwoo$             elif sentiment_score <= -1:
-bash: syntax error near unexpected token `elif'
MacBook-Pro-7:~ walterwoo$                 sentiment = "🔴 BEARISH"
-bash: sentiment: command not found
MacBook-Pro-7:~ walterwoo$             else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$                 sentiment = "🟡 NEUTRAL"
-bash: sentiment: command not found
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             # Display comprehensive results
MacBook-Pro-7:~ walterwoo$             print(f"\n📊 COMPREHENSIVE ANALYSIS:")
-bash: syntax error near unexpected token `f"\n📊 COMPREHENSIVE ANALYSIS:"'
MacBook-Pro-7:~ walterwoo$             print(f"=" * 50)
-bash: syntax error near unexpected token `f"="'
MacBook-Pro-7:~ walterwoo$             print(f"Symbol: {symbol}")
-bash: syntax error near unexpected token `f"Symbol: {symbol}"'
MacBook-Pro-7:~ walterwoo$             print(f"Current Price: ${current_price:.2f} ({price_change:+.2f}%)")
-bash: syntax error near unexpected token `f"Current Price: ${current_price:.2f} ({price_change:+.2f}%)"'
MacBook-Pro-7:~ walterwoo$             print(f"Realized Vol (5d): {realized_vol:.1f}%")
-bash: syntax error near unexpected token `f"Realized Vol (5d): {realized_vol:.1f}%"'
MacBook-Pro-7:~ walterwoo$             print(f"Implied Vol (avg): {avg_iv:.1f}%")
-bash: syntax error near unexpected token `f"Implied Vol (avg): {avg_iv:.1f}%"'
MacBook-Pro-7:~ walterwoo$             print(f"IV/RV Ratio: {avg_iv/realized_vol:.2f}x" if realized_vol > 0 else "")
-bash: syntax error near unexpected token `f"IV/RV Ratio: {avg_iv/realized_vol:.2f}x"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if all_support or all_resistance:
>                 print(f"")
-bash: syntax error near unexpected token `f""'
MacBook-Pro-7:~ walterwoo$                 print(f"📈 KEY LEVELS:")
-bash: syntax error near unexpected token `f"📈 KEY LEVELS:"'
MacBook-Pro-7:~ walterwoo$                 if all_support:
>                     support_str = ", ".join([f"${s:.0f}" for s in sorted(set(all_support), reverse=True)[:3]])
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     print(f"  Support: {support_str}")
-bash: syntax error near unexpected token `f"  Support: {support_str}"'
MacBook-Pro-7:~ walterwoo$                 if all_resistance:
>                     resistance_str = ", ".join([f"${r:.0f}" for r in sorted(set(all_resistance))[:3]])
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     print(f"  Resistance: {resistance_str}")
-bash: syntax error near unexpected token `f"  Resistance: {resistance_str}"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             print(f"")
-bash: syntax error near unexpected token `f""'
MacBook-Pro-7:~ walterwoo$             print(f"📊 VOLUME & POSITIONING:")
-bash: syntax error near unexpected token `f"📊 VOLUME & POSITIONING:"'
MacBook-Pro-7:~ walterwoo$             print(f"  Call Volume: {total_call_volume:,.0f} | Put Volume: {total_put_volume:,.0f}")
-bash: syntax error near unexpected token `f"  Call Volume: {total_call_volume:,.0f} | Put Volume: {total_put_volume:,.0f}"'
MacBook-Pro-7:~ walterwoo$             print(f"  Call OI: {total_call_oi:,} | Put OI: {total_put_oi:,}")
-bash: syntax error near unexpected token `f"  Call OI: {total_call_oi:,} | Put OI: {total_put_oi:,}"'
MacBook-Pro-7:~ walterwoo$             print(f"  P/C Volume: {pcr_volume:.3f} | P/C OI: {pcr_oi:.3f}")
-bash: syntax error near unexpected token `f"  P/C Volume: {pcr_volume:.3f} | P/C OI: {pcr_oi:.3f}"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if total_call_gamma != 0 or total_put_gamma != 0:
>                 net_gamma_exposure = total_call_gamma + total_put_gamma
>                 print(f"  Net Gamma Exposure: {net_gamma_exposure:,.0f}")
-bash: syntax error near unexpected token `f"  Net Gamma Exposure: {net_gamma_exposure:,.0f}"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             print(f"")
-bash: syntax error near unexpected token `f""'
MacBook-Pro-7:~ walterwoo$             print(f"🎯 SENTIMENT: {sentiment} (Score: {sentiment_score})")
-bash: syntax error near unexpected token `f"🎯 SENTIMENT: {sentiment} (Score: {sentiment_score})"'
MacBook-Pro-7:~ walterwoo$             if sentiment_factors:
>                 print(f"   Key Factors: {', '.join(sentiment_factors)}")
-bash: syntax error near unexpected token `f"   Key Factors: {', '.join(sentiment_factors)}"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if earnings_info and earnings_info['days_until'] <= 7:
>                 print(f"")
-bash: syntax error near unexpected token `f""'
MacBook-Pro-7:~ walterwoo$                 print(f"⚠️  EARNINGS ALERT: {earnings_info['days_until']} days until earnings!")
>                 print(f"   Expect increased volatility and potential IV crush post-earnings")
-bash: syntax error near unexpected token `f"⚠
                print(f"'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             result = {
-bash: result: command not found
MacBook-Pro-7:~ walterwoo$                 'symbol': symbol,
-bash: symbol:: command not found
MacBook-Pro-7:~ walterwoo$                 'current_price': current_price,
-bash: current_price:: command not found
MacBook-Pro-7:~ walterwoo$                 'price_change_pct': price_change,
-bash: price_change_pct:: command not found
MacBook-Pro-7:~ walterwoo$                 'realized_vol': realized_vol,
-bash: realized_vol:: command not found
MacBook-Pro-7:~ walterwoo$                 'implied_vol': avg_iv,
-bash: implied_vol:: command not found
MacBook-Pro-7:~ walterwoo$                 'iv_rv_ratio': avg_iv/realized_vol if realized_vol > 0 else None,
-bash: iv_rv_ratio:: command not found
MacBook-Pro-7:~ walterwoo$                 'sentiment': sentiment,
-bash: sentiment:: command not found
MacBook-Pro-7:~ walterwoo$                 'sentiment_score': sentiment_score,
-bash: sentiment_score:: command not found
MacBook-Pro-7:~ walterwoo$                 'pcr_volume': pcr_volume,
-bash: pcr_volume:: command not found
MacBook-Pro-7:~ walterwoo$                 'pcr_oi': pcr_oi,
-bash: pcr_oi:: command not found
MacBook-Pro-7:~ walterwoo$                 'total_call_volume': total_call_volume,
-bash: total_call_volume:: command not found
MacBook-Pro-7:~ walterwoo$                 'total_put_volume': total_put_volume,
-bash: total_put_volume:: command not found
MacBook-Pro-7:~ walterwoo$                 'unusual_call_count': len(all_unusual_calls),
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 'unusual_put_count': len(all_unusual_puts),
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 'support_levels': list(set(all_support))[:3],
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 'resistance_levels': list(set(all_resistance))[:3],
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 'earnings_days': earnings_info['days_until'] if earnings_info else None,
-bash: earnings_days:: command not found
MacBook-Pro-7:~ walterwoo$                 'sector': sector_info['sector'],
-bash: sector:: command not found
MacBook-Pro-7:~ walterwoo$                 'beta': sector_info['beta'],
-bash: beta:: command not found
MacBook-Pro-7:~ walterwoo$                 'timestamp': datetime.now()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             }
-bash: syntax error near unexpected token `}'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if save_result:
>                 self.save_results(result)
-bash: syntax error near unexpected token `result'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             return result
-bash: return: result: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$         except Exception as e:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$             print(f"❌ Error analyzing {symbol}: {e}")
-bash: syntax error near unexpected token `f"❌ Error analyzing {symbol}: {e}"'
MacBook-Pro-7:~ walterwoo$             return None
-bash: return: None: numeric argument required
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def load_watchlist(self):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Load saved watchlist"""
-bash: Load saved watchlist: command not found
MacBook-Pro-7:~ walterwoo$         self.watchlist = []
-bash: self.watchlist: command not found
MacBook-Pro-7:~ walterwoo$         if os.path.exists(self.watchlist_file):
-bash: syntax error near unexpected token `self.watchlist_file'
MacBook-Pro-7:~ walterwoo$             try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                 with open(self.watchlist_file, 'r') as f:
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     self.watchlist = json.load(f)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$                 self.watchlist = []
-bash: self.watchlist: command not found
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def save_watchlist(self):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Save watchlist to file"""
-bash: Save watchlist to file: command not found
MacBook-Pro-7:~ walterwoo$         try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$             with open(self.watchlist_file, 'w') as f:
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 json.dump(self.watchlist, f, indent=2)
-bash: syntax error near unexpected token `self.watchlist,'
MacBook-Pro-7:~ walterwoo$             print(f"💾 Watchlist saved with {len(self.watchlist)} symbols")
-bash: syntax error near unexpected token `f"💾 Watchlist saved with {len(self.watchlist)} symbols"'
MacBook-Pro-7:~ walterwoo$         except Exception as e:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$             print(f"⚠️  Could not save watchlist: {e}")
-bash: syntax error near unexpected token `f"⚠️  Could not save watchlist: {e}"'
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def add_to_watchlist(self, symbol):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Add symbol to watchlist"""
-bash: Add symbol to watchlist: command not found
MacBook-Pro-7:~ walterwoo$         symbol = symbol.upper()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         if symbol not in self.watchlist:
>             self.watchlist.append(symbol)
-bash: syntax error near unexpected token `symbol'
MacBook-Pro-7:~ walterwoo$             self.save_watchlist()
>             print(f"✅ Added {symbol} to watchlist")
-bash: syntax error near unexpected token `print'
MacBook-Pro-7:~ walterwoo$         else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$             print(f"⚠️  {symbol} already in watchlist")
-bash: syntax error near unexpected token `f"⚠️  {symbol} already in watchlist"'
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def remove_from_watchlist(self, symbol):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Remove symbol from watchlist"""
-bash: Remove symbol from watchlist: command not found
MacBook-Pro-7:~ walterwoo$         symbol = symbol.upper()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         if symbol in self.watchlist:
>             self.watchlist.remove(symbol)
-bash: syntax error near unexpected token `symbol'
MacBook-Pro-7:~ walterwoo$             self.save_watchlist()
>             print(f"❌ Removed {symbol} from watchlist")
-bash: syntax error near unexpected token `print'
MacBook-Pro-7:~ walterwoo$         else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$             print(f"⚠️  {symbol} not in watchlist")
-bash: syntax error near unexpected token `f"⚠️  {symbol} not in watchlist"'
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def scan_watchlist(self):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Scan all watchlist symbols"""
-bash: Scan all watchlist symbols: command not found
MacBook-Pro-7:~ walterwoo$         if not self.watchlist:
>             print("📭 Watchlist is empty. Add symbols with 'add SYMBOL'")
-bash: syntax error near unexpected token `"📭 Watchlist is empty. Add symbols with 'add SYMBOL'"'
MacBook-Pro-7:~ walterwoo$             return
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         print(f"\n🔄 SCANNING WATCHLIST ({len(self.watchlist)} symbols)")
-bash: syntax error near unexpected token `f"\n🔄 SCANNING WATCHLIST ({len(self.watchlist)} symbols)"'
MacBook-Pro-7:~ walterwoo$         print("=" * 60)
-bash: syntax error near unexpected token `"="'
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         results = []
-bash: results: command not found
MacBook-Pro-7:~ walterwoo$         for i, symbol in enumerate(self.watchlist, 1):
-bash: syntax error near unexpected token `symbol'
MacBook-Pro-7:~ walterwoo$             print(f"\n[{i}/{len(self.watchlist)}] Processing {symbol}...")
-bash: syntax error near unexpected token `f"\n[{i}/{len(self.watchlist)}] Processing {symbol}..."'
MacBook-Pro-7:~ walterwoo$             result = self.analyze_symbol(symbol, save_result=False, detailed=False)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             if result:
>                 results.append(result)
-bash: syntax error near unexpected token `result'
MacBook-Pro-7:~ walterwoo$             time.sleep(1)  # Rate limiting
-bash: syntax error near unexpected token `1'
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         if not results:
>             print("❌ No valid results from watchlist scan")
-bash: syntax error near unexpected token `"❌ No valid results from watchlist scan"'
MacBook-Pro-7:~ walterwoo$             return
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         # Sort by sentiment score
MacBook-Pro-7:~ walterwoo$         results.sort(key=lambda x: x['sentiment_score'], reverse=True)
-bash: syntax error near unexpected token `key=lambda'
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         print(f"\n📊 WATCHLIST SUMMARY:")
-bash: syntax error near unexpected token `f"\n📊 WATCHLIST SUMMARY:"'
MacBook-Pro-7:~ walterwoo$         print("=" * 80)
-bash: syntax error near unexpected token `"="'
MacBook-Pro-7:~ walterwoo$         print(f"{'Rank':<4} {'Symbol':<8} {'Price':<10} {'Change':<8} {'P/C Vol':<8} {'IV':<6} {'Sentiment':<15}")
-bash: syntax error near unexpected token `f"{'Rank':<4} {'Symbol':<8} {'Price':<10} {'Change':<8} {'P/C Vol':<8} {'IV':<6} {'Sentiment':<15}"'
MacBook-Pro-7:~ walterwoo$         print("-" * 80)
-bash: syntax error near unexpected token `"-"'
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         for i, result in enumerate(results, 1):
-bash: syntax error near unexpected token `result'
MacBook-Pro-7:~ walterwoo$             iv_str = f"{result['implied_vol']:.0f}%" if result['implied_vol'] else "N/A"
-bash: iv_str: command not found
MacBook-Pro-7:~ walterwoo$             print(f"{i:<4} {result['symbol']:<8} ${result['current_price']:<9.2f} "
-bash: syntax error near unexpected token `f"{i:<4} {result['symbol']:<8} ${result['current_price']:<9.2f} "'
MacBook-Pro-7:~ walterwoo$                   f"{result['price_change_pct']:+5.1f}%  {result['pcr_volume']:<8.3f} "
-bash: f{result['price_change_pct']:+5.1f}%  {result['pcr_volume']:<8.3f} : command not found
MacBook-Pro-7:~ walterwoo$                   f"{iv_str:<6} {result['sentiment']}")
-bash: syntax error near unexpected token `)'
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def show_history(self, limit=10):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Display historical results with filtering"""
-bash: Display historical results with filtering: command not found
MacBook-Pro-7:~ walterwoo$         history = self.load_history()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         if not history:
>             print("📭 No historical data found")
-bash: syntax error near unexpected token `"📭 No historical data found"'
MacBook-Pro-7:~ walterwoo$             return
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         print(f"\n📚 RECENT ANALYSIS HISTORY (last {min(limit, len(history))})")
-bash: syntax error near unexpected token `f"\n📚 RECENT ANALYSIS HISTORY (last {min(limit, len(history))})"'
MacBook-Pro-7:~ walterwoo$         print("=" * 70)
-bash: syntax error near unexpected token `"="'
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         for i, result in enumerate(history[-limit:], 1):
-bash: syntax error near unexpected token `result'
MacBook-Pro-7:~ walterwoo$             timestamp = datetime.fromisoformat(result['timestamp'])
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             iv_str = f", IV: {result['implied_vol']:.0f}%" if result.get('implied_vol') else ""
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             print(f"{i:2d}. {result['symbol']} - ${result['current_price']:.2f} - {result['sentiment']}")
-bash: syntax error near unexpected token `f"{i:2d}. {result['symbol']} - ${result['current_price']:.2f} - {result['sentiment']}"'
MacBook-Pro-7:~ walterwoo$             print(f"    {timestamp.strftime('%Y-%m-%d %H:%M')} - P/C: {result['pcr_volume']:.3f}{iv_str}")
-bash: syntax error near unexpected token `f"    {timestamp.strftime('%Y-%m-%d %H:%M')} - P/C: {result['pcr_volume']:.3f}{iv_str}"'
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     def export_data(self, format='csv'):
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         """Export analysis data"""
-bash: Export analysis data: command not found
MacBook-Pro-7:~ walterwoo$         history = self.load_history()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$         if not history:
>             print("📭 No data to export")
-bash: syntax error near unexpected token `"📭 No data to export"'
MacBook-Pro-7:~ walterwoo$             return
-bash: return: can only `return' from a function or sourced script
MacBook-Pro-7:~ walterwoo$         
MacBook-Pro-7:~ walterwoo$         if format.lower() == 'csv':
-bash: syntax error near unexpected token `=='
MacBook-Pro-7:~ walterwoo$             df = pd.DataFrame(history)
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             filename = f"options_analysis_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
-bash: filename: command not found
MacBook-Pro-7:~ walterwoo$             df.to_csv(filename, index=False)
-bash: syntax error near unexpected token `filename,'
MacBook-Pro-7:~ walterwoo$             print(f"📊 Exported {len(history)} records to {filename}")
-bash: syntax error near unexpected token `f"📊 Exported {len(history)} records to {filename}"'
MacBook-Pro-7:~ walterwoo$         else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$             filename = f"options_analysis_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
-bash: filename: command not found
MacBook-Pro-7:~ walterwoo$             with open(filename, 'w') as f:
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                 json.dump(history, f, indent=2)
-bash: syntax error near unexpected token `history,'
MacBook-Pro-7:~ walterwoo$             print(f"📊 Exported {len(history)} records to {filename}")
-bash: syntax error near unexpected token `f"📊 Exported {len(history)} records to {filename}"'
MacBook-Pro-7:~ walterwoo$ 
MacBook-Pro-7:~ walterwoo$ def main():
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$     print("🚀 Advanced Options Analyzer v2.0")
-bash: syntax error near unexpected token `"🚀 Advanced Options Analyzer v2.0"'
MacBook-Pro-7:~ walterwoo$     print("=" * 50)
-bash: syntax error near unexpected token `"="'
MacBook-Pro-7:~ walterwoo$     print("Enhanced Commands:")
-bash: syntax error near unexpected token `"Enhanced Commands:"'
MacBook-Pro-7:~ walterwoo$     print("  - SYMBOL: Analyze symbol")
-bash: syntax error near unexpected token `"  - SYMBOL: Analyze symbol"'
MacBook-Pro-7:~ walterwoo$     print("  - 'compare AAPL,MSFT,GOOGL': Compare multiple")
-bash: syntax error near unexpected token `"  - 'compare AAPL,MSFT,GOOGL': Compare multiple"'
MacBook-Pro-7:~ walterwoo$     print("  - 'add SYMBOL': Add to watchlist")
-bash: syntax error near unexpected token `"  - 'add SYMBOL': Add to watchlist"'
MacBook-Pro-7:~ walterwoo$     print("  - 'remove SYMBOL': Remove from watchlist")
-bash: syntax error near unexpected token `"  - 'remove SYMBOL': Remove from watchlist"'
MacBook-Pro-7:~ walterwoo$     print("  - 'watchlist': Show watchlist")
-bash: syntax error near unexpected token `"  - 'watchlist': Show watchlist"'
MacBook-Pro-7:~ walterwoo$     print("  - 'scan': Scan all watchlist symbols")
-bash: syntax error near unexpected token `"  - 'scan': Scan all watchlist symbols"'
MacBook-Pro-7:~ walterwoo$     print("  - 'history [N]': View last N results")
-bash: syntax error near unexpected token `"  - 'history [N]': View last N results"'
MacBook-Pro-7:~ walterwoo$     print("  - 'export csv|json': Export data")
-bash: syntax error near unexpected token `"  - 'export csv|json': Export data"'
MacBook-Pro-7:~ walterwoo$     print("  - 'quick SYMBOL': Fast analysis (no advanced metrics)")
-bash: syntax error near unexpected token `"  - 'quick SYMBOL': Fast analysis (no advanced metrics)"'
MacBook-Pro-7:~ walterwoo$     print("  - 'quit': Exit")
-bash: syntax error near unexpected token `"  - 'quit': Exit"'
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     analyzer = AdvancedOptionsAnalyzer()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$     
MacBook-Pro-7:~ walterwoo$     while True:
>         try:
>             user_input = input(f"\n📝 Enter command [{len(analyzer.watchlist)} in watchlist]: ").strip()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if user_input.lower() in ['quit', 'exit', 'q']:
-bash: syntax error near unexpected token `in'
MacBook-Pro-7:~ walterwoo$                 print("👋 Goodbye!")
>                 break
>             
>             if user_input.lower().startswith('history'):
>                 try:
>                     limit = int(user_input.split()[1]) if len(user_input.split()) > 1 else 10
>                     analyzer.show_history(limit)
>                 except:
>                     analyzer.show_history()
>                 continue
>             
>             if user_input.lower() == 'watchlist':
>                 if analyzer.watchlist:
>                     print(f"\n📋 WATCHLIST ({len(analyzer.watchlist)} symbols):")
-bash: syntax error near unexpected token `"👋
                break
            
            if user_input.lower().startswith('history'):
                try:
                    limit = int(user_input.split()[1]) if len(user_input.split()) > 1 else 10
                    analyzer.show_history(limit)
                except:
                    analyzer.show_history()
                continue
            
            if user_input.lower() == 'watchlist':
                if analyzer.watchlist:
                    print(f"\n📋'
MacBook-Pro-7:~ walterwoo$                     for i, symbol in enumerate(analyzer.watchlist, 1):
-bash: syntax error near unexpected token `symbol'
MacBook-Pro-7:~ walterwoo$                         print(f"  {i}. {symbol}")
-bash: syntax error near unexpected token `f"  {i}. {symbol}"'
MacBook-Pro-7:~ walterwoo$                 else:
-bash: else:: command not found
MacBook-Pro-7:~ walterwoo$                     print("📭 Watchlist is empty")
-bash: syntax error near unexpected token `"📭 Watchlist is empty"'
MacBook-Pro-7:~ walterwoo$                 continue
-bash: continue: only meaningful in a `for', `while', or `until' loop
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if user_input.lower() == 'scan':
-bash: syntax error near unexpected token `=='
MacBook-Pro-7:~ walterwoo$                 analyzer.scan_watchlist()
>                 continue
-bash: syntax error near unexpected token `continue'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if user_input.lower().startswith('add '):
-bash: syntax error near unexpected token `.startswith'
MacBook-Pro-7:~ walterwoo$                 try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                     symbol = user_input.split()[1].upper()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     analyzer.add_to_watchlist(symbol)
-bash: syntax error near unexpected token `symbol'
MacBook-Pro-7:~ walterwoo$                 except IndexError:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$                     print("❌ Usage: add SYMBOL")
-bash: syntax error near unexpected token `"❌ Usage: add SYMBOL"'
MacBook-Pro-7:~ walterwoo$                 continue
-bash: continue: only meaningful in a `for', `while', or `until' loop
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if user_input.lower().startswith('remove '):
-bash: syntax error near unexpected token `.startswith'
MacBook-Pro-7:~ walterwoo$                 try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                     symbol = user_input.split()[1].upper()
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     analyzer.remove_from_watchlist(symbol)
-bash: syntax error near unexpected token `symbol'
MacBook-Pro-7:~ walterwoo$                 except IndexError:
-bash: except: command not found
MacBook-Pro-7:~ walterwoo$                     print("❌ Usage: remove SYMBOL")
-bash: syntax error near unexpected token `"❌ Usage: remove SYMBOL"'
MacBook-Pro-7:~ walterwoo$                 continue
-bash: continue: only meaningful in a `for', `while', or `until' loop
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if user_input.lower().startswith('export'):
-bash: syntax error near unexpected token `.startswith'
MacBook-Pro-7:~ walterwoo$                 try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                     format_type = user_input.split()[1] if len(user_input.split()) > 1 else 'csv'
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     analyzer.export_data(format_type)
-bash: syntax error near unexpected token `format_type'
MacBook-Pro-7:~ walterwoo$                 except:
-bash: except:: command not found
MacBook-Pro-7:~ walterwoo$                     analyzer.export_data()
>                 continue
-bash: syntax error near unexpected token `continue'
MacBook-Pro-7:~ walterwoo$             
MacBook-Pro-7:~ walterwoo$             if user_input.lower().startswith('compare'):
-bash: syntax error near unexpected token `.startswith'
MacBook-Pro-7:~ walterwoo$                 try:
-bash: try:: command not found
MacBook-Pro-7:~ walterwoo$                     symbols_part = user_input.split(' ', 1)[1]
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     symbols = [s.strip().upper() for s in symbols_part.split(',')]
-bash: syntax error near unexpected token `('
MacBook-Pro-7:~ walterwoo$                     print(f"\n🔄 COMPARING {len(symbols)} SYMBOLS")
-bash: syntax error near unexpected token `f"\n🔄 COMPARING {len(symbols)} SYMBOLS"'
MacBook-Pro-7:~ walterwoo$                     print("=" * 60)
-bash: syntax error near unexpected token `"="'
MacBook-Pro-7:~ walterwoo$                     
MacBook-Pro-7:~ walterwoo$                     results = []
-bash: results: command not found
MacBook-Pro-7:~ walterwoo$                     for symbol in symbols:
>                         result = analyzer.analyze_symbol(symbol, save_result=False, detailed=False)
-bash: syntax error near unexpected token `result'
MacBook-Pro-7:~ walterwoo$                         if result:
>                             results.append(result)
-bash: syntax error near unexpected token `result'
MacBook-Pro-7:~ walterwoo$                         time.sleep(0.5)
-bash: syntax error near unexpected token `0.5'
MacBook-Pro-7:~ walterwoo$                     
MacBook-Pro-7:~ walterwoo$                     if results:
>                         results.sort(key=lambda x: x['sentiment_score'], reverse=True)
-bash: syntax error near unexpected token `key=lambda'
MacBook-Pro-7:~ walterwoo$                         print(f"\n📊 COMPARISON SUMMARY:")
-bash: syntax error near unexpected token `f"\n📊 COMPARISON SUMMARY:"'
MacBook-Pro-7:~ walterwoo$                         print("=" * 80)
-bash: syntax error near unexpected token `"="'
MacBook-Pro-7:~ walterwoo$                         print(f"{'Rank':<4} {'Symbol':<8} {'Price':<10} {'P/C Vol':<8} {'IV':<6} {'Sentiment':<15}")
-bash: syntax error near unexpected token `f"{'Rank':<4} {'Symbol':<8} {'Price':<10} {'P/C Vol':<8} {'IV':<6} {'Sentiment':<15}"'
MacBook-Pro-7:~ walterwoo$                         print("-" * 80)
-bash: syntax error near unexpected token `"-"'
MacBook-Pro-7:~ walterwoo$                         
MacBook-Pro-7:~ walterwoo$                         for i, result in enumerate(results, 1):
-bash: syntax error near unexpected token `result'
MacBook-Pro-7:~ walterwoo$                             iv_str = f"{result['implied_vol']:.0f}%" if result['implied_vol'] else "N/A"
-bash: iv_str: command not found
MacBook-Pro-7:~ walterwoo$                             print(f"{i:<4} {result['symbol']:<8} ${result['current_price']
> # Save the enhanced code to a new file
> nano advanced_options_analyzer.py
> # Paste the enhanced code, then Ctrl+X, Y, Enter
> 
> # Run the enhanced version
> python advanced_options_analyzer.py
> 
> exit()
> # Try python3 instead of python
> python3 --version
> 
> # Or try these alternatives
> which python3
> which python
> >>exit
> 
> ls -la /usr/bin/python*
> ls -la /usr/local/bin/python*
> 
> pwd
> 
MacBook-Pro-7:~ walterwoo$ # Create a new file
MacBook-Pro-7:~ walterwoo$ nano advanced_options_analyzer.py
MacBook-Pro-7:~ walterwoo$ python advanced_options_analyzer.py
-bash: python: command not found
MacBook-Pro-7:~ walterwoo$ ls -la *.py
-rw-r--r--  1 walterwoo  staff  14469 Aug 15 10:58 advanced_options_analyzer.py
-rw-r--r--  1 walterwoo  staff  10399 Aug 14 22:15 enhanced_options_analyzer.py
-rw-r--r--  1 walterwoo  staff   1873 Aug 14 21:41 options_analysis.py
-rw-r--r--  1 walterwoo  staff  30173 Aug 15 10:48 options_analyzer.py
MacBook-Pro-7:~ walterwoo$ ls -la options_analyzer.py
-rw-r--r--  1 walterwoo  staff  30173 Aug 15 10:48 options_analyzer.py
MacBook-Pro-7:~ walterwoo$ python options_analyzer.py
-bash: python: command not found
MacBook-Pro-7:~ walterwoo$ head -10 options_analyzer.py
#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import json
import os
import time
import math
from collections import defaultdict
MacBook-Pro-7:~ walterwoo$ python enhanced_options_analyzer.py
-bash: python: command not found
MacBook-Pro-7:~ walterwoo$ nano enhanced_options_analyzer.py
MacBook-Pro-7:~ walterwoo$ python enhanced_options_analyzer.py
-bash: python: command not found
MacBook-Pro-7:~ walterwoo$ rm options_results.json
MacBook-Pro-7:~ walterwoo$ python enhanced_options_analyzer.py
-bash: python: command not found
MacBook-Pro-7:~ walterwoo$ head -5 options_analyzer.py
#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
MacBook-Pro-7:~ walterwoo$ rm options_analyzer.py
MacBook-Pro-7:~ walterwoo$ nano options_analyzer.py
MacBook-Pro-7:~ walterwoo$ python options_analyzer.py
-bash: python: command not found
MacBook-Pro-7:~ walterwoo$ python enhanced_options_analyzer.py
-bash: python: command not found
MacBook-Pro-7:~ walterwoo$ # Use python3 instead of python
MacBook-Pro-7:~ walterwoo$ python3 enhanced_options_analyzer.py
  File "/Users/walterwoo/enhanced_options_analyzer.py", line 378
    main()import yfinance as yf
          ^^^^^^
SyntaxError: invalid syntax
MacBook-Pro-7:~ walterwoo$ which python3
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
MacBook-Pro-7:~ walterwoo$ source options_env/bin/activate
(options_env) MacBook-Pro-7:~ walterwoo$ pip list | grep yfinance
yfinance           0.2.65
(options_env) MacBook-Pro-7:~ walterwoo$ pip install yfinance pandas
Requirement already satisfied: yfinance in ./options_env/lib/python3.13/site-packages (0.2.65)
Requirement already satisfied: pandas in ./options_env/lib/python3.13/site-packages (2.3.1)
Requirement already satisfied: numpy>=1.16.5 in ./options_env/lib/python3.13/site-packages (from yfinance) (2.3.2)
Requirement already satisfied: requests>=2.31 in ./options_env/lib/python3.13/site-packages (from yfinance) (2.32.4)
Requirement already satisfied: multitasking>=0.0.7 in ./options_env/lib/python3.13/site-packages (from yfinance) (0.0.12)
Requirement already satisfied: platformdirs>=2.0.0 in ./options_env/lib/python3.13/site-packages (from yfinance) (4.3.8)
Requirement already satisfied: pytz>=2022.5 in ./options_env/lib/python3.13/site-packages (from yfinance) (2025.2)
Requirement already satisfied: frozendict>=2.3.4 in ./options_env/lib/python3.13/site-packages (from yfinance) (2.4.6)
Requirement already satisfied: peewee>=3.16.2 in ./options_env/lib/python3.13/site-packages (from yfinance) (3.18.2)
Requirement already satisfied: beautifulsoup4>=4.11.1 in ./options_env/lib/python3.13/site-packages (from yfinance) (4.13.4)
Requirement already satisfied: curl_cffi>=0.7 in ./options_env/lib/python3.13/site-packages (from yfinance) (0.13.0)
Requirement already satisfied: protobuf>=3.19.0 in ./options_env/lib/python3.13/site-packages (from yfinance) (6.32.0)
Requirement already satisfied: websockets>=13.0 in ./options_env/lib/python3.13/site-packages (from yfinance) (15.0.1)
Requirement already satisfied: python-dateutil>=2.8.2 in ./options_env/lib/python3.13/site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: tzdata>=2022.7 in ./options_env/lib/python3.13/site-packages (from pandas) (2025.2)
Requirement already satisfied: soupsieve>1.2 in ./options_env/lib/python3.13/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.7)
Requirement already satisfied: typing-extensions>=4.0.0 in ./options_env/lib/python3.13/site-packages (from beautifulsoup4>=4.11.1->yfinance) (4.14.1)
Requirement already satisfied: cffi>=1.12.0 in ./options_env/lib/python3.13/site-packages (from curl_cffi>=0.7->yfinance) (1.17.1)
Requirement already satisfied: certifi>=2024.2.2 in ./options_env/lib/python3.13/site-packages (from curl_cffi>=0.7->yfinance) (2025.8.3)
Requirement already satisfied: pycparser in ./options_env/lib/python3.13/site-packages (from cffi>=1.12.0->curl_cffi>=0.7->yfinance) (2.22)
Requirement already satisfied: six>=1.5 in ./options_env/lib/python3.13/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Requirement already satisfied: charset_normalizer<4,>=2 in ./options_env/lib/python3.13/site-packages (from requests>=2.31->yfinance) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in ./options_env/lib/python3.13/site-packages (from requests>=2.31->yfinance) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./options_env/lib/python3.13/site-packages (from requests>=2.31->yfinance) (2.5.0)
(options_env) MacBook-Pro-7:~ walterwoo$ ls -la *.py
-rw-r--r--  1 walterwoo  staff  14469 Aug 15 10:58 advanced_options_analyzer.py
-rw-r--r--  1 walterwoo  staff  25708 Aug 15 11:01 enhanced_options_analyzer.py
-rw-r--r--  1 walterwoo  staff   1873 Aug 14 21:41 options_analysis.py
-rw-r--r--  1 walterwoo  staff   6162 Aug 15 11:04 options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 enhanced_options_analyzer.py
  File "/Users/walterwoo/enhanced_options_analyzer.py", line 378
    main()import yfinance as yf
          ^^^^^^
SyntaxError: invalid syntax
(options_env) MacBook-Pro-7:~ walterwoo$ python3_options_analyzer.py
-bash: python3_options_analyzer.py: command not found
(options_env) MacBook-Pro-7:~ walterwoo$ tail -10 enhanced_options_analyzer.py
        # Ask if user wants to continue
        continue_choice = input("\nAnalyze another symbol? (y/n): ").lower().strip()
        if continue_choice in ['n', 'no']:
            break

if __name__ == "__main__":
    print("📦 Required packages: yfinance pandas numpy matplotlib seaborn")
    print("Install with: pip3 install yfinance pandas numpy matplotlib seaborn")
    print()
    main()
(options_env) MacBook-Pro-7:~ walterwoo$ # Remove the corrupted file
(options_env) MacBook-Pro-7:~ walterwoo$ rm enhanced_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ # Create a clean version
(options_env) MacBook-Pro-7:~ walterwoo$ nano enhanced_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 enhanced_options_analyzer.py
🚀 Advanced Options Analyzer
==================================================
Commands:
  - SYMBOL: Analyze symbol
  - 'add SYMBOL': Add to watchlist
  - 'remove SYMBOL': Remove from watchlist
  - 'watchlist': Show watchlist
  - 'scan': Scan all watchlist symbols
  - 'history': View recent results
  - 'quit': Exit
🚀 Advanced Options Analyzer initialized

📝 Enter command [0 in watchlist]: panw

🔍 Analyzing PANW...
==================================================
💰 Current price: $175.38 (+1.06%)
🏢 Palo Alto Networks, Inc. (Market Cap: $117.1B)
📅 Available expirations: 20
  📊 Processing 2025-08-15 (1/3)...
    Calls: 15,363.0 vol, 104,330.0 OI
    Puts:  4,324.0 vol, 52,676.0 OI
  📊 Processing 2025-08-22 (2/3)...
    Calls: 5,227 vol, 40,432 OI
    Puts:  4,198.0 vol, 31,187 OI
  📊 Processing 2025-08-29 (3/3)...
    Calls: 2,783.0 vol, 8,384 OI
    Puts:  353.0 vol, 4,623 OI

📊 ANALYSIS RESULTS:
==================================================
Symbol: PANW
Current Price: $175.38 (+1.06%)
Expirations Analyzed: 3

📊 VOLUME & POSITIONING:
  Call Volume: 23,373 | Put Volume: 8,875
  Call OI: 153,146.0 | Put OI: 88,486.0
  P/C Volume: 0.380 | P/C OI: 0.578

🎯 SENTIMENT: 🟢 VERY BULLISH (Score: 4)
   Key Factors: Very high call volume, Call-heavy positioning
💾 Results saved to options_results.json

✅ Analysis complete for PANW!

📝 Enter command [0 in watchlist]: nano enhanced_options_analyzer.py

🔍 Analyzing NANO ENHANCED_OPTIONS_ANALYZER.PY...
==================================================
HTTP Error 404: 
$NANO ENHANCED_OPTIONS_ANALYZER.PY: possibly delisted; no price data found  (period=5d) (Yahoo error = "No data found, symbol may be delisted")
❌ No price data for NANO ENHANCED_OPTIONS_ANALYZER.PY
❌ Failed to analyze NANO ENHANCED_OPTIONS_ANALYZER.PY

📝 Enter command [0 in watchlist]: quit
👋 Goodbye!
(options_env) MacBook-Pro-7:~ walterwoo$ nano enhanced_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 enhanced_options_analyzer.py
  File "/Users/walterwoo/enhanced_options_analyzer.py", line 689
    import yfinance as yf import pandas as pd from datetime import datetime, timedelta import json import os import time import math from collections import defaultdict import numpy as np
    ^^^^^^
SyntaxError: f-string: expecting '=', or '!', or ':', or '}'
(options_env) MacBook-Pro-7:~ walterwoo$ rm enhanced_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ nano enhanced_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 enhanced_options_analyzer.py
  File "/Users/walterwoo/enhanced_options_analyzer.py", line 688
    print(f"{i:<4} {result['symbol']:<8} ${result['current_price']
                                          ^
SyntaxError: '{' was never closed
(options_env) MacBook-Pro-7:~ walterwoo$ nano enhanced_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ # Remove the corrupted file
(options_env) MacBook-Pro-7:~ walterwoo$ rm enhanced_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ # Create the new complete version
(options_env) MacBook-Pro-7:~ walterwoo$ nano complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py
🚀 Complete Advanced Options Analyzer v3.0
============================================================
💡 Enhanced Commands:
  📈 SYMBOL: Detailed analysis of any stock symbol
  🔍 'quick SYMBOL': Fast analysis (less detail)
  ⚖️  'compare AAPL,MSFT,GOOGL': Compare multiple stocks
  ➕ 'add SYMBOL': Add to watchlist
  ➖ 'remove SYMBOL': Remove from watchlist
  📋 'watchlist': Show current watchlist
  🔄 'scan': Analyze all watchlist symbols
  📚 'history [N]': View last N analysis results
  💾 'export csv|json': Export all data
  🚪 'quit': Exit analyzer
============================================================
🚀 Complete Advanced Options Analyzer initialized

📝 Enter command: panw
🔬 Performing detailed analysis for PANW...

🔍 Analyzing PANW...
==================================================
💰 Current price: $175.71 (+1.24%)
📊 10-day realized volatility: 34.6%
🏢 Palo Alto Networks, Inc. (Market Cap: $117.4B)
🏭 Technology - Software - Infrastructure, Beta: 0.94
📅 Available expirations: 20
  📊 Processing 2025-08-15 (1/3)...
    Calls: 16,167 vol, 104,330 OI, IV: 742.9%
    Puts:  4,673 vol, 52,676 OI, IV: 242.3%
    🎯 Max Pain: $520.00 ($344.29 from current)
    🚨 Unusual Put Activity: 1 strikes
      $205 - 1,220 vol (152.5x OI)
  📊 Processing 2025-08-22 (2/3)...
    Calls: 5,580 vol, 40,432 OI, IV: 80.0%
    Puts:  4,945 vol, 31,187 OI, IV: 89.0%
  📊 Processing 2025-08-29 (3/3)...
    Calls: 2,886 vol, 8,384 OI, IV: 61.5%
    Puts:  389 vol, 4,623 OI, IV: 64.3%

📊 COMPREHENSIVE ANALYSIS:
==================================================
Symbol: PANW
Current Price: $175.71 (+1.24%)
Realized Vol (10d): 34.6%
Implied Vol (avg): 328.0%
IV/RV Ratio: 9.47x

📈 KEY OPTION LEVELS:
  Support: $175, $170
  Resistance: $180, $200, $210
  Max Pain: $520.00

📊 VOLUME & POSITIONING:
  Call Volume: 24,633 | Put Volume: 10,007
  Call OI: 153,146 | Put OI: 88,486
  P/C Volume: 0.406 | P/C OI: 0.578

🎯 SENTIMENT: 🟢 VERY BULLISH (Score: 3)
   Key Factors: Very high call volume, Heavy call positioning, Unusual put buying, High IV premium

   💰 HIGH IV PREMIUM - 9.5x realized vol
💾 Results saved to options_results.json

✅ Complete analysis finished for PANW!
💡 Type 'add PANW' to add to watchlist

📝 Enter command: quick panw
🚀 Quick analysis mode for PANW

🔍 Analyzing PANW...
==================================================
💰 Current price: $175.57 (+1.16%)
📊 10-day realized volatility: 34.6%
🏢 Palo Alto Networks, Inc. (Market Cap: $117.3B)
🏭 Technology - Software - Infrastructure, Beta: 0.94
📅 Available expirations: 20
  📊 Processing 2025-08-15 (1/3)...
    Calls: 16,663 vol, 104,330 OI, IV: 771.5%
    Puts:  4,949 vol, 52,676 OI, IV: 236.9%
  📊 Processing 2025-08-22 (2/3)...
    Calls: 5,673 vol, 40,432 OI, IV: 81.9%
    Puts:  4,961 vol, 31,187 OI, IV: 86.5%
  📊 Processing 2025-08-29 (3/3)...
    Calls: 2,896 vol, 8,384 OI, IV: 61.3%
    Puts:  389 vol, 4,623 OI, IV: 62.1%

📊 COMPREHENSIVE ANALYSIS:
==================================================
Symbol: PANW
Current Price: $175.57 (+1.16%)
Realized Vol (10d): 34.6%
Implied Vol (avg): 337.6%
IV/RV Ratio: 9.77x

📊 VOLUME & POSITIONING:
  Call Volume: 25,232 | Put Volume: 10,299
  Call OI: 153,146 | Put OI: 88,486
  P/C Volume: 0.408 | P/C OI: 0.578

🎯 SENTIMENT: 🟢 EXTREMELY BULLISH (Score: 4)
   Key Factors: Very high call volume, Heavy call positioning, High IV premium
❌ Error analyzing PANW: cannot access local variable 'earnings_info' where it is not associated with a value
Traceback (most recent call last):
  File "/Users/walterwoo/complete_options_analyzer.py", line 502, in analyze_symbol
    'earnings_days': earnings_info['days_until'] if earnings_info else None,
                                                    ^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'earnings_info' where it is not associated with a value
❌ Failed to analyze PANW

📝 Enter command: quit
👋 Thanks for using the Advanced Options Analyzer!
(options_env) MacBook-Pro-7:~ walterwoo$ # Update your file with the fixed version
(options_env) MacBook-Pro-7:~ walterwoo$ cp complete_options_analyzer.py complete_options_analyzer_backup.py  # backup
(options_env) MacBook-Pro-7:~ walterwoo$ nano complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py
🚀 Complete Advanced Options Analyzer v3.0
============================================================
💡 Enhanced Commands:
  📈 SYMBOL: Detailed analysis of any stock symbol
  🔍 'quick SYMBOL': Fast analysis (less detail)
  ⚖️  'compare AAPL,MSFT,GOOGL': Compare multiple stocks
  ➕ 'add SYMBOL': Add to watchlist
  ➖ 'remove SYMBOL': Remove from watchlist
  📋 'watchlist': Show current watchlist
  🔄 'scan': Analyze all watchlist symbols
  📚 'history [N]': View last N analysis results
  💾 'export csv|json': Export all data
  🚪 'quit': Exit analyzer
============================================================
🚀 Complete Advanced Options Analyzer initialized

📝 Enter command: quick panw
🚀 Quick analysis mode for PANW

🔍 Analyzing PANW...
==================================================
💰 Current price: $175.68 (+1.23%)
📊 10-day realized volatility: 34.6%
🏢 Palo Alto Networks, Inc. (Market Cap: $117.3B)
🏭 Technology - Software - Infrastructure, Beta: 0.94
📅 Available expirations: 20
  📊 Processing 2025-08-15 (1/3)...
    Calls: 16,733 vol, 104,330 OI, IV: 756.0%
    Puts:  4,949 vol, 52,676 OI, IV: 239.8%
  📊 Processing 2025-08-22 (2/3)...
    Calls: 5,745 vol, 40,432 OI, IV: 80.6%
    Puts:  4,967 vol, 31,187 OI, IV: 88.4%
  📊 Processing 2025-08-29 (3/3)...
    Calls: 2,900 vol, 8,384 OI, IV: 60.6%
    Puts:  394 vol, 4,623 OI, IV: 62.3%

📊 COMPREHENSIVE ANALYSIS:
==================================================
Symbol: PANW
Current Price: $175.68 (+1.23%)
Realized Vol (10d): 34.6%
Implied Vol (avg): 333.5%
IV/RV Ratio: 9.63x

📊 VOLUME & POSITIONING:
  Call Volume: 25,378 | Put Volume: 10,310
  Call OI: 153,146 | Put OI: 88,486
  P/C Volume: 0.406 | P/C OI: 0.578

🎯 SENTIMENT: 🟢 EXTREMELY BULLISH (Score: 4)
   Key Factors: Very high call volume, Heavy call positioning, High IV premium
💾 Results saved to options_results.json

✅ Quick analysis complete for PANW!
💡 Use 'PANW' for detailed analysis with all advanced metrics

📝 Enter command: add panw
💾 Watchlist saved with 1 symbols
✅ Added PANW to watchlist

📝 Enter command [1 symbols]: hood
🔬 Performing detailed analysis for HOOD...

🔍 Analyzing HOOD...
==================================================
💰 Current price: $112.70 (+1.80%)
📊 10-day realized volatility: 45.1%
🏢 Robinhood Markets, Inc. (Market Cap: $100.1B)
🏭 Financial Services - Capital Markets, Beta: 2.37
📅 Available expirations: 18
  📊 Processing 2025-08-15 (1/3)...
    Calls: 130,511 vol, 347,476 OI, IV: 30.5%
    Puts:  42,490 vol, 216,773 OI, IV: 405.0%
    🎯 Max Pain: $96.00 ($16.70 from current)
    🚨 Unusual Call Activity: 2 strikes
      $113 - 25,474 vol (3.6x OI)
      $112 - 22,382 vol (3.0x OI)
    🚨 Unusual Put Activity: 3 strikes
      $111 - 7,134 vol (4.3x OI)
      $112 - 6,291 vol (3.3x OI)
  📊 Processing 2025-08-22 (2/3)...
    Calls: 56,013 vol, 119,426 OI, IV: 40.0%
    Puts:  18,104 vol, 72,431 OI, IV: 91.5%
  📊 Processing 2025-08-29 (3/3)...
    Calls: 8,467 vol, 43,178 OI, IV: 36.7%
    Puts:  4,292 vol, 26,170 OI, IV: 74.9%

📊 COMPREHENSIVE ANALYSIS:
==================================================
Symbol: HOOD
Current Price: $112.70 (+1.80%)
Realized Vol (10d): 45.1%
Implied Vol (avg): 166.4%
IV/RV Ratio: 3.69x

📈 KEY OPTION LEVELS:
  Support: $110, $100
  Resistance: $115, $116, $120
  Max Pain: $96.00

📊 VOLUME & POSITIONING:
  Call Volume: 194,991 | Put Volume: 64,886
  Call OI: 510,080 | Put OI: 315,374
  P/C Volume: 0.333 | P/C OI: 0.618

🎯 SENTIMENT: 🟢 EXTREMELY BULLISH (Score: 5)
   Key Factors: Very high call volume, Heavy call positioning, Unusual call buying, High IV premium

   🚨 HIGH UNUSUAL ACTIVITY - 2 calls, 3 puts
   🟢 EXTREME CALL VOLUME - P/C ratio 0.33
   💰 HIGH IV PREMIUM - 3.7x realized vol
💾 Results saved to options_results.json

✅ Complete analysis finished for HOOD!
💡 Type 'add HOOD' to add to watchlist

📝 Enter command [1 symbols]: # Backup your current file
cp complete_options_analyzer.py complete_options_analyzer_backup.py

# Update with the enhanced version
nano complete_options_analyzer.py❌ Please enter a valid stock symbol (1-5 letters)

📝 Enter command [1 symbols]: ❌ Please enter a valid stock symbol (1-5 letters)

📝 Enter command [1 symbols]: 📈 Using default symbol: AAPL
🔬 Performing detailed analysis for AAPL...

🔍 Analyzing AAPL...
==================================================

💰 Current price: $230.73 (-0.88%)
📊 10-day realized volatility: 35.7%
🏢 Apple Inc. (Market Cap: $3424.1B)
🏭 Technology - Consumer Electronics, Beta: 1.17
📅 Available expirations: 20
  📊 Processing 2025-08-15 (1/3)...
    Calls: 202,501 vol, 454,414 OI, IV: 241.5%
    Puts:  112,429 vol, 462,526 OI, IV: 219.4%
    🎯 Max Pain: $220.00 ($10.73 from current)
    🚨 Unusual Call Activity: 1 strikes
      $232 - 60,418 vol (3.4x OI)
  📊 Processing 2025-08-22 (2/3)...
    Calls: 76,019 vol, 188,047 OI, IV: 78.2%
    Puts:  48,075 vol, 124,809 OI, IV: 51.2%
  📊 Processing 2025-08-29 (3/3)...
    Calls: 21,757 vol, 111,712 OI, IV: 66.8%
    Puts:  7,554 vol, 59,405 OI, IV: 50.1%

📊 COMPREHENSIVE ANALYSIS:
==================================================
Symbol: AAPL
Current Price: $230.73 (-0.88%)
Realized Vol (10d): 35.7%
Implied Vol (avg): 175.8%
IV/RV Ratio: 4.93x

📈 KEY OPTION LEVELS:
  Support: $230, $215, $210
  Resistance: $235
  Max Pain: $220.00

📊 VOLUME & POSITIONING:
  Call Volume: 300,277 | Put Volume: 168,058
  Call OI: 754,173 | Put OI: 646,740
  P/C Volume: 0.560 | P/C OI: 0.858

🎯 SENTIMENT: 🟢 EXTREMELY BULLISH (Score: 4)
   Key Factors: Very high call volume, Unusual call buying, High IV premium

   💰 HIGH IV PREMIUM - 4.9x realized vol
💾 Results saved to options_results.json

✅ Complete analysis finished for AAPL!
💡 Type 'add AAPL' to add to watchlist

📝 Enter command [1 symbols]: ❌ Please enter a valid stock symbol (1-5 letters)

📝 Enter command [1 symbols]: ❌ Please enter a valid stock symbol (1-5 letters)

📝 Enter command [1 symbols]: quit
👋 Thanks for using the Advanced Options Analyzer!
🚀 Complete Advanced Options Analyzer v3.0
============================================================
💡 Enhanced Commands:
  📈 SYMBOL: Detailed analysis of any stock symbol
  🔍 'quick SYMBOL': Fast analysis (less detail)
  ⚖️  'compare AAPL,MSFT,GOOGL': Compare multiple stocks
  ➕ 'add SYMBOL': Add to watchlist
  ➖ 'remove SYMBOL': Remove from watchlist
  📋 'watchlist': Show current watchlist
  🔄 'scan': Analyze all watchlist symbols
  📚 'history [N]': View last N analysis results
  💾 'export csv|json': Export all data
  🚪 'quit': Exit analyzer
============================================================
🚀 Complete Advanced Options Analyzer initialized

📝 Enter command [1 symbols]: quit
👋 Thanks for using the Advanced Options Analyzer!
(options_env) MacBook-Pro-7:~ walterwoo$ # Backup your current file
(options_env) MacBook-Pro-7:~ walterwoo$ cp complete_options_analyzer.py complete_options_analyzer_backup.py
(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ # Update with the enhanced version
(options_env) MacBook-Pro-7:~ walterwoo$ nano complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py
  File "/Users/walterwoo/complete_options_analyzer.py", line 281
    def get_top_expirations(self, ticker, max_expirations=5):
SyntaxError: expected 'except' or 'finally' block
(options_env) MacBook-Pro-7:~ walterwoo$ # Remove the problematic file and start fresh
(options_env) MacBook-Pro-7:~ walterwoo$ rm complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ # Create a clean version
(options_env) MacBook-Pro-7:~ walterwoo$ nano complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py

(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ >>exit
(options_env) MacBook-Pro-7:~ walterwoo$ python omplete_options_analyzer.py
/Library/Frameworks/Python.framework/Versions/3.13/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/walterwoo/omplete_options_analyzer.py': [Errno 2] No such file or directory
(options_env) MacBook-Pro-7:~ walterwoo$ # Check the file size and first few lines
(options_env) MacBook-Pro-7:~ walterwoo$ ls -la complete_options_analyzer.py
-rw-r--r--  1 walterwoo  staff  30149 Aug 15 11:55 complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ head -10 complete_options_analyzer.py
#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import json
import os
import time
import math
from collections import defaultdict
(options_env) MacBook-Pro-7:~ walterwoo$ # Check for syntax errors without running
(options_env) MacBook-Pro-7:~ walterwoo$ python3 -m py_compile complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ # Run with verbose error reporting
(options_env) MacBook-Pro-7:~ walterwoo$ python3 -u complete_options_analyzer.py

(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ # Create a minimal test file
(options_env) MacBook-Pro-7:~ walterwoo$ cat > test_analyzer.py << 'EOF'
> #!/usr/bin/env python3
> 
> print("🚀 Test - Program starting...")
> 
> try:
>     import yfinance as yf
>     import pandas as pd
>     print("✅ All imports successful")
>     
>     print("🎯 Starting main function...")
>     
>     while True:
>         user_input = input("📝 Enter test command (or 'quit'): ").strip()
>         
>         if user_input.lower() in ['quit', 'exit', 'q']:
>             print("👋 Test complete!")
>             break
>         
>         print(f"You entered: {user_input}")
> 
> except Exception as e:
>     print(f"❌ Error: {e}")
>     import traceback
>     traceback.print_exc()
> 
> print("Program finished.")
> EOF
(options_env) MacBook-Pro-7:~ walterwoo$ 
(options_env) MacBook-Pro-7:~ walterwoo$ # Run the test
(options_env) MacBook-Pro-7:~ walterwoo$ python3 test_analyzer.py
🚀 Test - Program starting...
✅ All imports successful
🎯 Starting main function...
📝 Enter test command (or 'quit'): pltr
You entered: pltr
📝 Enter test command (or 'quit'): qui
You entered: qui
📝 Enter test command (or 'quit'): quit
👋 Test complete!
Program finished.
(options_env) MacBook-Pro-7:~ walterwoo$ # Check the end of your main file to see if it's complete
(options_env) MacBook-Pro-7:~ walterwoo$ tail -20 complete_options_analyzer.py
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
(options_env) MacBook-Pro-7:~ walterwoo$ python complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ rm complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ nano complete_options_analyzer.py
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py
🚀 Complete Advanced Options Analyzer v3.0
============================================================
💡 Enhanced Commands:
  📈 SYMBOL: Detailed analysis of any stock symbol
  🔍 'quick SYMBOL': Fast analysis (less detail)
  ⚖️  'compare AAPL,MSFT,GOOGL': Compare multiple stocks
  ➕ 'add SYMBOL': Add to watchlist
  ➖ 'remove SYMBOL': Remove from watchlist
  📋 'watchlist': Show current watchlist
  🔄 'scan': Analyze all watchlist symbols
  📚 'history [N]': View last N analysis results
  💾 'export csv|json': Export all data
  🚪 'quit': Exit analyzer
============================================================
🚀 Complete Advanced Options Analyzer initialized

📝 Enter command [1 symbols]: panw
🔬 Performing detailed analysis for PANW...

🔍 Analyzing PANW...
==================================================
💰 Current price: $176.37 (+1.62%)
📊 10-day realized volatility: 35.0%
🏢 Palo Alto Networks, Inc. (Market Cap: $117.8B)
🏭 Technology - Software - Infrastructure, Beta: 0.94
📅 Available expirations: 20
  🔍 Scanning 20 expirations for highest activity...
  📊 Top 5 most active expirations identified
    1. 2025-08-15 (0d): 24,360 vol, 157,006 OI
    2. 2025-09-19 (35d): 6,440 vol, 219,867 OI
    3. 2026-01-16 (154d): 4,149 vol, 176,242 OI
    4. 2025-08-22 (7d): 12,032 vol, 71,619 OI
    5. 2025-10-17 (63d): 1,254 vol, 54,700 OI
📅 Analyzing top 5 most active expirations:
  📊 Processing 2025-08-15 (1/5) - 0 days...
    Calls: 19,065 vol, 104,330 OI, IV: 750.0% [TODAY]
    Puts:  5,308 vol, 52,676 OI, IV: 243.6%
    📈 Enhanced analysis for top 1 expiration:
      🎯 Max Pain: $520.00 ($343.63 below current)
      🚨 Unusual Put Activity: 1 strikes
        $205 - 1,220 vol (152.5x OI)
      📊 Key Levels from OI:
        Support: $170, $175
        Resistance: $180, $210
      ⚡ High Volume Concentration: 100.0% of total volume
  📊 Processing 2025-09-19 (2/5) - 35 days...
    Calls: 3,981 vol, 86,880 OI, IV: 173.6% [QUARTERLY]
    Puts:  2,459 vol, 132,987 OI, IV: 61.2%
    📈 Enhanced analysis for top 2 expiration:
      🎯 Max Pain: $520.00 ($343.63 below current)
      🚨 Unusual Put Activity: 1 strikes
        $340 - 600 vol (5.5x OI)
      📊 Key Levels from OI:
        Resistance: $180, $190
  📊 Processing 2026-01-16 (3/5) - 154 days...
    Calls: 2,527 vol, 96,895 OI, IV: 90.1%
    Puts:  1,622 vol, 79,347 OI, IV: 30.4%
    📈 Enhanced analysis for top 3 expiration:
      🎯 Max Pain: $520.00 ($343.63 below current)
      📊 Key Levels from OI:
        Support: $170, $155
        Resistance: $205, $200
  📊 Processing 2025-08-22 (4/5) - 7 days...
    Calls: 6,439 vol, 40,432 OI, IV: 80.7% [WEEKLY]
    Puts:  5,593 vol, 31,187 OI, IV: 88.9%
  📊 Processing 2025-10-17 (5/5) - 63 days...
    Calls: 948 vol, 35,062 OI, IV: 57.6% [QUARTERLY]
    Puts:  306 vol, 19,638 OI, IV: 46.5%

📊 COMPREHENSIVE ANALYSIS:
==================================================
Symbol: PANW
Current Price: $176.37 (+1.62%)
Realized Vol (10d): 35.0%
Implied Vol (avg): 294.3%
IV/RV Ratio: 8.41x
Expirations Analyzed: 5 (most active)

📈 KEY OPTION LEVELS (from top expirations):
  Support: $175, $170, $155
  Resistance: $180, $190, $195, $200, $205
  Max Pain: $520.00

📊 VOLUME & POSITIONING:
  Call Volume: 32,960 | Put Volume: 15,288
  Call OI: 363,599 | Put OI: 315,835
  P/C Volume: 0.464 | P/C OI: 0.869

🎯 SENTIMENT: 🟢 STRONG BULLISH (Score: 2)
   Key Factors: Very high call volume, Unusual put buying, High IV premium

   💰 HIGH IV PREMIUM - 8.4x realized vol
💾 Results saved to options_results.json

✅ Complete analysis finished for PANW!
💡 Type 'add PANW' to add to watchlist

📝 Enter command [1 symbols]: quit
👋 Thanks for using the Advanced Options Analyzer!
(options_env) MacBook-Pro-7:~ walterwoo$ python3 options_analyzer.py
🚀 Simple Options Analyzer
==================================================
📊 Simple Options Analyzer initialized

📝 Enter stock symbol (or 'quit' to exit): quit
👋 Goodbye!
(options_env) MacBook-Pro-7:~ walterwoo$ python3 complete_options_analyzer.py
🚀 Complete Advanced Options Analyzer v3.0
============================================================
💡 Enhanced Commands:
  📈 SYMBOL: Detailed analysis of any stock symbol
  🔍 'quick SYMBOL': Fast analysis (less detail)
  ⚖️  'compare AAPL,MSFT,GOOGL': Compare multiple stocks
  ➕ 'add SYMBOL': Add to watchlist
  ➖ 'remove SYMBOL': Remove from watchlist
  📋 'watchlist': Show current watchlist
  🔄 'scan': Analyze all watchlist symbols
  📚 'history [N]': View last N analysis results
  💾 'export csv|json': Export all data
  🚪 'quit': Exit analyzer
============================================================
🚀 Complete Advanced Options Analyzer initialized

📝 Enter command [1 symbols]: ibm
🔬 Performing detailed analysis for IBM...

🔍 Analyzing IBM...
==================================================
💰 Current price: $239.72 (+1.10%)
📊 10-day realized volatility: 25.1%
🏢 International Business Machines Corporation (Market Cap: $223.3B)
🏭 Technology - Information Technology Services, Beta: 0.68
📅 Available expirations: 16
  🔍 Scanning 16 expirations for highest activity...
  📊 Top 5 most active expirations identified
    1. 2025-08-15 (0d): 33,189 vol, 61,894 OI
    2. 2025-09-19 (35d): 10,272 vol, 70,162 OI
    3. 2026-01-16 (154d): 4,533 vol, 72,110 OI
    4. 2025-08-22 (7d): 9,129 vol, 16,580 OI
    5. 2025-11-21 (98d): 2,017 vol, 46,551 OI
📅 Analyzing top 5 most active expirations:
  📊 Processing 2025-08-15 (1/5) - 0 days...
    Calls: 9,135 vol, 47,960 OI, IV: 184.5% [TODAY]
    Puts:  24,054 vol, 13,934 OI, IV: 168.9%
    📈 Enhanced analysis for top 1 expiration:
      🎯 Max Pain: $242.50 ($2.78 below current)
      🚨 Unusual Put Activity: 5 strikes
        $258 - 10,015 vol (12.1x OI)
        $280 - 2,237 vol (20.5x OI)
      📊 Key Levels from OI:
        Resistance: $240, $245
      ⚡ High Volume Concentration: 100.0% of total volume
  📊 Processing 2025-09-19 (2/5) - 35 days...
    Calls: 6,530 vol, 40,488 OI, IV: 59.7% [QUARTERLY]
    Puts:  3,742 vol, 29,674 OI, IV: 48.4%
    📈 Enhanced analysis for top 2 expiration:
      🎯 Max Pain: $250.00 ($10.28 below current)
      🚨 Unusual Call Activity: 1 strikes
        $170 - 643 vol (214.3x OI)
      🚨 Unusual Put Activity: 1 strikes
        $280 - 1,280 vol (10.4x OI)
      📊 Key Levels from OI:
        Resistance: $250, $260
  📊 Processing 2026-01-16 (3/5) - 154 days...
    Calls: 4,222 vol, 38,224 OI, IV: 40.6%
    Puts:  311 vol, 33,886 OI, IV: 35.3%
    📈 Enhanced analysis for top 3 expiration:
      🎯 Max Pain: $230.00 ($9.72 above current)
      📊 Key Levels from OI:
        Support: $200, $230
        Resistance: $260, $250
  📊 Processing 2025-08-22 (4/5) - 7 days...
    Calls: 7,000 vol, 8,708 OI, IV: 52.3% [WEEKLY]
    Puts:  2,129 vol, 7,872 OI, IV: 43.5%
  📊 Processing 2025-11-21 (5/5) - 98 days...
    Calls: 1,032 vol, 21,494 OI, IV: 37.5%
    Puts:  985 vol, 25,057 OI, IV: 32.1%

📊 COMPREHENSIVE ANALYSIS:
==================================================
Symbol: IBM
Current Price: $239.72 (+1.10%)
Realized Vol (10d): 25.1%
Implied Vol (avg): 120.0%
IV/RV Ratio: 4.78x
Expirations Analyzed: 5 (most active)

📈 KEY OPTION LEVELS (from top expirations):
  Support: $230, $220, $200
  Resistance: $240, $245, $250, $255, $260
  Max Pain: $230.00

📊 VOLUME & POSITIONING:
  Call Volume: 27,919 | Put Volume: 31,221
  Call OI: 156,874 | Put OI: 110,423
  P/C Volume: 1.118 | P/C OI: 0.704

🎯 SENTIMENT: 🔴 BEARISH (Score: -1)
   Key Factors: Unusual put buying, High IV premium

   🚨 HIGH UNUSUAL ACTIVITY - 1 calls, 6 puts
   💰 HIGH IV PREMIUM - 4.8x realized vol
💾 Results saved to options_results.json

✅ Complete analysis finished for IBM!
💡 Type 'add IBM' to add to watchlist

📝 Enter command [1 symbols]: quit
👋 Thanks for using the Advanced Options Analyzer!
(options_env) MacBook-Pro-7:~ walterwoo$ 
