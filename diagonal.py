input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
def diagonal(input):
    output=[]
    for i in range(len(input_tuple)):
        output.append(input[i][i])
    return tuple(output)
print(diagonal(input_tuple))