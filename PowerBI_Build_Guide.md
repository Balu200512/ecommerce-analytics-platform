# Power BI Build Guide

## 1. Import the data
Open Power BI Desktop → Get data → Excel workbook → select `Ecommerce_Analytics_Sample_Data.xlsx`. Load Customers, Products, Orders, OrderItems, and Payments.

## 2. Check data types
- Date columns: Date
- IDs: Text
- Quantity: Whole number
- Prices, sales, costs, profit, payment amounts: Decimal number
- DiscountRate: Decimal number

## 3. Create relationships
Create one-to-many relationships:
- Customers[CustomerID] → Orders[CustomerID]
- Orders[OrderID] → OrderItems[OrderID]
- Products[ProductID] → OrderItems[ProductID]
- Orders[OrderID] → Payments[OrderID]
- Date[Date] → Orders[OrderDate]

Keep filter direction single unless a specific need requires otherwise. Do not directly relate fact tables to each other except through their defined keys.

## 4. Create Date table and measures
Use `powerbi/Measures.dax`. Create the Date table first via Modeling → New table. Mark it as the date table and sort Date[Month] by Date[MonthNo]. Create measures one at a time via Modeling → New measure.

## 5. Recommended report pages
### Executive Overview
Cards: Completed Revenue, Completed Profit, Profit Margin %, Completed Orders, Average Order Value.
Charts: monthly revenue line chart, revenue by category bar chart, order status chart.
Slicers: Date[YearMonth], Products[Category], Orders[ShippingState], Orders[PaymentMethod].

### Product Analysis
Bar chart: revenue by ProductName.
Matrix: Category → ProductName with revenue, profit, units sold.
Use Top N filter to show the top 10 products.

### Customer Analysis
Table or bar chart of customer order frequency and revenue. Use customer segment, city, and state slicers.

### Order & Payment Analysis
Order status distribution, payment status distribution, and an order details table.

## 6. Important metric note
The included measures calculate completed-order revenue and profit only. Returned, cancelled, and processing orders are excluded from those measures. For real business use, confirm the company's policy for refunds, cancellations, taxes, shipping, and revenue recognition.

## 7. Save the report
Save as `Ecommerce_Analytics_Dashboard.pbix`. The repository includes the data and build guide, not a prebuilt PBIX file.
