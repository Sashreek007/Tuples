new_tuple=tuple('sashreek')
new_tuple2=tuple('Siddarth')
num_tuple=(1,2,3,4,5,6)
num_tuple2=(7,8,9,10,11,12,13)
new_tuple3=(num_tuple+num_tuple2)
print(new_tuple3)
print(num_tuple*3)
init_tuple = ()
print (init_tuple.__len__())
init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)