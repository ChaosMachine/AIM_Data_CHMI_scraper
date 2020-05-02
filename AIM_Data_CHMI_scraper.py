import requests
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import datetime
def zapis(url, filename):

    response = urllib.request.urlopen(url)
    webContent = response.read()

    soup = BeautifulSoup(webContent)
    ##print(soup.prettify())

    map = soup.find('map')
    ##print(map)

    tipNO2 = []
    tipPM10 = []
    timeNO2 = []
    timePM10 = []

    areas = map.findAll('area')
    for obl in areas:
        tip = obl['onmouseover'].split(", ")
        title = tip[2].split(" ")[0].split("'")[1]
        if (title == "NO2"):
                a = (tip[0].split("strong>")[3].split(" ")[0])
                time = tip[0].split("<strong>")[1].split("</strong>")[0].split(" SEČ")[0]
                a = float(a.replace(',', '.'))
                tipNO2.append(a)
                timeNO2.append(time)
                print((a))
        if (title == "PM10"):
                a = (tip[0].split("strong>")[3].split(" ")[0])
                a = float(a.replace(',', '.'))
                tipPM10.append(a)
                time = tip[0].split("<strong>")[1].split("</strong>")[0].split(" SEČ")[0]
                timePM10.append(time)
                print((a))
    dnes = datetime.date.today().strftime("%Y-%m-%d")
    maxNO2 = max(tipNO2)
    maxPM10 = max(tipPM10)
    print("Dnes; maxNO2 ; DEN NO2 ;  čas NO2 ; maxPM10 ; DEN PM10 ;  čas PM10")
    print(dnes,";", maxNO2 ,";", timeNO2[tipNO2.index(maxNO2)].split(" ")[0], ";", timeNO2[tipNO2.index(maxNO2)].split(" ")[1], ";",maxPM10, ";", timePM10[tipPM10.index(maxPM10)].split(" ")[0], ";", timePM10[tipPM10.index(maxPM10)].split(" ")[1])

    nope = False
    try:
         f = open(filename,"r+")
    except IOError:
        nope=True
    else:
        f.close()


    if(nope):
        f = open(filename,"w+")
        print("Vytvářím složku,přidávám zápis")
        f.write("Dnes; maxNO2 ; DEN NO2 ;  čas NO2 ; maxPM10 ; DEN PM10 ;  čas PM10 \n")
        f.write("{};{};{};{};{};{};{} \n".format(dnes, maxNO2 , timeNO2[tipNO2.index(maxNO2)].split(" ")[0],timeNO2[tipNO2.index(maxNO2)].split(" ")[1],maxPM10,timePM10[tipPM10.index(maxPM10)].split(" ")[0],timePM10[tipPM10.index(maxPM10)].split(" ")[1]))
             
       
    else:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            print ("Poslední naměřená hodnota je: ",last_line)
            ##cas =   datetime.datetime.strptime(last_line.split(";")[0],"%Y-%m-%d").strftime("%Y-%m-%d")
            ##print(cas)
            f.close()
        if(True):
            with open(filename, 'a') as f:
                print("přidávám zápis")
                f.write("{};{};{};{};{};{};{}\n".format(dnes, maxNO2 , timeNO2[tipNO2.index(maxNO2)].split(" ")[0],timeNO2[tipNO2.index(maxNO2)].split(" ")[1],maxPM10,timePM10[tipPM10.index(maxPM10)].split(" ")[0],timePM10[tipPM10.index(maxPM10)].split(" ")[1])) 
            f.close()


zapis("http://portal.chmi.cz/files/portal/docs/uoco/web_generator/aqindex_slide1/mp_ALEGA_CZ.html","hodnotyALEGA.txt")
zapis("http://portal.chmi.cz/files/portal/docs/uoco/web_generator/aqindex_slide1/mp_AKOBA_CZ.html","hodnotyAKOBA.txt")
zapis("http://portal.chmi.cz/files/portal/docs/uoco/web_generator/aqindex_slide1/mp_ABREA_CZ.html","hodnotyABREA.txt")
end = input("Makej---")

