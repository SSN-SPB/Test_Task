# a
import pandas as pd
import folium
import geopandas
# b
m = folium.Map(location=[0,0], zoom_start=2)
# c
m.save("mymap.html")
# e
political_countries = geopandas.read_file("world-countries.json")
folium.GeoJson(political_countries, name="Political World Map").add_to(m)
m.save("mymap.html")
# f
wh = pd.read_csv("2019.csv")
# Check the difference of notation of country name
set(political_countries["name"])-set(wh["Country or region"])
set(wh["Country or region"])-set(political_countries["name"])
# Correct the difference
wh.loc[wh["Country or region"] == "United States", "Country or region"] = "United States of America"
wh.loc[wh["Country or region"] == "Trinidad & Tobago", "Country or region"] = "Trinidad and Tobago"
wh.loc[wh["Country or region"] == "Tanzania", "Country or region"] = "United Republic of Tanzania"
wh.loc[wh["Country or region"] == "Serbia", "Country or region"] = "Republic of Serbia"
wh.loc[wh["Country or region"] == "Palestinian Territories", "Country or region"] = "West Bank"
wh.loc[wh["Country or region"] == "North Macedonia", "Country or region"] = "Macedonia"
wh.loc[wh["Country or region"] == "Congo (Brazzaville)", "Country or region"] = "Republic of the Congo"
wh.loc[wh["Country or region"] == "Congo (Kinshasa)", "Country or region"] = "Democratic Republic of the Congo"
#Visualize the World Map
folium.Choropleth(geo_data="world-countries.json",
                  name="Happiness Score",
                  data=wh,
                  columns=["Country or region", "Score"],
                  key_on="feature.properties.name",
                  fill_color="YlGnBu",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  nan_fill_color="white",
                  legend_name="Happiness Score",
                  show=False
).add_to(m)
m.save("mymap.html")
# h
# Scatter plot matrix to choose data for layers
import seaborn as sns
data = wh[["Score", "GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]]
ax = sns.pairplot(data, diag_kind="kde")
print(ax)
# GDP per capita
folium.Choropleth(geo_data="world-countries.json",
                  name="GDP per capita",
                  data=wh,
                  columns=["Country or region", "GDP per capita"],
                  key_on="feature.properties.name",
                  fill_color="PuBu",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  nan_fill_color="white",
                  legend_name="GDP per capita",
                  show=False
).add_to(m)
# Social support
folium.Choropleth(geo_data="world-countries.json",
                  name="Social support",
                  data=wh,
                  columns=["Country or region", "Social support"],
                  key_on="feature.properties.name",
                  fill_color="BuGn",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  nan_fill_color="white",
                  legend_name="Social support",
                  show=False
).add_to(m)
# Healthy life expectancy
folium.Choropleth(geo_data="world-countries.json",
                  name="Healthy life expectancy",
                  data=wh,
                  columns=["Country or region", "Healthy life expectancy"],
                  key_on="feature.properties.name",
                  fill_color="RdPu",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  nan_fill_color="white",
                  legend_name="Healthy life expectancy",
                  show=False
).add_to(m)
m.save("mymap.html")
# Pop-up names
folium.features.GeoJson('world-countries.json', name="Names", popup=folium.features.GeoJsonPopup(fields=['name'], aliases=["Name"])).add_to(m)
m.save("mymap.html")
# Layers
folium.LayerControl(collapsed=False).add_to(m)
m.save("mymap.html")
