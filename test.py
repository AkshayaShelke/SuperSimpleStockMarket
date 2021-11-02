import random
import unittest
from StockCalculationMethods import StockClass as stock

class ApiTestCase(unittest.TestCase):

    symbols = [1,2,3,4,5]
    types = [1,2]
    quantities = range(0, 1000, 5)
    prices = [20,69000,78,31.7,8,0,856]

    @classmethod
    def test_calculate_divident(self):
        print('\n')
        for symbol in self.symbols:
            print('Dividend yield for %s:' % symbol,
                  stock.calculate_divident(int(symbol),float(random.choice(self.prices))))
    
    @classmethod
    def test_calculate_pe_ratio(self):
        print('\n')
        for symbol in self.symbols:
            print('P/E Ratio for %s:' % symbol,
                  stock.calculate_pe_ratio(int(symbol),float(random.choice(self.prices))))

    @classmethod
    # test_record_trade
    def record_trade(self):
        print('\n')
        for i in range(10):
            stock.record_trade(random.choice(self.symbols), random.choice(self.quantities), random.choice(self.types),
                               random.choice(self.prices))

    @classmethod
    def test_volume_weighted_stock_price(self):
        print('\n')
        for symbol in self.symbols:
            print('Stock price for %s:' % symbol,
                  stock.volume_weighted_stock_price(int(symbol)))

    @classmethod
    def test_GBCE_share_index(self):
        print('\n')
        print('GBCE:', stock.GBCE_share_index())



if __name__ == '__main__':
    unittest.main()
