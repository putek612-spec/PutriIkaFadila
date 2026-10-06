profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}

print("data:", profile)
print("total keys:", len(profile))

print("name:", profile["name"])

print("hobbies:", profile["hobbies"])

#pretty print dictionary
import pprint
pprint.pprint(profile)

#menggunakan json dumps
import json
print (json.dumps(profile, indent=4))