import pandas  as pd

url='https://www.espn.co.uk/football/team/squad/_/id/83/barcelona'
df=pd.read_html(url)

# print(df)

df_goalkeepers=df[0]
df_fieldplayers=df[1]

print(df_fieldplayers)
print("Age Mean value for players in the field is",round(df_goalkeepers.Age.mean(),2))
print("Age Mean value for players in the field is",round(df_fieldplayers.Age.mean(),2))