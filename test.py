height = float(input("Height:"))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Should not be 3 meters. ")

bmi = weight / height ** 2