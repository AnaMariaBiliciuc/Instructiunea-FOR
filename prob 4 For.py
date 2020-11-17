a=int(input("Introduceti primul nr din interval: "))
b=int(input("Introduceti ultimul nr din interval: "))
for n in range(a-1 ,b, 1) :
    if n%2!=0 :
        print(n, end=' ')