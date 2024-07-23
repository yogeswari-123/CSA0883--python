def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def max_of_binaries(binaries):
    max_binary = binaries[0]
    for binary in binaries:
        if binary_to_decimal(binary) > binary_to_decimal(max_binary):
            max_binary = binary
    return max_binary

binaries = ["1101", "1011", "1001"]


max_binary = max_of_binaries(binaries)


print(f"Maximum Number: {max_binary}")


