# Thanks to this S.O question: https://es.stackoverflow.com/questions/365497/cambiar-datos-columna-de-dataframe-usando-regex/367093


import pandas as pd
# Import regex module
import re

# Create an example dataframe
df = pd.DataFrame(pd.date_range(start='1-1-2020', end ='1-6-2020', freq='12H'), columns=['date'])

# If print(df), the data is:

#                   date
# 0  2020-01-01 00:00:00
# 1  2020-01-01 12:00:00
# 2  2020-01-02 00:00:00
# 3  2020-01-02 12:00:00
# 4  2020-01-03 00:00:00
# 5  2020-01-03 12:00:00
# 6  2020-01-04 00:00:00
# 7  2020-01-04 12:00:00
# 8  2020-01-05 00:00:00
# 9  2020-01-05 12:00:00
# 10 2020-01-06 00:00:00

# We need to separe 31-12-1999
# Then, we can use the following regular expresion: ((\d{4})\-(0[1-9]|1[012])\-(0[1-9]|[12]\d|3[01]))

expresion_regular = "((\d{4})\-(0[1-9]|1[012])\-(0[1-9]|[12]\d|3[01]))"
print(df['date'].astype(str).str.extract(pat = expresion_regular))

# Result:

#                0     1   2   3
#   0   2020-01-01  2020  01  01
#   1   2020-01-01  2020  01  01
#   2   2020-01-02  2020  01  02
#   3   2020-01-02  2020  01  02
#   4   2020-01-03  2020  01  03
#   5   2020-01-03  2020  01  03
#   6   2020-01-04  2020  01  04
#   7   2020-01-04  2020  01  04
#   8   2020-01-05  2020  01  05
#   9   2020-01-05  2020  01  05
#   10  2020-01-06  2020  01  06