def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Переміщуємо елементи arr[0..i-1], які більші за key, на одну позицію вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляємо key
        arr[j + 1] = key


if __name__ == "__main__":
    test_arr = [12, 11, 5, 13, 5, 6, 7]
    print("Вхідний масив:", test_arr)
    insertion_sort(test_arr)
    print("Відсортований масив:", test_arr)
