import csv
res={}
def csvread(filename):
    with open(filename, 'r') as file:
        csv_file = csv.reader(file)
        f=0
        for row in csv_file:
            if(f == 0):
                for i in row:
                    res[i]=[]
                f+=1
            else:
                j = 0
                for key, value in res.items():
                    value.append(row[j])
                    j+=1
    return res

res = csvread("sample.csv")
for i in res:
    print(i,res[i])

