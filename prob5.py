n=int(input("Introduceti numarul: "))
suma=0
for i in range (1,n) :
    if (i%3==0) and (i%5==0):
        suma+=i

print("Suma nr ce se impart la 3 si 5 este: ", suma)