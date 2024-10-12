print("hello.")
# num1= int(input("enter first number")) 
# num2= int(input("enter second number")) 

# for i in range(num1,num2):
#     #print(i) 
#     #print(i+1)

#     product = i *(i +1)
#     #print(product)

#     print(f"-{i} x {i+1} = {product}")

num = int(input(":type a number!"))

for i in range(1,num):

    product = i * (i+1)

    if num == product:
        print(f"{num} is a pronic number!")
        is_pronic = True
        break

if is_pronic == False:
    print("this is not a pronic number.")

