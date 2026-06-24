"""
🔐 Password Strength Checker
==============================
A complete Password Strength Checker & Generator tool.
Pure Python - no external libraries needed.
"""

import random
import string
import re
import json
import os
from datetime import datetime


# ── Colors for terminal ────────────────────────────────────────────────────
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

SAVE_FILE = "saved_passwords.json"


# ══════════════════════════════════════════════════════════════════════════
# 1. PASSWORD STRENGTH CHECKER
# ══════════════════════════════════════════════════════════════════════════
def check_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️  Use at least 12 characters for better security")
    else:
        feedback.append("❌ Password too short! Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add UPPERCASE letters (A-Z)")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")

    # Special character check
    if re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]", password):
        score += 2
    else:
        feedback.append("❌ Add special characters (!@#$%^&*)")

    # Common passwords check
    common = ["password", "123456", "password123", "admin", "qwerty",
              "abc123", "letmein", "welcome", "monkey", "dragon"]
    if password.lower() in common:
        score = 0
        feedback.append("🚨 This is a very common password! Never use this!")

    # Repeated characters check
    if re.search(r"(.)\1{2,}", password):
        score -= 1
        feedback.append("⚠️  Avoid repeating characters (aaa, 111)")

    # Determine strength level
    if score >= 6:
        strength = "STRONG"
        color = GREEN
        bar = "█████████████████████" + " (100%)"
    elif score >= 4:
        strength = "MEDIUM"
        color = YELLOW
        bar = "██████████████░░░░░░░" + " (65%)"
    elif score >= 2:
        strength = "WEAK"
        color = RED
        bar = "███████░░░░░░░░░░░░░░" + " (35%)"
    else:
        strength = "VERY WEAK"
        color = RED
        bar = "███░░░░░░░░░░░░░░░░░░" + " (10%)"

    return strength, color, bar, score, feedback


def display_strength(password):
    strength, color, bar, score, feedback = check_strength(password)

    print(f"\n{BOLD}{'='*50}{RESET}")
    print(f"{BOLD}🔍 PASSWORD ANALYSIS{RESET}")
    print(f"{'='*50}")
    print(f"  Password  : {CYAN}{password}{RESET}")
    print(f"  Length    : {len(password)} characters")
    print(f"  Score     : {score}/7")
    print(f"\n  Strength  : {color}{BOLD}{strength}{RESET}")
    print(f"  {color}{bar}{RESET}")

    if feedback:
        print(f"\n{BOLD}📋 Suggestions:{RESET}")
        for tip in feedback:
            print(f"   {tip}")
    else:
        print(f"\n  {GREEN}✅ Excellent! Your password is very strong!{RESET}")

    print(f"{'='*50}\n")
    return strength


# ══════════════════════════════════════════════════════════════════════════
# 2. PASSWORD GENERATOR
# ══════════════════════════════════════════════════════════════════════════
def generate_password(length=16, use_upper=True, use_lower=True,
                      use_digits=True, use_symbols=True):
    chars = ""
    required = []

    if use_upper:
        chars += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_lower:
        chars += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))
    if use_digits:
        chars += string.digits
        required.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        chars += symbols
        required.append(random.choice(symbols))

    if not chars:
        print(f"{RED}❌ Select at least one character type!{RESET}")
        return None

    # Fill remaining length randomly
    remaining = length - len(required)
    password_list = required + [random.choice(chars) for _ in range(remaining)]
    random.shuffle(password_list)
    return "".join(password_list)


# ══════════════════════════════════════════════════════════════════════════
# 3. SAVE / LOAD PASSWORDS
# ══════════════════════════════════════════════════════════════════════════
def load_passwords():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_password(site, password):
    data = load_passwords()
    data[site] = {
        "password": password,
        "saved_on": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "strength": check_strength(password)[0]
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n{GREEN}✅ Password saved for '{site}'!{RESET}")


def view_saved():
    data = load_passwords()
    if not data:
        print(f"\n{YELLOW}⚠️  No passwords saved yet!{RESET}")
        return

    print(f"\n{BOLD}{'='*55}{RESET}")
    print(f"{BOLD}🔐 SAVED PASSWORDS{RESET}")
    print(f"{'='*55}")
    for i, (site, info) in enumerate(data.items(), 1):
        strength = info["strength"]
        color = GREEN if strength == "STRONG" else YELLOW if strength == "MEDIUM" else RED
        print(f"  {i}. {CYAN}{site}{RESET}")
        print(f"     Password : {info['password']}")
        print(f"     Strength : {color}{strength}{RESET}")
        print(f"     Saved on : {info['saved_on']}")
        print()
    print(f"{'='*55}\n")


def delete_password(site):
    data = load_passwords()
    if site in data:
        del data[site]
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"{GREEN}✅ Password for '{site}' deleted!{RESET}")
    else:
        print(f"{RED}❌ No password found for '{site}'!{RESET}")


# ══════════════════════════════════════════════════════════════════════════
# 4. MAIN MENU
# ══════════════════════════════════════════════════════════════════════════
def print_menu():
    print(f"\n{BOLD}{CYAN}{'='*50}{RESET}")
    print(f"{BOLD}{CYAN}  🔐 PASSWORD STRENGTH CHECKER & MANAGER{RESET}")
    print(f"{BOLD}{CYAN}{'='*50}{RESET}")
    print(f"  {BOLD}1.{RESET} Check Password Strength")
    print(f"  {BOLD}2.{RESET} Generate Strong Password")
    print(f"  {BOLD}3.{RESET} Save a Password")
    print(f"  {BOLD}4.{RESET} View Saved Passwords")
    print(f"  {BOLD}5.{RESET} Delete a Password")
    print(f"  {BOLD}6.{RESET} Exit")
    print(f"{CYAN}{'='*50}{RESET}")


def main():
    print(f"\n{BOLD}{GREEN}Welcome to Password Strength Checker! 🔐{RESET}")

    while True:
        print_menu()
        choice = input(f"\n{BOLD}Enter your choice (1-6): {RESET}").strip()

        # ── Option 1: Check Strength ──────────────────────────────────
        if choice == "1":
            pwd = input(f"\n{BOLD}Enter password to check: {RESET}").strip()
            if pwd:
                display_strength(pwd)
            else:
                print(f"{RED}❌ Please enter a password!{RESET}")

        # ── Option 2: Generate Password ───────────────────────────────
        elif choice == "2":
            print(f"\n{BOLD}🔧 Password Generator Settings:{RESET}")
            try:
                length = int(input("  Length (default 16): ").strip() or 16)
                length = max(8, min(length, 64))
            except ValueError:
                length = 16

            upper   = input("  Include UPPERCASE? (y/n, default y): ").strip().lower() != "n"
            lower   = input("  Include lowercase? (y/n, default y): ").strip().lower() != "n"
            digits  = input("  Include numbers?   (y/n, default y): ").strip().lower() != "n"
            symbols = input("  Include symbols?   (y/n, default y): ").strip().lower() != "n"

            pwd = generate_password(length, upper, lower, digits, symbols)
            if pwd:
                print(f"\n{GREEN}{BOLD}✅ Generated Password:{RESET}")
                print(f"   {CYAN}{BOLD}{pwd}{RESET}")
                display_strength(pwd)

                save = input("💾 Save this password? (y/n): ").strip().lower()
                if save == "y":
                    site = input("   Enter site/app name: ").strip()
                    if site:
                        save_password(site, pwd)

        # ── Option 3: Save Password ───────────────────────────────────
        elif choice == "3":
            site = input(f"\n{BOLD}Enter site/app name: {RESET}").strip()
            pwd  = input(f"{BOLD}Enter password: {RESET}").strip()
            if site and pwd:
                display_strength(pwd)
                save_password(site, pwd)
            else:
                print(f"{RED}❌ Site and password cannot be empty!{RESET}")

        # ── Option 4: View Saved ──────────────────────────────────────
        elif choice == "4":
            view_saved()

        # ── Option 5: Delete ──────────────────────────────────────────
        elif choice == "5":
            view_saved()
            site = input(f"{BOLD}Enter site name to delete: {RESET}").strip()
            if site:
                confirm = input(f"{RED}Are you sure? (y/n): {RESET}").strip().lower()
                if confirm == "y":
                    delete_password(site)

        # ── Option 6: Exit ────────────────────────────────────────────
        elif choice == "6":
            print(f"\n{GREEN}{BOLD}Goodbye! Stay safe online! 🔐{RESET}\n")
            break

        else:
            print(f"{RED}❌ Invalid choice! Enter 1-6{RESET}")


if __name__ == "__main__":
    main()
