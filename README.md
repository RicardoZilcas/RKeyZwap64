# 🔐 RKeyZwap64 v1.0.0

> ⚠️ **Disclaimer:** Este proyecto fue desarrollado como una prueba de concepto utilizando inteligencia artificial. La programación fue realizada mayoritariamente por **ChatGPT-4o de OpenAI**, a partir de las instrucciones, ideas, y dirección de **Ricardo (Zilcas)**. Aunque Ricardo no escribió directamente el código, su participación consistió en revisar, corregir y validar la lógica paso a paso, solicitando cambios precisos y guiando el diseño y flujo del cifrado hasta su versión final estable.

---

**Cifrado personalizado simbólico basado en teclado y codificación Base64**

---

## 🛠️ Proceso de desarrollo (WriteUp)

A continuación se presenta una representación ASCII de cómo comenzó el proyecto, basado en la observación directa del teclado QWERTY y el teclado de símbolos superpuestos en un smartphone Android:

```
Teclado QWERTY:           Teclado de símbolos (superpuesto):
 q w e r t y u i o p       ! @ # $ % ^ & * ( )
 a s d f g h j k l ñ       _ ? : ; ' " < > , .
 z x c v b n m             { } [ ] \ |         
```

Cada letra fue asociada con el símbolo que físicamente aparecía en la misma posición del teclado cuando se alternaba entre modos. Este mapeo fue la base conceptual de RKeyZwap64, aunque posteriormente se optó por una tabla explícita de símbolos ASCII compatibles con Base64.

El desarrollo de RKeyZwap64 fue un viaje iterativo de experimentación y aprendizaje. Estos fueron los hitos clave:

1. **Idea original:** Ricardo propuso un sistema de cifrado inspirado en la superposición entre el teclado alfabético QWERTY y el teclado de símbolos en su smartphone.
2. **Captura visual:** Se analizaron imágenes reales de ambos teclados para extraer una simbología inicial asociada a cada letra.
3. **Primera implementación:** Se intentó codificar directamente el texto en símbolos, pero surgieron problemas por incompatibilidades de caracteres no ASCII, y errores al intentar descifrar símbolos no válidos en Base64.
4. **Exploración del teclado en capas:** Se comprobó que el símbolo ½ en Android solo significaba "siguiente página de símbolos", y se descartó del mapeo inicial.
5. **Estrategia combinada:** Se decidió introducir una capa intermedia de codificación Base64 para estandarizar los caracteres. Luego, se aplicó la sustitución simbólica sobre ese resultado, asegurando compatibilidad total con símbolos visibles ASCII.
6. **Eliminación de minúsculas:** Se determinó que trabajar exclusivamente con mayúsculas mejoraba la consistencia y simplificaba los diccionarios.
7. **Transformación a mayúsculas:** Se añadió una etapa para transformar todo el texto de entrada a mayúsculas antes de la codificación.
8. **Depuración de diccionario:** Se analizaron errores al decodificar símbolos como `^`, y se perfeccionó el mapeo para evitar colisiones o símbolos duplicados.
9. **Validación progresiva:** Cada error encontrado llevó a pequeños ajustes y pruebas incrementales, con Ricardo supervisando cada resultado y proponiendo soluciones.
10. **Uso de print statements de depuración:** Se incluyeron trazas internas para observar paso a paso el proceso de cifrado y descifrado.
11. **Implementación de control de flujo:** Se agregó validación de entradas `c/d` para mejorar la experiencia en consola.
12. **Pruebas con textos amplios:** Se usaron frases completas con múltiples palabras, números y caracteres extendidos.
13. **Soporte para espacios y símbolos conservados:** Se decidió que espacios y caracteres válidos en Base64 (`+/=`) no debían ser cifrados para mantener compatibilidad.
14. **Tratamiento especial de la letra `ñ`:** Se observó cómo `ñ` se convierte a `w5E=` en Base64 y se probó que el sistema lo manejaba correctamente.
15. **Identificación y resolución del bug en la `O`:** Se detectó que el símbolo de la letra `O` era sobrescrito en algunos casos; se solucionó aislando símbolos únicos.
16. **Revisión de simbolismo en teclados internacionales:** Se evitó el uso de símbolos problemáticos como `~` o caracteres no ASCII.
17. **Estabilidad final:** Se alcanzó una versión que cifraba y descifraba correctamente sin errores binarios ni colisiones.
18. **Modularización del código:** Se separó la lógica principal del cifrado/decodificación en `rkeyzwap64.py`, y la interfaz de usuario en `main.py`, facilitando el mantenimiento y la escalabilidad.
19. **Optimización del diccionario:** Se reescribieron los diccionarios de forma explícita y sin símbolos duplicados, garantizando una codificación y decodificación 1:1 sin ambigüedades.
20. **Revisión y validación final del flujo:** Ricardo dio su aprobación tras validar casos extremos y verificar que el resultado final reflejaba su visión inicial.

Este proyecto demuestra cómo una idea, con dirección humana y el apoyo de inteligencia artificial, puede transformarse en una solución funcional y reutilizable.

---

## 📊 Descripción

RKeyZwap64 es un sistema de cifrado desarrollado por **Ricardo (Zilcas)**, que combina:

- Transformación de texto a **mayúsculas**
- Codificación en **Base64**
- Sustitución de caracteres Base64 por **símbolos ASCII visibles**, sobre la lógica de un teclado simbólico QWERTY

Este sistema convierte un mensaje legible en una secuencia segura y reversible, usando solo Python estándar.

---

## 🔧 Estructura del proyecto

```
RKeyZwap64/
├── main.py              # Interfaz de consola (CLI)
├── keyswap64.py         # Lógica de codificación y decodificación
├── README.md            # Documentación del proyecto
├── LICENSE              # Licencia MIT modificada (sin fines comerciales)
```

---

## ⚖️ Requisitos

- Python 3.x
- No requiere dependencias externas

---

## ⚡ Uso

### Codificar

```bash
python main.py
```

Elegir `c` y escribir el mensaje.

### Decodificar

```bash
python main.py
```

Elegir `d` y pegar el texto cifrado.

---

## 🪧 Ejemplo de uso

**Entrada:** `Hola Mundo`

**Salida cifrada:** `@%9.>@":]\5%[w==`

**Decodificación:** `HOLA MUNDO`

---

## 🌟 Características clave

- 100% reversible
- Evita conflictos Base64 (`+/=` intactos)
- Todos los símbolos son ASCII visibles y seguros
- Cifrado por sustitución simple, ideal para aprendizaje o aplicaciones lúdicas
- Incluye soporte para letras acentuadas y `ñ`

---

## 🚀 Estado del proyecto

**Versión:** `v1.0.0`

**Autor:** [Ricardo / Zilcas]

**Ayuda técnica y programación:** ChatGPT-4o de OpenAI

**Estado:** ✅ Completado y funcional

---

## 🚨 Licencia

Este proyecto utiliza una **licencia MIT modificada**. Está permitido:

- Usar, copiar, modificar y distribuir el código libremente.

🚫 **No está permitido revender, sublicenciar o comercializar este software sin autorización escrita del autor.**

Consulta el archivo `LICENSE` para más detalles.

---

## 🚀 Ideas futuras (opcional)

- Interfaz web (Flask)
- Diferenciación de mayúsculas y minúsculas
- Integración con archivos (cifrado de textos .txt)
- Versión encriptada con llave secreta

---

> "Lo simple, si es reversible, es poderosamente funcional."
> — Ricardo aka Zilcas

> "Creo que cualquier persona que pueda acceder a herramientas avanzadas y tenga la creatividad necesaria, puede completar su idea sin necesidad de ser un experto. Solo se requiere ingenio, entusiasmo y las herramientas de calidad que estén a su alcance."
