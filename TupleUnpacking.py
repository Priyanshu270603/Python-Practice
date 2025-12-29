def get_coordiantes():
        x = int(input("Enter the  x co-ordinate:  "))
        y = int(input("Enter the  y co-ordinate:  "))
        z = int(input("Enter the  z co-ordinate:  "))

        return x,y,z


x_coord, y_coord, z_coord = get_coordiantes()

print("x: ", x_coord, "degrees")
print("y: ", y_coord, "degrees")
print("z: ", z_coord, "degrees")