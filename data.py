import pandas as pd
from config import get_collection

def load_sales(flag=None):
    """flag=True for experiment, False for control"""
    coll = get_collection()
    query_filter = {}
    if flag is True:
        query_filter["experimentFlag"] = True
    elif flag is False:
        query_filter["experimentFlag"] = {"$ne": True}

    fields = {
        "_id": 0,
        "saleDate": 1,
        "storeLocation": 1,
        "couponUsed": 1,
        "purchaseMethod": 1,
        "customer": 1,
        "items": 1,
        "experimentFlag": 1,
        "age_group": 1,
    }
    return pd.DataFrame(list(coll.find(query_filter, fields)))

def flatten_customer(df):
    df["age"]    = df["customer"].apply(lambda x: x.get("age"))
    df["email"]  = df["customer"].apply(lambda x: x.get("email"))

    def age_to_group(age):
        if age is None:   return "unknown"
        if age < 18:
            return "<18"
        elif age < 25:
            return "18–24"
        elif age < 35:
            return "25–34"
        elif age < 50:
            return "35–49"
        elif age < 65:
            return "50–64"
        else:
            return "65+"

    df["age_group"] = df["age"].apply(age_to_group)
    return df.drop(columns=["customer"])
