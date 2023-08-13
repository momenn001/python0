def calculate_membership_fee(months_as_client, age):
    base_fee = 150
    discount_percentage = 30

    if months_as_client >= 24 or age < 16:
        discount_amount = base_fee * (discount_percentage / 100)
        final_fee = base_fee - discount_amount
    else:
        final_fee = base_fee

    return final_fee

def main():
    months_as_client = int(input("Enter the number of months you've been a client: "))
    age = int(input("Enter your age: "))

    fee = calculate_membership_fee(months_as_client, age)
    print(f"Your membership fee is {fee} JD.")

if __name__ == "__main__":
    main()
