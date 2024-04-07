def calculate_bmi(weight, height):

    """Calculating the Body Mass Index of the person (formula: kg/m2)"""

    body_mass_index = weight / height**2
    return body_mass_index


def calculate_calories_burned(duration):

    """Standart rate of calories burned per minute = 13"""

    calories_burned = duration * 13
    return calories_burned

def filter_overweight_people(people_data):

    """If a person has BMI > 25 then it's considered overweight"""

    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person["weight"],person["height"])
        if bmi > 25:
            person["bmi"] = bmi
            overweight_people.append(person)
        else:
            continue
    return overweight_people


people_data = []
print("Enter fitness data for each person (Enter a blank name to finish)")

while True:

    name = input("Enter person's name: ").strip()
    if not name:
        break

    valid_weight = False
    while not valid_weight:
        weight = input("Enter person's weight in kilograms: ")
        try:
            weight = float(weight)
            if weight > 0:
                valid_weight = True
            else:
                print("Weight must be a positive number. Please try again.")
        except ValueError:
            print("Invalid weight. Please enter a number.")

    valid_height = False
    while not valid_height:
        height = input("Enter person's height in meters: ")
        try:
            height = float(height)
            if height > 0:
                valid_height = True
            else:
                print("Height must be a positive number. Please try again.")
        except ValueError:
            print("Invalid height. Please enter a number.")

    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

print(f"\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person["weight"], person["height"])
    calories_burned = calculate_calories_burned(person["duration"])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

overweight_people = filter_overweight_people(people_data)
if overweight_people:  # Check if overweight_people is not None
    print("\nOverweight People:")
    for person in overweight_people:
        bmi = person["bmi"]
        print(f"{person['name']}: BMI = {bmi:.2f}")
else:
    print("\nNo overweight people found.")

