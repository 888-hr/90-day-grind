def main():
    print("-------------------------\n- Welcome to your expense tracker! Add items and costs here throughout the day to track your spending.\n- Do 'list' for a list of purchases so far as well as a current total, and when you're done simply do 'end' to return the days total.\n-------------------------\nHappy spending!\n-------------------------")
    expenses()

def expenses():
    expenses = {
    }

    total = 0

    while True:
        try:
            purchase = input("Purchase: ").replace('$', '')
        except EOFError:
            print()
            break
        if purchase == "end":
            print(f"You have spent ${total:.2f} Today.")
            break
        elif purchase == "list":
            print("\n-")
            for item in expenses:
                print(f"{item.title()}: {expenses[item]}$\n", end="")
            print("-\n")
            print(f"Your total so far is: ${total:.2f}")
            continue
        try:
            item, cost = purchase.split(' ')
            if item.isalpha():
                cost = float(cost)
                expenses[item] = cost
                total += cost
            else:
                print("Item cannot be numeric.")
                continue
        except ValueError:
            print("Format needs to be: (Item) ($cost)")
            continue

main()