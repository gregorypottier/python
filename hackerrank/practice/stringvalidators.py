if __name__ == '__main__':
    s = input()
    # any returns True if at least one element of an iterable object is "truthy" (non empty iterable, non empty string, 1)
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
