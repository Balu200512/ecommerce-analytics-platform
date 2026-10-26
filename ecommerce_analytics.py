from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
DB_PATH = ROOT / "ecommerce_analytics.db"

FILES = {
    "Customers": "customers.csv",
    "Products": "products.csv",
    "Orders": "orders.csv",
    "OrderItems": "order_items.csv",
    "Payments": "payments.csv",
}

def load_data():
    tables = {table: pd.read_csv(DATA / filename) for table, filename in FILES.items()}
    for column in ["OrderDate", "SignupDate", "PaymentDate"]:
        for table in tables:
            if column in tables[table].columns:
                tables[table][column] = pd.to_datetime(tables[table][column], errors="coerce")
    return tables

def validate_data(tables):
    assert tables["Customers"]["CustomerID"].is_unique, "CustomerID must be unique."
    assert tables["Products"]["ProductID"].is_unique, "ProductID must be unique."
    assert tables["Orders"]["OrderID"].is_unique, "OrderID must be unique."
    assert tables["OrderItems"]["OrderItemID"].is_unique, "OrderItemID must be unique."
    assert tables["Payments"]["PaymentID"].is_unique, "PaymentID must be unique."
    assert set(tables["Orders"]["CustomerID"]).issubset(set(tables["Customers"]["CustomerID"])), "Order has unknown customer."
    assert set(tables["OrderItems"]["OrderID"]).issubset(set(tables["Orders"]["OrderID"])), "Order item has unknown order."
    assert set(tables["OrderItems"]["ProductID"]).issubset(set(tables["Products"]["ProductID"])), "Order item has unknown product."
    assert (tables["OrderItems"]["Quantity"] > 0).all(), "Quantity must be positive."
    assert (tables["OrderItems"]["LineSalesINR"] >= 0).all(), "Line sales must be non-negative."

def load_sqlite(tables):
    with sqlite3.connect(DB_PATH) as conn:
        for table, df in tables.items():
            df.to_sql(table, conn, if_exists="replace", index=False)

def save_chart(fig, name):
    REPORTS.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(REPORTS / name, dpi=160, bbox_inches="tight")
    plt.close(fig)

def generate_reports(tables):
    REPORTS.mkdir(exist_ok=True)
    orders, items, products = tables["Orders"], tables["OrderItems"], tables["Products"]
    completed = orders.loc[orders["OrderStatus"] == "Completed", ["OrderID", "OrderDate"]]
    completed_items = items.merge(completed, on="OrderID").merge(products[["ProductID","ProductName","Category"]], on="ProductID")

    monthly = completed_items.assign(OrderMonth=completed_items["OrderDate"].dt.to_period("M").astype(str)).groupby("OrderMonth", as_index=False)["LineSalesINR"].sum()
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(monthly["OrderMonth"], monthly["LineSalesINR"], marker="o")
    ax.set_title("Monthly Revenue (Completed Orders)")
    ax.set_xlabel("Month"); ax.set_ylabel("Revenue (INR)")
    ax.tick_params(axis="x", rotation=40)
    save_chart(fig, "monthly_revenue.png")

    category = completed_items.groupby("Category")["LineSalesINR"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(9,5))
    category.plot(kind="barh", ax=ax)
    ax.set_title("Revenue by Product Category")
    ax.set_xlabel("Revenue (INR)"); ax.set_ylabel("Category")
    save_chart(fig, "revenue_by_category.png")

    top = completed_items.groupby("ProductName")["LineSalesINR"].sum().sort_values().tail(10)
    fig, ax = plt.subplots(figsize=(9,6))
    top.plot(kind="barh", ax=ax)
    ax.set_title("Top 10 Products by Revenue")
    ax.set_xlabel("Revenue (INR)"); ax.set_ylabel("Product")
    save_chart(fig, "top_products.png")

    status = orders["OrderStatus"].value_counts()
    fig, ax = plt.subplots(figsize=(8,5))
    status.plot(kind="bar", ax=ax)
    ax.set_title("Order Count by Status")
    ax.set_xlabel("Order Status"); ax.set_ylabel("Orders")
    save_chart(fig, "orders_by_status.png")

    completed_revenue = float(completed_items["LineSalesINR"].sum())
    completed_profit = float(completed_items["LineProfitINR"].sum())
    completed_order_count = int(completed["OrderID"].nunique())
    customer_count = int(orders.loc[orders["OrderStatus"] == "Completed", "CustomerID"].nunique())
    metrics = pd.DataFrame([
        ("Customers in sample", int(tables["Customers"]["CustomerID"].nunique())),
        ("Orders in sample", int(orders["OrderID"].nunique())),
        ("Completed orders", completed_order_count),
        ("Customers with completed orders", customer_count),
        ("Completed-order revenue (INR)", round(completed_revenue, 2)),
        ("Completed-order profit (INR)", round(completed_profit, 2)),
        ("Average order value (INR)", round(completed_revenue/completed_order_count, 2) if completed_order_count else 0),
    ], columns=["Metric","Value"])
    metrics.to_csv(REPORTS / "ecommerce_summary_metrics.csv", index=False)
    lines=["| Metric | Value |","|---|---:|"]+[f"| {r['Metric']} | {r['Value']} |" for _,r in metrics.iterrows()]
    (REPORTS / "ecommerce_summary_metrics.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

def main():
    tables = load_data()
    validate_data(tables)
    load_sqlite(tables)
    generate_reports(tables)
    print("E-commerce Analytics Platform completed successfully.")
    for name, df in tables.items():
        print(f"{name}: {len(df):,} rows")
    print(f"SQLite database: {DB_PATH}")
    print(f"Reports folder: {REPORTS}")
    print("Dataset validation passed.")

if __name__ == "__main__":
    main()
