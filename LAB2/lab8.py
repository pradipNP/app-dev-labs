print("Choose a color:")
print("R - Red")
print("G - Green")
print("B - Blue")

choice = input("Enter your choice: ").upper()

if choice == 'R':
    print("Red")
elif choice == 'G':
    print("Green")
elif choice == 'B':
    print("Blue")
else:
    print("Invalid choice")
