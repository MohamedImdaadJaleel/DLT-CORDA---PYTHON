import extended_trade
import order_values
import trade
import trade_interval

Total_Trades = trade.trade_count + extended_trade.e_trade_count
Number_of_trades = trade.trade_count
Number_of_ex_trades = extended_trade.e_trade_count
Maximum_Length_Comment = trade.highest_length
Longest_Comment = trade.longest_comment
Unique_Traders = trade.unique_trade_list
Trade_Interval = trade_interval.trade_interval
Trade_Interval2 = trade_interval.trade_interval2
Total_Buy_Order = order_values.Total_Buy
Total_Sell_Order = order_values.Total_Sell

print("----------------------------------------------")
print("Summary")
print("----------------------------------------------")
print("Total Number of Trades: ", Total_Trades)
print("Number of Trades: ", Number_of_trades)
print("Number of Extra Trades: ", Number_of_ex_trades)
print("Length of the longest comment:", Maximum_Length_Comment)
print("Longest comment: ", Longest_Comment)
print(f"Trade, Trade Interval: {Trade_Interval} seconds")
print(f"Extended Trade, Trade Interval: {Trade_Interval2} seconds")
print("Total Buy Value of Trades: ", Total_Buy_Order)
print("Total Sell Value of Trades: ", Total_Sell_Order)

print("----------------------------------------------")
print("List of Firms")
print("----------------------------------------------")
print("Number of unique firms: ", len(Unique_Traders))
print("Unique firm IDs: ")
for unique_trade in Unique_Traders:
    print(unique_trade),
print("----------------------------------------------")
