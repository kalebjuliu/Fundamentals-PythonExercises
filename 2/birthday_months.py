from collections import Counter

birthday_dict = {
    "Benjamin Franklin": "17 January 1706",
    "Albert Einstein": "14 March 1879",
    "Isaac Newton": "4 January 1643"
}
months = []

birthday_months = list(birthday_dict.values())
for dates in birthday_months:
  dates = dates.split()
  months.append(dates[1])

c = Counter(months)
print(c)
