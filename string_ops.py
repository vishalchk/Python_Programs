def is_string_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def count_words(s):
    return len(s.split())
