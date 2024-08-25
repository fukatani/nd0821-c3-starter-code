import pandas

df = pandas.read_csv("./data/census.csv")
df.drop_duplicates()
df.to_csv("./data/cleaned_census.csv")
