# 1Convert from JSON to Python:

# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])


#2 Convert from Python to JSON:

# import json
# x = {"name": "John","age": 30,"city": "New York"}
# y = json.dumps(x)
# print(y)



# 3
# import json

# x = {"name": "John","age": 30,
# "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# with open("Meraki3.json","w") as f:
#     json.dump(x,f,indent=4)


# import json
# a={"name": "David", "class": "I",  "age": 6},{"name": "John","age": 30,"city": "New York"}
# print(json.dumps(a))




