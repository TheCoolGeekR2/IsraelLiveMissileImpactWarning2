import json
import DataDisplay

def to_file(f): #Dumps to Json format and then logs the alert
    print(json.dumps(f))
    DataDisplay.get_locs(f)
    p = open("Alerts.txt", "a")
    p.write(json.dumps(f)+"\n")
    p.close()

def conv_txt(l): #Converts the filtered message into a proper Json element then goes to "to_file"
    l = l.replace("•", "") #removes the dots
    temp=(l.split("\n", 1)[1]).split("|", 1)
    i=0
    while i<len(temp):
        if temp[i].find('|') != -1:
            del temp[i]
        i += 1
    temp = ', '.join(temp)
    temp = temp.split('\n\n')
    while '' in temp:
        temp.remove('')
    tempB = []
    AlertDict = {}
    Time = ""
    Date = ""
    Regions =[]
    Towns = []
    tempC = []
    i=0
    while i<len(temp):
        tempB = temp[i].split('\n')
        if(i==0):
            del tempB[0]
        TimeDate =(tempB.pop(0).split())
        Date = TimeDate[0]
        Time = TimeDate[1].rstrip(":")
        t=0
        Regions.clear()
        Towns.clear()
        while t<len(tempB):
            tempC=(tempB[t].split('-'))
            Regions.append(tempC[0].strip())
            Towns.append(tempC[1].strip())
            tempC.clear()
            t += 1
        Regions = list(set(Regions))
        AlertDict={
            'Time': Time,
            'Date': Date,
            'Regions': Regions,
            'Towns': Towns
        }
        to_file(AlertDict)
        tempB.clear()
        i += 1