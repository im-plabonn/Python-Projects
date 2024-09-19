class HealthMate:
    def __init__(self, name, weight, height, age, gender, religion):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.religion = religion
        self.greet = ""
        self.main()

    def main(self):
        self.name = input("Enter Your Name: ")
        self.weight = float(input("Enter Your Weight(kg): "))
        self.height = float(input("Enter Your Height(m): "))
        self.age = float(input("Enter Your Age(y): "))
        self.gender = input("Enter Your Gender(Male/Female): ").lower()
        self.religion = str(input("Enter Yor Religion: ")).lower()

        if self.religion == "islam":
            self.greet = "Assalamu Alaikum (السلام عليكم)"
        elif self.religion == "hinduism":
            self.greet = "Namaste (नमस्ते)"
        elif self.religion == "christianity":
            self.greet = "Peace be with you."
        elif self.religion == "buddhism":
            self.greet = "Namo Buddhaya (नमो बुद्धाय)"
        else:
            self.greet = "Hello"

        print(f'{self.greet}, Welcome to "HealthMate"')
        print()
        user_input = int(input("""Type what you want to calculate:
        1. BMI (Body Mass Index)
        2. BMR (Basal Metabolic Rate)
        Enter Number Between 1 to 2: """))

        if user_input == 1:
            self.calculate_bmi()
        elif user_input == 2:
            self.calculate_bmr()
        else:
            print("Invalid option, type between 1 to 2!")
            self.main()

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        status = ""
        if bmi < 18.5:
            status = "Underweight"
        elif (bmi >= 18.5) and (bmi <= 24.5):
            status = "Normal Weight"
        elif (bmi >= 25.0) and (bmi <= 29.9):
            status = "Overweight"
        elif (bmi >= 30.0) and (bmi <= 34.9):
            status = "Obese(Class-I)"
        elif (bmi >= 35.0) and (bmi <= 39.9):
            status = "Obese(Class-II)"
        else:
            status = "Obese(Class-III)"
        print(f"Hii, {self.name}. Your BMI is: {bmi:.2f}. Status: {status}")

    def calculate_bmr(self):
        if self.gender == "male":
            bmr = 655 + (9.6 * self.weight) + (1.8 * self.height*100) - (4.7 * self.age)
        elif self.gender == "female":
            bmr = 66 + (13.7 * self.weight) + (5 * self.height * 100) - (6.8 * self.age)
        else:
            print("Invalid Gender")
            return
        print(f"BMR: {bmr:.2f}")

user = HealthMate(None, None, None, None, None, None)
