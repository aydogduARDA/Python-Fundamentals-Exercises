# --- Project 3: Body Mass Index (BMI) Calculator ---
# AUTHOR: Arda Aydogdu
# DESCRIPTION: Calculates BMI based on user input for weight and height,
#              and provides a health category based on the result.

print("--- Welcome to the Body Mass Index (BMI) Calculator ---")

# 1. Get data from the user.
# We use float() because weight and height can be decimal numbers (e.g., 75.5 kg, 1.78 m).
weight_kg = float(input("Please enter your weight in kilograms (kg): "))
height_m = float(input("Please enter your height in meters (m) (e.g., 1.75): "))

# 2. Calculate the BMI using the standard formula.
# Formula: weight / (height * height) or weight / (height squared)
bmi_result = weight_kg / (height_m ** 2)

# --- 3. INTERPRET THE RESULT USING CONDITIONAL LOGIC (IF-ELIF-ELSE) ---
# Python checks these conditions from top to bottom and stops at the first one that is True.

if bmi_result < 18.5:
    category = "Underweight"
elif bmi_result < 25:  # If not < 18.5, but < 25...
    category = "Normal weight"
elif bmi_result < 30:  # If not < 25, but < 30...
    category = "Overweight"
else:                  # If none of the above were true...
    category = "Obese"

# 4. Display the final, formatted results to the user.
# The {bmi_result:.2f} syntax formats the number to only show two decimal places.
print("\n--- YOUR RESULTS ---")
print(f"Your Body Mass Index (BMI) is: {bmi_result:.2f}")
print(f"This puts you in the category of: {category}")
print("--------------------")
print("Thank you for using the calculator. Stay healthy!")