n = int(input("Привет, введите количество билетов для покупки "))
print("Количество билетов", n)
cost_tic = 0
i = 0
a = 0
b = 990
c = 1390
for i in range(n):
    i += 1
    age = int(input(f"Введите возраст покупателя, билета {i} "))
    if age < 18:
         print(f"Цена билета: {a} руб.")
    elif 18 <= age < 25:
         cost_tic += b
         print(f"Цена билета:",b,"руб.")
    else:
         cost_tic += c
         print(f"Цена билета:",c,"руб.")
print(cost_tic)
if n > 3:
    d = (cost_tic / 100) * 10
    total_cost_tic = cost_tic - d
    print(f"Стоимость билетов при покупке от 3 шт: {total_cost_tic} руб. Скидка 10% {d} руб.")
else:
    print(f'Сумма к оплате - {cost_tic} руб.')
