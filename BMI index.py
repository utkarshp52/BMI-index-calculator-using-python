def calculate_bmi():
    try:
        print("Welcome to the BMI Calculator")
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")

    except ValueError:
        print("Invalid input! Please enter numeric values for weight and height.")

# Run the BMI calculator
if __name__ == "__main__":
    calculate_bmi()

