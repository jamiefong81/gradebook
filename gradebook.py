

running = True
def main():
    response = input("Do you want to add to a student or check a student's grade? a/c\n'quit' to quit\n")
    if response == "a":
        newGrade()
    elif response == "c":
        checkStudent()
    elif response == "quit":
        quit()


def newGrade():
    with open('grades.csv', 'a') as f:
        adding = True
        name = input("Enter the student's name\n")
        while adding == True:
            grade = input("Enter grade for student. Type 'quit' to quit\n")
            if grade == "quit":
                adding = False
                break
            f.write(f"{name},{grade}\n")

def checkStudent():
    getAve = []
    searchfile = open("grades.csv", "r")
    name = input("Enter the student's name\n")
    for line in searchfile:
        if line.startswith(name):
            print(line.split(",")[-1])
            lAve = line.split(",")[-1]
            lAve = int(lAve)
            getAve.append(lAve)
            Average = sum(getAve) / len(getAve)
    print("Your final grade", Average)
    searchfile.close()


while running == True:
    main()

def quit():
    if response == "quit":
        running = False
