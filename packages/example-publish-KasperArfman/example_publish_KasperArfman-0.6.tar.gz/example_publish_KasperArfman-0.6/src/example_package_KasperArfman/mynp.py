import numpy as np

def displacement(v, dt=1):
    """ Return list of difference x[i+dt] - x[i]
    """
    if dt<1: raise ValueError("Stride must be 1 or greater")
    return np.array([b-a for a, b in zip(v[:-dt], v[dt:])])


def remove_nan(x, axis=None):
    """      (-> axis 0)
      1   2 NaN inf NaN
      5 NaN NaN   4   0
      4   3   2   1   3
    """
    result = []

    # if axis is None, return a 1D array of all values that are not NaN
    # [1, 2, inf, 5, 4, 0, 4, 3, 2, 1, 3]
    if axis is None:
        for row in x:
            result.extend(row[~np.isnan(row)])

    # if axis is 0, return every row that does not contain nan
    # [[4 3 2 1 3]]      
    elif axis == 0:
        for row in x:
            if np.all(row==row):  # if there are no NaN values
                result.append(row)
        result = np.array(result)

    # if axis is 1, return every col that does not contain nan
    # [1 inf]
    # [5   4]
    # [4   1]
    elif axis == 1:
        for row in x.T:
            if np.all(row==row):  # if there are no NaN values
                result.append(row)
        result = np.array(result).T

    return result



def linear_lstsq(x, y, rcond=None):
    """ Compute coefficients of: y = ax + b """
    A = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(A, y, rcond)[0]
    return a, b


def main():
    v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


    q = displacement(v, dt=5)

    print(q)

if __name__ == "__main__":
    main()