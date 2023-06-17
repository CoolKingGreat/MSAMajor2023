def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin_chosen = 0
        try:
            coin_chosen = int(input("Insert Coin:\n"))
            if coin_chosen not in [1, 5, 10, 25]:
                continue
            amount_due -= coin_chosen
        except ValueError:
            continue
    print(f"Change Owed: {0-amount_due}")

main()