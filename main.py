#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.
def hello_name(user_name):
    print(f'hello_{user_name.upper()}!')
#Testing
#hello_name("mstentler")

#Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and 
# returns nothing
def first_odds():
    for i in range(1,100,2):
        print(i,end=" ")
#Testing
#first_odds()


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given 
#list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    temp = sorted(a_list)
    return temp.pop()

#Testing
#a_list = [3,8,99,4,1,33,2,85,100,49,46,37]
#print(max_num_in_list(a_list))


#Qestion 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
#but not divisible by 100, unless it is also divisible by 400. The return should be boolean 
#Type (true/false).

def is_leap_year(a_year):
    #year is divisble by 4
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 4 == 0 and a_year % 400 == 0:
        return True
    else:
        return False

#Testing   
#a_list = [1700,1800,1900,2000,2023,2024,2025,2028,2100]
#for year in a_list:
#    print(is_leap_year(year), end="\n")
    
    
    
#Question 5
 #Write a function to check to see if all numbers in list are consecutive numbers. 
 #For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive 
 #numbers. The return should be boolean Type.      

def is_consecutive(a_list):
    temp_list = sorted(a_list)
    num1 = temp_list.pop()
    while temp_list:
        if num1 - temp_list[-1] == 1:
            num1 = temp_list.pop()
            continue
        else:
            return False
    return True 

#Testing 
#list_1 = [1,2,3,4,5]
#list_2 = [9,5,7,4,1,2,6,8,10]
#print("List 1: " + str(is_consecutive(list_1)), end="\n")
#print("List 2: " + str(is_consecutive(list_2)), end=" ")