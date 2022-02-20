# def bubble_sort(our_list):
#     # We want to stop passing through the list
#     # as soon as we pass through without swapping any elements
#     has_swapped = True
#
#     while(has_swapped):
#         has_swapped = False
#         for i in range(len(our_list) - 1):
#             if our_list[i] > our_list[i+1]:
#                 # Swap
#                 our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
#                 has_swapped = True
#
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array :")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")