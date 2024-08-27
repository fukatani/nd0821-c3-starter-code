import pandas

df = pandas.read_csv("./data/census.csv")
df = df.drop_duplicates()
df = df.rename(columns=lambda s: s.strip())
df.to_csv("./data/cleaned_census.csv", index=False)
