f1 = open('ventas.csv', 'r')
f2 = open('ventas.csv.tmp', 'w')
for line in f1:
    f2.write(line.replace(',', '.'))
f1.close()
f2.close()