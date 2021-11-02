# SuperSimpleStockMarket
Console application of Super Simple Stock Market, which is helpful for calculating stock related amounts and maintaining new trade records  


## Description
The source code that will :

- For a given stock, 
    - calculate the dividend yield
    - calculate the P/E Ratio
    - record a trade, with timestamp, quantity of shares, buy or sell indicator and price
    - Calculate Stock Price based on trades recorded in past 5 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

##### Constraints & Notes

1.	No database or GUI is required, all data need only be held in memory.

2.	Formulas and data provided are simplified representations for the purpose of this exercise.

##### Global Beverage Corporation Exchange

Stock Symbol  | Type | Last Dividend | Fixed Dividend | Par Value
------------- | ---- | ------------: | :------------: | --------: 
TEA           | Common    | 0  |    | 100
POP           | Common    | 8  |    | 100
ALE           | Common    | 23 |    | 60
GIN           | Preferred | 8  | 2% | 100
JOE           | Common    | 13 |    | 250


## Requirements

- Python 3.x version
- Tested on Windows

## Main Application File
```
main.py
```

## Test File
```
test.py
```

## Author

Akshaya Shelke


