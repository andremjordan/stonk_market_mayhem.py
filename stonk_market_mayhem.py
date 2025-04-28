# BAD STOCK TRADING APP - DO NOT USE IN REAL LIFE

import random

stocks = {
    "AAPL": 150,
    "GOOG": 2800,
    "TSLA": 720,
    "AMZN": 3400
}

portfolio = {}
money = 10000

def show_menu() -> None:
    """
    Displays the main menu options for the stock trading application.
    """
    print("1. View Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Exit")
def view_stocks():
    """
    Displays the current prices of all available stocks, updating each price with a random fluctuation.
    
    Each time this function is called, stock prices are adjusted by a random amount between -100 and 100 before being displayed.
    """
    for stock, price in stocks.items():
        # Prices fluctuate wildly each time you look
        new_price = price + random.randint(-100, 100)
        stocks[stock] = new_price
        print(f"{stock}: ${new_price}")

def buy_stock():
    """
    Processes the purchase of a specified stock by the user.
    
    Prompts the user to enter a stock symbol and quantity to buy. If sufficient funds are available, deducts the total cost from the user's cash balance and adds the purchased shares to the portfolio. Prints a confirmation message upon successful purchase or notifies the user if funds are insufficient.
    """
    global money
    stock = input("Which stock do you want to buy? ")
    qty = int(input("How many shares? "))
    cost = stocks[stock] * qty
    if money >= cost:
        money -= cost
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty
        print(f"Bought {qty} shares of {stock}")
    else:
        print("You broke.")

def sell_stock():
    """
    Sells a specified quantity of a stock from the user's portfolio.
    
    Prompts the user to enter a stock symbol and the number of shares to sell. If the user owns enough shares, the shares are deducted from the portfolio and the proceeds are added to the cash balance. If not, notifies the user of insufficient shares.
    """
    global money
    stock = input("Which stock do you want to sell? ")
    qty = int(input("How many shares? "))
    if stock in portfolio and portfolio[stock] >= qty:
        money += stocks[stock] * qty
        portfolio[stock] -= qty
        print(f"Sold {qty} shares of {stock}")
    else:
        print("You don’t own that much.")

def view_portfolio() -> None:
    """
    Displays the user's current stock holdings, cash balance, and total portfolio value.
    
    Prints each owned stock with the number of shares, current price per share, and total value. If no stocks are owned, indicates this. Also shows available cash and the combined value of cash and stocks.
    """
    print("Your portfolio:")
    total_value = 0

    if not portfolio:
        print("  No stocks owned.")

    for stock, qty in portfolio.items():
        value = qty * stocks[stock]
        total_value += value
        print(f"{stock}: {qty} shares (${stocks[stock]} each, total: ${value})")

    print(f"Cash: ${money}")
    print(f"Total portfolio value: ${total_value + money}")
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        view_stocks()
    elif choice == "2":
        buy_stock()
    elif choice == "3":
        sell_stock()
    elif choice == "4":
        view_portfolio()
    elif choice == "5":
        print("k bye")
        break
    else:
        print("wat")




