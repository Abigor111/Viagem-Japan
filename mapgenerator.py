import folium

# Coordenadas centrais do Japão
mapa_tokyo = folium.Map(location=[35.6895, 139.6917], zoom_start=8,
    tiles="CartoDB dark_matter" )
water_icon = folium.Icon(icon="tint", prefix='fa', color='blue')
# Locais famosos
locais = [
    {"nome": "Monte Fuji", "coordenadas": [35.3606, 138.7274], "preco": "...", "icon": water_icon},
    {"nome": "Tokyo Tower", "coordenadas": [35.6586, 139.7454], "preco": "Tokyo Pass", "icon": "camera"},
]

# Adiciona marcadores com popups
for local in locais:
    if local["preco"] == "Tokyo Pass":
        folium.Marker(
            location=local["coordenadas"],
            popup=local["nome"],
            icon=folium.Icon(color="green", icon="info-sign")
        ).add_to(mapa_tokyo)
    else:
        folium.Marker(
            location=local["coordenadas"],
            popup=local["nome"],
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(mapa_tokyo)
# Guarda o mapa num ficheiro HTML
mapa_tokyo.save("mapa_tokyo.html")
# Coordenadas centrais do Japão
mapa_kyouto = folium.Map(location=[35.0116, 135.7681], zoom_start=7,
    tiles="CartoDB dark_matter" )

# Locais famosos
locais = [

]

# Adiciona marcadores com popups
for local in locais:
    folium.Marker(
        location=local["coordenadas"],
        popup=local["nome"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(mapa_kyouto)

# Guarda o mapa num ficheiro HTML
mapa_kyouto.save("mapa_kyouto.html")
# Coordenadas centrais do Japão
mapa_hokkaido = folium.Map(location=[43.2203, 142.8635], zoom_start=7,
    tiles="CartoDB dark_matter" )

# Locais famosos
locais = [
    {"nome": "Otaru Canal", "coordenadas": [43.200021, 141.001558]},
]

# Adiciona marcadores com popups
for local in locais:
    folium.Marker(
        location=local["coordenadas"],
        popup=local["nome"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(mapa_hokkaido)

# Guarda o mapa num ficheiro HTML
mapa_hokkaido.save("mapa_hokkaido.html")