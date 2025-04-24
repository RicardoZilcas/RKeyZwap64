from rkeyzwap64 import cifrar_doble, descifrar_doble

print("=== RKeyZwap64 ===")

modo = ""
while modo not in ['c', 'd']:
    modo = input("¿Codificar o Decodificar? (c/d): ").strip().lower()
    if modo not in ['c', 'd']:
        print("Opción no válida. Por favor escribe 'c' para codificar o 'd' para decodificar.")

mensaje = input("Escribe tu mensaje: ").strip()

if modo == 'c':
    print(f"\n🔤 Texto original ingresado: {mensaje}")
    resultado = cifrar_doble(mensaje)
    print(f"\n✅ Mensaje cifrado final: {resultado}")
else:
    print(f"\n🔏 Texto cifrado recibido: {mensaje}")
    resultado = descifrar_doble(mensaje)
    print(f"\n✅ Mensaje original descifrado: {resultado}")
