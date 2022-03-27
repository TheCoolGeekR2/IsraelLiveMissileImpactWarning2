from geopy.geocoders import MapBox
from soc import MapIt


geocoder = MapBox(user_agent='Reddy',api_key='')#Geopy API key
def get_locs(g):
    Locs = g["Towns"]
    nLocs = ''
    nLocs= (', '.join(Locs)).split(', ')
    t=0
    LocDict={}
    while t<len(nLocs):
        locl = geocoder.geocode(nLocs[t]+ ' ,israel')
        try:
            country = (locl.raw["context"][1])['text']
        except:
            country = None
        if locl != None and country == 'Israel':
            LocDict={
                "Name": nLocs[t],
                "lat": locl.latitude,
                "lon": locl.longitude}
            MapIt([LocDict["lat"], LocDict["lon"], LocDict["Name"]])
        else:
            print("No town found named: "+nLocs[t])
        LocDict.clear()
        t += 1
