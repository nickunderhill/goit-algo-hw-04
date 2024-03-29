# Алгоритми - домашнє завдання 4

Було порівняно 3 алгоритми сортування:

- Merge sort
- Insertion sort
- Timsort

У якості вхідних даних було використано 3 масиви цілих додатніх чисел різного
розміру - 1000, 10000 та 100000 чисел.

За допомогою модулю `timeit` було виконано вимірювання середнього часу
сортування у секундах для кожного з алгоритмів на основі 10 замірів. Результати
наведені на зображенні нижче:

![Results](/images/comparison_result.png)

## Висновок

Можна зробити висновок, що поєднання сортування злиттям і сортування вставками
дійсно робить алгоритм Timsort набагато ефективнішим, особливо це помітно при
зростанні обсягу вхідних даних.
