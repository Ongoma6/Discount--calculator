def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return the original price if the discount is less than 20%

def get_positive_float(prompt):
    """Prompt user for a positive float input and return it."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("The value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def main():
    """Main function to execute the discount calculator."""
    print("Welcome to the Discount Calculator!")
    
    # Get the original price and discount percentage from the user
    original_price = get_positive_float("Enter the original price of the item: ")
    discount_percentage = get_positive_float("Enter the discount percentage: ")
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result with formatting
    if final_price != original_price:
        print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount was applied. The original price remains: ${original_price:.2f}")

# Run the program
if __name__ == "__main__":
    main()
