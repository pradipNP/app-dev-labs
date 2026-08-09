def area_of_circle(radius):
    return 3.14 * radius * radius

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

print("Choose an option to calculate area:")
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter radius: "))
    print(f"Area of Circle: {area_of_circle(radius)}")
elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(f"Area of Rectangle: {area_of_rectangle(length, width)}")
elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print(f"Area of Triangle: {area_of_triangle(base, height)}")
else:
    print("Invalid choice")
