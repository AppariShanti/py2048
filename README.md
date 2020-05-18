# 2048 GAME in Python
## Introduction
This game is based on the famous 2048 game. It is the terminal version of the same.The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048.

(THIS PROGRAM RUNS ON WINDOWS.)        
## Rules to Play
1. The game asks whether the player wants to play a **default** game. If yes it sets the game size as 5 and the winning number as 2048. 

2. If the player chooses not to play default the following details are asked:
   
   (i) Enter the size of game you want to play.                             

   (ii) Enter the End number.(This means the 2048 Game can be modified. It can be set for any number which is a power of 2)                            

3. **Both ARROW KEYS and WASD KEYS can be used for sliding the gameboard**:                                 
     
     (i)  W,w, UP KEY    : "**Up**"                  
    (ii)  A,a, LEFT KEY  : "**LEFT**"                      
    (iii) S,s, DOWN KEY  : "**DOWN**"                           
    (iv)  D,d, RIGHT KEY : "**RIGHT**"                                
    (iv)  Q,q, Esc KEY   : "**QUIT GAME**"
  
4. The terminal window is cleared 2 seconds after every input direction is given.The player need not wait for screen to get cleared.Just input the direction it will show result after 2 seconds 

5. If the game gets over then a play again option is prompted.

## Dependencies
1. The game runs on Windows.

2. It uses **numpy , random , colorama , getch , time and os packages**.

## Game Logic Used
Merging the 2 tiles with same numbers when a particular direction is specified:                        
1. **LEFT SHIFT** : It can be visualiseD as first compressing the board (In case there are blank spaces in between) then merging it (to combine same numbers) , example when two adjacent blocks are 4 they merge to form 8, after that again compress to remove addional spaces so formed.After all this process a random 2 is added on the board.

2. **RIGHT SHIFT** : It can be treated same as Left Shift. Only thing is to REVERSE the board such that left shift occurs and again REVERSE to get the required output.

3. **UP SHIFT** : Surprisingly this can also be treated as left shift. Just TRANSPOSE the game board do the left shift and again TRANSPOSE. This gives the desired output.

4. **DOWN SHIFT** : It can be also treated same as left Shift. We need to first TRANSPOSE the board and then REVERSE it and Voila!!! it is the same as Left Shift. To get the output just REVERSE the board again and Transpose it.

Thus all the directional shifts can be executed by using few MATRIX TRANSFORMATIONS. For the implementation of above process compress , merge , transpose and reverse functions are written.

**Any INVALID MOVE doesn't add a random 2... It asks for another direction to move.**
