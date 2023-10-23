# Write your MySQL query statement below
SELECT product_name,year,price
FROM Product 
RIGHT JOIN Sales USING (product_id)
