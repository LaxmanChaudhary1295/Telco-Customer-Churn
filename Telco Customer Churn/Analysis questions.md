Section 1 — Pandas (10 Questions)

Data analysis, grouping, aggregation, filtering

Q1. Overall Churn Rate
What is the overall churn percentage in the company?
How many customers are retained vs churned?

Q2. Churn by Contract Type
Compare churn rates across different Contract types.
Which contract has the highest churn and why might that be?

Q3. Tenure Impact
Analyze how tenure affects churn.
Do customers with lower tenure churn more?

Q4. Monthly Charges Segmentation
Segment customers into 3 buckets based on MonthlyCharges:
Low, Medium, High.
Compare churn rate across these buckets.

Q5. Service Usage vs Churn
Analyze churn rate for customers using:
Internet Service
Online Security
Tech Support
Which services seem to reduce churn?

Q6. Payment Method Analysis
Compare churn across PaymentMethod.
Which payment method has the worst churn and what is the business risk?

Q7. Senior Citizens Risk
Compare churn for SeniorCitizen = Yes vs No.
Is age a strong churn driver?

Q8. Revenue at Risk
Calculate total MonthlyCharges lost due to churn.
Which customer segment contributes most to revenue loss?

Q9. Multi-Service Customers
Compare churn for customers with:
Multiple services
Only one service
Do bundled customers churn less?

Q10. High-Risk Customer Profile (Advanced)
Create a high-risk segment definition using at least 3 features
(e.g. short tenure + high charges + month-to-month).
How many customers fall into this segment?

Section 2 — NumPy (4 Questions)

Statistics, percentages, conditions

Q11. Statistical Difference
Using NumPy, compare average MonthlyCharges for churned vs retained customers.
Is the difference statistically meaningful?

Q12. Percentile Analysis
Find the 90th percentile of MonthlyCharges.
What is the churn rate among customers above this threshold?

Q13. Outlier Detection
Detect outliers in TotalCharges using Z-score or IQR.
Are high-value customers more likely to churn?

Q14. Revenue Contribution
Using NumPy, calculate what percentage of total revenue comes from churned customers.

Section 3 — SQL (6 Questions)
GROUP BY, CASE WHEN, business logic
Assume table name: telco_customers

Q15. Churn Summary
Write a SQL query to show:
Total customers
Churned customers
Churn percentage

Q16. Contract-wise Churn
Find churn rate per Contract using GROUP BY.

Q17. Service Impact
Using CASE WHEN, calculate churn rate for:
Customers with TechSupport
Customers without TechSupport

Q18. Revenue Loss by Segment
Find total MonthlyCharges lost due to churn for each InternetService type.

Q19. Tenure Buckets (Advanced)
Create tenure groups using CASE WHEN:
0–12 months
13–24 months
25+ months
Find churn rate for each bucket.

Q20. High-Risk SQL Segment (Advanced)
Write a query to identify customers who:
Are on Month-to-month contract
Have MonthlyCharges above average
Have Tenure < 12
How many such customers exist?

Section 4 — Visualization (6 Questions)
Matplotlib / Seaborn

Q21. Churn Distribution
Create a countplot of Churn.
What does this tell you about the business problem?

Q22. Contract vs Churn
Create a bar chart showing churn rate by Contract.

Q23. Charges vs Churn
Create a boxplot of MonthlyCharges by Churn.
Do churned customers pay more?

Q24. Tenure vs Churn
Create a histogram or KDE plot of Tenure for churned vs retained customers.

Q25. Correlation Heatmap
Create a heatmap of correlations for numeric features.
Which variables correlate most with churn?

Q26. Multi-Factor Visualization (Advanced)
Create a visualization that shows churn across:
Contract
MonthlyCharges
Tenure
All in one meaningful chart.

Section 5 — Power BI (4 Tasks)
Business dashboard thinking

Q27. Executive KPI Dashboard
Create KPIs:
Total customers
Churn rate
Revenue lost
Average tenure of churned customers

Q28. Churn Driver Dashboard
Create visuals for:
Contract vs Churn
Payment Method vs Churn
Internet Service vs Churn

Q29. Customer Segmentation Dashboard
Create slicers for:
Contract
Tenure
MonthlyCharges
Allow business users to explore churn.

Q30. Retention Strategy Dashboard (Advanced)
Design a dashboard that helps management:
Identify high-risk customers
Estimate revenue at risk
Decide where to invest retention budget