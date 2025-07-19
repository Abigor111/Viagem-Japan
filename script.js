let indexAtual = 1
const id = "map"
const mapas = [
    { url: "mapa_tokyo.html", title: "Tokyo" },
    { url: "mapa_kyouto.html", title: "Kyouto" },
    { url: "mapa_hokkaido.html", title: "Hokkaido" }
];

function mudarMapa() {
    const title = document.querySelector("h1");
    const text = mapas[indexAtual].title;
    title.textContent = text;

    const mapa = mapas[indexAtual].url;
    document.getElementById(id).src = mapa;

    indexAtual = (indexAtual + 1) % mapas.length;
}
