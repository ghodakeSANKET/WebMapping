import folium

import pandas


data=pandas.read_csv("airports.csv")  #taking airport csv file

print(data)

lat=list(data["latitude"])  #data of longitude from csv file
lon=list(data["longitude"])   # data of latitude from csv file

map=folium.Map(location=[38.58,-99.09])  #set primary location

for i,j in zip(lat,lon):
    map.add_child(folium.Marker(location=[i,j],popup="airport location in USA", icon=folium.Icon(color="green")))

map.save("map1.html")  #save map file