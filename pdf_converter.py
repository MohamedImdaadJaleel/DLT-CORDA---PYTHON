from fpdf import FPDF
import output_main
import item_id_values

pdf = FPDF()
pdf.add_page()

pdf.set_font('Courier', 'BI''U', 16)
pdf.cell(200, 10, txt="Trade Structures and It's Summary", ln=1, align='C')

pdf.set_font('Courier', 'B''U', 13)
pdf.cell(100, 8, txt="Summary", ln=2, align='L')

pdf.set_font('Courier', 'B', 12)
pdf.cell(100, 8, txt="Number of trades: " + str(output_main.Number_of_trades), ln=3, align='L')
pdf.cell(100, 8, txt="Number of extended trades: " + str(output_main.Number_of_ex_trades), ln=4, align='L')
pdf.cell(100, 8, txt="Total Number Of Trades: " + str(output_main.Total_Trades), ln=4, align='L')
pdf.cell(100, 8, txt="Total value of BUY trades: " + str(output_main.Total_Buy_Order), ln=4, align='L')
pdf.cell(100, 8, txt="Total value of SELL trades: " + str(output_main.Total_Sell_Order), ln=4, align='L')
pdf.cell(100, 8, txt="Length of the longest comment: " + str(output_main.Maximum_Length_Comment), ln=4, align='L')
pdf.cell(100, 8, txt="Longest comment: " + str(output_main.Longest_Comment), ln=4, align='L')
pdf.cell(100, 8, txt="Trade interval: " + str(output_main.Trade_Interval), ln=4, align='L')
pdf.cell(100, 8, txt="Extended Trade interval: " + str(output_main.Trade_Interval2), ln=2, align='L')

pdf.set_font('Courier', 'B''U', 13)
pdf.cell(100, 15, txt="List of Firms", ln=2, align='L')

pdf.set_font('Courier', 'B', 12)
pdf.cell(100, 8, txt="Number of unique firms: " + str(len(output_main.Unique_Traders)), ln=4, align='L')
pdf.cell(100, 8, txt="Unique firm IDs:", ln=4, align='L')

pdf.set_font('Courier', size=12)
for unique_trade in output_main.Unique_Traders:
    pdf.cell(100, 8, txt=str(unique_trade), ln=4, align='L')

pdf.set_font('Courier', 'B''U', 13)
pdf.cell(100, 15, txt="Totals per Item ID", ln=2, align='L')

pdf.set_font('Courier', 'B', 12)
pdf.cell(100, 15, txt="1. Trade", ln=2, align='L')

pdf.set_font('Courier', 'B', 12)
for item_value in item_id_values.trade_list:
    pdf.cell(100, 8, txt="Item Id: " + item_value, ln=4, align='L')

pdf.set_font('Courier', 'B', 12)
pdf.cell(100, 15, txt="2. Extended Trade", ln=2, align='L')

pdf.set_font('Courier', 'B', 12)
for item_value in item_id_values.extended_trade_list:
    pdf.cell(100, 8, txt="Item Id: " + item_value, ln=4, align='L')


def pdf_converter():
    pdf.output("trade.pdf")


