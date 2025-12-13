# Temperature Range
#🔹 Check temperature range and print appropriate message


temp=int(input("Enter Temperature : "))

if temp<0:
    print("It's Freezing !!")
elif temp >0 and temp<10:
    print("It's Cold !")
elif temp>10 and temp<20:
    print("It's Cool !")
elif temp>20 and temp<30:
    print("It's Warm !")
else:
    print("It's Hot !!")
