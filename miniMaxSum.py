    min = arr[0]
    max = 0
    minTotal = 0
    maxTotal = 0
    total = 0

    for i in range(0, len(arr)):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]
        total += arr[i]

    minTotal = total - max
    maxTotal = total - min
    print(str(minTotal)+ " " + str(maxTotal))
