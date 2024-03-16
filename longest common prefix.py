def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Sort the list of strings to easily find the common prefix
    strs.sort()
    
    # Compare the first and last string in the sorted list
    # The common prefix can only be as long as the shortest string
    prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break
    return prefix

# Test the function
strs = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(strs))
