def repeatingString(s, n):
    pointer = 0
    for i in s:
        pointer += 1
        print(pointer)
        print(i)
        if pointer == len(s):
            pointer = 0
            for x in s:
                pointer += 1
                print(pointer)
                print(x)

    return pointer

print(repeatingString("Thisisthesavage", 4))