# Calculate difference of each
# track number with the head position
def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)

# Find unaccessed track which is
# at minimum distance from head
def findMin(diff):

    index = -1
    minimum = 999999999

    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index


def SSTF(request, head):
    if (len(request) == 0):
        return

    l = len(request)
    diff = [0] * l

    # Initialize array
    for i in range(l):
        diff[i] = [0, 0]

    # Count total number of seek operation
    seek_count = 0

    # Stores sequence in which disk
    # access is done
    seek_sequence = [0] * (l + 1)

    for i in range(l):
        seek_sequence[i] = head
        calculateDifference(request, head, diff)
        index = findMin(diff)

        diff[index][1] = True

        # Increase the total count
        seek_count += diff[index][0]

        # Accessed track is now new head
        head = request[index]

    # For last accessed track
    seek_sequence[len(seek_sequence) - 1] = head

    print("Total number of seek operations =", seek_count)

    print("Seek Sequence: ")

    # Print the sequence
    for i in range(l + 1):
        print(seek_sequence[i])


# Driver code
if __name__ == "__main__":

    # Request array
    proc = [176, 79, 34, 60,
            92, 11, 41, 114]
    SSTF(proc, 50)
