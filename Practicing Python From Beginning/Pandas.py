import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
print(df)
print(pd.options.display.max_rows)
print(df.head())
print(df.tail())
print(df.info())

'''a = [1,7,2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])'''

'''data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[0, 1])'''