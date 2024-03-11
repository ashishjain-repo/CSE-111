from math import pi
from datetime import datetime
def tire_volume(width,aspect_ratio,diameter):
    volume = float((pi*(width**2)*aspect_ratio*(width*aspect_ratio+2540*diameter))/10000000000)
    return volume
"""
current_date_and_time = datetime.now()
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = tire_volume(width,aspect_ratio,diameter)
print(f"The approximate volume is {volume:.2f} liters")
with open("volumes.txt","at") as volumeData:
    print(f"{current_date_and_time:%Y-%m-%d}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume:.2f}",file=volumeData)

"""
# To make it show extra effort make the rest of the work inside the function and add some function to add name in the text document
def main():
    current_date_and_time = datetime.now()
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = tire_volume(width, aspect_ratio, diameter)
    print(f"The approximate volume is {volume:.2f} liters")
    tempResponse = input("Do you want tire with these dimensions. [Y/N]")
    with open("volumes.txt", "at") as volumeData:
        if tempResponse.lower() == 'y':
            yourName = input("Please enter your name. Ex: Jane Doe. - ")
            phoneNumber = input("Please enter your phone number. Ex: 1234567890 - ");
            print(f"{current_date_and_time:%Y-%m-%d}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume:.2f}",
              file=volumeData)
            print(f"Name: {yourName}, Contact Info: {phoneNumber}",file=volumeData)
        else:
            print(f"{current_date_and_time:%Y-%m-%d}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume:.2f}",
                  file=volumeData)

if __name__ == "__main__":
    main()