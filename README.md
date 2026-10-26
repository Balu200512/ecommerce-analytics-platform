# E-commerce Analytics Platform | SQL, Power BI & Python

## 1. Project Overview

The E-commerce Analytics Platform is a data analytics project developed using SQL, Python, Pandas, Matplotlib, and Power BI. It is designed to analyze online orders, products, customers, payments, revenue, and profitability.

The project transforms synthetic e-commerce transactions into useful business insights through relational database tables, SQL queries, automated Python reports, and an interactive Power BI dashboard that you can build using the included guide and DAX measures.

**Project Type:** Data Analytics and Business Intelligence

**Tools Used:** SQL, SQLite, Python, Pandas, Matplotlib, Power BI, Excel, CSV

## 2. Problem Statement

E-commerce businesses generate data about customers, orders, products, and payments. Without a structured data model and consistent analysis, it can be difficult to monitor revenue, identify top-selling products, compare categories, understand order status, and evaluate customer purchasing behavior.

This project demonstrates how SQL data modeling and Python analysis can prepare e-commerce records for reporting and visualization.

## 3. Project Objectives

- Design a relational database schema for customers, products, orders, order items, and payments.
- Analyze revenue and profit from completed orders.
- Identify top-performing products and categories.
- Track order counts and order status distribution.
- Summarize customer purchasing activity.
- Demonstrate SQL joins, aggregations, grouping, and filtering.
- Use Python and Pandas to validate and analyze source datasets.
- Generate charts and summary reports automatically.
- Build an interactive Power BI report with slicers and drill-down analysis.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| SQL / SQLite | Relational schema, joins, aggregations, and analytical queries |
| Python | Data validation and automated reporting |
| Pandas | Data loading, transformation, and analysis |
| Matplotlib | Charts and visual summaries |
| Microsoft Power BI Desktop | Interactive business intelligence dashboard |
| DAX | KPI and time-based measures |
| Microsoft Excel | Browsing the sample datasets |
| CSV | Portable data files |

## 5. Dataset Description

All records are synthetic and generated for educational and portfolio purposes. They do not represent real customers, orders, or a real business.

The workbook is named `Ecommerce_Analytics_Sample_Data.xlsx` and contains five sheets.

### 5.1 Customers

Contains 250 synthetic customer profiles.

| Column | Description |
|---|---|
| CustomerID | Unique customer identifier |
| CustomerName | Synthetic customer label |
| City | Sample city |
| State | Sample state |
| SignupDate | Customer signup date |
| CustomerSegment | New, Returning, or Loyal sample segment |

### 5.2 Products

Contains the sample product catalog.

| Column | Description |
|---|---|
| ProductID | Unique product identifier |
| ProductName | Product name |
| Category | Product category |
| UnitPriceINR | Illustrative listed unit price |
| UnitCostINR | Illustrative unit cost |

### 5.3 Orders

Contains 1,000 synthetic order records from 2025.

| Column | Description |
|---|---|
| OrderID | Unique order identifier |
| CustomerID | Customer who placed the order |
| OrderDate | Order date |
| OrderStatus | Completed, Returned, Cancelled, or Processing |
| PaymentMethod | Sample payment method |
| ShippingCity | Sample shipping city |
| ShippingState | Sample shipping state |

### 5.4 OrderItems

Contains one or more product line items per order.

| Column | Description |
|---|---|
| OrderItemID | Unique order line identifier |
| OrderID | Associated order |
| ProductID | Product in the order line |
| Quantity | Units ordered |
| UnitPriceINR | Unit price used for the line |
| DiscountRate | Discount as a decimal |
| LineSalesINR | Quantity × unit price after discount |
| LineCostINR | Illustrative line cost |
| LineProfitINR | Line sales minus line cost |

### 5.5 Payments

Contains one sample payment record per order.

| Column | Description |
|---|---|
| PaymentID | Unique payment identifier |
| OrderID | Associated order |
| PaymentStatus | Paid, Pending, Refunded, or Failed |
| PaymentAmountINR | Sample payment amount |
| PaymentDate | Payment date |

## 6. Key Business Metrics

### Completed Revenue

Sum of line sales for orders with `OrderStatus = Completed`.

### Completed Profit

Sum of line profit for completed orders.

### Profit Margin %

Completed profit divided by completed revenue, multiplied by 100.

### Completed Orders

Count of distinct orders marked Completed.

### Average Order Value (AOV)

Completed revenue divided by completed order count.

### Units Sold

Sum of item quantities for completed orders.

### Product and Category Revenue

Sales contribution grouped by product or category for completed orders.

### Order Status Distribution

Count of orders by status, including Completed, Returned, Cancelled, and Processing.

**Metric note:** The sample measures exclude returned, cancelled, and processing orders from completed revenue/profit. Real reporting should follow the business's policies for refunds, cancellations, shipping, taxes, and revenue recognition.

## 7. SQL Database Schema

The SQL schema is available in `sql/schema.sql`.

It defines five related tables:

- `Customers`
- `Products`
- `Orders`
- `OrderItems`
- `Payments`

### Relationship overview

```text
Customers ──< Orders ──< OrderItems >── Products
                  |
                  └──< Payments
```

- One customer can place many orders.
- One order can contain many order items.
- One product can appear in many order items.
- An order can have a payment record.

The schema uses primary keys and foreign key declarations to document the intended relational design.

## 8. SQL Analytics Queries

The file `sql/analytics_queries.sql` contains example queries for:

1. Monthly revenue from completed orders.
2. Top 10 products by completed-order revenue.
3. Revenue by product category.
4. Customer order frequency and revenue.
5. Order status distribution.
6. Profit by category for completed orders.

The queries demonstrate `JOIN`, `GROUP BY`, aggregate functions, filtering with `WHERE`, sorting, and `LIMIT`.

## 9. Project Folder Structure

```text
ecommerce-analytics-platform/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── payments.csv
│
├── sql/
│   ├── schema.sql
│   └── analytics_queries.sql
│
├── powerbi/
│   └── Measures.dax
│
├── docs/
│   └── PowerBI_Build_Guide.md
│
├── reports/                         # generated when the script runs
├── Ecommerce_Analytics_Sample_Data.xlsx
├── ecommerce_analytics.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Descriptions

- `data/` — CSV source datasets.
- `sql/schema.sql` — relational table definitions.
- `sql/analytics_queries.sql` — useful SQL analytics examples.
- `powerbi/Measures.dax` — DAX measures for the Power BI report.
- `docs/PowerBI_Build_Guide.md` — data model and dashboard instructions.
- `Ecommerce_Analytics_Sample_Data.xlsx` — Excel workbook containing the datasets.
- `ecommerce_analytics.py` — data validation, SQLite loading, chart generation, and KPI summary exports.
- `requirements.txt` — Python package dependencies.
- `.gitignore` — excludes virtual environments, generated databases, reports, and local PBIX files.
- `README.md` — project documentation.

## 10. How to Run the Python Project

### Prerequisites

- Python 3.10 or later
- Visual Studio Code (recommended)
- Internet connection for installing Python packages

### Step 1: Download or clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-analytics-platform.git
cd ecommerce-analytics-platform
```

Replace `YOUR_USERNAME` with your GitHub username. If you downloaded the ZIP instead, extract it and open a terminal in the extracted folder.

### Step 2: Create a virtual environment (recommended)

In PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell activation is blocked, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the analysis

```bash
python ecommerce_analytics.py
```

The script validates the datasets, loads tables into a local SQLite database, generates charts, and exports summary metrics.

## 11. Generated Outputs

The program creates these outputs in the `reports/` folder:

- `monthly_revenue.png` — monthly revenue from completed orders.
- `revenue_by_category.png` — revenue by product category.
- `top_products.png` — top 10 products by revenue.
- `orders_by_status.png` — order counts by status.
- `ecommerce_summary_metrics.csv` — summary KPIs in CSV format.
- `ecommerce_summary_metrics.md` — summary KPIs in Markdown format.

It also creates `ecommerce_analytics.db` in the project root. The database is rebuilt from the CSV source data whenever the program runs.

## 12. How to Build the Power BI Dashboard

The repository includes DAX measures and a step-by-step guide. It does not include a prebuilt `.pbix` file.

1. Open Power BI Desktop.
2. Select **Get data → Excel workbook**.
3. Choose `Ecommerce_Analytics_Sample_Data.xlsx`.
4. Load the Customers, Products, Orders, OrderItems, and Payments sheets.
5. Verify the column data types.
6. Create relationships as described in `docs/PowerBI_Build_Guide.md`.
7. Create the Date table and measures from `powerbi/Measures.dax`.
8. Build the report pages and add slicers.
9. Save the report as `Ecommerce_Analytics_Dashboard.pbix`.

### Recommended dashboard pages

**Executive Overview**
- Completed Revenue
- Completed Profit
- Profit Margin %
- Completed Orders
- Average Order Value
- Monthly revenue trend
- Revenue by category
- Order status distribution

**Product Analysis**
- Top products by revenue
- Units sold by product
- Category and product profitability
- Category → Product drill-down

**Customer Analysis**
- Order frequency by customer
- Revenue by customer
- Customer segment and location filters

**Order & Payment Analysis**
- Order status distribution
- Payment status distribution
- Detailed order and payment table

Recommended slicers include Year-Month, Category, Shipping State, Payment Method, and Order Status.

## 13. Data Validation and Modeling Notes

The Python program checks that:
- Customer, product, order, order-item, and payment identifiers are unique in their respective tables.
- Order customer IDs exist in the customer table.
- Order-item order IDs and product IDs exist in their parent tables.
- Item quantities are positive.
- Line sales amounts are non-negative.

The sample payment status is independently generated for demonstration and may not reconcile with order status. In a real system, payment and refund records should be modeled and reconciled according to business rules.

## 14. Limitations

- All data is synthetic and for portfolio demonstration only.
- The project is a local analysis workflow, not a deployed e-commerce website.
- The repository includes Power BI source measures and build instructions, not a completed PBIX file.
- Payment data is illustrative and not connected to any real payment provider.
- Customer segmentation is sample data, not the result of a production segmentation model.
- Business metrics must be validated against the organization's accounting and operational definitions before production use.

## 15. Future Enhancements

- Add customer lifetime value (CLV) and repeat-purchase analysis.
- Add RFM (Recency, Frequency, Monetary) customer segmentation.
- Add cohort retention analysis.
- Add product inventory and stock-out reporting.
- Build an interactive Streamlit front end.
- Add scheduled data refresh and automated tests.
- Connect to a managed SQL database.
- Publish the report to Power BI Service where permitted.

## 16. Skills Demonstrated

This project demonstrates:
- SQL schema design and relational modeling
- SQL joins and aggregate queries
- Python programming
- Pandas data preparation and analysis
- Matplotlib visualization
- Data validation
- KPI design and business reporting
- Power BI data modeling and DAX
- E-commerce sales and customer analytics

## 17. Author

**Balaji Mudugal**

GitHub: https://github.com/Balu200512

## 18. Conclusion

The E-commerce Analytics Platform demonstrates how SQL, Python, Pandas, Matplotlib, and Power BI can work together to analyze e-commerce data.

It provides a portfolio foundation for exploring revenue, profitability, product performance, customer purchasing activity, and order statuses. The synthetic data and documented workflow can be extended with additional metrics, data sources, and dashboard functionality.
