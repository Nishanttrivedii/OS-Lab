capacity = 4
processList = [7, 0, 1, 2, 0, 3, 0,
               4, 2, 3, 0, 3, 2]

# List of current pages in Main Memory
s = []

page_faults = 0
# pageHits = 0

for i in processList:

    # If i is not present in currentPages list
    if i not in s:

        # Check if the list can hold equal pages
        if(len(s) == capacity):
            s.remove(s[0])
            s.append(i)

        else:
            s.append(i)

        # Increment Page faults
        page_faults += 1

    # If page is already there in
    # currentPages i.e in Main
    else:

        # Remove previous index of current page
        s.remove(i)

        # Now append it, at last index
        s.append(i)

print("{}".format(page_faults))
