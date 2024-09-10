class HealthMate:
    def __init__(self, name, weight, height, age):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.main()

    def main(self):
        print('Hello, Welcome to "HealthMate"')

        # User Details
        self.name = input("Enter Your Name:")
        self.weight = float(input("Enter Your Weight (kg):"))
        self.height = float(input("Enter Your Height (meter):"))
        self.age = float(input("Enter Your Age (years):"))
        self.gender = input("Enter Your Gender (Male/Female):").lower()

        user_input = int(input("""Type what you want to calculate:
        1. BMI (Body Mass Index)
        2. BMR (Basal Metabolic Rate)
        3. TDEE (Total Daily Energy Expenditure)
        4. IBW (Ideal Body Weight)
        5. WtHR (Waist-to-Height Ratio)
        6. LBM (Lean Body Mass)
        7. BFP (Body Fat Percentage)
        
        Enter Number Between 1 to 7:"""))

        if user_input == 1:
            self.calculate_bmi()
        elif user_input == 2:
            self.calculate_bmr()
        elif user_input == 3:
            self.calculate_tdee()
        elif user_input == 4:
            self.calculate_ibw()
        elif user_input == 5:
            self.calculate_wthr()
        elif user_input == 6:
            self.calculate_lbm()
        elif user_input == 7:
            self.calculate_bfp()
        else:
            print("Invalid option, type between 1 to 7")
            
            
            self.main()

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        print(f"BMI: {bmi:.2f}")

    def calculate_bmr(self):
        if self.gender == "male":
            bmr = 10 * self.weight + 6.25 * (self.height * 100) - 5 * self.age + 5
        elif self.gender == "female":
            bmr = 10 * self.weight + 6.25 * (self.height * 100) - 5 * self.age - 161
        else:
            print("Invalid gender")
            return
        print(f"BMR: {bmr:.2f}")

    def calculate_tdee(self):
        activity_level = float(input("Enter activity level (1.2, 1.375, 1.55, 1.725, 1.9): "))
        bmr = self.calculate_bmr()
        tdee = bmr * activity_level
        print(f"TDEE: {tdee:.2f}")

    def calculate_ibw(self):
        if self.gender == "male":
            ibw = 50 + 2.3 * ((self.height * 100) / 2.54 - 60)
        elif self.gender == "female":
            ibw = 45.5 + 2.3 * ((self.height * 100) / 2.54 - 60)
        else:
            print("Invalid gender")
            return
        print(f"IBW: {ibw:.2f}")

    def calculate_wthr(self):
        waist = float(input("Enter Waist Circumference (cm): "))
        wthr = waist / (self.height * 100)
        print(f"WtHR: {wthr:.2f}")

    def calculate_lbm(self):
        if self.gender == "male":
            lbm = 0.407 * self.weight + 0.267 * (self.height * 100) - 19.2
        elif self.gender == "female":
            lbm = 0.252 * self.weight + 0.473 * (self.height * 100) - 48.3
        else:
            print("Invalid gender")
            return
        print(f"LBM: {lbm:.2f}")

    def calculate_bfp(self):
        bmr = self.calculate_bmr()
        body_fat_percentage = (1.20 * (self.weight / (self.height ** 2))) + (0.23 * self.age) - (10.8 * (1 if self.gender == "male" else 0)) - 5.4
        print(f"BFP: {body_fat_percentage:.2f}")

user = HealthMate(None, None, None, None)
