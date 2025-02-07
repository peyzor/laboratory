import csv
import random

NUM_ROWS = 40_000_000
BATCH_SIZE = 1_000_000

with open("orders_data.csv", "w") as file:
    writer = csv.writer(file)
    for _ in range(NUM_ROWS):
        product_id = random.randint(1, 100000)
        amount = round(random.uniform(1.0, 500.0), 2)
        description = f"Product {product_id} description"
        writer.writerow([product_id, amount, description])

print("CSV file generated.")
