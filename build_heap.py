def heapify(data, n, i, swaps):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and data[l] > data[largest]:
        largest = l

    if r < n and data[r] > data[largest]:
        largest = r

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        swaps.append((i, largest))
        heapify(data, n, largest, swaps)


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps


def heap_sort(data):
    swaps = []
    n = len(data)
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        heapify(data, i, 0, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps1 = build_heap(data)
    swaps2 = heap_sort(data)
    swaps = swaps1 + swaps2
    assert len(swaps) <= 4 * n
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
