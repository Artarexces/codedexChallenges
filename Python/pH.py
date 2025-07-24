import random 

pH = random.choice(range(0, 14))

if pH < 7:
    print("El pH es", pH, "y es ácido")
elif pH == 7:
    print("El pH es", pH, "y es neutral")
else:
    print("El pH es", pH, "y es básico")

print("El pH es", pH)
