profile = {
    "name": "mario",
}
print("len:", len(profile), "data:", profile)

profile["favourite_colour"] = "red"
print("len:", len(profile), "data:", profile)

profile.update({"race": "italian"})
print("len:", len(profile), "data:", profile)