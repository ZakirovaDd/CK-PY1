money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
money_for_living = salary + money_capital
# TODO Оформить решение

while money_for_living > 0:
    money_for_living -= spend
    money_for_living -= spend * increase * month
    month += 1
print(month)
