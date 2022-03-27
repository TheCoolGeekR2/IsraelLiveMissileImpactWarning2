# Israel Live Missile Impact Warning
This project is a personal project that is meant to display predicted rocket impacts on israel on top of a live interactive map.

Main data server is run using KAFKA


## How does it work?

1. We scan a telegram group that posts about rocket sirens in towns.
2. We then filter that info down and exctract a coheret Town list per alarm
3. We pass the town list to a geolocation API that is going to return us coordinates
4. We Post the coordinates and a timestamp to the kafka server which then is read by another python script to display the data on a map.

### Message Example

>Red Alert at Ashkelon, Jerusalem, Herzeliya, Rishon LeZion, Hadera [18:15]:
>
>03/11/2021 18:15:02:
 >• West Lachish - Ashkelon - South, Ashkelon - North
 >• Jerusalem - Jerusalem - Atarot Industrial Zone, Jerusalem - South, Jerusalem - Qafr 'Aqab, Jerusalem - East
 >• Dan - Herzeliya - Center and Glil Yam
 >• HaShfela - Rishon LeZion - East
 >• Menashe - Hadera - Neveh Haim_
>
>|| Major cities: Ashkelon, Jerusalem, Herzeliya, Rishon LeZion, Hadera ||
>
>Sent by @CumtaAlertsEnglishChannel
