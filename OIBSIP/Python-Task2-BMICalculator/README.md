# BMI Calculator

**Oasis Infobyte - Python Programming | Task 2 | Beginner Tier**

A beginner-friendly command-line BMI Calculator written in Python. It asks the user for weight in kilograms and height in metres, calculates Body Mass Index, and displays the corresponding category.

## Features

- Accepts weight in kilograms and height in metres.
- Calculates BMI using `BMI = weight / (height ** 2)`.
- Displays BMI rounded to two decimal places.
- Classifies the result using the task's categories:
  - Underweight: BMI below 18.5
  - Normal: BMI from 18.5 to below 25
  - Overweight: BMI from 25 to below 30
  - Obese: BMI 30 or above
- Validates input and rejects non-numeric, zero, and negative values.
- Includes automated unit tests using Python's built-in `unittest` module.

## Technology

- Python 3
- Python standard library (`unittest`)

No third-party packages are required.

## Project structure

```text
Python-Task2-BMICalculator/
├── bmi_calculator.py
├── README.md
├── requirements.txt
├── .gitignore
└── tests/
    └── test_bmi_calculator.py
```

## Requirements

- Python 3.8 or newer
- A terminal / command prompt

## Run the project

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

```bash
python bmi_calculator.py
```

On some systems, use `python3 bmi_calculator.py` instead.

### Example

```text
==========================================
             BMI CALCULATOR
==========================================
Enter your details below.

Enter your weight in kilograms (kg): 70
Enter your height in metres (m): 1.75

------------------------------------------
Your BMI       : 22.86
BMI Category   : Normal
------------------------------------------
Note: BMI is a general screening measure, not a diagnosis.
For personal health advice, consult a qualified healthcare professional.
```

## Run the tests

From the project folder, run:

```bash
python -m unittest discover -s tests -v
```

The tests check BMI calculation, invalid zero/negative measurements, and category boundaries.

## Manual testing checklist

- [ ] Enter valid values such as `70` kg and `1.75` m.
- [ ] Enter letters for weight; confirm the program asks again.
- [ ] Enter `0` or a negative height; confirm the program asks again.
- [ ] Try values that produce Underweight, Normal, Overweight, and Obese categories.
- [ ] Run the automated test command and confirm all tests pass.

## GitHub upload

The Oasis Infobyte task guide asks interns to use one public repository named **OIBSIP** and place each task in the required folder format.

If you have not created the repository yet:

1. Sign in to GitHub.
2. Create a **public** repository named `OIBSIP`.
3. Do not create a separate repository for this task.

Then, from the parent folder containing `OIBSIP`, run:

```bash
git init
git add OIBSIP/Python-Task2-BMICalculator
git commit -m "Add beginner BMI calculator - Python Task 2"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/OIBSIP.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If the repository already has a Git history, do not run `git init` again; add, commit, and push the project from your existing local repository instead.

## Learning outcomes

This project demonstrates Python input/output, numeric conversion, arithmetic, conditional statements, functions, exception handling, and basic unit testing.

## Disclaimer

BMI is a general screening measure and does not directly measure body fat or diagnose health conditions. The result should not be used as a substitute for professional medical advice.
