type = ""
POUCES = 2.54
CM = 0.394

def converter(type):
    value = 0
    if type == "A":
        value = input("Quelle est la valeur que vous souhaitez convertir en cm ? ")
        result = float(value) * POUCES
        print(f"{value} pouces valent {result} cm")
    else:
        value = input("Quelle est la valeur que vous souhaitez convertir en pouces ? ")
        result = float(value) * CM
        print(f"{value} cm valent {result} pouces")


print("Convertisseur")
print("A: pouces vers cm")
print("B: cm vers pouces")

while (type != "A" and type != "B"):
    type = input("Choisissez le type de convertion entre A & B : ")
    print(type)

converter(type)






