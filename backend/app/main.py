from market_data import fetch_current_prices
from calculations import calculate_portfolio_total, calculate_portfolio_gainloss
from csv_reader import parse_portfolio

portfolio = parse_portfolio("example_csv/ex1.csv")
portfolio = fetch_current_prices(portfolio)
print(portfolio)
print(calculate_portfolio_total(portfolio))
print(calculate_portfolio_gainloss(portfolio))