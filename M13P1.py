def display_names(last_name):
    print("Names in normal order:")
    for i in range(len(last_name)):
        print(last_name[i])


def display_names_reverse(last_name):
    print("Names in reverse order:")
    for i in range(len(last_name) - 1, -1, -1):
        print(last_name[i])


last_name = ["Maxwell", "Johnson", "Williams", "Jones", "Brown", "Lee", "Smith", "Davis", "Miller", "Wilson"]

display_names(last_name)
print()
display_names_reverse(last_name)