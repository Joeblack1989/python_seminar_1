# # Напишите программу для проверки истинности утверждения ¬(X ⋁(или) Y ⋁ Z) = ¬X ⋀ (и) ¬Y ⋀ ¬Z для всех значений предикат.

for x in range (2):
    for y in range (2):
        for z in range (2):
            print(f'for X = {x}, Y = {y}, Z = {z} ¬(X ⋁ (или) Y ⋁ Z) = ¬X ⋀ (и) ¬Y ⋀ ¬Z {not (x or y or z)==(not x and not y and not z)}')