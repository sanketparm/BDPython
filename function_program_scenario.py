#Scenario: Processing Transaction Data

# Imagine you're working on a project that involves processing a large dataset of financial transactions. Each transaction contains information such as the transaction amount, type (debit or credit), and category (e.g., groceries, utilities, entertainment).

# Your task is to perform various operations on this dataset, such as:

# Calculate the total amount of transactions.
# Filter transactions based on certain criteria (e.g., transactions above a certain amount).
# Group transactions by category and calculate the total amount for each category.
# Transform transaction data (e.g., convert amounts to a different currency).
# Find anomalies in the data (e.g., unusually high transactions).


transactions = [
    {"amount": 100, "type": "debit", "category": "groceries"},
    {"amount": 50, "type": "debit", "category": "utilities"},
    {"amount": 200, "type": "debit", "category": "entertainment"},
    # More transactions...
]

# Calculate total amount of transactions
total_amount = sum(transaction["amount"] for transaction in transactions)

# Filter transactions above a certain amount
high_value_transactions = filter(lambda x: x["amount"] > 100, transactions)

# Group transactions by category and calculate total amount for each category
from collections import defaultdict
category_totals = defaultdict(int)
for transaction in transactions:
    category_totals[transaction["category"]] += transaction["amount"]

# Convert amounts to a different currency (dummy example)
def convert_to_usd(amount):
    return amount * 0.85

transactions_usd = [{"amount": convert_to_usd(transaction["amount"]), "type": transaction["type"], "category": transaction["category"]} for transaction in transactions]

# Find anomalies in the data (dummy example)
anomalies = filter(lambda x: x["amount"] > 1000, transactions)

print("Total amount of transactions:", total_amount)
print("High value transactions:", list(high_value_transactions))
print("Category totals:", dict(category_totals))
print("Transactions in USD:", transactions_usd)
print("Anomalies:", list(anomalies))
