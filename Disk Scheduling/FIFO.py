size = 8


def FIFO(arr, head):

    seek_count = 0
    distance, cur_track = 0, 0

    for i in range(size):
        cur_track = arr[i]

        # Calculate absolute distance
        distance = abs(cur_track - head)

        # Increase the total count
        seek_count += distance

        # Accessed track is now new head
        head = cur_track

    print("Total number of seek operations = ", seek_count)

    # Seek sequence would be the same
    # as request array sequence
    print("Seek Sequence: ")

    for i in range(size):
        print(arr[i])


# Driver code
if __name__ == '__main__':

    # Request array
    arr = [176, 79, 34, 60,
           92, 11, 41, 114]
    head = 50

    FIFO(arr, head)
