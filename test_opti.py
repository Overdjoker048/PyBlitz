# ==========================================================
# PYTHON PERFORMANCE HEADER — NUCLEAR MODE
# Objectif : vitesse maximale coûte que coûte
# Risque     : élevé
# Gain       : élevé (30–50 % selon contexte)
# ==========================================================

import sys
import gc
import os
import builtins
import threading

# GC OFF
gc.disable()

# Aucune traceback
sys.tracebacklimit = 0
sys.excepthook = lambda *args: None

# UTF-8 strict
os.environ["PYTHONUTF8"] = "1"

# Import system figé
sys.meta_path.clear()
sys.path_hooks.clear()

# IO neutralisé
sys.stdin = None
sys.stderr = None

# Stack minimale
threading.stack_size(64 * 1024)

# Supprimer builtins inutiles
for name in (
    "help", "dir", "vars", "globals",
    "locals", "input", "compile"
):
    builtins.__dict__.pop(name, None)

# Lier localement les builtins critiques
range = builtins.range
len   = builtins.len
min   = builtins.min
max   = builtins.max
sum   = builtins.sum

# Nettoyage
del builtins
del threading
del os

# ==========================================================


# Programme de calculs mathématiques
# Déclaration des variables
a = 15
b = 7
c = 3.5

# Différents calculs
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b
puissance = a ** 2
modulo = a % b
division_entiere = a // b
moyenne = (a + b + c) / 3
assert modulo == 1
if x := 10 > 5:
    print(f"x est {x}")
# Affichage des résultats
a = 12
lst = []
for i in range(20):
    lst.append(i)
    x = (12+5j)
lst2 = [i for i in "Hey"]
print(f"Addition: {a} + {b} = {addition}")
print(f"Soustraction: {a} - {b} = {soustraction}")
print(f"Multiplication: {a} × {b} = {multiplication}")
print(f"Division: {a} ÷ {b} = {division:.2f}")
print(f"Puissance: {a}² = {puissance}")
print(f"Modulo: {a} % {b} = {modulo}")
print(f"Division entière: {a} // {b} = {division_entiere}")
print(f"Moyenne de {a}, {b}, {c} = {moyenne:.2f}")
print(a)
a = complex(12)
raise ValueError