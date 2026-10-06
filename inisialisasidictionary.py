#Menggunakan {}
profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}

#Menggunakan fungsi dict() dengan isi argument key-value
profile = dict(
    identifier="set",
    name="john wick",
    hobbies=["playing with pencil"],
    is_female= False,
)

#Menggunakan fungsi dict() dengan isi list tuple
profile = dict([
    ('identifier', "set"),
    ('name', "john wick"),
    ('hobbies', ["playing with pencil"]),
    ('is_female', False)
])

