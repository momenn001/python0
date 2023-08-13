def main():
    try:
        item_price = float(input("Enter the item's price: "))
        has_voucher = input("Do you have a voucher? (yes/no): ").lower()

        if has_voucher == "yes":
            try:
                discount_amount = float(input("Enter the discount amount: "))
                if discount_amount >= 0 and discount_amount <= 100:
                    discount = (discount_amount / 100) * item_price
                    total_cost = item_price - discount
                    print(f"Total cost after applying {discount_amount}% discount: {total_cost}")
                else:
                    print("Invalid input: Discount amount should be between 0 and 100.")
            except ValueError:
                print("Invalid input: Please enter a valid number.")
        elif has_voucher == "no":
            total_cost = item_price
            print(f"Total cost: {total_cost}")
        else:
            print("Invalid input: Please answer with 'yes' or 'no'.")

    except ValueError:
        print("Invalid input: Please enter a valid number for the item's price.")

if __name__ == "__main__":
    main()
