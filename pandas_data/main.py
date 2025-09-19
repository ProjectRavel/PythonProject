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



def agregasi():
    df_agregasi_total_penjualan = df.groupby("shop_name", as_index=False)["price"].sum()
    df_agregasi_ratarata_penjualan = df.groupby('shop_name', as_index=False)["price"].mean()

    def visualitation_data(df, x, y, kind,  xlabel, ylabel):
        ax = df.plot(x=x, y=y, kind=kind)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    df_agregasi_total_penjualan.plot(x="shop_name", y="price", kind="bar", ax=axes[0], title="Total Penjualan")
    df_agregasi_ratarata_penjualan.plot(x="shop_name", y="price", kind="bar", ax=axes[1], title="Rata-rata Penjualan")

    plt.tight_layout()
    plt.show()