<img alt="A red cube pushes a grey cube off screen" width="100%" height="100%" src="https://github.com/krissendev/upbge-player/blob/master/ImagesForHelp/Img0_header.jpg">

<h1 align="center">Upbge-player</h1> 
Made with Version UPBGE 0.36.1<br>
https://upbge.org/#/

<br>

## About
<p>This project demo is meant as a simple reference file for setting up a UPBGE project.<br>
It's for artists wanting to move their character model around in som 3D environment in blender or for anyone wanting a ready made setup for the blender driven game-engine UPBGE. <br>
This basic 3rd person player setup enables for example imported geometry from blender to become walkable.<br>
The setup uses WASD for movement and Mouse position for camera rotation and spacebar for jump.</p>

<br>

## Prerequisite
<p>Know how to navigate in blender.<br>
Know how to extract a zip folder <br>
(Optional) Have used a blueprint system before.<br>
(Optional) Know abit of coding. <br></p>
<br>

## How to run
* \#0  Download this project by pressing the "code" button and your preferred method for example by pressing "Download zip" <br>
or by using git command:
  ```bash
  git clone https://github.com/krissendev/upbge-player
  ```
* \#1  Download and install [UPBGE](https://github.com/UPBGE/upbge/releases/tag/v0.36.1)
* \#2  Run the UPBGE launcher and in it open the [upbge.blend](https://github.com/krissendev/upbge-player/blob/master/upbge.blend) file from this project.
* *Info: UPBGE supports both Editor: "Logic Bricks Editor" and Editor: "Logic Node Editor"*
* *Info: UPBGE comes preloaded with "Logic Bricks Editor".*
* \#3  To load "Logic Node Editor" go to **/Edit/Preferences/Add-ons** search for "node" and enable **"Game Engine:Logic Nodes"**<br>      You might need to install something(most likely just a button in this context menu) on this step. 
* \#4  To run game in UPBGE **press "p" to play and "Esc" to quit.**

<br>

## Notes for further expansion or use
All meshes added in UPBGE have by default their /Editor: Outliner/Physics/Physics-Type: "Static",
this can be change to "No Collision" for example if needed or Rigid-Body.<br>
Player **movement speed** can be set in **/Editor:Logic-Node-Editor/Player: Speed** (node)<br>
Player **jump** can be set it **/Editor:Logic-Node-Editor/Player: Apply Force: Z** (node)<br>
Player **gravity** can be set it **/Editor:Logic-Node-Editor/Player: Set Gravity: Z** (node)<br>
Player **mass** can be set it **/Editor:Outliner/Physics/Attributs/Mass** <br>
Camera **focal lenght** or **clipping distance** can be changed in **/Editor: Outliner/Data**<br>
Imported or created models can simply be parented to "player", then deleting cube or hiding it to replace it with the desired player geometry.
<img alt="The default 3D cube has been replaced with a character model by parenting the Character Model Armature to the player" width="100%" height="100%" src="https://github.com/krissendev/upbge-player/blob/master/ImagesForHelp/Img6_import_fbx_parent_player.jpg">

 <br>
<br>

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

<br>

## Acknowledgments
This project was developed using [UPBGE](https://upbge.org/), a fork of Blender's Game Engine. 


Project made by https://github.com/krissendev
