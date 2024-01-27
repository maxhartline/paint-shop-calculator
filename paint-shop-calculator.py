def main():

    import math

    #Display welcome message
    print("Welcome to the Paint Shop!\nThis program will help calculate how much paint to buy, based on the room dimensions.")

    #User input
    length = float(input("Enter the length of the room, in feet: "))
    width = float(input("Enter the width of the room, in feet: "))
    height = float(input("Enter the height of the room, in feet: "))

    #Calculate total surface area
    surface_area = 2 * (length * height + width * height)

    #Calculate gallons needed 
    #1 gallon covers 150 square feet 
    gallons_needed = surface_area / 150 

    #Round up to number of cans needed
    #Paint can only be purcashed in 1 gallon cans
    rounded_up = math.ceil(gallons_needed)

    #Output
    print(f"The total surface area of your room is {surface_area:.2f} square feet")
    print(f"The total amount of paint needed is {gallons_needed:.2f} gallons")
    print(f"The total number of cans of paint needed is {rounded_up}")

    #Display goodbye message
    print("Happy painting!")

if __name__ == "__main__":
    main()