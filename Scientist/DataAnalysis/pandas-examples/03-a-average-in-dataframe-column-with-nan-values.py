# Thanks to this S.O question: https://es.stackoverflow.com/questions/386319/pandas-promedio-columna-dataframe/386323

# Example dataframe:

#    Numbers_One  Numbers_Two
# 0        10.05        11.04
# 1         5.23        15.00
# 2         2.22         4.65
# 3          NaN          NaN

import pandas as pd

# Create a list with data lists (one of then with NaN values)
data = [[10.05, 11.04], [5.23, 15], [2.22, 4.65], [None, None]]

# Create a dataframe with the data list and set columns names:
df = pd.DataFrame(data, columns = ['Numbers_One', 'Numbers_Two'])

# Fill NaN values with 0:
df['Numbers_One'] = df['Numbers_One'].fillna(0)

# IMPORTANT: With fillna(0) we include the 0 values in our average calc:

# 10.05
# 5.23
# 2.22
# 0


# Print column average:
print(df['Numbers_One'].mean())

# 4.375
