def is_string_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def count_words(s):
    return len(s.split())

def count_consonants(s):
    return sum(1 for ch in s.lower() if ch.isalpha() and ch not in "aeiou")

def count_uppercase(s):
    return sum(1 for ch in s if ch.isupper())

def count_lowercase(s):
    return sum(1 for ch in s if ch.islower())

def remove_whitespace(s):
    return "".join(s.split())

def trim_string(s):
    return s.strip()

def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())
