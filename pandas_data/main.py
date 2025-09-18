import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Membaca Data
df = pd.read_csv('data_produk.csv')

# Filter Data
df_filter = df[df['price'] > 200000]

# Jika ingin membuat top 5
df.head(5) 

# GroupBy
shop_high_value = df.groupby('shop_name')["price"].sum().sort_values(ascending=False)

# manipulate data
tax_price = 0.12
df['tax_price'] = df['price'] * (1 + tax_price)


df["item_name"] = df["item_name"].fillna("Unknown")


# Agregasi data & Visualisasi Python
df_agregasi = df.groupby("shop_name", as_index=False)["price"].sum()
ax = df_agregasi.plot(x="shop_name", y="price", kind="bar")

ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f"Rp {x:,.0f}".replace(",", "."))
)

plt.xlabel("Nama Toko")
plt.ylabel("Total Penjualan")
plt.title("Total Penjualan Per Toko")

plt.show()