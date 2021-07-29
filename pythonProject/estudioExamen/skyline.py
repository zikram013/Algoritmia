edificios=int(input())
listaEdiCar=list()
for i in range(edificios):
    ini,altura,fin=map(int,input().strip().split())
    listaEdiCar.append((ini,altura,fin))
