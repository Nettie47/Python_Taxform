"""
Program:taxform.py
Nanette 2/13/2026

Compute a person's income tax, inputs will be the user's income, and number of dependents. Outputs will be the income tax owed.
"""

# Variables and Constants
TAX_RATE = 0.20
STANDARD_DEDUCTION =10000.0
DEPENDENT_DEDUCTION = 3000.0

# Input phase (nesting inside the float)
grossIncome = float(input("Please, enter the gross income: $"))
numDependents = int(input("Next, enter the number of dependents: "))

# Processing Phase
taxableIncome = grossIncome - STANDARD_DEDUCTION -DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
incomeTax = round(incomeTax, 2)

# Output Phase- could also use ...print("Your income tax amount is $", incomeTax, sep="")
print("Your income tax amount is $" + str(incomeTax))

# Final input to prevent window closure
input("Press ENTER to exit")