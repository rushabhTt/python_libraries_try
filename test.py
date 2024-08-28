import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myVar = pd.DataFrame(mydataset)

# print(myVar, pd.__version__)

# a = [45, 78, 90]

# myVar2 = pd.Series(a, index = ["j", "k", "u"])
# print(myVar2)

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(pd.Series(calories))
# print(myvar)




# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar[["calories", "duration"]])



# df = pd.read_csv('data.csv')

# print(df.to_string()) 




# pd.options.display.max_rows = 9999

# df = pd.read_csv('data.csv')

# print(df) 




# df = pd.read_json('data.json')

# print(df.to_string()) 




# df = pd.read_csv('data.csv')

# print(df.head(11))
# print(df.info())


# new_df = df.dropna()
# print(new_df.to_string())


# df.dropna(inplace = True)
# print(df.to_string())


# df = pd.read_csv('data.csv')
# df.fillna(130, inplace = True)


# df = pd.read_csv('data.csv')
# df["Calories"].fillna(130, inplace = True)
# print(df.to_string())


df = pd.read_csv('data.csv')
# x = df["Calories"].median()         # or mean or mode()[0] (since mode can have multiple values)

# df["Calories"].fillna(x, inplace = True)



print(df.corr())