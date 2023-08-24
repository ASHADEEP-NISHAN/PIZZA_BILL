#PIZZA BILL GENERATOR
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
number_of_pizzas=int(input("enter no of pizza"))
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ") 
sz=size.lower()
p=add_pepperoni.lower()
e=extra_cheese.lower()
list={'s':15,'m':20,'l':25}
s=list[sz]
bill=number_of_pizzas*s
if sz=='s':
    if p=='y':
        bill +=number_of_pizzas*2
    else:
        pass
else:
    if p == 'y':
        bill +=number_of_pizzas * 3
    else:
        pass
if e=='y':
    bill+=number_of_pizzas*1
else:
    pass


print(f"your orders are '{number_of_pizzas}' '{size}'size pizza with pepperoni :{add_pepperoni}  and extra chese :{extra_cheese} ")

print(" your final bill is:",bill)