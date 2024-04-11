def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length")
    sum_result = []
    for i in range(len(tuple1)):
        sum_result.append(tuple1[i] + tuple2[i])
    return tuple(sum_result)
