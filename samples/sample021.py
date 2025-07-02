# Tuple unpacking example
def unpack_tuple(t):
    a, b, c = t
    return a, b, c

# Example usage
if __name__ == "__main__":
    my_tuple = (1, 2, 3)
    a, b, c = unpack_tuple(my_tuple)
    print(f"Unpacked values: a={a}, b={b}, c={c}")