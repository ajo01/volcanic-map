import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano Information</h4>
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br>
Height: %sm
"""


def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fg_vol = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (
        nm, nm, str(el)), width=200, height=100)
    fg_vol.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(
        iframe), radius=8, fill_color=color_producer(el), color='grey', fill_opacity=0.7))


fg_pop = folium.FeatureGroup(name="Population")

fg_pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fg_vol)
map.add_child(fg_pop)
map.add_child(folium.LayerControl())
map.save("map1.html")
