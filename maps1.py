import pandas as pd
import folium

df = pd.read_csv(r'D:\Maps\basindata\wells1.csv')
df.head()

map = folium.Map(16.418,91.968)


for index,df in df.iterrows():
    location = [df.Latitude, df.Longitude]
    folium.Maker(location,popup=f'Name:{df.weel_name}').add_to(map)

map.save('D:\wells1.html')