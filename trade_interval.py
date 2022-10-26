from datetime import datetime
import extended_trade
import trade

# convert time string to datetime
# Extended Trade : Trade Interval
time_start = datetime.strptime(trade.final_start_time, "%H:%M:%S.%f")
time_end = datetime.strptime(trade.final_end_time, "%H:%M:%S.%f")
time_difference = time_end - time_start

trade_interval = time_difference.total_seconds()

# Extended Trade : Trade Interval
extended_time_start = datetime.strptime(extended_trade.final_start_time, "%H:%M:%S.%f")
extended_time_end = datetime.strptime(extended_trade.final_end_time, "%H:%M:%S.%f")
time_difference2 = extended_time_end - extended_time_start

trade_interval2 = time_difference2.total_seconds()
