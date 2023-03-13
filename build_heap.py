# python 3

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
    # input from keyboard or file
    source = input("Enter 'K' for keyboard input, 'F' for file input: ")
    if source == 'K':
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements separated by space: ").split()))
    elif source == 'F':
        filename = input("Enter the filename: ")
        with open(filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input source")
        return
    
    # input for heap type
    heap_type = input("Enter 'I' for a min-heap, 'D' for a max-heap: ")
    if heap_type not in ['I', 'D']:
        print("Invalid heap type")
        return
    
    # check length of data
    assert len(data) == n
    
    # build the heap and get swaps
    swaps = build_heap(data)
    
    # output number of swaps and all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    
    # output sorted data
    if heap_type == 'I':
        sorted_data = []
        for i in range(n):
            sorted_data.append(data[0])
            data[0] = data[-1]
            data.pop()
            swaps += sift_down(0, data)
        print(" ".join(map(str, sorted_data)))
    elif heap_type == 'D':
        sorted_data = []
        for i in range(n):
            sorted_data.append(data[-1])
            data[-1] = data[0]
            data.pop(0)
            swaps += sift_down(0, data)
        print(" ".join(map(str, sorted_data[::-1])))

if __name__ == "__main__":
    main()