import csv
res={}
with open("sample.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        l=[]
        print(row)
        for i in row:
            if i in res:
                res[i] += row[i]+" "
            else:
                res[i] = l.append(row[i])
print(res)