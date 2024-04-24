def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    
    BMI Formula: weight (kg) / height^2 (m^2)
    
    Args:
    weight (float): Weight of the person in kilograms.
    height (float): Height of the person in meters.
    
    Returns:
    float: Calculated BMI value.
    """
    bmi = weight / (height ** 2)
    return bmi


def main():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    
    # Interpret BMI value
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You are normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")


if __name__ == "__main__":
    main()
