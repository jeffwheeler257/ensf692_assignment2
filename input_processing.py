# input_processing.py
# YOUR NAME, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # Replace these comments with your function commenting
    def update_status(): # You may decide how to implement the arguments for this function
        pass




# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(Sensor):
    if Sensor.light == "red" or Sensor.pedestrian == "yes" or Sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif Sensor.light == "green":
        print("\nProceed\n")
    elif Sensor.light == "yellow":
        print("\nCaution\n")
    print("Light = " + Sensor.light + " , Pedestrian = " + Sensor.pedestrian + " , Vehicle = " + Sensor.vehicle + " .\n")



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    sensor = Sensor()
    while 1 == 1:
        print("Are changes detected in the vision input?")
        n = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end program: ") 
        if n == '1':
            x = input("What change has been identified?: ")
            if x == "red" or x == "green" or x == "yellow":
                sensor.light = x
                print_message(sensor)
            else: 
                print("Invalid vision change.\n")
                print_message(sensor)
        elif n == '2':
            y = input("What change has been identified?: ")
            if y == "yes" or y == "no":
                sensor.pedestrian = y
                print_message(sensor)
            else:
                print("Invalid vision change.\n")
                print_message(sensor)            
        elif n == '3':
            z = input("What change has been identified?: ")
            if z == "yes" or z == "no":
                sensor.vehicle = z
                print_message(sensor)
            else:
                print("Invalid vision change")
                print_message(sensor)
        elif n == '0':
            print("Program Ended\n")
            break
        else:
            print("You must select either 1, 2, 3 or 0.\n")  
    
    
    
            




# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

