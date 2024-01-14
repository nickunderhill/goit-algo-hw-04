def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = arr_index = 0

        # Копіювання даних у тимчасові масиви
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                arr[arr_index] = left[left_index]
                left_index += 1
            else:
                arr[arr_index] = right[right_index]
                right_index += 1
            arr_index += 1

        # Перевірка, чи залишились елементи
        while left_index < len(left):
            arr[arr_index] = left[left_index]
            left_index += 1
            arr_index += 1

        while right_index < len(right):
            arr[arr_index] = right[right_index]
            right_index += 1
            arr_index += 1


if __name__ == "__main__":
    test_arr = [12, 11, 5, 13, 5, 6, 7]
    print("Вхідний масив:", test_arr)
    merge_sort(test_arr)
    print("Відсортований масив:", test_arr)
