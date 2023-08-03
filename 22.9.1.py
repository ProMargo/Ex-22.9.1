def sort_list(n):
    x = len(n)
    count = 0
    for i in range(x):
        for j in range(x - i - 1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] >= element:
        if array[middle - 1] < element and element <= array[middle]:
            return middle - 1
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
    elif element == array[middle - 1]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


n_list = list(map(int, input('Введите числа через пробел: ').split(' ')))
x = int(input("Введите число: "))

print(sort_list(n_list))
while x < n_list[0] or x > n_list[-1]:
    print("Числа нет в диапозоне")
    x = int(input("Введите число: "))
else:
    print(binary_search(n_list, x, 0, len(n_list)-1))