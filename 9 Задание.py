credits = float(input("Введите количество кредитов:"))
rate_usd = 1.25
rate_eur = 1.15
usd_amount = credits * rate_usd
eur_amount = credits * rate_eur
print(f"{credits} кредитов = {usd_amount} $")
print(f"{credits} кредитов = {eur_amount} €")