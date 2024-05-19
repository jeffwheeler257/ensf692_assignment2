# input_processing.py
# JEFF WHEELER, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# No global variables are permitted



class Sensor:

    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # This function takes a string input and tests that it is a valid input "0, 1, 2, or 3"
    # If the inital input is valid, it updates the corresponding instance variable and output the print_message function
    def update_status(self):
        n = ""
        while n != "0":
            print("Are changes detected in the vision input?")
            L = ['0', '1', '2', '3']
            n = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end program: ")
            try:
                if n not in L:
                    raise ValueError
            except ValueError:
                print("You must select either 1, 2, 3 or 0.\n")
                continue
            if n == "1":
                x = input("What change has been identified?: ")
                if x == "red" or x == "green" or x == "yellow":
                    self.light = x
                else: 
                    print("Invalid vision change.\n")
            elif n == "2":
                y = input("What change has been identified?: ")
                if y == "yes" or y == "no":
                    self.pedestrian = y
                else:
                    print("Invalid vision change.\n")          
            elif n == "3":
                z = input("What change has been identified?: ")
                if z == "yes" or z == "no":
                    self.vehicle = z
                else:
                    print("Invalid vision change")
            elif n == "0":
                print("Program Ended\n")
            if n != "0":
                print_message(self)





# This function takes a Sensor object and prints a course of action variable based on the current Sensor instance variable
def print_message(Sensor):
    if Sensor.light == "red" or Sensor.pedestrian == "yes" or Sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif Sensor.light == "green":
        print("\nProceed\n")
    elif Sensor.light == "yellow":
        print("\nCaution\n")
    print("Light = " + Sensor.light + " , Pedestrian = " + Sensor.pedestrian + " , Vehicle = " + Sensor.vehicle + " .\n")



def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    sensor = Sensor()
    
    sensor.update_status()


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

