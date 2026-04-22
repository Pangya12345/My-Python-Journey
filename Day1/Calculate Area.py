real_width = int(input("Width: "))
real_length = int(input("Length: "))

def calculate_area(width, length):
    area = width * length
    return area
area = calculate_area(real_width, real_length)
print(f"The area of Rectangle is {area}")
