from math_ops import add_numbers, subtract_numbers, multiply_numbers, divide_numbers, power, modulus, square_root, factorial, is_prime, reverse_number, is_palindrome, is_anagram
from string_ops import is_string_palindrome, reverse_string, count_vowels, count_words, count_consonants, count_uppercase

print("1:", "Hello World!")
print("2:", "Vishal Chauhan")
print("3:", "Learning Python is fun!")
print("4:", "This is my first script.")
print("5:", "Let's keep coding.")

for i in range(1, 6):
    print("6:", i)

n = 1
while n <= 5:
    print("7:", n)
    n += 1

print("8:", add_numbers(3, 4))
print("9:", subtract_numbers(10, 4))
print("10:", multiply_numbers(3, 4))
print("11:", divide_numbers(12, 4))
print("12:", power(2, 3))
print("13:", modulus(10, 3))
print("14:", square_root(16))
print("15:", factorial(5))
print("16:", is_prime(7))
print("17:", is_palindrome(121))
print("18:", is_anagram(123, 456))
print("19:", is_string_palindrome("A man a plan a canal Panama"))
print("20:", reverse_string("Vishal"))
print("21:", count_vowels("Vishal Chauhan"))
print("22:", count_words("Learning Python is fun"))
print("23:", count_consonants("Vishal Chauhan"))
print("24:", count_uppercase("Vishal Chauhan"))
