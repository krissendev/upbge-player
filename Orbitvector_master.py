import bge

# The 'move' function calculates the movement vector for a player based on input and camera orientation.
# It makes the direction of forward and sideways take the camera rotation or rather the orbit which camera 
# is parented to, into account when moving the player.

def move(orbit_rotation, wasd_vector):

    # Extract the right vector/ x-axis of orbit_rotation camera rotation to adjust right-left movement
    right_vector = orbit_rotation.col[0].copy()

    # Extract the forward vector/ y2-axis of orbit_rotation camera rotation to adjust forward-backward movement
    forward_vector = orbit_rotation.col[1].copy()

    # Calculate the movement vector: scale right_vector by x-input/ "A", "D"  and forward_vector by y-input/ "W", "S" 
    # then add them in a vector. This aligns movement direction with the camera's orientation 
    movement_vector = (right_vector * wasd_vector.x) + (forward_vector * wasd_vector.y)

    # Set the z component of movement_vector to 0 to prevent upward/downward movement
    # This is important as the camera's rotation includes a z-component, which we don't want for 2D movement
    movement_vector.z = 0
    
    return movement_vector



# Indepth math explanation:
# This is a vector scaling done by multiplying `2D`vector "wasd_vector" (x,y,-) by the rotational axis `inside` 
# the 3x3 matrix of "orbit_rotation".
# The rotational vector axis component inside orbit_rotation is used to scale and direct the movement of wasd_vector.
# For example: orbit_rotation.col[0] is the x-axis in orbit-camera.


# The following is a reiteration of what happens in the code above:

# Imaginary variable indexes like "x4" are used for math-illustration purposes.
# The function move has parameters: 
    # orbit_rotation - which is the rotation component of object "orbit" 
    # wasd_vector - which is a vector put together of the WASD key input values

# orbit_rotation :(x0,y0,z0) (x1,y1,z1) (x2,y2,z2)
# For example: orbit_rotation.col[0] is (x0,y0,z0)
# 	All matrix entries ranging between -1 and 1
# wasd_vector: (x4,y4,z4)
# 	x4 and y4 ranging between -1 and 1 while z4 is always 0. This is because "A","D" is x4 and "W","S" is y4 and z4 is unused.



# [code] movement_vector = (right_vector * wasd_vector.x) + (forward_vector * wasd_vector.y)
# Which translates to:
#((x0,y0,z0) * x4 ) + (x1,y1,z1) * y4) => ((x0x4,y0x4,z0x4) + (x1y4,y1y4,z1y4))

# [code] movement_vector.z = 0
# Which translates to:
#((x0x4,y0x4,0) + (x1y4,y1y4,0))