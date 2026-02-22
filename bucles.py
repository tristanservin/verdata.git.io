x = int(input("how many hectares did you? "))
for i in range(1, x+1):
    print(f"working on hectare {i}")

    total = 0
for i in range(5):
    horas = float(input("Horas estudiadas hoy: "))
    total += horas

print("Total de horas:", total)