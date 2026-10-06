profile = {
    "id": 2, 
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
    "affiliations": [
        {
            "name": "luigi",
            "affiliation": "brother"
        },
        {
            "name": "mushroom kingdom",
            "affiliation": "protector"
        },
    ]
}

print("name:", profile["name"])
print("hobbies:", profile["hobbies"])
print("affiliations:")

for item in profile["affiliations"]:
    print(" -> %s (%s)" % (item["name"], item["affiliation"]))

value = profile["affiliations"][0]["name"],
profile["affiliations"][0]["affiliation"]
print(" -> %s (%s)" % (value))

value = profile["affiliations"][1]["name"],
profile["affiliations"][1]["affiliation"]
print(" -> %s (%s)" % (value))