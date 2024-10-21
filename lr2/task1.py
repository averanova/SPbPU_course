money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0 #количество месяцев без долгов
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital+salary>=spend:
    money_capital = money_capital-spend+salary
    months += 1
    spend += spend*increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
