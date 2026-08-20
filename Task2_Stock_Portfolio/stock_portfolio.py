# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 185,
    "META": 500,
    "NVDA": 130
}

portfolio = []
total_investment = 0

print("=" * 50)
print("          STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when you have finished adding stocks.\n")

while True:

    stock = input("Enter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.\n")
        continue

    # Enter quantity
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

    except ValueError:
        print("Please enter a valid number.\n")
        continue

    # Calculate investment
    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    # Store information
    portfolio.append({
        "stock": stock,
        "price": price,
        "quantity": quantity,
        "investment": investment
    })

    print(f"{stock} added successfully!")
    print(f"Investment: ${investment}\n")


# Display portfolio
print("\n" + "=" * 60)
print("                    YOUR PORTFOLIO")
print("=" * 60)

if not portfolio:
    print("No stocks were added.")

else:
    print(
        f"{'Stock':<10}"
        f"{'Price':<12}"
        f"{'Quantity':<12}"
        f"{'Investment':<15}"
    )

    print("-" * 60)

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"${item['price']:<11}"
            f"{item['quantity']:<12}"
            f"${item['investment']:<14}"
        )

    print("-" * 60)
    print(f"Total Investment: ${total_investment}")

    # Save portfolio to text file
    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n\n")

        for item in portfolio:
            file.write(
                f"Stock: {item['stock']}\n"
                f"Price: ${item['price']}\n"
                f"Quantity: {item['quantity']}\n"
                f"Investment: ${item['investment']}\n"
                f"{'-' * 30}\n"
            )

        file.write(f"\nTotal Investment: ${total_investment}\n")

    print("\nPortfolio saved successfully to portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker!")
