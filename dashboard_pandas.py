# dashboard_generator.py

import operator

import pandas



# def to_usd(my_price):
#   # return "${0:,.2f}".format(my_price)
#   return f"${my_price:,.2f}"

# INFO INPUTS

csv_filepath = "sales-201803.csv" 
df = pandas.read_csv(csv_filepath)

# breakpoint()

# csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

# csv_data = pandas.read_csv(csv_filepath)



# monthly_total = csv_data["sales price"].sum()

# product_totals = product_totals.sort_values("sales price", ascending=False)


# top_sellers = []
# rank = 1
# for i, row in product_totals.iterrows():
#     d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
#     top_sellers.append(d)
#     rank = rank + 1

# print("-----------------------")
# print("MONTH: March 2018")

# print("-----------------------")
# print("CRUNCHING THE DATA...")

# print("-----------------------")
# print("TOTAL MONTHLY SALES:")
# print(f"MONTH: {month} {year}")
# print(f"TOTAL SALES: {to_usd(total_sales)}")

# print("-----------------------")
# print("TOP SELLING PRODUCTS:")
# for d in top_sellers:
#     print("  " + str(d["rank"]) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))

# print("-----------------------")
# print("VISUALIZING THE DATA...")