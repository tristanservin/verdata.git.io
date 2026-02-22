# 1️⃣ Preguntar cuántos días quieres registrar
dias = int(input("¿Cuántos días quieres registrar? "))

total_horas = 0

# 2️⃣ Usar un for
for i in range(1, dias + 1):
    
    # 3️⃣ Pedir horas estudiadas cada día
    horas = float(input(f"Horas estudiadas el día {i}: "))
    
    # 4️⃣ Calcular total
    total_horas += horas

# 5️⃣ Calcular promedio
if dias > 0:
    promedio = total_horas / dias
else:
    promedio = 0

# 6️⃣ Usar if para evaluar disciplina
if promedio >= 4:
    nivel = "Excelente disciplina 💪"
elif promedio >= 2:
    nivel = "Buena disciplina 👍"
else:
    nivel = "Necesitas mejorar tu disciplina 📚"

# 7️⃣ Imprimir resultados claros
print("\n📊 RESULTADOS")
print(f"Total de horas estudiadas: {total_horas} horas")
print(f"Promedio diario: {promedio:.2f} horas")
print(f"Evaluación: {nivel}")

