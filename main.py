import pip._vendor.requests 

file1 = open("strecken.txt", 'r')
Lines = file1.readlines()

strecke = 0
fluege = 0
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
            print(data5)
            fluege += 1


for i in range(5):
    print(" ")
print("Gesamtstrecke: " + str(strecke))





