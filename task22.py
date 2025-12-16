salary = 5000      # Ежемесячная зарплата
spend = 6000       # Траты за первый месяц
months = 10        # Количество месяцев
increase = 0.03    # Ежемесячный рост цен

money_capital = 0

for _ in range(months):
    if spend > salary:
        money_capital += spend - salary
    spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))