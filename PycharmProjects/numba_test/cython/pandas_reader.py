import pandas as pd
d = pd.read_csv("/home/an.agrawal1/Downloads/SalesJan2009.csv")
print type(d['Transaction_date'][0])