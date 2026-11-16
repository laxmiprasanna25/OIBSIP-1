"""
BMI Calculator - Oasis Infobyte Python Programming Task 2 (Beginner)

Calculates Body Mass Index (BMI) from weight in kilograms and height in metres.
This is an educational calculator, not a medical diagnostic tool.
"""


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI rounded to two decimal places."""
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")

    return round(weight_kg / (height_m ** 2), 2)


def get_bmi_category(bmi: float) -> str:
    """Classify BMI using the ranges specified in the internship task."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def get_positive_number(prompt: str) -> float:
    """Read a positive number from the user, repeating after invalid input."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if value <= 0:
            print("Please enter a value greater than zero.")
            continue

        return value


def main() -> None:
    print("=" * 42)
    print("             BMI CALCULATOR")
    print("=" * 42)
    print("Enter your details below.\n")

    weight = get_positive_number("Enter your weight in kilograms (kg): ")
    height = get_positive_number("Enter your height in metres (m): ")

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("\n" + "-" * 42)
    print(f"Your BMI       : {bmi:.2f}")
    print(f"BMI Category   : {category}")
    print("-" * 42)
    print("Note: BMI is a general screening measure, not a diagnosis.")
    print("For personal health advice, consult a qualified healthcare professional.")


if __name__ == "__main__":
    main()
