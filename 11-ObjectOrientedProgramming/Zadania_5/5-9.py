class C():
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        result = f"{self.surname}{self.name[0]}{self.seniority}"

        if self.age >= 18:
            return result.upper()
        else:
            return result.lower()
        
def main():
    e1 = C("Anna", "May", 17, 7)
    e2 = C("George", "Brown", 21, 4)

    print(e1)
    print(e2)

if __name__ == '__main__':
    main()