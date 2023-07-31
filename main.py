# Entferungsrechner von LuxusTastisch 
# Discord: luxustastisch 
# Selbstständiges Bearbeiten der Datei untersagt, Weitergabe an Dritte ebenso!
# Zum Berechnen muss die Datei strecken.txt vorhanden sein.

import pip._vendor.requests 

file = open("strecken.txt", 'r')
Lines = file.readlines()

strecke = 0
fluege = 0
print("Berechne..")
for line in Lines:
    route = line.split("	")
    dep = route[0]
    arr = route[1]

    url = "https://www.luftlinie.org/" + dep + "/"+ arr

    r = pip._vendor.requests.get(url, stream=True)
    for line in r.iter_lines():
        if '<span class="headerAirline">Entfernung:' in str(line):
            data = str(line).split("value")
            data2 = str(data[1]).split("</span>")
            data3 = data2[0].split(">")
            data4 = str(data3[1]).split(",")[0]
            data5 = data4.replace(".", "")
            strecke += int(data5)
            fluege += 1

print("Gesamtstrecke: " + str(strecke))





