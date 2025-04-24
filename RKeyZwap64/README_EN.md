# 🔐 RKeyZwap64 v1.0.0

> ⚠️ **Disclaimer:** This project was developed as a proof of concept using artificial intelligence. Most of the programming was done by **ChatGPT-4o (OpenAI)**, based on the instructions, ideas, and direction of **Ricardo (Zilcas)**. While Ricardo didn’t directly write the code, his role was to guide, correct, and validate the logic at each step, requesting precise changes and driving the design and development of the encryption flow until it was complete.

---

**Custom symbolic encryption based on keyboard mapping and Base64 encoding**

---

## 🛠️ Development Process (WriteUp)

This project started with a simple visual comparison between a QWERTY keyboard and the symbol keyboard on a smartphone. Here's an ASCII representation:

```
QWERTY Keyboard:          Symbol Keyboard (overlaid):
 q w e r t y u i o p       ! @ # $ % ^ & * ( )
 a s d f g h j k l ñ       _ ? : ; ' " < > , .
 z x c v b n m             { } [ ] \ |         
```

Each letter was associated with the symbol that physically appeared in the same key location when switching modes. This mapping was the conceptual base of RKeyZwap64. Later, a cleaner ASCII symbol substitution was used for full compatibility.

Here’s a chronological list of the key steps we followed:

1. **Original idea:** Ricardo proposed a symbolic cipher based on overlaying two keyboard modes.
2. **Visual capture:** Real smartphone screenshots were used to extract the initial mapping.
3. **First version:** We attempted to encrypt directly using symbols, but encountered non-ASCII errors and Base64 decoding issues.
4. **Understanding the ½ key:** Realized it just switched pages, so it was excluded.
5. **Combined strategy:** We introduced Base64 encoding to normalize characters before symbol substitution.
6. **Lowercase removed:** To simplify the logic, all lowercase handling was removed.
7. **Uppercase transformation:** All input was transformed to uppercase before encoding.
8. **Dictionary cleanup:** Fixed collisions and refined the mapping to ensure unique substitutions.
9. **Progressive testing:** Each bug was iteratively tested and resolved under Ricardo’s supervision.
10. **Debug printing:** Internal steps were logged to make tracing easier.
11. **Flow validation:** Input control for codify/decode was added to the UI.
12. **Real sentence tests:** Full phrases, symbols, and numbers were tested.
13. **Preserved space and Base64 symbols:** Characters like `+`, `/`, `=` and spaces were left untouched.
14. **Support for `ñ`:** The Base64 `w5E=` for `ñ` was tested and confirmed.
15. **The ‘O’ bug:** An overwrite issue in the mapping was discovered and fixed.
16. **Symbol conflict resolution:** Problematic Unicode symbols like `~` were discarded.
17. **Final stability:** The result was a clean, reversible encryption system.
18. **Modular code structure:** Logic was separated into `keyswap64.py` and UI into `main.py`.
19. **Explicit dictionary:** A complete symbol dictionary with no duplicates was created.
20. **Final approval:** Ricardo gave the green light after full testing and alignment with the original vision.

This project proves that with the right tools, direction, and creativity, even someone without programming knowledge can build a complete solution with AI support.

---

## 📊 Description

RKeyZwap64 is a symbolic encryption system combining:

- Uppercased text conversion
- Base64 encoding
- Symbol substitution using a customized QWERTY-inspired mapping

It turns readable text into secure and reversible symbol sequences using only Python standard libraries.

---

## 🔧 Project Structure

```
RKeyZwap64/
├── main.py              # Console interface (CLI)
├── keyswap64.py         # Logic for encoding and decoding
├── README.md            # Project documentation (Spanish)
├── README_EN.md         # Project documentation (English)
├── LICENSE              # Modified MIT license (non-commercial)
```

---

## ⚖️ Requirements

- Python 3.x
- No external libraries needed

---

## ⚡ Usage

### To encode

```bash
python main.py
```
Choose `c` and enter your message.

### To decode

```bash
python main.py
```
Choose `d` and paste your encrypted string.

---

## 🪧 Example

**Input:** `Hola Mundo`  
**Encrypted:** `@%9.>@":]\5%[w==`  
**Decoded:** `HOLA MUNDO`

---

## 🌟 Key Features

- 100% reversible
- Base64-friendly (`+`, `/`, `=` kept intact)
- Only printable ASCII symbols
- Great for learning, puzzles, or custom encoding ideas
- Supports accents and `ñ` without breaking

---

## 🚀 Project Status

**Version:** `v1.0.0`  
**Author:** [Ricardo / Zilcas]  
**Technical guidance & programming:** ChatGPT-4o (OpenAI)  
**Status:** ✅ Fully functional and complete

---

## 🚨 License

This project uses a **modified MIT license**. It allows:

- Free use, copying, modification, and distribution

🚫 **You may not sell, sublicense or commercially distribute this software without written permission from the author.**

See `LICENSE` for full terms.

---

## 🚀 Future Ideas

- Web version (Flask)
- Case-sensitive version (uppercase/lowercase)
- File support (.txt encryption)
- Secret-key encryption version

---

> "Simplicity, when reversible, is powerfully functional."
> — Ricardo aka Zilcas

> "Anyone with access to advanced tools and enough creativity can realize their idea—without being an expert. All it takes is ingenuity, enthusiasm, and the best tools you can reach."
