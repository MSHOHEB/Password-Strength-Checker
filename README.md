# 🔐 Password Strength Checker & Manager

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Library](https://img.shields.io/badge/Libraries-None_(Pure_Python)-orange)

A **command-line Password Strength Checker & Manager** built with Pure Python.
No external libraries needed — just run and use!

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💪 Strength Checker | Weak / Medium / Strong rating with score |
| 🔧 Password Generator | Custom length, symbols, numbers, uppercase |
| 💾 Save Passwords | Save passwords with site name to JSON file |
| 👁️ View Passwords | See all saved passwords with strength rating |
| 🗑️ Delete Password | Remove any saved password |
| 📋 Suggestions | Tips to improve weak passwords |
| 🚨 Common Password Detection | Warns if password is too common |

---

## 📸 Preview

    ==================================================
      🔐 PASSWORD STRENGTH CHECKER & MANAGER
    ==================================================
      1. Check Password Strength
      2. Generate Strong Password
      3. Save a Password
      4. View Saved Passwords
      5. Delete a Password
      6. Exit
    ==================================================

    🔍 PASSWORD ANALYSIS
    ==================================================
      Password  : TestPassword123!
      Length    : 16 characters
      Score     : 7/7

      Strength  : STRONG
      █████████████████████ (100%)

      ✅ Excellent! Your password is very strong!
    ==================================================

---

## 🚀 How to Run

    git clone https://github.com/MSHOHEB/password-strength-checker.git
    cd password-strength-checker
    python password_checker.py

No pip install needed! Pure Python only. ✅

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `password_checker.py` | Main program file |
| `saved_passwords.json` | Auto-created when you save passwords |
| `README.md` | Project documentation |

---

## 🔍 How Strength is Calculated

| Check | Points |
|-------|--------|
| Length 12+ characters | +2 |
| Length 8+ characters | +1 |
| Has UPPERCASE letters | +1 |
| Has lowercase letters | +1 |
| Has numbers | +1 |
| Has special characters | +2 |
| Common password detected | Score = 0 |
| Repeated characters (aaa) | -1 |

**Score 6-7 = STRONG 💚 | Score 4-5 = MEDIUM 🟡 | Score 2-3 = WEAK 🔴 | Score 0-1 = VERY WEAK 🔴**

---

## 🛠️ Tech Stack

- **Python 3.10+** — Core language
- **re** — Regex for pattern matching
- **json** — Saving passwords locally
- **random & string** — Password generation
- **os & datetime** — File handling & timestamps

---
