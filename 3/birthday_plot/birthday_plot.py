from bokeh.plotting import figure, show, output_file
from collections import Counter

#Data
birthday_dict = {
    "Benjamin Franklin": "17 January 1706",
    "Albert Einstein": "14 March 1879",
    "Michael Faraday": "22 September 1791",
    "James Clerk Maxwell": "13 June 1831",
    "Isaac Newton": "4 January 1643"
}
months = []

birthday_months = list(birthday_dict.values())
for dates in birthday_months:
  dates = dates.split()
  months.append(dates[1])

c = Counter(months).items()
months_counter = []

for elem in c:
  months_counter.append(elem[1])

#Bokeh Stuff
output_file("plot.html")

x_categories = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]

x = months
y = months_counter

p = figure(x_range = x_categories)
p.vbar(x=x, top=y, width=0.5)

show(p)