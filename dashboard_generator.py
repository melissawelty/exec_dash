# dashboard_generator.py

import csv
import os 

def to_usd(my_price):
  # return "${0:,.2f}".format(my_price)
  return f"${my_price:,.2f}"

# INFO INPUTS

csv_filename = "sales-201803.csv" 

csv_filepath = os.path.join(os.path.dirname(__file__),"data", csv_filename)

rows = [] 

with open(csv_filepath, "r") as csv_file:
  reader = csv.DictReader(csv_file)
  for row in reader:
      print(row)
  #for od in reader:
   # rows.append(dict(od))

sales_price = [float(row["sales price"]) for row in rows]

total_sales = sum(sales_price)

month = "MARCH"
year = 2018 


print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES:")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")