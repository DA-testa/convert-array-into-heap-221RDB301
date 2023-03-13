# python 3

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        SiftDown(data, i, swaps)
    return swaps


def SiftDown(data, i, swaps):
    size = len(data)
    min_index = i
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2 
    if leftChild < size and data[leftChild] < data[min_index]:
        min_index = leftChild
    if rightChild < size and data[rightChild] < data[min_index]:
        min_index = rightChild
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        SiftDown(data, min_index, swaps)


def main():
    source = input("Enter 'I' for keyboard input, 'F' for file input: ")
    if "I" in source:
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements separated by space: ").split()))
    else:
        if "F" in source:
            filename = input("Enter the filename: ")
            with open("./tests/" + filename, mode = "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    assert len(data) == n
    
    swaps = build_heap(data)
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

