import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as request
import json
import re

url1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
with request.urlopen(url1) as response:
    data=json.load(response)
spot_list=data["data"]["results"]
#print(spot_list)
with request.urlopen(url2) as response:
    data=json.load(response)
mrt_list=data["data"]
#print(mrt_list)

merge_list=[]
for spot in spot_list:
    for mrt in mrt_list:
        if spot["SERIAL_NO"] == mrt["SERIAL_NO"]:
            merge_list.append({**spot, **mrt})
#print(merge_list)                 

with open("spot.csv","w",encoding="utf-8") as file:
    for merge in merge_list:
        first_url=re.search(r"https?://.*?\.(jpg|JPG)", merge["filelist"], re.IGNORECASE) # 正則表達式
        district=re.search(r"\w+區", merge["address"])
        file.write(f"{merge["stitle"]},{district.group(0)},{merge["longitude"]},{merge["latitude"]},{first_url.group(0)}\n")

mrt_dict={}
for merge in merge_list: 
    mrt=merge["MRT"]
    stitle=merge["stitle"]
    if mrt in mrt_dict:
        mrt_dict[mrt].append(stitle)
    else:
        mrt_dict[mrt]=[stitle]
#print(mrt_dict)

with open("mrt.csv","w",encoding="utf-8") as file:
    for key, value in mrt_dict.items():
            value_str=",".join(value)
            file.write(f"{key},{value_str}\n")



