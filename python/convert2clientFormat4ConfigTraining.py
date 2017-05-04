import json
import os

f = file("config_training.json", "rw");
data = json.load(f)
f.close()

print data
formatData = {}

for value in data :
    if value.has_key("name"):
        formatData[value["name"]] = {}
        
        if value.has_key("index"):
            del value["index"]

        if value.has_key("advantage"):
            for valueAd in value["advantage"]:
                value[valueAd] = 1
            del value["advantage"]

        if value.has_key("disadvantage"):
            for valueDisad in value["disadvantage"]:
                value[valueDisad] = -1
            del value["disadvantage"]

        if value.has_key("average"):
            for valueAvrg in value["average"]:
                value[valueAvrg] = 0
            del value["average"]

        formatData[value["name"]].update(value)
        if formatData[value["name"]]["name"]:
            del formatData[value["name"]]["name"]

jsonData = json.dumps(formatData)
print jsonData

os.rename("config_training.json", "old_config_training.json")

f2 = file("config_training.json", "w");
f2.write(jsonData)
f2.close()





