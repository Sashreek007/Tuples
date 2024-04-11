new_tuple= tuple('sashreek')
def access_element(tuple,index):
    for i in range(len(tuple)):
        if index == i:
            print(tuple[i])
access_element(new_tuple,3)