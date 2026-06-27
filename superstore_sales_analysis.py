import pandas as pd
import numpy as np


df = pd.read_csv("./assets/superstore_sales.csv")

print(f"Original Data Frame:\n\n{df}")
df.drop_duplicates(inplace=True)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(f"Remove Duplicates:\n\n {df}")
print(f"Basic Info:\n {df.info()}")
print("\n")
print(f"Statistics:\n {df.describe()}")
print("\n")
print(f"Missing Values:\n\n {df.isnull().sum()}")
print("\n\n")
df["Sales"].fillna(df["Sales"].median(), inplace=True)
print(f"Filled Missing Values of Sales:\n\n {df}")
print(f"Again Information of Empty:\n\n {df.isnull().sum()}")
print("\n\n")

df["Quantity"] = np.abs(df["Quantity"])
print(f"Converted Negative Values to Positive of Quantity:\n\n {df}")
print("\n\n")
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month_name()
df["Day"] = df["Order_Date"].dt.day_name()
print("\n\n")

print(f"Adding the column of Year, Month, Day:\n\n {df}")
print("\n\n")
df["Total_Sales"] = df["Sales"] * df["Quantity"]
print(f"Adding the column of Total Sales:\n\n {df}")

ProductWiseSales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print(f"Total Product Sales:\n\n {ProductWiseSales}")
print("\n\n")

TopProduct = ProductWiseSales.idxmax()
LowProduct = ProductWiseSales.idxmin()
print(f"Top Product Sales: {TopProduct}")
print("\n\n")
print(f"Low Product Sales: {LowProduct}")
print("\n\n")

RegionWiseSales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
print(f"Total Region Sales:\n\n {RegionWiseSales}")
print("\n\n")

CityWiseSales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)
print(f"Top City Sales:\n\n {CityWiseSales}")
print("\n\n")

TopSalesRegion = RegionWiseSales.idxmax()
LowSalesRegion = RegionWiseSales.idxmin()
print(f"Top Sales Region: {TopSalesRegion}")
print("\n\n")
print(f"Low Sales Region: {LowSalesRegion}")
print("\n\n")

TopSalesCity = CityWiseSales.idxmax()
LowSalesCity = CityWiseSales.idxmin()
print(f"Top Sales City: {TopSalesCity}")
print("\n\n")
print(f"Low Sales City: {LowSalesCity}")
print("\n\n")


print("=" * 120)
print(f"{"=" * 52} Business KPIs {"=" * 52}")
print("=" * 120)
print("\n\n")

TotalSales = df["Sales"].sum()
AverageSales = df["Sales"].mean()
HighestSales = df["Sales"].max()


print("=" * 100)
print(f"{"=" * 44} Sales KPIs {"=" * 44}")
print("=" * 100)
print(f"Total Sales Products: {TotalSales}")
print(f"Average Sales Products: {AverageSales}")
print(f"Maximum Sales Products: {HighestSales}")
print("\n\n")

TotalQuantity = df["Quantity"].sum()
AverageQuantity = df["Quantity"].mean()
HighestQuantity = df["Quantity"].max()


print("=" * 100)
print(f"{"=" * 42} Quantity KPIs {"=" * 42}")
print("=" * 100)
print(f"Total Sales Quantity: {TotalQuantity}")
print(f"Average Sales Quantity: {AverageQuantity}")
print(f"Maximum Sales Quantity: {HighestQuantity}")
print("\n\n")

TotalDiscount = df["Discount"].sum()
AverageDiscount = df["Discount"].mean()
HighestDiscount = df["Discount"].max()

print("=" * 100)
print(f"{"=" * 42} Discount KPIs {"=" * 42}")
print("=" * 100)
print(f"Total Discount: {TotalDiscount}")
print(f"Average Discount: {AverageDiscount}")
print(f"Maximum Discount: {HighestDiscount}")
print("\n\n")

TotalProfit = df["Profit"].sum()
AverageProfit = df["Profit"].mean()
HighestProfit = df["Profit"].max()

print("=" * 100)
print(f"{"=" * 43} Profit KPIs {"=" * 43}")
print("=" * 100)
print(f"Total Profit: {TotalProfit}")
print(f"Average Profit: {AverageProfit}")
print(f"Maximum Profit: {HighestProfit}")
print("\n\n")

print("=" * 100)
print(f"{"=" * 38} CUSTOMER SEGMENTATION {"=" * 38}")
print("=" * 100)
df["Customer_Segmentation"] = np.where(df["Total_Sales"] > 100000, "High", np.where(df["Total_Sales"] > 50000, "Medium", "Low"))
print(f"\n\nAdd the Column of Customer Segmentation:\n\n {df}")

CustomerBehaviour = df.groupby("Customer_Segmentation")["Total_Sales"].value_counts()
print(f"Customer segmentation Counts\n\n {CustomerBehaviour}")
print("\n\n")
CustomerStatusCounts = df["Customer_Segmentation"].value_counts()
print(CustomerStatusCounts.sort_values(ascending=False))
print("\n\n")
YearlySalesTrend = df.groupby("Year")["Total_Sales"].sum()
MonthlySalesTrend = (
    df.groupby("Month")["Total_Sales"]
      .sum()
      .reindex([
          "January","February",
          "March","April","May",
          "June","July","August",
          "September","October",
          "November","December"
      ])
)

print(f"Yearly Sales Trend\n\n {YearlySalesTrend}")
print(f"Monthly Sales Trend\n\n {MonthlySalesTrend}")


print("\n========== BUSINESS INSIGHTS ==========\n")

print(f"Best Performing Region: {TopSalesRegion}")

print(f"Lowest Performing Region: {LowSalesRegion}")

print(f"Best Selling Product: {TopProduct}")

print(f"Lowest Selling Product: {LowProduct}")

df.to_excel("Super_Store_Sales_Data.xlsx", index=False)
df.to_csv("Super_Store_Sales_Data.csv", index=False)







