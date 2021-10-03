def first_fit(block_sizes, process_sizes, m, n):
    block_id = [-1] * n

    for i in range(n):
        for j in range(m):
            if block_sizes[j] >= process_sizes[i]:
                block_id[i] = j
                block_sizes[j] -= process_sizes[i]
                break

    print("Process Size\tBlock No.")
    for i in range(n):
        print(process_sizes[i], end="\t\t")

        if block_id[i] != -1:
            print(block_id[i] + 1)
        else:
            print("NA")


m = int(input("Enter no. of blocks: "))
n = int(input("Enter no. of processes: "))

block_sizes = [int(i) for i in input("Enter block sizes: ").split()]
process_sizes = [int(i) for i in input("Enter process sizes: ").split()]

first_fit(block_sizes, process_sizes, m, n)
