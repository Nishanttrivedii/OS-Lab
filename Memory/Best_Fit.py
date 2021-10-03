def best_fit(block_sizes, process_sizes, m, n):
    block_id = [-1] * n

    for i in range(n):
        best_index = -1
        for j in range(m):
            if block_sizes[j] >= process_sizes[i]:
                if best_index == -1:
                    best_index = j
                elif block_sizes[best_index] > block_sizes[j]:
                    best_index = j

        if best_index != -1:
            block_id[i] = best_index
            block_sizes[best_index] -= process_sizes[i]

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

best_fit(block_sizes, process_sizes, m, n)
