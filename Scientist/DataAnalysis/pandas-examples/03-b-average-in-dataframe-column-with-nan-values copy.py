# Thanks to this S.O question: https://es.stackoverflow.com/questions/386319/pandas-promedio-columna-dataframe/386323

# See the another example: 03-a-average-in-dataframe-column-with-nan-values.py
# Example dataframe:

#    Numbers_One  Numbers_Two
# 0        10.05        11.04
# 1         5.23        15.00
# 2         2.22         4.65
# 3          NaN          NaN


# In this case, we don't use fillna. We don't need the empty values as 0 value in the average:

import pandas as pd

data = [[10.05, 11.04], [5.23, 15], [2.22, 4.65], [None, None]]

df = pd.DataFrame(data, columns = ['Numbers_One', 'Numbers_Two'])

# We calc: 10.05, 5.23, 2.22 (we don't include the NaN value in this average)
print(df['Numbers_One'].mean(skipna = True))

# Result: 5.833333333333333
