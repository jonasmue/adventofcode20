from common import first_invalid, get_input


def encryption_weakness():
    invalid = first_invalid()
    
    # Complexity we don't consider part 1 (previous line):
    # O(n+c) time and O(1) space
    # with n: length of input, c: length of contiguous sequence
    
    numbers = get_input()
    left, right = contiguous_sequence_pointers(numbers, invalid)
    max_item = numbers[left]
    min_item = numbers[left]
    for i in range(left, right + 1):
        max_item = max(max_item, numbers[i])
        min_item = min(min_item, numbers[i])
    return min_item + max_item
    

def contiguous_sequence_pointers(numbers, invalid):
    left = 0
    right = 1
    current_sum = numbers[left] + numbers[right]
    while True:
        if current_sum == invalid:
            return left, right
        elif current_sum < invalid or left == right - 1:
            right += 1
            current_sum += numbers[right]
        else:
            current_sum -= numbers[left]
            left += 1
    
    
if __name__ == "__main__":
    print(encryption_weakness())
