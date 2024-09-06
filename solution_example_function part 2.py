# 1) Faktorial rekursif

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(3))

# 2) Map function ganjil genap

def ganjilGenap(angka) :
    if(angka % 2 == 0) :
        return 'Genap'
    return 'Ganjil'

def ubahJadiGanjilGenap(listAngka) :
    return list(map(ganjilGenap, listAngka))

list1 = [1,3,4,5]
list2 = [22,17,19,20,14]
list3 = [1,3,5]
list4 = [2,4,6]

list1 = ubahJadiGanjilGenap(list1)
list2 = ubahJadiGanjilGenap(list2)
list3 = ubahJadiGanjilGenap(list3)
list4 = ubahJadiGanjilGenap(list4)

print(list1)
print(list2)
print(list3)
print(list4)

# 3) Filter function gaji

def filterGaji(listGaji) :
    return list(filter(lambda gaji : gaji * 95/100 > 9000000, listGaji))

list1 = [9100000,9800000,9500000,10300000,9300000]

list1 = filterGaji(list1)

print(list1)
