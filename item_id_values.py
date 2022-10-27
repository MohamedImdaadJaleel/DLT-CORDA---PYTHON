import extended_trade
import trade

extended_trade_list = []
trade_list = []


def calc_item_value(a, b):
    return a * b


sell_order_ext = float(extended_trade.sell_order1)
int(sell_order_ext)
sell_quantity_ext = float(extended_trade.sell_quantity1)
int(sell_quantity_ext)

sell_ext = calc_item_value(sell_order_ext, sell_quantity_ext)

buy_order_ext = float(extended_trade.buy_order1)
int(buy_order_ext)
buy_quantity_ext = float(extended_trade.buy_quantity1)
int(buy_quantity_ext)

buy_ext = calc_item_value(buy_order_ext, buy_quantity_ext)

ext_item_id_1 = str(extended_trade.item_id_List[0]) + ": " + str(sell_ext)
ext_item_id_2 = str(extended_trade.item_id_List[1]) + ": " + str(buy_ext)

extended_trade_list.append(ext_item_id_1)
extended_trade_list.append(ext_item_id_2)

# Item Value of Trade Orders
# OCP0ED209MK1 - Item ID
buy_order_1 = float(trade.buy_order1)
int(buy_order_1)
buy_quantity1 = float(trade.buy_quantity1)
int(buy_quantity1)

buy_order_2 = float(trade.buy_order2)
int(buy_order_2)
buy_quantity2 = float(trade.buy_quantity2)
int(buy_quantity2)

buy1 = calc_item_value(buy_order_1, buy_quantity1)
buy2 = calc_item_value(buy_order_2, buy_quantity2)
Total_Buy_Order = buy1 + buy2

trade_item_id_2 = str(trade.item_id_List[1]) + ": " + str(buy1)
trade_item_id_3 = str(trade.item_id_List[2]) + ": " + str(buy2)
sum_trade2_3 = str(trade.item_id_List[2]) + " Total Value: " + str(Total_Buy_Order)

# CYB0T800M101 - Item ID


sell_order_1 = float(trade.sell_order1)
int(sell_order_1)
sell_quantity1 = float(trade.sell_quantity1)
int(sell_quantity1)

# AWY0ATMOPRC1 - Item ID

sell_order_2 = float(trade.sell_order2)
int(sell_order_2)
sell_quantity2 = float(trade.sell_quantity2)
int(sell_quantity2)

sell1 = calc_item_value(sell_order_1, sell_quantity1)
sell2 = calc_item_value(sell_order_2, sell_quantity2)

trade_item_id_1 = str(trade.item_id_List[0]) + ": " + str(sell1)
trade_item_id_4 = str(trade.item_id_List[3]) + ": " + str(sell2)

trade_list.append(trade_item_id_1)
trade_list.append(trade_item_id_2)
trade_list.append(trade_item_id_3)
trade_list.append(sum_trade2_3)
trade_list.append(trade_item_id_4)
