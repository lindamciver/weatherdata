from websocket import create_connection
import json
import datetime
from datetime import date


wood = "118.139.125.148"
blackburn = "118.139.125.200"
request = { "init": False, "time": 1456550000 }

outfile = open("blackburn"+str(date.today())+".csv",'w')

ws = create_connection("ws://"+blackburn+":80/websocket")

ws.send(json.dumps(request))
result =  ws.recv()
#print "Received '%s'" % result

datalist = result.split("[")

for item in datalist:


    #print item.strip().strip('],')

    if item:
        item = item.strip().strip('],')
        itemlist = item.split(',')
        itemlist[0] = datetime.datetime.fromtimestamp(int(itemlist[0])).strftime('%Y-%m-%d %H:%M:%S')
        t = int(itemlist[0][14:16])
        if t%30 == 0:
            print t
            outfile.write(itemlist[0]+','+itemlist[3]+','+itemlist[4]+'\n')
#outfile.write(result)
outfile.close()

ws.close()