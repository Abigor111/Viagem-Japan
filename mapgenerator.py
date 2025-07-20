import folium

mapa_tokyo = folium.Map(location=[35.6895, 139.6917], zoom_start=8,
    tiles="CartoDB Voyager" )

locais_tokyo = [
    {"nome": "Tokyo Tower", "coordenadas": [35.65890736822251, 139.7453899825577], "preco": "Tokyo Pass", "icon": "camera"},
    {"nome": "Tokyo Sea Life Park", "coordenadas": [35.64005411937297, 139.86223807091343], "preco": "Tokyo Pass", "icon": "water"},
    {"nome": "Edo-Tokyo Open Air Architectural Museum", "coordenadas": [35.71572025959437, 139.51198549845037], "preco": "...", "icon": "university"},
    {"nome": "Miraikan – The National Museum of Emerging Science and Innovation", "coordenadas": [35.619575653419105, 139.776378031249], "preco": "...", "icon": "flask"},
    {"nome": "Tama Zoological Park", "coordenadas": [35.6497541092538, 139.40326768440679], "preco": "...", "icon": "paw"},
    {"nome": "Kiyosumi Garden", "coordenadas": [35.68105022400575, 139.79732927091393], "preco": "...", "icon": "leaf"},
    {"nome": "Greenhouse Dome", "coordenadas": [35.65129094472841, 139.8294014555711], "preco": "...", "icon": "leaf"},
    {"nome": "Mukojima-Hyakkaen Gardens", "coordenadas": [35.72441480380048, 139.81562205557256], "preco": "...", "icon": "leaf"},
    {"nome": "Kyu-Isawaki Gardens", "coordenadas": [35.71000294230464, 139.76756264022998], "preco": "...", "icon": "leaf"},
    {"nome": "Akihabara", "coordenadas": [35.702294171531776, 139.77440869967648], "preco": "...", "icon": "gamepad"},
    {"nome": "Shibuya", "coordenadas": [35.658034, 139.701636], "preco": "...", "icon": "camera"},
    {"nome": "Yoyogi Park", "coordenadas": [35.66999941438408, 139.6949614931253], "preco": "...", "icon": "tree"},
    {"nome": "Meiji Jingu", "coordenadas": [35.67636218146025, 139.69933665145447], "preco": "...", "icon": "star"},
    {"nome": "Templo Senso-JI", "coordenadas": [35.7147973046263, 139.7966266229833], "preco": "...", "icon": "gopuram"},
    {"nome": "SMALL WORLDS Miniature Museum", "coordenadas": [35.63797508952107, 139.78836632673526], "preco": "...", "icon": "cube"},
    {"nome": "East Gardens", "coordenadas": [35.68679980089686, 139.75714449790038], "preco": "...", "icon": "tree"},
]


# Adiciona marcadores com popups
for local in locais_tokyo:
    description = f"<b style='font-size:16px'>{local['nome']}</b><br><br><b style='font-size:14px'>Preço:</b> {local['preco']}"
    if local["preco"] == "Tokyo Pass" or local["preco"] == "Grátis":
        folium.Marker(
            location=local["coordenadas"],
            popup=description,
            icon=folium.Icon(color="green", prefix="fa",icon=local["icon"])
        ).add_to(mapa_tokyo)
    else:
        folium.Marker(
            location=local["coordenadas"],
            popup=description,
            icon=folium.Icon(color="red", prefix="fa", icon=local["icon"])
        ).add_to(mapa_tokyo)
casa_tokyo1 = folium.Marker(
            location=[35.65735413872696, 139.7559189705854],
            popup="<b style='font-size:16px'>Hotel Capsula</b>",
            icon=folium.Icon(color="orange", prefix="fa", icon="house")
        )
casa_tokyo2 = folium.Marker(
            location=[35.54724048278734, 139.75089732430973],
            popup="<b style='font-size:16px'>Casa</b>",
            icon=folium.Icon(color="orange", prefix="fa", icon="house")
        )
casa_tokyo3 = folium.Marker(
            location=[35.54373671469915, 139.76593730508648],
            popup="<b style='font-size:16px'>Hotel Aeroporto</b>",
            icon=folium.Icon(color="orange", prefix="fa", icon="house")
        )
aeroporto_tokyo_1 = folium.Marker(
            location=[35.54790, 139.78878],
            popup="<b style='font-size:16px'>Aeroporto Haneda</b>",
            icon=folium.Icon(color="blue", prefix="fa", icon="plane")
        )
aeroporto_tokyo_2 = folium.Marker(
            location=[35.77655, 140.38275],
            popup="<b style='font-size:16px'>Aeroporto Narita</b>",
            icon=folium.Icon(color="blue", prefix="fa", icon="plane")
        )
casa_tokyo1.add_to(mapa_tokyo)
casa_tokyo2.add_to(mapa_tokyo)
casa_tokyo3.add_to(mapa_tokyo)
aeroporto_tokyo_1.add_to(mapa_tokyo)
aeroporto_tokyo_2.add_to(mapa_tokyo)
mapa_tokyo.save("mapa_tokyo.html")
# Kyouto
mapa_kyouto = folium.Map(location=[35.0116, 135.7681], zoom_start=8,
    tiles="CartoDB Voyager" )

locais_kyouto = [
    {"nome": "Mercado Nishiki", "coordenadas": [35.005280624534755, 135.76498048901183], "preco": "", "icon": "shopping-cart"},
    {"nome": "Gion", "coordenadas": [35.0037, 135.7788], "preco": "", "icon": "theater-masks"},
    {"nome": "Fushimi Inari", "coordenadas": [34.96794064879568, 135.7791339527735], "preco": "", "icon": "fire"},
    {"nome": "Templo Ryoan-Ji", "coordenadas": [35.03471389342938, 135.7182741257903], "preco": "", "icon": "gopuram"},
    {"nome": "Templo Tenryu-Ji", "coordenadas": [35.01603118308893, 135.67362592208914], "preco": "", "icon": "gopuram"},
    {"nome": "Templo Kinkaku-Ji", "coordenadas": [35.03950173734025, 135.7295756908635], "preco": "", "icon": "gopuram"},
    {"nome": "Sanjusangendo", "coordenadas": [34.98810421863275, 135.77208810620448], "preco": "", "icon": "church"},
    {"nome": "Rio Hozu", "coordenadas": [35.02687269714935, 135.65331407941872], "preco": "", "icon": "water"},
    {"nome": "Arashiyama", "coordenadas": [35.010210262021275, 135.6690008034045], "preco": "", "icon": "tree"},
    {"nome": "Templo Ginkaku-Ji", "coordenadas": [35.02714510777314, 135.79819456148633], "preco": "", "icon": "gopuram"},
    {"nome": "Templo das Águas Kyomizu-dera", "coordenadas": [34.99483316582546, 135.78543347312763], "preco": "", "icon": "water"},
    {"nome": "Floresta de Bambu", "coordenadas": [35.016880179859875, 135.6715909755194], "preco": "", "icon": "tree"},
    {"nome": "Templo Otagi Nenbutsu-Ji", "coordenadas": [35.03128333579624, 135.66202666572784], "preco": "", "icon": "gopuram"},
    {"nome": "Nara", "coordenadas": [34.6851, 135.8050], "preco": "Grátis", "icon": "paw"},
    {"nome": "Dotombori District", "coordenadas": [34.6687, 135.5012], "preco": "", "icon": "city"},
    {"nome": "Pontocho", "coordenadas": [35.00426323658411, 135.77128965065418], "preco": "", "icon": "road"},
    {"nome": "Samurai Ninja Museum", "coordenadas": [35.007410003468785, 135.76448997682854], "preco": "24€", "icon": "user-secret"},
    {"nome": "Monkey Park", "coordenadas": [35.01172889031941, 135.67760082100745], "preco": "5€", "icon": "paw"},
]


for local in locais_kyouto:
    description = f"<b style='font-size:16px'>{local['nome']}</b><br><br><b style='font-size:14px'>Preço:</b> {local['preco']}"
    if local["preco"] == "Grátis":
        folium.Marker(
            location=local["coordenadas"],
            popup=description,
            icon=folium.Icon(color="green", prefix="fa",icon=local["icon"])
        ).add_to(mapa_kyouto)
    else:
        folium.Marker(
            location=local["coordenadas"],
            popup=description,
            icon=folium.Icon(color="red", prefix="fa", icon=local["icon"])
        ).add_to(mapa_kyouto)
casa_kyouto = folium.Marker(
            location=[34.66285769453742, 135.51250832595048],
            popup="<b style='font-size:16px'>Casa</b>",
            icon=folium.Icon(color="orange", prefix="fa", icon="house")
        )
aeroporto_kyouto = folium.Marker(
            location=[34.4272990, 135.2440030],
            popup="<b style='font-size:16px'>Aeroporto</b>",
            icon=folium.Icon(color="blue", prefix="fa", icon="plane")
        )
casa_kyouto.add_to(mapa_kyouto)
aeroporto_kyouto.add_to(mapa_kyouto)
mapa_kyouto.save("mapa_kyouto.html")
# Hokkaido
mapa_hokkaido = folium.Map(location=[43.2203, 142.8635], zoom_start=6,
    tiles="CartoDB Voyager" )

locais_hokkaido = [
    {"nome": "Otaru Canal", "coordenadas": [43.200021, 141.001558], "preco": "", "icon": "water"},
    {"nome": "Hokkaido Greenland", "coordenadas": [43.166667, 141.779389], "preco": "30-50€", "icon": "skiing"},
    {"nome": "Lago Shikotsu", "coordenadas": [42.75686992226468, 141.32756937144265], "preco": "", "icon": "water"},
    {"nome": "Sakaimachi Street", "coordenadas": [35.00369024442211, 135.7631162698021], "preco": "", "icon": "road"},
    {"nome": "Otaru Tenguyama Ropeway", "coordenadas": [43.17202715396662, 140.97217398057697], "preco": "12€", "icon": "tram"},
    {"nome": "Shakotan Peninsula", "coordenadas": [43.234905014110986, 140.45860502609324], "preco": "", "icon": "tree"},
    {"nome": "Niseko", "coordenadas": [42.80529218595222, 140.6871088637589], "preco": "Onsen, Ski", "icon": "skiing"},
    {"nome": "Yoichi Town", "coordenadas": [43.195284135469684, 140.78509704551422], "preco": "", "icon": "whiskey-bottle"},
    {"nome": "Whiskey distillery", "coordenadas": [43.18737243313848, 140.79190114169398], "preco": "", "icon": "whiskey-glass"},
    {"nome": "Jozankei Onsen", "coordenadas": [42.97039989467906, 141.16768613077534], "preco": "", "icon": "hot-tub"},
    {"nome": "Mt. Observatório Okura", "coordenadas": [43.05096423026993, 141.28621229260673], "preco": "6€", "icon": "binoculars"},
    {"nome": "Nijo Market", "coordenadas": [43.05836952322021, 141.3583065231995], "preco": "", "icon": "shopping-cart"},
    {"nome": "Odori Park", "coordenadas": [43.06075913904715, 141.35443124395985], "preco": "", "icon": "tree"},
    {"nome": "Historic Village of Hokkaido", "coordenadas": [43.0484434022979, 141.49745683799244], "preco": "6€", "icon": "landmark"},
    {"nome": "Mt. Moiwa Ropeway", "coordenadas": [43.02265225798352, 141.3237415249309], "preco": "~20€", "icon": "tram"},
    {"nome": "Lake Toya", "coordenadas": [42.60241435125939, 140.8527624220369], "preco": "", "icon": "water"},
]


for local in locais_hokkaido:
    description = f"<b style='font-size:16px'>{local['nome']}</b><br><br><b style='font-size:14px'>Preço:</b> {local['preco']}"
    if local["preco"] == "Grátis":
        folium.Marker(
            location=local["coordenadas"],
            popup=description,
            icon=folium.Icon(color="green", prefix="fa",icon=local["icon"])
        ).add_to(mapa_hokkaido)
    else:
        folium.Marker(
            location=local["coordenadas"],
            popup=description,
            icon=folium.Icon(color="red", prefix="fa", icon=local["icon"])
        ).add_to(mapa_hokkaido)
casa_hokkaido = folium.Marker(
            location=[43.141972, 141.144130],
            popup="<b style='font-size:16px'>Casa</b>",
            icon=folium.Icon(color="orange", prefix="fa", icon="house")
        )
aeroporto_hokkaido = folium.Marker(
            location=[42.7752000, 141.6920010],
            popup="<b style='font-size:16px'>Aeroporto</b>",
            icon=folium.Icon(color="blue", prefix="fa", icon="plane")
        )
casa_hokkaido.add_to(mapa_hokkaido)
aeroporto_hokkaido.add_to(mapa_hokkaido)
mapa_hokkaido.save("mapa_hokkaido.html")

# Adicionar o styles.css
ficheiros = ["mapa_tokyo.html", "mapa_kyouto.html", "mapa_hokkaido.html"]

linha_css = '<link rel="stylesheet" href="style.css">\n'

for ficheiro in ficheiros:
    with open(ficheiro, 'r', encoding='utf-8') as f:
        conteudo = f.readlines()

    for i, linha in enumerate(conteudo):
        if "<head>" in linha:
            conteudo.insert(i+1, linha_css)
            break

    with open(ficheiro, 'w', encoding='utf-8') as f:
        f.writelines(conteudo)