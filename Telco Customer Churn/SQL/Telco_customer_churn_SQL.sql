CREATE DATABASE telco_db;
USE telco_db;

select * from telco_customer_churn;

-- Q15. Churn Summary
-- Write a SQL query to show:
-- Total customers
-- Churned customers
-- Churn percentage 
select count(*) as Total_Customers,
sum(case when Churn = "Yes" then 1 else 0 end) as Churned_Customers,
round(
sum(case when Churn = "Yes" then 1 else 0 end)*100
/ count(*), 
2
) as Churn_Percentage 
from telco_customer_churn;

-- Q16. Contract-wise Churn
-- Find churn rate per Contract using GROUP BY.
select Contract,
round(
sum(case when Churn = "Yes" then 1 else 0 end)
/ count(*)*100, 
2
) as Churn_Rate
from telco_customer_churn
group by(Contract);

-- Q18. Revenue Loss by Segment
-- Find total MonthlyCharges lost due to churn for each InternetService type.
select InternetService,
round(
sum(case when Churn = "Yes" then MonthlyCharges else 0 end)
) as Revenue_Loss 
from telco_customer_churn
group by(InternetService);

-- Q19. Tenure Buckets (Advanced)
-- Create tenure groups using CASE WHEN:
-- 0–12 months
-- 13–24 months
-- 25+ months
-- Find churn rate for each bucket.
select
case
when tenure between 0 and 12 then "0-12 Months"
when tenure between 13 and 24 then "13-24 Months"
else "25+ Months" 
end
as Tenure_Bucket,
round(
sum(case when Churn = "Yes" then 1 else 0 end)*100
/ count(*), 
2
) as Churn_Percentage
from telco_customer_churn
group by (Tenure_Bucket);

-- Q20. High-Risk SQL Segment (Advanced)
-- Write a query to identify customers who:
-- Are on Month-to-month contract
-- Have MonthlyCharges above average
-- Have Tenure < 12
-- How many such customers exist?

select count(*) as High_Risk_Customers 
from telco_customer_churn
where Contract = "Month-to-month"
and 
MonthlyCharges > (
  select avg( MonthlyCharges) from telco_customer_churn
)
and 
tenure < 12;

