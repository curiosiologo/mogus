#!/usr/bin/env python3

import sqlite3
import os
import sys

if input("Queres continuar (vais remover a base de dados)? (y/N) ").lower() != "y":
    sys.exit()

if os.path.isfile("database.sqlite"):
    os.remove("database.sqlite")

import database

idninja = 0
database.initdb()
while True:
    nome = input("Nome do ninja: ")
    if not nome:
        break
    impostor = 1 if input("É impostor? (y/N)").lower() == "y" else 0
    ninja = (idninja, impostor, nome, None, 0)
    database.query("INSERT INTO ninja VALUES (?, ?, ?, ?, ?)", ninja)
    idninja += 1