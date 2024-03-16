def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Initialize a pointer to keep track of the current unique element position
    unique_pos = 0
    # Iterate through the list
    for i in range(1, len(nums)):
        # If the current element is different from the previous unique element, move it to the next unique position
        if nums[i] != nums[unique_pos]:
            unique_pos += 1
            nums[unique_pos] = nums[i]
    
    # Return the length of the list up to the last unique element
    return unique_pos + 1

# Test the function
nums = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
length = remove_duplicates(nums)
print("Length after removing duplicates:", length)
print("List after removing duplicates:", nums[:length])
