message="Hello there. My name is Sadık Turan."
# message= message.upper() #herşeyi büyük harf yapma
# message= message.lower() #her şeyi küçük harf yapma
# message= message.title() #her kelimenin ilk harfi büyük yapma
# message= message.capitalize() #ilk harfi büyük yapma
# message= message.strip() #boşlukları kaldırıp düzeltme vb. # rstrip sağdan olanları siliyor. lstrip soldan olanları siliyor.
# message= message.split() #kelimeleri hep ayırır
# message=" ".join(message) #kelimeleri hep birleştirir
# message= message.split(".")
# index=message.find("Sadık")
# print(index)
# isFound= message.startswith("H")
# isFound= message.endswith(".")
# print(isFound)
# message=message.replace("Sadık","Çınar")
# message=message.replace("Ç","c").replace("ö","o").replace(" ","-")
message=message.center(100,"-")
print(message)

#STRİNGS-DEMO

website= "http://www.sadikturan.com"
course="python kursu: baştan sona python programlama rehberiniz (40 saat)"
print(len(course))
print(website[7:10])
print(website[-3:])
print(course[0:15])
print(course[-15:])
print(course[::-1])
s="hello world"
s="H"+s[1:6]+"W"+s[-4:]
print(s)

yazı="abc "*3
print(yazı)

###

name=" ilyas efe"
surname=" sarısüleyman"
age=18
aynı="My name is"
greeting=(aynı+name+surname+".\nI'm "+str(age)+" years old.")
length=len(greeting)
# print(greeting)
# print(length)
# print(greeting[0])
# print(greeting[length-1])
# print(greeting[-1])
# print(greeting[0:9])
# print(greeting[0:56:2])

#STRİNGS METHODS UYGULAMA

website= "http://www.sadikturan.com"
course="python kursu: baştan sona python programlama rehberiniz (40 saat)"

# result1=" Hello World ".strip()
# # result1=result1.strip
# print(result1)

# result2=website.strip(".htp:wcom/")
# print(result2)

# result3= course.lower()
# print(result3)

# result4= website.count("a",-4:)  # son 4 harfte a harfi var mı?
# print(result4)

# result5=website.startswith("www")
# result51=website.endswith("com")
# print(result5)
# print(result51)

# result6=website.find(".com")
# result61=website.find(".com",0,10)
# result62=course.rfind("python")
# result62=website.index("com")
# result62=website.rindex("com") # bulamazsa valueError verir.
# print(result6)
# print(result61)
# print(result62)


# result7= course.isalpha()
# result71="hello".isalpha()
# print(result7)
# print(result71)
# result72=course.isdigit()
# result73="123".isdigit()
# print(result72)
# print(result73)

# result8="contents".center(50,"*")
# result81="contents".ljust(50,"*")
# result82="contents".rjust(50,"*")
# print(result8)
# print(result81)
# print(result82)

# result9=course.replace(" ", "-",2)
# print(result9)

# result10="Hello World".replace("World","There")
# print(result10)

# result11=course.split(" ")
# # result11=result11[2]
# print(result11[2])


