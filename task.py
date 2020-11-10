# |TASK#1|------------|


# def chisla(num) :

#     '''ОТ 1 ДО NUM'''

#     if num == 0 :
#          return []
#     else:
#         return chisla (num -1) + [num]

# print(chisla(41))



#|------------|TASK#2|------------|


# def summa (num) :

#     '''Cуммa цифр всех чисел включительно NUM'''

#     if num == 0 :
#          return 0
#     elif num == 1: 
#         return 1
#     else:
#         return num + summa (num - 1)

# print(summa(5))



# |TASK#3|------------|


# def naoborot(num):
#     if num < 10:
#         return num
#     return int(str(num % 10) + str(naoborot(num // 10)))

# print (naoborot(2334))



# |TASK#4|------------|


# def fib(num):
#     if num <= 1:
#         return num
#     else:
#         return fib(num - 1) + fib(num - 2)

# print(fib(12))



# TASK#5|------------|

# lol = dict()

# def stepPerms(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     if n not in lol:
#         lol[n] = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
#     return lol[n]


#------------|END|------------|
