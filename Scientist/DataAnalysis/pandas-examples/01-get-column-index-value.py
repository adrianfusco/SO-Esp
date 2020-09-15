# Thanks to this S.O question: https://es.stackoverflow.com/questions/383251/como-obtener-un-valor-de-una-columna-de-grupo-en-un-dataframe/383255

# Import pandas
import pandas as pd

# Create a list with two data lists:
data = [
['2020-08-19', '21.12', '21.71', '20.87', '21.71', '635549', 'EUR'],
['2020-08-18', '21.00', '21.67', '20.81', '21.15', '631806', 'EUR']
]

# Convert it into a dataframe and set columns names:
df = pd.DataFrame(data, columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Currency'])

# Set dataframe index:
df = df.set_index('Date')

# Dataframe value:

#	             Open   High    Low  Close  Volume Currency
#	Date                                                   
#	2020-08-19  21.12  21.71  20.87  21.71  635549      EUR
#	2020-08-18  21.00  21.67  20.81  21.15  631806      EUR

# if print(df.index)
# Index(['2020-08-19', '2020-08-18'], dtype='object', name='Date')

# Access to index column:
print(df.index[0])

# Result 
# 2020-08-19

