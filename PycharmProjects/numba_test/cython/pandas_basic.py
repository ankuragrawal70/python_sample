import pandas as pd
import numpy as np
from datetime import date
from dateutil import relativedelta
# current_date = date.today()
# prev_date = current_date - relativedelta.relativedelta(years=1)
# print prev_date
# dates = pd.date_range(start=prev_date, end=current_date, freq='B')
# print len(dates.to_frame())
#
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# print s
# print type(s)
# print type(s.values)

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index,
                   columns=['A', 'B', 'C'])

print(df)

print type(df.iloc[0])
print df.sub(df.iloc[0], axis='columns')