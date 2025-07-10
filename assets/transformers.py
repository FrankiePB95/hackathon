# create a file for transformers

import numpy as np
import seaborn as sb
import matplotlib as mb
import matplotlib.pyplot as plt
import plotly as pl
import pandas as pd
import sklearn as sk
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import feature_engine as fe

# drop specific columns
def drop_columns(bc):
    return bc.drop(columns=["CLIENTNUM", "Dependent_count", "Education_Level", "Marital_Status", "Card_Category", "Total_Relationship_Count", "Contacts_Count_12_mon", "Total_Revolving_Bal", "Avg_Open_To_Buy", "Total_Amt_Chng_Q4_Q1", "Total_Ct_Chng_Q4_Q1", "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1", "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"], errors="ignore")

# convert data types
def convert_data_types(bc):
    if "Attrition_Flag" in bc.columns:
        bc["Attrition_Flag"] = bc["Attrition_Flag"].astype(str)
    if "Customer_Age" in bc.columns:
        bc["Customer_Age"] = bc["Customer_Age"].astype(int)
    if "Gender" in bc.columns:
        bc["Gender"] = bc["Gender"].astype(str)
    if "Income_Category" in bc.columns:
        bc["Income_Category"] = bc["Income_Category"].astype(str)
    if "Months_on_book" in bc.columns:
        bc["Months_on_book"] = bc["Months_on_book"].astype(int)
    if "Months_Inactive_12_mon" in bc.columns:
        bc["Months_Inactive_12_mon"] = bc["Months_Inactive_12_mon"].astype(int)
    if "Credit_Limit" in bc.columns:
        bc["Credit_Limit"] = bc["Credit_Limit"].astype(float)
    if "Total_Trans_Amt" in bc.columns:
        bc["Total_Trans_Amt"] = bc["Total_Trans_Amt"].astype(int)
    if "Total_Trans_Ct" in bc.columns:
        bc["Total_Trans_Ct"] = bc["Total_Trans_Ct"].astype(int)
    if "Avg_Utilization_Ratio" in bc.columns:
        bc["Avg_Utilization_Ratio"] = bc["Avg_Utilization_Ratio"].astype(float)
    return bc

# remove outliers using IQR method
def remove_outliers(bc):
    columns = ["Customer_Age", "Months_on_book", "Months_Inactive_12_mon", "Credit_Limit", "Total_Trans_Amt", "Total_Trans_Ct", "Avg_Utilization_Ratio"]
    bc_one = bc.copy()
    
    for col in columns:
        if col in bc_one.columns: 
            Q1 = bc_one[col].quantile(0.25)
            Q3 = bc_one[col].quantile(0.75)
            IQR = Q3 - Q1
            bc_two = (bc_one[col] >= Q1 - 1.5 * IQR) & (bc_one[col] <= Q3 + 1.5 * IQR)
            bc_one = bc_one[bc_two]
    
    return bc_one

# rename columns
def rename_columns(bc):
    return bc.rename(columns={
        "Customer_Age": "Age",
        "Attrition_Flag": "Customer_Status",
        "Income_Category": "Income_Level",
        "Months_on_book": "Tenure_Months",
        "Months_Inactive_12_mon": "Inactive_Months_in_Last_12",
        "Total_Trans_Amt": "Total_Trans_Amount",
        "Total_Trans_Ct": "Total_Trans_Count"
    })

# capitalize column names
def capitalize_columns(bc):
    bc.columns = [col.title() for col in bc.columns]
    return bc

# drop missing values
def drop_missing_values(bc):
    return bc.dropna()

# remove duplicates
def remove_duplicates(bc):
    return bc.drop_duplicates()

# round numerical values
def round_values(bc):
    return bc.round(2)

# scale numerical values and encode categorical values
scaling_transformer = ColumnTransformer([
    ("num", StandardScaler(), ["Age", "Tenure_Months", "Inactive_Months_In_Last_12", "Credit_Limit", "Total_Trans_Amount", "Total_Trans_Count", "Avg_Utilization_Ratio"]), 
    ("cat", OneHotEncoder(), ["Customer_Status", "Gender", "Income_Level"])  
])

# define transformers
drop_columns_transformer = FunctionTransformer(drop_columns)
convert_data_types_transformer = FunctionTransformer(convert_data_types)
remove_outliers_one_transformer = FunctionTransformer(remove_outliers)
rename_columns_transformer = FunctionTransformer(rename_columns)
capitalize_columns_transformer = FunctionTransformer(capitalize_columns)
drop_missing_values_transformer = FunctionTransformer(drop_missing_values)
remove_duplicates_transformer = FunctionTransformer(remove_duplicates)
round_values_transformer = FunctionTransformer(round_values)

# fit the pipeline
pipeline = Pipeline([
    ("drop_cols", FunctionTransformer(drop_columns)),
    ("drop_missing", FunctionTransformer(drop_missing_values)),
    ("remove_duplicates", FunctionTransformer(remove_duplicates)),
    ("remove_outliers", FunctionTransformer(remove_outliers)),
    ("convert_types", FunctionTransformer(convert_data_types)),
    ("rename", FunctionTransformer(rename_columns)),
    ("capitalize", FunctionTransformer(capitalize_columns)),
    ("round_values", FunctionTransformer(round_values))
])
