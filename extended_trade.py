import csv
import numpy as np


filename = input("Enter Name Of Extended Trade file: ")
# Check
# filename = "ExtendedTrade.csv"
with open(filename) as file:
    extended_trade_reader = csv.DictReader(file)
    buy_tradeList = []
    sell_tradeList = []
    time_List = []
    total_amount_list = []
    total_quantity_list = []
    item_id_List = []
    e_trade_count = 0;

    for row in extended_trade_reader:
        e_trade_count += 1
        sell_trades = row['Seller']
        buy_trades = row['Buyer']
        time = row['File Date']
        time_List.append(time)

        order_amount = row['Price']
        order_quantity = row['Quantity']

        item_id = row['ItemID']
        item_id_List.append(item_id)

        total_amount_list.append(order_amount)
        total_quantity_list.append(order_quantity)

        buy_tradeList.append(buy_trades)
        sell_tradeList.append(sell_trades)

# combining the buyers and sellers of the extended trade to import this variable in trade.py
extended_traders_combined = np.concatenate((buy_tradeList, sell_tradeList))

start_time = time_List[0]
final_start_time = start_time[11:23]

end_time = time_List[1]
final_end_time = end_time[11:23]

sell_order1 = total_amount_list[0]
sell_quantity1 = total_quantity_list[0]

buy_order1 = total_amount_list[1]
buy_quantity1 = total_quantity_list[1]

