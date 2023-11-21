import bge

# The 'move' function calculates the movement vector for a player based on input and camera orientation.
# It's a vector scaling done by multiplying `2D`vector "wasd_vector" (x,y,-) by rotational axis inside a 3x3 matrix "orbit_rotation"
# The rotational vector axis component inside orbit_rotation is used to scale and direct the movement of wasd_vector.

# Imaginary variable indexes like "x4" are used for math-illustration purposes:
# orbit_rotation :(x0,y0,z0) (x1,y1,z1) (x2,y2,z2)
# 	All matrix entries ranging between -1 and 1
# wasd_vector: (x4,y4,z4)
# 	x4 and y4 ranging between -1 and 1 while z4 is always 0


def move(orbit_rotation, wasd_vector):

    # Extract the right vector/ x-axis of orbit_rotation camera rotation to adjust right-left movement
    right_vector = orbit_rotation.col[0].copy()

    # Extract the forward vector/ y2-axis of orbit_rotation camera rotation to adjust forward-backward movement
    forward_vector = orbit_rotation.col[1].copy()

    # Calculate the movement vector: scale right_vector by x-input/ "A", "D"  and forward_vector by y-input/ "W", "S" then add them in a vector
    # This aligns movement direction with the camera's orientation 
    #((x0,y0,z0) * x4 ) + (x1,y1,z1) * y4) = ((x0x4,y0x4,z0x4) + (x1y4,y1y4,z1y4))
    movement_vector = (right_vector * wasd_vector.x) + (forward_vector * wasd_vector.y)


    # Set the z component of movement_vector to 0 to prevent upward/downward movement
    # This is important as the camera's rotation includes a z-component, which we don't want for 2D movement
    #((x0x4,y0x4,0) + (x1y4,y1y4,0))
    movement_vector.z = 0
    
    return movement_vector
