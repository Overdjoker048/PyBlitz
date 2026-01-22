from main import *
from pympler import asizeof

for i in range(4):
    arr = array(8, 2**i)
    print(asizeof.asizeof(arr), ":", 2**i)
"""printf(f"{len(arr)}\n{arr}\n")
printf(f"{asizeof.asizeof(True)*8}\n{asizeof.asizeof(arr)}")"""
"""var.resize(18)
printf(f"{len(var)}\n")
"""

#len    ✅
#str    ✅
#get    ✅
#set    ✅
#iter   
#next   
#resize 
#faire en sorte que le set mette l'info a l index en partant de la gauche

#bool     (1 bits)
#char     (8 bits)

#int2     (2 bits)
#uint2    (2 bits)
#int4     (4 bits)
#uint4    (4 bits)
#int8     (8 bits)
#uint8    (8 bits)
#int16    (16 bits)
#uint16   (16 bits)
#int32    (32 bits)
#uint32   (32 bits)

#float16  (16 bits)
#float32  (32 bits)
#float64  (64 bits)
#array custom (1bits 2bits 4bits 8bits)

#ajouter type file
#optimiser code
#refaire le code en c++
#créer des remakes des type (deriver de int avec convertion et conso de ram optimiser)
#faire systeme de stockage de type
#type matrice nD