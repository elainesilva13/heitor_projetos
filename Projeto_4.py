contador = ""
for atesemacento in range(1000,-1,-1):
    contador = contador + str(atesemacento) 
    if atesemacento != 0:
         contador = contador + ", "
print(contador)