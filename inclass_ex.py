from datetime import date

birt = date(571, 4, 22)
death = date(632, 6, 8)

print(date.toordinal(death) - date.toordinal(birt))



