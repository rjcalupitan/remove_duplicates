def remove_duplicate(value):
    output = []
    seen = set()
    for value in a:
        if value not in seen:
                output.append(value)
                seen.add(value)
    return output

a = input("ENTER A LIST:")

result = remove_duplicate(a)
print (result)