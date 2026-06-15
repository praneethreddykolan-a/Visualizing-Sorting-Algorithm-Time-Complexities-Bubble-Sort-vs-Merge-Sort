import random
import time
import matplotlib.pyplot as plt

# -------------------------
# Bubble Sort
# -------------------------
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# -------------------------
# Merge Sort
# -------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -------------------------
# Input Sizes
# -------------------------
sizes = [100, 500, 1000, 2000, 5000]

bubble_times = []
merge_times = []

print("Running tests...\n")

for size in sizes:

    data = [random.randint(1, 10000) for _ in range(size)]

    # Bubble Sort Timing
    start = time.perf_counter()
    bubble_sort(data)
    end = time.perf_counter()

    bubble_time = end - start
    bubble_times.append(bubble_time)

    # Merge Sort Timing
    start = time.perf_counter()
    merge_sort(data)
    end = time.perf_counter()

    merge_time = end - start
    merge_times.append(merge_time)

    print(f"Size: {size}")
    print(f"Bubble Sort Time: {bubble_time:.6f} sec")
    print(f"Merge Sort Time : {merge_time:.6f} sec")
    print("-" * 40)

# -------------------------
# Plot Graph
# -------------------------
plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    bubble_times,
    marker='o',
    linewidth=2,
    label='Bubble Sort'
)

plt.plot(
    sizes,
    merge_times,
    marker='s',
    linewidth=2,
    label='Merge Sort'
)

plt.title("Bubble Sort vs Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# -------------------------
# Display Results Table
# -------------------------
print("\nFinal Results")
print("=" * 50)

for i in range(len(sizes)):
    print(
        f"Size={sizes[i]:5d} | "
        f"Bubble={bubble_times[i]:.6f}s | "
        f"Merge={merge_times[i]:.6f}s"
    )