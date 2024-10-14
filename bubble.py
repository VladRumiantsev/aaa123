def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
short_list = [6, 50, 14]
bubble_sort(short_list)
print("Sorted Short List:", short_list)
long_list = [65, 10, 2, 77, 1551, 688,]
bubble_sort(long_list)
print("Sorted Long List:", long_list)
additional_list = [53, 22, 98, 13, 341, 1, 18, 111, 88,]
bubble_sort(additional_list)
print("Sorted Additional List:", additional_list)