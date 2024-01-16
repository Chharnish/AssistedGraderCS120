#Initial code produced by Jeremy Escobar
#This is not the final version of this code as it will be improving throughout the semester.
#BSU CS120 Assisted Grader V0.1

import datetime
import os

def clear():
    #clear screen function to clear the screen.
    os.system("cls")
    
def alg():
    #algorithm
    clear()
    #initial grade amount. adds on based on what the answer for each question is.
    grade = 0
    print("Algorithm and pseudocode (MAX 50 POINTS)\n")
    q1 = int(input("On a scale of 0-5 how do you feel the problem has been solved? \n"))
    grade += q1 * 5
    q2 = input("Is the solution broken down step by step in a separate file? (Y/N)\n")
    q2 = q2.upper()
    if "Y" in q2:
        grade += 10
    q3 = input("Do functions and classes have their own algoritm? (Y/N)\n")
    q3 = q3.upper()
    if "Y" in q3:
        grade += 15
    return grade

def guide():
    #guidelines
    clear()
    print("Follows the guidelines (MAX 20 POINTS)\n")
    try:
        grade = int(input("Please enter the amount of points based on the criteria met on Canvas. (MAX 20 POINTS)\n"))
    except:
        grade = 0
    return grade

def expected():
    #Expected results
    grade = 0
    clear()
    print("Code runs as expected (MAX 20 POINTS)\n")
    q1 = input("Are there no syntax or logic errors? (Y/N)\n")
    q1 = q1.upper()
    if "Y" in q1:
        grade += 5
    q2 = input("Are all file names thoughtfully named? (Y/N)\n")
    q2 = q2.upper()
    if "Y" in q2:
        grade += 5
    q3 = input("Are all required dependencies present? (Y/N)\n")
    q3 = q3.upper()
    if "Y" in q3:
        grade += 10
    return grade

def Personal():
    #Personal style
    clear()
    print("Personal Style (MAX 5 POINTS)\n")
    
    try:
        grade = int(input("From 0-5, how personalized do you think the assignment was? (MAX 5 POINTS)\n"))
    except:
        grade = 0
    return grade

def Beyond():
    #pushing beyond
    clear()
    print("Pushing the envelope (MAX 5 POINTS)\n")
    try:
        grade = int(input("From 0-5, how much do you feel was pushed beyond what was covered this week? (MAX 5 POINTS)\n"))
    except:
        grade = 0
    return grade

def writeData(grader, name, date, totalPoints, rubric):
    #all data compiled to a easy to read document which will be displayed/saved on a local machine
    data = f"""
Date:           {date}
Student:        {name}

Total Grade:    {totalPoints} out of 100
                {totalPoints}/100

Rubric Criteria

Algorithm and pesudocode: 
                {rubric[0]} out of 50
                {rubric[0]}/50
     
Follows the guidelines:
                {rubric[1]} out of 20
                {rubric[1]}/20
            
Code runs as expected:
                {rubric[2]} out of 20
                {rubric[2]}/20
                
Personal Style:
                {rubric[3]} out of 5
                {rubric[3]}/5
                
Pushing the envelope
                {rubric[4]} out of 5
                {rubric[4]}/5

                
This Assignment was graded by {grader} on {date}

This is confidential property of Ball State University and for the student who this grade is intended for.

    """
    return data

def export(name, data, date):
    #exporting the data into a file.
    clear()
    dateToday = date.strftime("%x")
    dateToday = dateToday.replace("/","-")
    directory = f"{dateToday}_graded_assignments"
    #change parent_dir to the directory of where you want to save your assignments at
    #example for parent_dir :  
    #parent_dir = "C:\Users\Jeremy\Desktop\BSU\OneDrive - Ball State University\Misc\graded assignments"
    parent_dir = ">>>>>CHANGE ME !!!!!!!<<<<"
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
        outFile = open(f"{dateToday}_graded_assignments/{name}.txt", "w")
    except:
        outFile = open(f"{dateToday}_graded_assignments/{name}.txt", "w")
    outFile.write(data)
    outFile.close()
    print("Data saved successfully.")

def main():
    #initial information for the file. if you want to not have to keep inputting your name, change the grader variable to a string instead of an input
    grader = input("input your name: ")
    name = input("Input the student name: ")
    date = datetime.datetime.now()
    #adding criteria and spitting out grade :)
    algorithm = alg()
    guidelines = guide()
    errorHandling = expected()
    personal = Personal()
    beyond = Beyond()
    rubric = [algorithm, guidelines, errorHandling, personal, beyond]
    totalPoints = algorithm + guidelines + errorHandling + personal + beyond
    data = writeData(grader, name, date, totalPoints, rubric)
    export(name, data, date)
    print(data)
    input("Press enter to continue")
    

if __name__ == "__main__":
    main()
