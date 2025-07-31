# Emergency QR Card Generator 🆘

A desktop application built with **Python and Tkinter** that generates a printable **emergency contact card** containing personal, medical, and contact information. The app allows users to **embed a personal image** (e.g. ID photo) and outputs a ready-to-use **PNG file** for physical or digital storage.

## ✨ Features

- User-friendly **Tkinter GUI**
- Input fields for:
  - Name, address, blood type, allergies, medical conditions
  - Primary and secondary emergency contacts
- Upload and paste an **image** onto the card
- Card data rendered with **Pillow (PIL)** and saved as `emergency_card.png`
- Data validation to ensure all fields and image are filled

## 📦 Tech Stack

- Python 3
- Tkinter (GUI)
- PIL / Pillow (image rendering)
- tkinter.messagebox and filedialog

## 🏁 How to Run

```bash
python emergency_card.py
