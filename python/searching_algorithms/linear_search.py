def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return False


states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

print(linear_search([1, 22, 3, 45, 65, 67, 23, 98, 123, 17], 98))
print(linear_search([1, 22, 3, 45, 65, 67, 23, 98, 123, 17], 100))
print(linear_search(states, "North Dakota"))
