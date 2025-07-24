height = int(input("Ingrese su altura: "))
credits = int(input("Ingrese sus creditos: "))

if height >= 137 and credits >= 10:
    print("Puedes subirte")
elif height < 137 and credits >= 10:    
    print("No puedes subirte por altura")
elif height >= 137 and credits < 10:
    print("No puedes subirte por creditos")
else:
    print("No puedes subirte por altura y creditos")
