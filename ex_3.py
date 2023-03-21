filename = ['1.arroz.txt', '2.tuyo.txt', '3.thue.txt']

for filename in filename:
    filename = filename.replace('.','-', 1)
    filename = filename(filename)

print(filename)
