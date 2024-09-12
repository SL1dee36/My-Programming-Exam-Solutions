def recover_password(sequence, requirements, max_length):

    last_occurrence = {}

    for i in range(len(sequence) - 1, -1, -1):
        char = sequence[i]
        if char in requirements:
            last_occurrence[char] = i
        if len(last_occurrence) == len(requirements) and i + max_length >= len(sequence):
            substring = sequence[i: min(len(sequence), i + max_length + 1)]

            if all(char in substring for char in requirements):
                return substring

    return '-1'

sequence = input()
requirements = input()
max_length = int(input())

password = recover_password(sequence, requirements, max_length)

print(password)