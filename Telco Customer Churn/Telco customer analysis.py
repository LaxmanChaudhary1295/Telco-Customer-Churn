
 
"""
Telco Customer Churn Analysis Project
Customer Churn Analysis Project
Author: Laxman R. Chaudhury
Tools: Python (Pandas, NumPy), SQL, Matplotlib, Seaborn, Power BI
Objective: Analyze telecom customer churn patterns and generate business insights.
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

tca = pd.read_excel("Dataset\\Telco_Customer_Churn.xlsx")
print(tca)
tca.columns = tca.columns.str.replace(" ", "")

#Q1
cc = (
    tca.
    groupby(
        "Churn", as_index=False
        ).
    agg(
        Customers_Count = ("customerID", "count")
    )
)

total_customers = tca["customerID"].count()

cc["churn_percentage"] = (cc["Customers_Count"]/total_customers*100
).round(2)
print(cc)


#Q2
contract_types = (
    tca
    .groupby(
        "Contract", as_index=False
    ).agg(
        Customer_Count = ("customerID","count"),
        Churned_Customers = ("Churn", lambda x: (x=="Yes").sum())
    )
)

contract_types["Churn Rate (%)"] =( contract_types["Churned_Customers"]
                                   /contract_types["Customer_Count"]*100)
print(contract_types.sort_values("Churn Rate (%)",ascending=False))

#Q3
bins = [0, 12, 24, 48, 72, float("inf")]
labels = ["0-1 yr", "1-2 yrs", "2-4 yrs","4-5 yrs", "6+ yrs"]
tca["Tenure Bucket"] = pd.cut(
    tca["tenure"],
    bins = bins,
    labels=labels,
    include_lowest=True
)
tenure_impact = (
    tca.
    groupby(
        "Tenure Bucket" , as_index=False
    ).
    agg(
        Customer_Count = ("customerID", "nunique"),
        Churned_Customers = ("Churn", lambda x : (x== "Yes").sum())
    )
)
tenure_impact["Churn Rate (%)"] = (tenure_impact["Churned_Customers"]/
                                   tenure_impact["Customer_Count"] *100).round(2)
print(tenure_impact)

#4
bin = [0, 40, 80, 119, float("inf")]
labels = ["Very Low","Low", "Medium", "High"]

tca["MonthlyCharges Bucket"] = pd.cut(
    tca["MonthlyCharges"], 
    bins =bin,
    labels=labels,
    include_lowest=True
)

Monthly_Charges_Segmentation = (
    tca.
    groupby(
        "MonthlyCharges Bucket", as_index=False
    ).
    agg(
        Customer_Count = ("customerID", "nunique"),
        Churned_Customers = ("Churn", lambda x : (x== "Yes").sum())
    )
)
Monthly_Charges_Segmentation["Churn Rate (%)"] = (Monthly_Charges_Segmentation["Churned_Customers"]/
                                   Monthly_Charges_Segmentation["Customer_Count"] 
                                   *100).round(2)
print(Monthly_Charges_Segmentation)

#5
Services = ["InternetService", "OnlineSecurity", "TechSupport"]
for col in Services:
    result = (
        tca
        .groupby(col, as_index=False)
        .agg(
            Customer_Count=("customerID", "nunique"),
            Churned_Customers=("Churn", lambda x: (x == "Yes").sum())
        )
    )

    result["Churn Rate (%)"] = (
        result["Churned_Customers"] /
        result["Customer_Count"] * 100
    ).round(2)

    print(f"\nChurn by {col}")
    print(result)

#6
Payment_Method_Analysis = (
    tca.
    groupby(
        "PaymentMethod", as_index=False
    ).
    agg(
        Customer_Count = ("customerID", "nunique"),
        Churned_Customers = ("Churn", lambda x : (x== "Yes").sum())
    )
)
Payment_Method_Analysis["Churn Rate (%)"] = (Payment_Method_Analysis ["Churned_Customers"]/
                                   Payment_Method_Analysis ["Customer_Count"] 
                                   *100).round(2)
print(Payment_Method_Analysis )
# Payment Method - Electronic check has worst churn rate 45.29%

#7 
SeniorCitizen_Churn = (
    tca
    .groupby("SeniorCitizen", as_index=False)
    .agg(
        Customer_Count=("customerID", "nunique"),
        Churned_Customers=("Churn", lambda x: (x == "Yes").sum())
    )
)

SeniorCitizen_Churn["Churn Rate (%)"] = (
    SeniorCitizen_Churn["Churned_Customers"] /
    SeniorCitizen_Churn["Customer_Count"] * 100
).round(2)

print(SeniorCitizen_Churn)

"""Senior citizens show slightly higher churn, 
suggesting price sensitivity and service usability 
factors rather than lack of interest. 
Targeted support programs and simplified plans 
may help reduce churn in this segment."""

#Q8
Revenue_at_Risk_Churn = (
    tca[tca["Churn"] == "Yes"].
    groupby(
        "Contract", as_index=False
    ).
    agg(
        Revenue_Lost =("MonthlyCharges", "sum"),
        Customer_Count = ("customerID", "nunique")
    )

)
Revenue_at_Risk_Churn["Average_Revenue_Lost_Per_Customer"] = (Revenue_at_Risk_Churn["Revenue_Lost"]
                                     /Revenue_at_Risk_Churn["Customer_Count"]
                                     ).round(2)

print(Revenue_at_Risk_Churn.sort_values("Revenue_Lost", ascending=False))

total_revenue_lost = tca.loc[
    tca["Churn"] == "Yes", "MonthlyCharges"
].sum()

print("Total Monthly Revenue Lost:", total_revenue_lost)

"""The company’s revenue exposure is concentrated in the 
month-to-month segment, indicating high volatility in 
recurring revenue and the need for 
contract-conversion retention strategies."""


#Q9

service_cols = [
    "PhoneService",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies"
]

tca["Service_Count"] = (
    tca[service_cols] == "Yes"
).sum(axis=1)

tca["Service_Type"] = np.where(
    tca["Service_Count"] >1,
    "Multiple Service",
    "Single Service"
)

multi_service_churn = (
    tca.
    groupby(
        "Service_Type", as_index=False
    ).
    agg(
        Customer_Count=("customerID", "nunique"),
        Churned_Customers=("Churn", lambda x: (x == "Yes").sum())
    )
)
multi_service_churn["Churn Rate (%)"] =(multi_service_churn["Churned_Customers"]/
                                        multi_service_churn["Customer_Count"]
                                        *100).round(2)
print(multi_service_churn)

"""Multiple-service customers churn less
Single-service customers churn more"""

#Q10

tca["short tenure"] = tca["tenure"]<=12
tca["high charges"] = tca["MonthlyCharges"] >=80
tca["month-to-month"] = tca["Contract"] == "Month-to-month"

tca["high_risk_segment"] =(
    tca["short tenure"] &
    tca["high charges"] &
    tca["month-to-month"]
)

high_risk_segment = (
    tca.
    groupby(
        "high_risk_segment", as_index=False
    ).
    agg(
        Customer_Count=("customerID", "nunique"),
        Churned_Customers=("Churn", lambda x: (x == "Yes").sum())
    )
)
high_risk_segment["Customer Rate (%)"] = (
    high_risk_segment["Churned_Customers"]/high_risk_segment["Customer_Count"]*100
).round(2)

print(high_risk_segment)

"""Customers with short tenure, high 
charges and month-to-month segmnet around 73.29% customers fall"""

#Q11
charges_churned = tca.loc[
    tca["Churn"] == "Yes", "MonthlyCharges"].values

charges_retained = tca.loc[
    tca["Churn"] == "No", "MonthlyCharges"].values

avg_churned = np.mean(charges_churned)
avg_retained = np.mean(charges_retained)

print("Average Monthly Charges(Churned):",round(avg_churned,2))
print("Average Monthly Charges(Retained):",round(avg_retained,2))


difference = avg_churned-avg_retained
print("Differance in Average Churned:", round(difference,2))

percent_diff = (difference / avg_retained) * 100
print("Percentage Difference:", round(percent_diff, 2), "%")

""" Customers who churn pay significantly higher average monthly charges, 
indicating that pricing pressure is likely a key churn driver."""

#Q12
p90 = np.nanpercentile(tca["MonthlyCharges"],90) 
high_charge_customers = tca[tca["MonthlyCharges"] > p90]

customer_count =high_charge_customers["customerID"].nunique()
churn_customers =( high_charge_customers["Churn"] == "Yes").sum()

Churn_Rate = churn_customers/customer_count*100

print("Monthly Charges above 90 percentile:",round(p90,2))
print("Customers above threshold:", customer_count)
print("The churn rate among customers above this threshold:", round(Churn_Rate,2))

#Q13
tca["TotalCharges"] = pd.to_numeric(
    tca["TotalCharges"],
    errors="coerce"
)

mean_value = np.mean(tca["TotalCharges"])
std_value = np.std(tca["TotalCharges"])

tca["Z score"] = (
    (tca["TotalCharges"] - mean_value)/std_value
    )

outlier = tca[abs(tca["Z score"])>3]

customer_count =outlier["customerID"].nunique()
churn_rate =(outlier["Churn"] == "Yes").sum()

Churn_Rate = churn_rate/customer_count*100


print("Number of outlier customers:", customer_count)
print("Churn rate among outliers:", round(churn_rate, 2))


#Q14

tca["TotalCharges"] = pd.to_numeric(
    tca["TotalCharges"],
    errors="coerce"
)
total_revenue = np.nansum(tca["TotalCharges"].values)

churned_revenu = np.nansum(tca.loc[
    tca["Churn"] == "Yes", "TotalCharges"
].values)

revenue_percentage = (churned_revenu/total_revenue)*100

print("Total Revenue:", total_revenue)
print("Revenue from churned customers:", churned_revenu)
print("Revenue from churned customers rate:", round(revenue_percentage,2))

#21

plt.figure(figsize=(6,6))

sns.countplot (data= tca, 
              x="Churn",
              order=("Yes", "No"),
              width = 0.5, 
              palette=["aqua", "Steelblue"],
              saturation=0.5,
              )
plt.xlabel("Churn")
plt.ylabel("Count")
plt.title("Countplot for Churn")
plt.tight_layout()
plt.show()

#Q22

cr_by_contract = (
    tca.groupby(
        "Contract", as_index=False
    ).agg(
        Customer_count = ("customerID", "nunique"),
        Churn_customers = ("Churn", lambda x:(x=="Yes").sum())
    )
)

cr_by_contract["Churn Rate (%)"] = (
    cr_by_contract["Churn_customers"] / cr_by_contract["Customer_count"]
    *100
).round(2)
print(cr_by_contract)

plt.figure(figsize=(10,6))
sns.barplot(
    data=cr_by_contract,
    x= "Contract",
    y = "Churn Rate (%)",
    width=0.3,
    palette=["sandybrown", "chocolate", "saddlebrown"],
    saturation=0.5,
    
            )
plt.xlabel("Contract")
plt.ylabel("Churn Rate (%)")
plt.title("Churn rate by Contract")
plt.tight_layout()
plt.show()

#Q23
plt.figure(figsize=(10,6))
sns.boxenplot(
    data=tca,
    x= "Churn",
    y="MonthlyCharges",
    palette=["yellowgreen", "darkolivegreen"]
    )
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.title("Monthly Charges by Churn")  
plt.tight_layout()
plt.show()
"""Churned customers have higher median MonthlyCharges"""

#Q24
plt.figure(figsize=(10,6))
sns.kdeplot(
    data=tca,
    x="tenure",
    hue="Churn",
    fill=True,
    common_norm=False,
    palette=["plum", "springgreen"]
)
plt.xlabel("Tenure")
plt.title("Tenure Distribution: Churned vs Retained Customers")
plt.tight_layout()
plt.show()




#Q25
tca["Churn Numeric"] = tca["Churn"].map({"Yes": 1, "No": 0})
numeric_df = tca.select_dtypes(include=["number"])
corr_matrix = numeric_df.corr()

sns.heatmap(
    corr_matrix,
    annot=True, 
    fmt=".2f",
    cmap="coolwarm",
    center=0
)
plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.show()

print(
    corr_matrix["Churn Numeric"]
    .sort_values(ascending=False)
)


#Q26


tca["Tenure Bucket"] = pd.cut(
    tca["tenure"],
    bins = [0, 12, 24, 48, 72, float("inf")],
    labels=["0-1 yr", "1-2 yrs", "2-4 yrs","4-6 yrs", "6+ yrs"],
    include_lowest=True
)

tca["Monthly Charges Bucket"] = pd.cut(
    tca["MonthlyCharges"],
    bins=[0,40,80,120, float("inf")],
    labels=["Very low", "Low", "Medium", "High"],
    include_lowest=True
)

churn_across = (
    tca
    .groupby(
        ["Contract", "Monthly Charges Bucket", "Tenure Bucket"],
        observed=True
    )
    .agg(
        Customer_Count=("customerID", "nunique"),
        Churn_customers=("Churn", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

churn_across["Churn Rate (%)"] = (
    churn_across["Churn_customers"] /
    churn_across["Customer_Count"] * 100
)

g = sns.FacetGrid(
    churn_across,
    col="Contract",
    col_wrap=3,
    height=4
)

g.map_dataframe(
    sns.scatterplot,
    x="Tenure Bucket",
    y="Monthly Charges Bucket",
    size="Churn Rate (%)",
    hue="Churn Rate (%)",
    palette="Reds",
    sizes=(50, 400),
    legend=False
)

g.set_axis_labels("Tenure Bucket", "Monthly Charges Bucket")
plt.tight_layout()
plt.show()


print("Key Insights:")
print("1. Highest churn observed in electronic check users")
print("2. Month-to-month contracts drive churn")
print("3. Short-tenure customers churn more")
