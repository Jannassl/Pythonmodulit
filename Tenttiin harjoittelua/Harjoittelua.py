import mysql.connector

def kohteet():
    sql = "SELECT airport.name, municipality, latitude_deg, longitude_deg, airport.ident FROM airport"
    sql += " inner join country on country.iso_country = airport.iso_country where country.name =" + "'Finland'"
    sql += " order by latitude_deg"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(rivi)
    return


yhteys = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'Nasslingmaga98',
    autocommit = True
)
# Helsinki- vantaa : EFHK
# Turku Airport: EFTU
# Lappeenranta airport : EFLP
# Tampere - Pirkkala: EFTP
# Pori : EFPO
# Mikkeli : EFMI
# savonlinna : EFSA
# Jyväskylä: EFJY
# Seinäjoki: EFSI
# Joensuu: EFJO
# Kuopio: EFKU
# Vaasa: EFVA
# Kokkola-pietarsaari: EFKK
# Kajaani: EFKI
# Oulu: EFOU
# Kemi-Tornio: EFKE
# Kuusamo: EFKS
# Rovaniemi: EFRO
Sijainti = ""

kohteet()