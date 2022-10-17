# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print()
print('утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно при')
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z)


# def f(x,y,z):
#     return [ x for x in range(2) y for y in range(2) for z in range(2) if not (x or y or z) == (not x and not y and not z)]
# # list = [x for x in range(2) y for y in range(2) for z in range(2) if not (x or y or z) == (not x and not y and not z)]  
# print (x, y, z)