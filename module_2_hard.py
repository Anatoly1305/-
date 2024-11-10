n = int(input("Введите Число От 3 до 20: "))
def password(number):
    password = ""
    for i in range(1, number):
        for j in range(2, number):
            if i >= j:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password
resilt = password(n)
print("Ваш Пароль", password(n))