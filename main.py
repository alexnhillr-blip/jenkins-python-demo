import csv

print("=== PROCESAMIENTO DE DATOS ===")

# leer archivo de ventas
ventas = []

with open("ventas.csv", newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        ventas.append({
            "producto": fila["producto"],
            "precio": float(fila["precio"]),
            "cantidad": int(fila["cantidad"])
        })

# cálculos
total_ventas = 0
producto_top = ""
max_ingreso = 0

for v in ventas:
    ingreso = v["precio"] * v["cantidad"]
    total_ventas += ingreso
    
    if ingreso > max_ingreso:
        max_ingreso = ingreso
        producto_top = v["producto"]

# resultados
print(f"Total de ventas: {total_ventas}")
print(f"Producto con mayor ingreso: {producto_top}")
