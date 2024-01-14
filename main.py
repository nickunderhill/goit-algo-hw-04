import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort

GREEN = '\033[32m'
YELLOW = '\033[33m'
COLOR_END = '\033[0m'


def compare_algorithms(arr):
    return {
        "Insertion sort": timeit.timeit(lambda: insertion_sort(arr[:]), number=10),
        "Merge sort": timeit.timeit(lambda: merge_sort(arr[:]), number=10),
        "Timsort": timeit.timeit(lambda: sorted(arr[:]), number=10)
    }


def print_results(results):
    header = f"| {'Algorithm':<15} | {'Execution time':<15} |"
    separator = "| " + "-"*15 + " | " + "-"*15 + " |"
    row_template = "| {key:<15} | {value:^15.5f} |"
    footer = "| " + "-"*33 + " |"

    print(header)
    print(separator)
    for key, value in results.items():
        print(row_template.format(key=key, value=value))
    print(footer)


def main():

    print(YELLOW + "\nStarting sorting alogirhtms time execution comparison" + COLOR_END)

    test_data = {
        "small": [random.randint(0, 1000) for _ in range(1000)],
        "medium": [random.randint(0, 10000) for _ in range(10000)],
        "big": [random.randint(0, 100000) for _ in range(100000)]
    }

    for key, value in test_data.items():
        print(
            GREEN + f"\nComparing algorithms using {key} dataset of {len(value)} items\n" + COLOR_END)
        results = compare_algorithms(value)
        print_results(results)


if __name__ == "__main__":
    main()
