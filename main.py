print("Hola Mundo")

import requests

response = requests.get("https://api.github.com")
print("Estado de la API de GitHub:", response.status_code)

import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("🎯 ¡Adivina el número entre 1 y 100!")

    while True:
        try:
            intento = int(input("🔢 Ingresa tu número: "))
            intentos += 1

            if intento < numero_secreto:
                print("📉 Muy bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("📈 Muy alto. Intenta de nuevo.")
            else:
                print(f"🎉 ¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intentos.")
                break
        except ValueError:
            print("❌ Ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()
