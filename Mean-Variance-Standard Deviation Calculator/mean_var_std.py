import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.") 

    myarray = np.array(list).reshape(3, 3)

    mean_r = np.mean(myarray, axis=0).tolist()
    mean_c = np.mean(myarray, axis=1).tolist()
    mean_f = np.mean(myarray).item()

    var_r = np.var(myarray, axis=0).tolist()
    var_c = np.var(myarray, axis=1).tolist()
    var_f = np.var(myarray).item()

    std_r = np.std(myarray, axis=0).tolist()
    std_c = np.std(myarray, axis=1).tolist()
    std_f = np.std(myarray).item()

    max_r = np.max(myarray, axis=0).tolist()
    max_c = np.max(myarray, axis=1).tolist()
    max_f = np.max(myarray).item()

    min_r = np.min(myarray, axis=0).tolist()
    min_c = np.min(myarray, axis=1).tolist()
    min_f = np.min(myarray).item()

    sum_r = np.sum(myarray, axis=0).tolist()
    sum_c = np.sum(myarray, axis=1).tolist()
    sum_f = np.sum(myarray).item()

    result = {
        'mean': [mean_r, mean_c, mean_f],
        'variance': [var_r, var_c, var_f],
        'standard deviation': [std_r, std_c, std_f],
        'max': [max_r, max_c, max_f],
        'min': [min_r, min_c, min_f],
        'sum': [sum_r, sum_c, sum_f]
    }

    return result
