from datetime import datetime
import csv

import numpy as np

import extended_trade

with open('GeneralTrade.csv') as file:
    trade_reader = csv.DictReader(file)

    commentList = []
    trade_commentList = []
    buy_tradeList = []
    sell_tradeList = []
    unique_trade_list = []
    time_List = []
    unique_buy_list = []
    unique_sell_list = []
    total_amount_list = []
    total_quantity_list = []

    trade_count = 0

    for row in trade_reader:
        comment = row['Trade Comment']
        trade_comment = comment

        comment_length = len(comment)
        commentList.append(comment_length)
        trade_commentList.append(comment)
        trade_count += 1

        sell_trades = row['Seller']
        buy_trades = row['Buyer']

        time = row['File Date']
        time_List.append(time)

        order_amount = row['Price']
        order_quantity = row['Quantity']

        total_amount_list.append(order_amount)
        total_quantity_list.append(order_quantity)

        buy_tradeList.append(buy_trades)
        sell_tradeList.append(sell_trades)


def unique(buy_list, sell_list):
    for buy in buy_list:
        if buy not in unique_buy_list:
            unique_buy_list.append(buy)

    for sell in sell_list:
        if sell not in unique_sell_list:
            unique_sell_list.append(sell)


def unique_trades(trader_List):
    for unique_trade in trader_List:
        if unique_trade not in unique_trade_list:
            unique_trade_list.append(unique_trade)


# maximum length of the comment list
highest_length = max(commentList)

# after finding maximum comment list, finding in which index it has the maximum comment
highest_length_index = commentList.index(highest_length)

# passing the maximum comment list's index to trade comment list array to display the comment
longest_comment = trade_commentList[highest_length_index]

# print(buy_tradeList)
unique(buy_tradeList, sell_tradeList)

# combining all buyers and sellers of trades and extended trades and finding the unique traders via numpy
combine_buy_sell = np.concatenate((unique_sell_list, unique_buy_list, extended_trade.extended_traders_combined))
unique_trades(combine_buy_sell)

start_time = time_List[0]
final_start_time = start_time[11:23]

end_time = time_List[3]
final_end_time = end_time[11:23]

sell_order1 = total_amount_list[0]
sell_order2 = total_amount_list[3]
sell_quantity1 = total_quantity_list[0]
sell_quantity2 = total_quantity_list[3]


buy_order1 = total_amount_list[1]
buy_order2 = total_amount_list[2]
buy_quantity1 = total_quantity_list[1]
buy_quantity2 = total_quantity_list[2]