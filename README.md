# Filament-approximation
This formula approximates the length and mass of filament on your spool. 
The formula sums the the circumference of each layer and multplies it with the rows of each layer. All input units should be in mm and the output value is in meters, gram. 
I first uploaded this to reddit, where you can see the formula written mathematically.
https://www.reddit.com/r/3Dprinting/comments/uxtdgs/i_made_a_formula_to_approximate_the_length_of/
If you have any questions just pm me on reddit u/watching-watches
![image](https://github.com/WatchingWatches/Filament-approximation/assets/106354710/d04712ab-3946-47a2-a8fb-a1213fce0728)

## How to use Klipper Macro:
There are two methods on how to use it in Klipper:
1. Copy all of the code in "filament_approx.cfg" in your printer.cfg 
2. Save the file and insert the (relative) path to the file in your printer.cfg like this: [include custom-commands/filament_aprox.cfg] (custom-commands is a folder)
