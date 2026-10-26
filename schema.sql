PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID TEXT PRIMARY KEY, CustomerName TEXT NOT NULL, City TEXT, State TEXT,
    SignupDate TEXT, CustomerSegment TEXT
);
CREATE TABLE IF NOT EXISTS Products (
    ProductID TEXT PRIMARY KEY, ProductName TEXT NOT NULL, Category TEXT NOT NULL,
    UnitPriceINR REAL NOT NULL, UnitCostINR REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS Orders (
    OrderID TEXT PRIMARY KEY, CustomerID TEXT NOT NULL, OrderDate TEXT NOT NULL,
    OrderStatus TEXT NOT NULL, PaymentMethod TEXT, ShippingCity TEXT, ShippingState TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
CREATE TABLE IF NOT EXISTS OrderItems (
    OrderItemID TEXT PRIMARY KEY, OrderID TEXT NOT NULL, ProductID TEXT NOT NULL,
    Quantity INTEGER NOT NULL, UnitPriceINR REAL NOT NULL, DiscountRate REAL NOT NULL,
    LineSalesINR REAL NOT NULL, LineCostINR REAL NOT NULL, LineProfitINR REAL NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
CREATE TABLE IF NOT EXISTS Payments (
    PaymentID TEXT PRIMARY KEY, OrderID TEXT NOT NULL, PaymentStatus TEXT NOT NULL,
    PaymentAmountINR REAL NOT NULL, PaymentDate TEXT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
