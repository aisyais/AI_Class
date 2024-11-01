import random

random.seed(20)

X = [random.randint(0, 10) for _ in range(20)]

print("List X:", X)

y1 = int(input("Masukkan angka genap (0-10): "))

if y1 % 2 == 0 and y1 in X:
    
    indeks = X.index(y1)
    print(f"Angka {y1} ada di indeks ke-{indeks}.")
else:
    print(f"Angka {y1} tidak ada dalam list atau bukan angka genap.")