# 🔐 Simple Account Manager

A command-line account management system built in Python. Demonstrates core authentication logic, role-based permissions, and account security features using in-memory data structures.

---

## Features

- User creation with role assignment (`admin`, `student`, `lecturer`)
- Login system with failed attempt tracking
- Automatic account lockout after 3 failed logins
- Password strength validation
- Admin-only controls to delete and unlock accounts
- Account summary and role-based reporting

## Technologies

- Python 3
- Dictionaries for in-memory data storage
- Modular function design

---

> **Note:** This project stores data in-memory — accounts reset when the program ends. For persistent storage and bcrypt password hashing, see [Account Manager v2](#).
