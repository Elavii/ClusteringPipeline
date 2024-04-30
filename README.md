Tekstiseikkailu dokumentaatio

Pelin Rakenne
Luokat ja niiden vastuut
Room
  Tarkoitus: Edustaa pelin yksittäisiä huoneita.
  Attribuutit:
    description (str): Huoneen kuvaus.
    exits (dict): Sanakirja, joka sisältää tiedot siitä, mihin suuntiin huoneesta pääsee liikkumaan.
    items (list): Lista Item-olioista, jotka ovat tässä huoneessa.
  Metodit:
    __init__: Alustaa huoneen kuvauksen, uloskäynnit ja esineet.
    get_description: Palauttaa huoneen kuvauksen.
    link_room: Yhdistää kaksi huonetta keskenään.
    set_item: Lisää esineen huoneeseen.
    get_details: Tulostaa huoneen kuvauksen ja uloskäynnit.
    move: Mahdollistaa liikkumisen toiseen huoneeseen.
Item
  Tarkoitus: Kuvaa yksittäisiä esineitä, joita pelaaja voi kerätä.
  Attribuutit:
    name (str): Esineen nimi.
  Metodit:
    __init__: Alustaa esineen nimellä.
    get_name: Palauttaa esineen nimen.
Player
  Tarkoitus: Edustaa pelaajaa, hallinnoi pelaajan sijaintia, inventaariota ja toimintoja.
  Attribuutit:
    inventory (list): Pelaajan hallussa olevat esineet.
    current_room (Room): Huone, jossa pelaaja tällä hetkellä on.
    used_items (list): Lista esineistä, jotka on käytetty.
  Metodit:
    __init__: Alustaa pelaajan, inventaarion ja nykyisen huoneen.
    move: Siirtää pelaajaa toiseen huoneeseen.
    take_item: Ottaa esineen huoneesta.
    use_item: Käyttää esinettä, mahdollisesti edistäen pelin juonta.
    read_map: Näyttää kartan, josta näkyy esineiden sijainnit.
    has_all_items: Tarkistaa, onko kaikki tarvittavat esineet kerätty.
Pelin Toiminnot
Liikkuminen: Pelaaja voi liikkua huoneesta toiseen käyttäen komentoa "go" seurattuna suunnalla (esim. "go east").
Esineiden kerääminen: Pelaaja voi kerätä esineitä käyttäen komentoa "take" seurattuna esineen nimellä (esim. "take Phoenix Feather").
Tavaraluettelo: Pelaaja voi tarkistaa mitä esineitä hänellä on mukanaan komennolla "inventory" tai "items".
Esineiden käyttö: Pelaaja voi käyttää esineitä tietyissä konteksteissa (esim. "use Phoenix Feather" kirjastossa).
Kartan katsominen: Pelaaja voi tarkastella karttaa, jossa näkyy, missä esineet sijaitsevat.
Pelin aloitus ja lopetus: Peli alkaa esittelyllä ja kysymyksellä pelin aloittamisesta. Peli loppuu, kun kaikki tarvittavat esineet on kerätty ja käytetty oikein.
Pelin Aloitus
Peli alkaa start_game()-funktiolla, joka käynnistää pelin, luo huoneet, yhdistää ne, lisää esineet ja hallinnoi pelin aloitusta.
 
Klusterointiputki

1. Kirjastojen ja moduulien tuonti
pandas: Tietorakenteiden käsittelyyn ja tiedostonlukemiseen.
sklearn.cluster.KMeans: K-means klusterointimalli.
sklearn.preprocessing.StandardScaler: Ominaisuuksien skaalaus.
sklearn.metrics.silhouette_score: Klusteroinnin laadun arviointiin.
matplotlib.pyplot: Visualisointiin.
2. ClusteringPipeline luokka
__init__(self, raw_data_path, new_data_path): Luokan alustusfunktio, joka ottaa parametreina raakadatan ja uuden datan tiedostopolut.
load_data(self): Funktio raakadatan ja uuden datan lataamiseen tiedostoista.
preprocess_data(self): Funktio datan esikäsittelyyn, jossa skaalataan ominaisuudet ja koulutetaan klusterointimalli alkuperäiselle datalle.
cluster_new_data(self): Funktio uuden datan klusterointiin skaalattujen ominaisuuksien perusteella.
evaluate_clusters(self): Funktio klusteroinnin laadun arviointiin silhouette-pisteiden avulla.
visualize_clusters(self): Funktio klusteroinnin tulosten visualisointiin.
run_pipeline(self): Funktio datan käsittelyn ja klusteroinnin suorittamiseen putken avulla.
3. Pääohjelma (__main__)
Määrittää raakadatan ja uuden datan tiedostopolut.
Luo ClusteringPipeline-olion ja suorittaa putken.
Käyttö
Tämä koodi lataa raakadatan ja uuden datan tiedostot, suorittaa esikäsittelyn (sisältäen ominaisuuksien skaalauksen), klusteroi datat K-means-menetelmällä ja arvioi klusteroinnin laadun silhouette-pisteiden avulla. lopuksi se visualisoi klusteroinnin tulokset.
