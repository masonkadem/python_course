# inches2centimeters.py

def inches_to_centimeters(inches):
    # Conversion factor: 1 inch = 2.54 centimeters
    centimeters = inches * 2.54
    return centimeters

if __name__ == "__main__":
    # Get input from the user
    inches = float(input("Enter a distance in inches: "))
    
    # Call the function to perform the conversion
    centimeters = inches_to_centimeters(inches)
    
    # Display the result
    print(f"{inches} inches is equal to {centimeters} centimeters.")
