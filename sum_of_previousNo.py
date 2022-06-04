# calculating sum of previous numbers.. 
print('calculating sum of previous  no ..') 
num = int(input('Enter last number :  '))
num_list = [num]
for i in range(1, num):
    # print(i) #=> working
    num_list.append(num-i) 

# print(num_list) # working 
print(sum(num_list))
