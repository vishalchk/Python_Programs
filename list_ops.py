def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def sum_list(numbers):
    return sum(numbers)

def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))

def sort_list(numbers):
    return sorted(numbers)

def second_largest(numbers):
    unique_sorted = sorted(set(numbers))
    return unique_sorted[-2]
