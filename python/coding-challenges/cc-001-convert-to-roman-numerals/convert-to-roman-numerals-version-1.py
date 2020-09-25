num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

num = input("Please enter a number between 1 and 3999, inclusively :")
# num = 55
if num == "exit":
    print("Good by !")
    
elif int(num)>4000 or int(num)<1:
    print("Not Valid Input !!!")

elif int(num) < 4000 or int(num) >0 :
    roman = ''
    a = int(num)
    while a > 0:
        for i, r in num_map:
            while a >= i:
                roman += r
                a -= i
    print(roman)


    
