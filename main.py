from StockCalculationMethods import StockClass as stock

'''
Simple Stock Market Console Application
'''

choice = 0
def TakeSymbol():
    symbol_in = input("Choose a stock symbol:" +
          "\n1) TEA " +
          "\n2) POP " +
          "\n3) ALE " +
          "\n4) GIN " +
          "\n5) JOE \n" +
          "----------------------------------------\n>")
    return symbol_in

while True:
    print ("---------------------------------------")
    choice = input("Enter the number of the Option you want:" +
                       "\n----------------------------------------" +
                       "\n1) Calculate dividend yield" +
                       "\n2) Calculate the P/E Ratio"
                       "\n3) Record Trade" +
                       "\n4) Calculate Volume Weighted Stock Price "
                       "\n5) Calculate the GBCE All Share Index"
                       "\n6) Exit\n" +
                       "----------------------------------------\n>")
    if(choice == '1'):
        symbol = TakeSymbol()
        price = input("Enter the stock price \n")
        status_code, result = stock.calculate_divident(symbol, price)
        print ("Dividend Yield : ", result,end='\n')

    elif(choice == '2'):
        symbol = TakeSymbol()
        price = input("Enter the stock price \n")
        status_code, result = stock.calculate_pe_ratio(symbol, price)
        print ("P/E Ratio : ", result,end ='\n')

    elif(choice == '3'):
        symbol = TakeSymbol()
        quantity = input("Enter Shares Quantity \n")
        indicator = input("Choose a indicator :" +
                              "\n1) BUY " +
                              "\n2) SELL \n" +
                              "----------------------------------------\n>")
        traded_price = input("Enter traded price \n")
        stock.record_trade(symbol, quantity, indicator, traded_price)
        print ("\n")

    elif(choice == '4'):
        symbol = TakeSymbol()
        stock.volume_weighted_stock_price(symbol)
        print ("\n")

    elif(choice == '5'):
        stock.GBCE_share_index()
        print ("\n")

    elif choice == '6':
        break
