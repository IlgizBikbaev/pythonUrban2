first =  int(input("Введите целое трезначное число: "))
second = int(input("Введите целое трезначное число: "))
third =  int(input("Введите целое трезначное число: "))

if first == second == third:
 print('3 совпадения')
elif first == second or second == third or first == third:
 print("2  совпадения")
else:
 print("0 совпадений")