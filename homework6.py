def bubble_sort(ahahaha):
    n = len(ahahaha)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ahahaha[j] > ahahaha[j + 1]:
                ahahaha[j], ahahaha[j + 1] = ahahaha[j + 1], ahahaha[j]
    return ahahaha

def selection_sort(ahahahaha):
    n = len(ahahahaha)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if ahahahaha[j] < ahahahaha[min_idx]:
                min_idx = j
        ahahahaha[i], ahahahaha[min_idx] = ahahahaha[min_idx], ahahahaha[i]
    return ahahahaha

def binary_search(aha, target):
    low = 0
    high = len(aha) - 1
    while low <= high:
        mid = (low + high) // 2
        if aha[mid] == target:
            return mid
        elif aha[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
list = [100, 200, 30, 45, 67, 120, 90, 34, 56, 76, 25]
print(list)
sorted_list_bubble = bubble_sort(list.copy())
print("(Bubble Sort):", sorted_list_bubble)
sorted_list_selection = selection_sort(list.copy())
print("(Selection Sort):", sorted_list_selection)
number = 30
index = binary_search(sorted_list_bubble, number)
if index != -1:
    print(f" {number} найден в {index}")
else:
    print(f"{number} не найден")