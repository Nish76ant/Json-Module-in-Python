#JSON _ Module - JavaScript Object Notation
import json

data = '{"var1":"harry","var2":56}'
#print(data)
#print(data['var1']) it will throw an error
parsed = json.loads(data)

print(parsed)
print(parsed['var1'])
print(type(parsed)) #it will give dictionary

#Task1 - Json.load


data2 = {
    "Channel_name":"Code with Nishant",
    "cars": ['BMW','AUDI A8',"FERRARI"],
    "Fridge":('Roti',540,'Paneer','Chicken'),
    "isbad":False
}
jscomp = json.dumps(data2)
print(jscomp)

#Task 2 - what is keys parameter in dums parameter

print(json.dumps(data2, indent=4, sort_keys=True))
