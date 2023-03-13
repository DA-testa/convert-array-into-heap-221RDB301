# python 3
import os

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        swaps += sift_down(i, data)
    return swaps


def sift_down(i, data):
    n = len(data)
    swaps = []
    min_idx = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_idx]:
        min_idx = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_idx]:
        min_idx = r
    if i != min_idx:
        swaps.append((i, min_idx))
        data[i], data[min_idx] = data[min_idx], data[i]
        swaps += sift_down(min_idx, data)
    return swaps


def main():
    source = input("Enter 'I' for keyboard input, 'F' for file input: ")
    if source == 'I':
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements separated by space: ").split()))
    elif source == 'F':
        filename = input("Enter the filename: ")
        path = './tests/'    
        mape = os.path.join(path, filename)
        with open(filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input source")
        return
    
    heap_type = 'I'
    
    assert len(data) == n
    
    swaps = build_heap(data)
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

