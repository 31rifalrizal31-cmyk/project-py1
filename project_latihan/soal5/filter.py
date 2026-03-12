users = [
 {"username": "andi", "umur": 20},
 {"username": "budi", "umur": 25},
 {"username": "caca", "umur": 18},
 {"username": "dodi", "umur": 30}
]
for user in users:
    if user["umur"] > 21:
        print(user["username"])
        print("mereka sudah tua")
    elif user["umur"] < 21:
        print(user["username"])
        print("masih muda")
# bagian pencarian
i = [
    {"username": "andi", "umur": 20},
 {"username": "budi", "umur": 25},
 {"username": "caca", "umur": 18},
 {"username": "dodi", "umur": 30}
]
for n in i:
    if n["username"] == "budi":
        print(n["username"], n["umur"])
    