def main():
    menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50,  "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}
    total_cost = 0
    while True:
        choice = input("Item: ")
        if choice.lower() == "end":
            break
        try:
            total_cost += menu[choice]
            print(f"Total: ${total_cost:.2f}")
        except KeyError:
            continue
main()