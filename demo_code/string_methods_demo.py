#capitalize a string
my_name = "aryan"
print(my_name.capitalize())

#uppercase
print(my_name.upper())

sentence = "I have a dog. My dog is cute. Do you want a dog."

#loop through a string
for letter in my_name:
    print(letter)

print("\n")
length_of_string = len(my_name)

for index in range(length_of_string):
    print(my_name[index])



dog_count = 0
#loop
more_dogs = True
start_index = 0
while more_dogs:
    #find the first instance of dog
    found_index = sentence.find("dog", start_index)
    if found_index != -1:
        #increment dog_count by 1
        dog_count += 1
        #update the index to the character after dog
        start_index = found_index + 1
    else:
        more_dogs = False


print(f"Number of Dogs: {dog_count}")