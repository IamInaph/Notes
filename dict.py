#dict kasari banaune:
car = {
   "name":"tesla",
   "model":"y",
   "color": "black",
   "year": {
    "start": 2020,
    "end": 2056,
   },
   "isexpensive":"true",
}
print(car)
#dict ko value change garne:dict_name["key_name"]= "value"
car["color"] = "white"
#dict ko ni dict ko value print garne way:print(dict_name["key"][key_ko_ni_key])
print(car["year"]["start"])