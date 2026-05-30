import pandas as pd

df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset.csv")

df["Unit_Price"] = df["Unit_Price"].replace("[\$,]", "", regex=True).astype(float)
df["Stock_Quantity"] = pd.to_numeric(df["Stock_Quantity"])
df["Sales_Volume"] = pd.to_numeric(df["Sales_Volume"])

print("欄位名稱：")
print(df.columns)

df["Total_Inventory_Value"] = df["Stock_Quantity"] * df["Unit_Price"]

print("\n每個商品的總庫存價值：")
print(df[["Product_Name", "Stock_Quantity", "Unit_Price", "Total_Inventory_Value"]])

best_selling_product = df.loc[df["Sales_Volume"].idxmax()]

print("\n最暢銷商品：")
print("商品名稱：", best_selling_product["Product_Name"])
print("銷售數量：", best_selling_product["Sales_Volume"])

df["Original_Revenue"] = df["Sales_Volume"] * df["Unit_Price"]
df["Discounted_Revenue"] = df["Original_Revenue"] * 0.9

print("\n9折後的收入：")
print(df[["Product_Name", "Sales_Volume", "Unit_Price", "Original_Revenue", "Discounted_Revenue"]])

df.to_csv("result.csv", index=False, encoding="utf-8-sig")

print("\n已完成計算，結果已輸出成 result.csv")