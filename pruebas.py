import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
df['tamano_familiar'] = df['sibsp'] + df['parch']

df.loc[df['tamano_familiar'] == 0,'viajo_solo'] = "Sí"
df.loc[df['tamano_familiar'] != 0,'viajo_solo'] = "No"

print(df[['tamano_familiar','viajo_solo']])

