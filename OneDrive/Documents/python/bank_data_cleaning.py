import pandas as pd
import numpy as np

df=pd.read_csv("bank_marketing.csv")


client_columns=["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]
client=df[client_columns]
campaign_columns=["client_id", "number_contacts", "contact_duration", 
                    "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "day", "month"]
campaign=df[campaign_columns]

month_map = {
    'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
    'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
}

campaign['last_contact_date']=pd.to_datetime('2022-' + campaign['month'].map(month_map) +'-'  + campaign['day'].astype(str), format= '%Y-%m-%d')
campaign=campaign.drop(columns=['day', 'month'])

economics_columns=["client_id", "cons_price_idx", "euribor_three_months"]
economics=df[economics_columns]

print("client data")
print(client.head())
print("campaign data")
print(campaign.head())
print("economics data")
print(economics.head())


import numpy as np
import pandas as pd

client["education"] = client["education"].str.replace(".", "_", regex=True).replace("unknown", np.NaN)
client["job"] = client["job"].str.replace(".", "_", regex=True)

# Check if 'campaign_outcome' column exists in the campaign DataFrame
if "campaign_outcome" in campaign.columns:
    campaign["campaign_outcome"] = campaign["campaign_outcome"].map({"yes": 1, "no": 0}).astype(bool)

if "previous_outcome" in campaign.columns:
    campaign["previous_outcome"] = campaign["previous_outcome"].map({"success": 1, "failure": 0, "nonexistent": 0}).astype(bool)

campaign["year"] = "2022"

# Check if 'day' column exists in the campaign DataFrame
if "day" in campaign.columns:
    campaign["day"] = campaign["day"].astype(str)

if "last_contact_date" in campaign.columns:
    campaign["last_contact_date"] = pd.to_datetime(campaign["last_contact_date"], format="%Y-%m-%d")

# Drop columns only if they exist in the DataFrame
columns_to_drop = ["month", "day", "year"]
existing_columns_to_drop = [col for col in columns_to_drop if col in campaign.columns]
campaign.drop(columns=existing_columns_to_drop, inplace=True)

print(client.head())
print("campaign data")
print(campaign.head())


client.to_csv("client.csv", index=False)

campaign.to_csv("campaign.csv", index=False)

economics.to_csv("economics.csv", index=False)

print("data frames saved as csv")