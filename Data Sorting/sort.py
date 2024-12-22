def sortNumbers(data, condition):
    for iteration in range(len(data)):
        for j in range(len(data)-iteration-1):
             if condition == 'ASC':
                 if data[j] > data[j + 1]:
                     data[j], data[j + 1] = data[j + 1], data[j]
             elif condition == 'DESC':
                 if data[j] < data[j+1]:
                     data[j], data[j+1] = data[j+1], data[j]
    return data
def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise (ValueError('Invalid input data'))
    for iteration in range(len(data)):
        for j in range(len(data) - iteration - 1):
            if condition == 'ASC':
                if weights[j] > weights[j + 1]:
                    weights[j], weights[j + 1] = weights[j + 1], weights[j]
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif condition == 'DESC':
                if weights[j] < weights[j + 1]:
                    weights[j], weights[j + 1] = weights[j + 1], weights[j]
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data