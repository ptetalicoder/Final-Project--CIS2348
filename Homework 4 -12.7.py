#Pranav Tetali
#ID 1541822
#Homework 4 12.7


def get_age(): #reads age
    age = int(input())
    if(age>=18 and age<=75): #checks if age is valid
        return age
    else:
        raise ValueError("Invalid age.") #if age is not valid, says invalid age

def fat_burning_heart_rate(age): #equation for heart rate
    return ((70 / 100) * (220 - age))

if __name__ == '__main__':
    try:
        age = get_age()
        print("Fat burning heart rate for a",age,"year-old:",fat_burning_heart_rate(age),"bpm") #output is age is in range
    except ValueError as ve:
        print(ve.args[0])
        print("Could not calculate heart rate info.""\n") #prints result if age is too young