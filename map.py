import folium
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
map.add_child(folium.Marker(
    location=[38.2, -99.1], popup="marker", icon=folium.Icon(color='green')))

map.save("map1.html")
