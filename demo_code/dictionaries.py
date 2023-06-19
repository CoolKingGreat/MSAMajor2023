student_scores = {"Alice": 87, "Bob": 79, "Jerry": 94, "Sara": 90}


print(student_scores["Bob"])

car = {"make": "Mercury", "model": "Sable", "year": 1988, "value": 10000}

for student in student_scores:
    print(f"{student}: {student_scores[student]}")

#Get all the keys and values from the cars dictionary
print("\n")
for key, value, in car.items():
    print(f"{key}: {value}")
