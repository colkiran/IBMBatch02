
import pandas as pd

data = {
    "name": ['Sachin', 'Sehwag', 'Rahul', 'Sourav', 'Yuvraj'],
    "runs": [120, 86, 93, 76, 80],
    "opponent" : ['WI', 'PAK', 'ENG', 'SA', 'AUS'],
    "gender": ['m', 'm', 'm', 'm', 'm']
}
print(f"data :{data}")
sportsDF = pd.DataFrame(data)
print("-" * 60)

print(f"Sports Dataframe :\n{sportsDF}")

print("-" * 60)

colDF = pd.DataFrame(data, columns=['Names', 'Runs', 'Opponent', 'Gender'])
print(colDF)

print("-" * 60)
print(sportsDF.head(3))

print("-" * 60)
print(sportsDF.tail(3))

print("-" * 60)
data = pd.read_csv("C:\\Training\\PycharmProjects\\IBMBatch02\\Day11\\vgsalesGlobale.csv")
print(data)

print("-" * 60)
print(data['Name'].sort_values(ascending=False))

print("-" * 60)
print(data.sort_values("Name"))

print("-" * 60)
print(data.sort_values(["Year", "Name"]))