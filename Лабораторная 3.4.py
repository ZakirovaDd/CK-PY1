salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
i = 0    # счетчик

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
for i in range(months + 1):
    if i >= 1 and i < 2:
        need_money += spend - salary
    elif i >= 2:
        spend = spend * (increase + 1)
        need_money += spend - salary


print(round(need_money))
