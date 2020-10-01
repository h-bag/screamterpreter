# Screamterpreter
 Simple interpreter for my esolang, [SCREAMCODE](https://esolangs.org/wiki/SCREAMCODE).
## Requirements
- Python 3.8

To use, just run `python screamterpreter.py` in the project directory.
Pre-written files must be stored in a folder named 'screams', in the same directory as the main .py file. File names are case-sensitive. I've included a 'Hello World' program to help you get a feel for how programs are written.

## Instruction Set
Instructions are seperated by a space.
 Command | Description                                                          
---------|----------------------------------------------------------------------
 AAAH    | Move the pointer to the right                                        
 AAAAGH  | Move the pointer to the left                                         
 FUCK    | Increment the memory cell at the pointer                             
 SHIT    | Decrement the memory cell at the pointer                             
 !!!!!!  | Output the character signified by the cell at the pointer            
 WHAT?!  | Input a character and store it in the cell at the pointer            
 OW      | Jump past the matching `OWIE` if the cell at the pointer is 0        
 OWIE    | Jump back to the matching `OW` if the cell at the pointer is nonzero 

## Planned Features
- Unix compatability

## Contribution
Feel free to contribute, as long as you follow [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) conventions.
