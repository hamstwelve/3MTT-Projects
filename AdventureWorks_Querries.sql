-- VIEW TABLE SalesLT.Customer--
SELECT * FROM SalesLT.Customer
-- VIEW TABLE SalesLT.OrderHeader--
SELECT * FROM SalesLT.SalesOrderHeader

-- QUESTIO 1: SPOLLING OF TOP TEN DATA FROM TABLE (SaleLT.Address, SaleLT.Customer and SaleLT.SalesOrderDetail)--
--Retrieving Top Ten Data From Three Tables--
SELECT TOP(10) CONCAT(c.FirstName, ' ', c.MiddleName, ' ', c.LastName) AS 'Full Name', 
	a.CountryRegion AS Country, 
	a.City,
SUM(sod.OrderQty * sod.UnitPrice) AS Revenue
FROM 
	SalesLT.Customer c JOIN SalesLT.SalesOrderHeader soh ON c.CustomerID = soh.CustomerID
--Combine Rows From Three Tables--
JOIN 
	SalesLT.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
JOIN 
	SalesLT.Address a ON soh.ShipToAddressID = a.AddressID
--Goruping Rows With the Same Values--
GROUP BY CONCAT(
	c.FirstName, ' ',
	c.MiddleName, ' ',
	c.LastName),
	a.CountryRegion, a.City
ORDER BY Revenue DESC;


-- QEUSTION 2: Creating 4 Distinct Customer Segments Based on Revenue--
--Retrieving Data--
WITH CustomerRevenue AS (
	SELECT 
		c.CustomerID, c.CompanyName, SUM(sod.OrderQty * sod.UnitPrice)
	AS 
		TotalRevenue
FROM 
	SalesLT.Customer c
--Combine Rows From Three Tables--
JOIN 
	SalesLT.SalesOrderHeader soh ON c.CustomerID = soh.CustomerID
JOIN 
	SalesLT.SalesOrderDetail sod ON sod.SalesOrderID = soh.SalesOrderID
--Goruping Rows With the Same Values--
GROUP BY 
	c.CustomerID, c.CompanyName),
RevenueSegments AS (
	SELECT 
	CustomerID, CompanyName, TotalRevenue,
	NTILE(4) OVER (ORDER BY TotalRevenue DESC) AS Segment
	FROM 
	CustomerRevenue)
SELECT 
	CustomerID, CompanyName, TotalRevenue,
--CASE Funtion to perform Conditional Logic WHEN and THEN--
	CASE 
		WHEN Segment = 1 THEN 'Premium'
		WHEN Segment = 2 THEN 'VVIP'
		WHEN Segment = 3 THEN 'VIP'
		WHEN Segment = 4 THEN 'Regular'
	END AS CustomerSegment
FROM RevenueSegments
ORDER BY TotalRevenue DESC;

--QUESTION 3: Selecting Latest Products and Categories Purchased on the Last Day of Business--
--SELECT to Retrieve Data From Table-- 
SELECT
	c.CustomerID,
	p.ProductID,
	p.Name AS Product_Name,
	pc.Name AS Category_Name,
	soh.OrderDate
FROM
	SalesLT.SalesOrderHeader soh
--JOIN To Join Four (4) Tables--
JOIN 
	SalesLT.Customer c ON soh.CustomerID = c.CustomerID
JOIN
	SalesLT.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
JOIN
	SalesLT.Product p ON sod.ProductID = p.ProductID
JOIN
	SalesLT.ProductCategory pc ON p.ProductCategoryID = pc.ProductCategoryID
WHERE
	soh.OrderDate = (
		SELECT MAX(OrderDate)
		FROM
			SalesLT.SalesOrderHeader)
ORDER BY
	c.CustomerID, p.Name;

--QUESTION 4: CREATING CUSTOMER SEGMENT VIEW--
--CREATE VIEW: Creating a Virtual Table--
CREATE VIEW CustomerSegment AS
SELECT
	c.CustomerID AS Id,
	c.CompanyName AS Name,
	SUM(sod.OrderQty * sod.UnitPrice * (1 - sod.UnitPriceDiscount)) AS Revenue,
CASE
	WHEN SUM(sod.OrderQty * sod.UnitPrice * (1 - sod.UnitPriceDiscount)) > 10000
		THEN 'HIGH Value'
	WHEN SUM(sod.OrderQty * sod.UnitPrice * (1 - sod.UnitPriceDiscount)) BETWEEN 5000 AND 10000
		THEN 'Medium Value'
	ELSE 'Low Value'
	END AS Segment
FROM
	SalesLT.Customer c
--JOIN: Joining Two (2) Tables--
JOIN
	SalesLT.SalesOrderHeader soh ON c.CustomerID = soh.CustomerID
JOIN
	SalesLT.SalesOrderDetail sod ON sod.SalesOrderID = soh.SalesOrderID
GROUP BY
	c.CustomerID, c.CompanyName;

--QUESTION 5: SELECTING TOP THREE (3) SELLING PRODUCT BY REVENUE--
WITH RankedProducts AS (
	SELECT TOP(3)
	pc.Name AS Category_Name,
	p.Name AS Product_Name,
	SUM(sod.UnitPrice * sod.OrderQty * (1 - sod.UnitPriceDiscount)) AS Revenue,
	DENSE_RANK() OVER (
		PARTITION BY pc.Name ORDER BY 
		SUM(sod.UnitPrice * sod.OrderQty * (1 - sod.UnitPriceDiscount)) DESC)
		AS ranknum
	FROM
		SalesLT.ProductCategory pc
		JOIN SalesLT.Product p ON pc.ProductCategoryID = p.ProductCategoryID
		JOIN SalesLT.SalesOrderDetail sod ON p.ProductID = sod.ProductID
	GROUP BY
		pc.Name, p.Name
)
SELECT
	Category_Name,
	Product_Name,
	Revenue
FROM
	RankedProducts
WHERE
	ranknum <= 3
ORDER BY
	Category_Name,
	ranknum;