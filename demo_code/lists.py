demo_list = [10, 16, 24, 77, 2, 14, 9]

print(demo_list)

demo_list.append(5)
print(demo_list)

number_of_items = len(demo_list)

print(f"Number of items: {number_of_items}")

print("\n")
print(demo_list[0])

print(demo_list[3])

print("\n")
for item in demo_list:
    print(item)

print("\n")
for index in range(number_of_items):
    print(demo_list[index])