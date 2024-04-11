tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
def common_element(input1,input2):
    new_list=[]
    for item in input1:
        if item in input2:
            new_list.append(item)
    return tuple(new_list)

print(common_element(tuple1,tuple2))

#alternate method
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))