import json
import csv
import requests

csvfile = open("14zpallnoagi.csv")
reader = csv.reader(csvfile)
data = list(reader)

total = 0
output = []
for stuff in data:
    if(stuff[0] == "STATEFIPS"):
        continue
    if(stuff[2] != "00000"):
        total += float(stuff[14])

with open('output.json') as data_file:    
    data1 = json.load(data_file)

for k in range(1, len(data1)):
    if(k%3 == 0):
        output.append(data1[k-1]*total/10000000)
    else:
        output.append(data1[k-1])

with open('output2.txt', 'w') as outfile:
    json.dump(output, outfile)

# for stuff in data:
#     if(stuff[0] == "STATEFIPS"):
#         continue
#     if(stuff[2] != "00000"):
#         url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + stuff[2] + "&key=AIzaSyAuEk30tlC7EjhfJ1eu952HuKDqgnFa0I0"
#         req = requests.get(url)
#         try:
#             lat = req.json()["results"][0]["geometry"]["location"]["lat"]
#             lng = req.json()["results"][0]["geometry"]["location"]["lng"]
#             agi = float(stuff[14])/total
#             output.append(lat)
#             output.append(lng)
#             output.append(agi)
#         except:
#             continue
        
# with open("output.txt", "w") as outfile:
#     json.dump(output, outfile)