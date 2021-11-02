from datetime import datetime, timedelta
import pickle
import csv
import os

symbols = {
    1: "TEA",
    2: "POP",
    3: "ALE",
    4: "GIN",
    5: "JOE"
}

indicators = {
    1: "BUY",
    2: "SELL"
}

freader = list(csv.DictReader(open('GBCE_CSV.csv')))

class TradeRecordClass():
    '''
    Record Trade data
    '''

    def __init__(self, symbol, quantity, indicator, traded_price, created_time):
        self.symbol = symbol
        self.quantity = quantity
        self.indicator = indicator
        self.traded_price = traded_price
        self.created_time = created_time

    def get_trade_details(self):
        data = "Symbol : {0} \n Quantity : {1} \n Indicator : {2} \n Trade Price : {3} \n Created Time : {4}".format(
            self.symbol, self.quantity, self.indicator, self.traded_price, self.created_time)
        return data

class StockClass():

    @classmethod
    def calculate_divident(self, symbol, price):
        '''
            Calculate dividend method taking 2 parameters:
            1) symbol: of the stock
            2) param price: price.
            Result: Divident yield value
        '''

        stock_symbol = symbols.get(int(symbol), None)

        if stock_symbol is None:
            return False, "Enter Valid Stock Symbol"

        try:
            if float(price) == 0.0:
                return False, "Enter valid price"
        except:
            return False, "Enter valid price"

        for gbce_stock in freader:
            if gbce_stock['stock_symbol'] == str(stock_symbol):
                if gbce_stock['stock_type'] == "Common":
                    try:
                        divident = float(gbce_stock.get('last_divident', 0)) / float(price)
                    except ZeroDivisionError:
                        divident = 0
                else:
                    try:
                        divident = (float(gbce_stock.get('fixed_divident', 0))/100) * \
                            float(gbce_stock.get('par_value', 0)) / float(price)
                    except ZeroDivisionError:
                        divident = 0

                return True, divident

    @classmethod
    def calculate_pe_ratio(self, symbol, price):
        '''
            Calculate P/E Ratio method required 2 parameters.
            1) symbol: of the stock
            2) param price: price.
            Result: P/E Ratio value
        '''

        status_code, result = self.calculate_divident(symbol, price)

        if not status_code:
            return status_code, result
        else:
            try:
                pe_ratio = float(price) / float(result)
            except ZeroDivisionError:
                pe_ratio = 0

            return True, pe_ratio

    @classmethod
    def record_trade(self, symbol, quantity, indicator, traded_price):
        '''
            This method is used to record trade.
            record_trade() method required 4 parameters
            1)symbol: of the stock
            2)indicator: SELL, BUY
            3)quantity: to trade
            4)traded_price: price of the trade
        '''

        trade_file = open('trade_records', 'rb')

        is_file_empty = os.path.getsize("trade_records") == 0

        if not is_file_empty:
            list_trade_records = pickle.load(trade_file,encoding='utf8')
        else:
            list_trade_records = []

        stock_symbol = symbols.get(int(symbol), None)
        quantity = int(quantity)
        indicator = indicators.get(int(indicator), None)
        traded_price = float(traded_price)

        try:
            trade_record_data = TradeRecordClass(stock_symbol, quantity, indicator, traded_price, datetime.now())

            trade_file = open("trade_records", "wb")
            list_trade_records.append(trade_record_data)
            pickle.dump(list_trade_records, trade_file)
            print ("Trade_record ", trade_record_data.get_trade_details())
            print ("Trade data recorded successfully!!! ")
        except KeyboardInterrupt:
            print ("Trade data Not Added")
        except EOFError:
            print ("Trade data Not Added")
        finally:
            trade_file.close()

    @classmethod
    def volume_weighted_stock_price(self, symbol):
        '''
            This method is used to calculate stock price for given stock based on trades from last 5 min.
            stock_price() method required only stock symbol parameter
        '''

        stock_symbol = symbols.get(int(symbol), None)
        trade_time = datetime.now() - timedelta(minutes=5)

        trade_file = open("trade_records", "rb")

        is_file_empty = os.path.getsize("trade_records") == 0

        quantity_sum = 0
        sum_trade_price = 0

        if not is_file_empty:
            list_trade_records = pickle.load(trade_file,encoding='utf8')

            for trade_record in list_trade_records:
                if trade_record.symbol == stock_symbol and trade_record.created_time >= trade_time:
                    print ("Trade_record ", trade_record.get_trade_details())
                    quantity_sum += trade_record.quantity
                    sum_trade_price += (trade_record.quantity * trade_record.traded_price)

            if sum_trade_price and quantity_sum:
                vol_weight_stock_price = sum_trade_price/quantity_sum
                print ("Volume Weighted Stock Price :  ", float(vol_weight_stock_price))

            else:
                trade_file.close()
                return "Trade record is empty for the stock {0} in the past 5 minutes".format(stock_symbol)

        else:
            trade_file.close()
            print ("Trade Record is empty")

    @classmethod
    def GBCE_share_index(self):
        '''
            This method is used to calculate the GBCE All Share Index using the geometric mean of prices
            for all stocks.
        '''

        trade_time = datetime.now() - timedelta(minutes=5)

        trade_file = open("trade_records", "rb")

        is_file_empty = os.path.getsize("trade_file") == 0

        quantity_sum = 0
        sum_trade_price = 0

        if not is_file_empty:
            list_trade_records = pickle.load(trade_file,encoding="utf8")

            for trade_record in list_trade_records:
                if trade_record.created_time >= trade_time:
                    print ("trade_record ", trade_record.get_trade_details())
                    quantity_sum += trade_record.quantity
                    sum_trade_price += (trade_record.quantity * trade_record.traded_price)

            if sum_trade_price and quantity_sum:
                gbce_share_index = sum_trade_price**(1/quantity_sum)
                print ("GBCE Share Index :  ", float(gbce_share_index))

            else:
                trade_file.close()
                return "Trade Record is empty"

        else:
            trade_file.close()
            print ("Trade Record is empty")
