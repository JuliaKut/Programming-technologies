# 2.і
# виведення констант

print("My constant", True)
print("CONSTANT2", None)
G=255
L=200
print("G=",G,"L=",L)
print("G-L=",G-L)

# 2.іі
# моє прізвище починається на букву "к" ,я не знайшла функції на цю букву,
# тому візму функцію на букву "с" та на букву "l" (chr , len)
print("------------------------------------------------------")
x=chr(10045)
y=len("довжина цього рядка")
print("Символ за номером 10045", x)
print("Довжина цього рядка ", y)


# 2.iii
# демонструю роботу циклів і розгалужень
print("------------------------------------------------------")
for k in range(7):
    print(k)
    k=2

z=15
if z<10:
    print("z<10")
elif z>10:
    print("z>10")
else:
    print("error")

# 2.iv
# Конструкція try->except->finally
print("------------------------------------------------------")
keys= {"a":1,"b":2,"c":3,"d":4}
try:
    value =keys['e']
except KeyError:
    print("даного ключа не існує")
finally:
    print("результат")

# 2.v
# Контекст-менеджер with
print("------------------------------------------------------")
with open("README.md", "r") as readme:
    for line in readme:
        print(line)

# 2.vi
# Python lambdas
print("------------------------------------------------------")

suma = lambda x, y ,z: x+y+z
print("Виклик функції:", suma(1,2,3))
