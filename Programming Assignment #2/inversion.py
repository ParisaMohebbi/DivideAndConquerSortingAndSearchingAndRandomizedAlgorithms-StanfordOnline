def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = count_inversions(arr[:mid])
    right, right_inversions = count_inversions(arr[mid:])
    merged, split_inversions = merge_and_count_split_inversions(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions

    return merged, total_inversions

def merge_and_count_split_inversions(left, right):
    merged = []
    i = j = split_inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            split_inversions += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, split_inversions

def read_file(filename):
    with open(filename, 'r') as file:
        arr = [int(line.strip()) for line in file]
    return arr

if __name__ == "__main__":
    arr = read_file("IntegerArray.txt")
    sorted_arr, inversions = count_inversions(arr)
    print("Number of inversions:", inversions)
