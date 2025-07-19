import folium

# Coordenadas centrais do Japão
mapa_tokyo = folium.Map(location=[36.2048, 138.2529], zoom_start=5,
    tiles="CartoDB positron" )

# Locais famosos
locais = [
    {"nome": "Monte Fuji", "coordenadas": [35.3606, 138.7274]},
    {"nome": "Templo Kiyomizu-dera", "coordenadas": [34.9949, 135.7850]},
    {"nome": "Torre de Tóquio", "coordenadas": [35.6586, 139.7454]},
    {"nome": "Castelo de Osaka", "coordenadas": [34.6873, 135.5259]},
    {"nome": "Santuário Fushimi Inari", "coordenadas": [34.9671, 135.7727]},
    {"nome": "Hiroshima Peace Memorial", "coordenadas": [34.3955, 132.4536]},
    {"nome": "Teste", "coordenadas": [34.3955, 132.4536]}
]

# Adiciona marcadores com popups
for local in locais:
    folium.Marker(
        location=local["coordenadas"],
        popup=local["nome"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(mapa_tokyo)

# Guarda o mapa num ficheiro HTML
mapa_tokyo.save("mapa_tokyo.html")
