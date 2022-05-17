message="Hello there. My name is Sadık Turan.".split()

list1=["one","two","theree"]
list2=["four","five","six"]
numbers=[list1,list2]

# print(numbers[0][0])
# print(numbers[0])
# # print(len(numbers))
# print(message[0])


# SORULAR
arabalar=["bmw","mercedes","opel","mazda"]
result=(len(arabalar))
result=arabalar[0]
result=arabalar[3]
# arabalar[-1]="toyota"
result=str(arabalar).find("mercedes") # alttakiyle aynı şey aslında
result= "mercedes" in arabalar
result=arabalar[-2]
result=arabalar[0:3]
result=arabalar[:3]
arabalar[-2:]=["toyota","renault"] # parantezler olmadığında da aynı sonucu veriyor.
result=arabalar+["audi","nissan"]
del arabalar[-1] # result=arabalar[0:3]
result=arabalar[::-1]

a=["yiğit","bilgi",2010, [70,60,70]]
b=["sena","turan",1999, [80,80,70]]
c=["ahmet" ,"turan" ,1998, [80,70,90]]
result=a[3][0],b[3][0],c[3][0]
result=f"{a[0]} {a[1]} {2019-a[2]} yaşında ve not ortalaması {(a[3][0]+a[3][1]+a[3][2])//3}"

# print(result)
# print(arabalar)



# LİSTS METHODSS

sayılar=[1,2,34,5,66]
letters=["a","g","s","b","y","a","s"]
val=min(sayılar)
val=max(sayılar)
val=max(letters)
val=min(letters)

val=sayılar[2:4]
val=sayılar[2:]
val=sayılar[:3]

sayılar[4]= 6

sayılar.append(49)
sayılar.append(59)
sayılar.insert(0,61)

# sayılar.pop()
# sayılar.pop(2)
# sayılar.remove(49)

sayılar.sort() # sıralar
sayılar.reverse() # tersten sıralar
letters.sort()
letters.reverse()



# print(sayılar)
# print(len(sayılar))
# print(letters)
# print(len(letters))

# print(sayılar.count(1))
# print(letters.count("a"))

# sayılar.clear()
# print(sayılar)



# LİSTS METHODS UYGULAMALAR

names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

# result=names+["Cenk"]
# names.append("Cenk")

# names.insert(0,"Sena")

# names.pop(-1) # listeden eleman silerler...
# names.remove("Deniz")
# del names[-1]

# result=names.index("Deniz")
# names.pop(result)

# result= "Ali" in names
# result=names.index("Ali")

# names.reverse()

# names.sort()

# years.sort() 

# str="Chevrolet , Dacia"
# result=str.split(",")

# result=max(years)
# result=min(years)

# result=years.count(1998)

# years.clear()

markalar=[]
marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)

print(markalar)