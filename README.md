# 🔐 Simple Account Manager

A command-line account management system built in Python. Demonstrates core authentication logic, role-based permissions, and account security features using in-memory data structures.

---

## 🖥️ Features

- User creation with role assignment (`admin`, `student`, `lecturer`)
- Login system with failed attempt tracking
- Automatic account lockout after 3 failed logins
- Password strength validation
- Admin-only controls to delete and unlock accounts
- Account summary and role-based reporting

## ⚙️ Technologies

- Python 3
- Dictionaries for in-memory data storage
- Modular function design

---

> **Note:** This project stores data in-memory and accounts reset when the program ends. I have made an upgraded version which feature persistent storage and bcrypt for password hashing. [Account Manager v2](https://github.com/Zeyrian/Account-Manager-v2).
