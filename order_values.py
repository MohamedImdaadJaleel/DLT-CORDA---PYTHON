import extended_trade
import trade


def calculate_order(a, b):
    return a * b


# Sell Trade Orders
sell_order_1 = float(trade.sell_order1)
int(sell_order_1)
sell_quantity1 = float(trade.sell_quantity1)
int(sell_quantity1)

sell_order_2 = float(trade.sell_order2)
int(sell_order_2)
sell_quantity2 = float(trade.sell_quantity2)
int(sell_quantity2)

sell1 = calculate_order(sell_order_1, sell_quantity1)
sell2 = calculate_order(sell_order_2, sell_quantity2)
Total_Sell_Order = sell1 + sell2
print(Total_Sell_Order)

# Buy Trade Orders

buy_order_1 = float(trade.buy_order1)
int(buy_order_1)
buy_quantity1 = float(trade.buy_quantity1)
int(buy_quantity1)

buy_order_2 = float(trade.buy_order2)
int(buy_order_2)
buy_quantity2 = float(trade.buy_quantity2)
int(buy_quantity2)

buy1 = calculate_order(buy_order_1, buy_quantity1)
buy2 = calculate_order(buy_order_2, buy_quantity2)
Total_Buy_Order = buy1 + buy2


# Sell Extended Order
sell_order_ext = float(extended_trade.sell_order1)
int(sell_order_ext)
sell_quantity_ext = float(extended_trade.sell_quantity1)
int(sell_quantity_ext)

sell_ext = calculate_order(sell_order_ext, sell_quantity_ext)

# Buy Extended Order

buy_order_ext = float(extended_trade.buy_order1)
int(buy_order_ext)
buy_quantity_ext = float(extended_trade.buy_quantity1)
int(buy_quantity_ext)

buy_ext = calculate_order(buy_order_ext, buy_quantity_ext)
print(buy_ext)

# Addition of Extended Trade and Trade buy orders and sell orders
Total_Buy = Total_Buy_Order + buy_ext
Total_Sell = Total_Sell_Order + sell_ext

