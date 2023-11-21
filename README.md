Upbge-player
Made with Version UPBGE 0.36.1  
https://upbge.org/#/

## About
This project demo is meant as a simple reference file for setting up a UPBGE project.
This basic 3rd person player setup enables for example imported geometry from blender to become walkable and the .blend file is intended to work out of the box.
The setup uses WASD for movement and Mouse position for camera rotation and spacebar for jump.


## Prerequisite
Know how to navigate in blender.
(optional) have used a blueprint system before
(optional) know abit of coding, abit of python

## How to run
#0 Download this project by pressing the "code" button and your preferred method for example by pressing "Download zip" or using git command git clone https://github.com/krissendev/upbge-player 
#1 Download and install UPBGE from https://upbge.org/#/download
#2 Run the UPBGE launcher and in it open the upbge.blend file from this project.
#3 Info: UPBGE supports both Editor: "Logic Bricks Editor" and Editor: "Logic Node Editor"
#4 Info: UPBGE comes preloaded with "Logic Bricks Editor".
#5 Info: To load "Logic Node Editor" go to /Edit/Preferences/Add-ons search for "node" and enable "Game Engine:Logic Nodes", you might need to install something(most likely just a button in this context menu) on this step. 
#6 To run any game in UPBGE press "P" to play and "Esc" to quit.

## Notes for further expansion or use
All meshes added in UPBGE have by default their /Editor: Outliner/Physics/Physics-Type: "Static" 
this can be change to "No Collision" for example if needed or Rigid-Body
Player movement speed can be set in /Editor:Logic-Node-Editor/Player: Speed (node)
Player jump can be set it /Editor:Logic-Node-Editor/Player: Apply Force: Z (node)
Player gravity can be set it /Editor:Logic-Node-Editor/Player: Set Gravity: Z (node)
Player mass can be set it /Editor:Outliner/Physics/Attributs/Mass
Camera focal lenght or clipping distance can be changed in /Editor: Outliner/Data
Imported or created models can simply be parented to player, then deleting cube or hiding it to replace it with the desired player geometry.


## Technical detail
The project consists of :
* A plane-mesh with the Blender inbuilt checker texture material.
  /Editor: Outliner/Physics plane is set to Physics Type: Static
* Some other primitives which are physics interactable.
* A player object of Object Type: "empty". The player uses "Logic Node Editor" with the DataBlock-Logic: Tree 
  element named "Player". This can be found in the editor after enabling "Logic Node Editor" from Add-ons as mentioned above. It uses the default WASD Movement template together with a python script named "Orbitvector_master.py".
  In essence it uses the local rotation from the "orbit" object of Object Type empty which the camera is based on
  to adjust the movement vector of the player.
  In addition to movement gravity is initiated once and spacebar adds an opposite force while player is in contact with ground.
  /Editor: Outliner/Physics player is set to Physics Type:Rigid-Body, Actor with Locked Rotations
* An empty of type orbit which is parented to Cube and which Camera is parented to. Camera rotates 
  around "orbit". As oposed to "player", "orbit" uses the "Logic Bricks Editor" to drive 
  the camera rotation around it's pivot by mouse movement.
* A camera parented to "orbit".
* A cone-mesh parented to "orbit". (For directional visualization)


## Acknowledgments
This project was developed using [UPBGE](https://upbge.org/), a fork of Blender's Game Engine. 


Project made by https://github.com/krissendev
