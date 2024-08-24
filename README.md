# 
## Gameplay patch for Pro Evolution Soccer 2017

 is the gameplay patch developed for the [4chan cup](https://implyingrigged.info/) for its use in PES2017. This is achieved like the previous PES2021 patch by changing the binary constants file Konami left in the game's data packs. 
**Current patch notes:**

TODO


### How do I read this shit again?
The text files follow this format:
```bash
PATCHED VALUE //variable description
```
To read the stock 16 values, you'll have to compare to a specific commit.


## Automate documentation

This repo includes a modified version of Tomato's tools from the 17 AI Pack that will help you go from the extracted binaries to documented text files. This is kind of still janky (some of the values actually don't line up properly yet!) but it will save you tons of time doing it by hand.

Basically just use bin.py to extract the contents of the files you previously dropped in the bin folders to newline-separated text files and join.py to join them with the variable names tomato extracted a long time ago.

The python tools have been modified so that you can clone this repo, execute them from the tools/ subfolder and they will automatically take the files in bins/common... as input. **Do NOT move any files' folders**. They **need to be unzlibbed**.


For 16:
```
constant_match: HEADER 284 INDEX 356 FILE N.0 (after modification INDEX is +6 - wtf?)
constant_player: HEADER 416 INDEX 432 FILE N.1 (after modification INDEX is 438 - wtf?)
constant_match: HEADER 200 INDEX 216 FILE N.2
```
Not sure why indexes gain bytes... GPE is really janky!

### Old instructions

You need the extracted variable names from his pack (included here) placed under a "reconst/" subfolder.

Put bin.py, join.py and the binary (match/player/team) in the same folder, execute bin.py (configured like below) and it will extract the binaries into values separated by new lines.

Then join.py will automatically join the files outputted by bin.py (from a raw/ subfolder) with the ones extracted by Tomato and put it in an output/ folder.
