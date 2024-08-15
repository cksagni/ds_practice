

def insert(arr, size, temp):
    if size == 0 or arr[size-1] <= temp:
        arr[size] = temp
        return
    val = arr[size-1]
    insert(arr, size-1, temp)
    arr[size] = val
    return


def sort_rec(arr, size):
    if size <= 1:
        return arr
    temp = arr[size - 1]
    size -= 1
    sort_rec(arr, size)
    insert(arr, size, temp)
    return arr


if __name__ == "__main__":
    arr1 = [2, 0, 1, 5, 7, 1]
    print(sort_rec(arr1, len(arr1)))
