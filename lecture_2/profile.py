user_name = input("Greetings! Please enter your full name: ")
print (f"Nice to meet you {user_name}!")
while True:
    birth_year_str = input("Please enter your birth year: ")
    birth_year = int(birth_year_str)
    if 1910 <= birth_year <= 2025:
        break
    else:
         print("Please enter a valid year between 1910 and 2025.")
current_age = 2025 - birth_year
def  generate_profile(current_age):
    if current_age <= 12:
        return ("child")
    elif current_age <= 18:
        return ("teenager")
    else:
        return ("adult")
life_stage = generate_profile(current_age)
hobbies = []
while True:
    hobby = input(f"{user_name}, enter a favourite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)
user_profile = {"name": user_name, "age": current_age, "life_stage": life_stage, "hobbies": hobbies}
print ("Profile summary:")
print (f"Name: {user_profile["name"]}")
print (f"Age: {user_profile["age"]}")
print (f"Life stage: {user_profile["life_stage"]}")
if not hobbies:
    print("You didn't mention any hobbies")
else:
    print (f"Favourite hobbies ({len(hobbies)}):")
    for i in user_profile["hobbies"]:
        print (f"-  {i}")