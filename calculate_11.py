def calculate_list(l):
    if len(l)==0:
        return 0
    return l[0]+calculate_list(l[1:])

def calculate_list_even(l):
    if l[0]%2==0:
        return l[0]+calculate_list_even(l[1:])
    return calculate_list_even(l)
    
my_list=list(map(int,input("enter numbers: ").split()))

while True:
    x=input("what do you want?(calculate / calculate even :")
    if x=="calculat":
        print("sum of list =" ,calculate_list(my_list))
    elif x == "calculat even":
        print("sum of list =" ,calculate_list_even(my_list))
    elif x=="exit":
        break
    else:
        print("Invalid option, try again.")
