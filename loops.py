#1.uzd

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

def filt(i): 

    if i > 5: 

        return False 

    else: 

        return True 

 

     

filtered = filter(filt, a) 

for i in filtered: 

    print(i) 


#2.uzd

year = int(input("Write any year you wish, and program will answer next leap year: ")) 

 

if  year % 4 == 0: 

  print("Next leap year is after 4 years")  

elif year % 4 == 1: 

  print("Next leap year is after 3 years")  

elif year % 4 == 2: 

  print("Next leap year is after 2 years")  

else: 

  print("Next leap year is next year"), year

#3.uzd

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

 

c = [] 

for i in a: 

  for j in b: 

    if i == j: 

      c.append(i) 

 

print(list(set(c))) 