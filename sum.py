def summing():
    print("Hello from a function")

    f = open("sample.txt", "r")
    numbers = f.readlines()
    total_to_add = 0
    for n in numbers:
        try:
            total_to_add += int(n)
        except ValueError:
            break

    f.close()

    # Append-adds at last
    f = open("sample.txt", "a")
    f.write("\n")
    f.write(str(total_to_add))
    f.close()

