#extract weather obs from json file, create list of timestamps, temp and humidity (or maybe a dict? list for orderedness)

import json

datafile = open("scoresbyobs.json")
outfile = open("scoresbyobs.csv",'w')

jsonstr = datafile.read()

data = json.loads(jsonstr)

outfile.write("timestamp,relative humidity,air temperature\n")
for item in data['observations']["data"]:
    t = str(item["local_date_time_full"])
    t = t[0:4]+'-'+t[4:6]+'-'+t[6:8]+","+t[8:10]+':'+t[10:12]
    print t
    outfile.write(t+','+str(item["rel_hum"])+","+str(item["air_temp"])+"\n")


outfile.close()

