import pandas as pd
from moon import signal, Regbot
from tothemoon.moon import signal as sig

df = pd.read_csv('/home/defi/Desktop/portfolio/projects/python/jupyter/tothemoon_validation_v011.csv')
print(df.columns)
def getSignal(open,close,utcdatetime):
    return signal(open,close,utcdatetime)

# select long profitable trades

print(df.head())

# Run all predictions
df['enter_long_pred'] = df.apply(lambda row: getSignal(row['open'], row['close'], row['date']), axis=1)


print(df.head(15))