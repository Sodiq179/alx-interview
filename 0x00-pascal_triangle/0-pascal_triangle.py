def pascal_triangle(n):
    """
    This function returns a list of lists of
    integers representing the Pascal’s triangle of n:
    """
    if n < 0:
        return []

    else:
        result = []
        for i in range(0,n):
            numElement = i + 1
            totalSum = 2**i
            indResult = []

            try:
                prev = result[i - 1]
                currResult = [prev[x]+prev[x-1] for x in range(1,i)]
                currResult = [1, *currResult, 1]
                result.append(currResult)
            except:
                result.append([1]*numElement)
        return result