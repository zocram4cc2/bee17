# 16sense
## Gameplay patch for Pro Evolution Soccer 2016

16sense is the gameplay patch developed for the [4chan cup](https://implyingrigged.info/) for its use in PES2016. This is achieved like the previous PES2021 patch by changing the binary constants file Konami left in the game's data packs. Its name is loosely inspired by pfSense, a product so named because "it makes sense of pf". This patch aims to "make sense" of PES 2016.

**Current patch notes:**
N/A

### How do I read this shit again?
The text files follow this format:
```bash
PATCHED VALUE //variable description
```
To read the stock 16 values, you'll have to compare to a specific commit.


## Automate documentation

This repo includes a modified version of Tomato's tools from the 17 AI Pack that will help you go from the extracted binaries to documented text files. This is kind of still janky but it will save you tons of time doing it by hand.

You need the extracted variable names from his pack (included here) placed under a "reconst/" subfolder.

Put bin.py, join.py and the binary (match/player/team) in the same folder, execute bin.py (configured like below) and it will extract the binaries into values separated by new lines.

Then join.py will automatically join the files outputted by bin.py (from a raw/ subfolder) with the ones extracted by Tomato and put it in an output/ folder.

For 16:
```
constant_match: HEADER 272 INDEX 330 FILE N.0
constant_player: HEADER 416 INDEX 426 FILE N.1
constant_match: HEADER 200 INDEX 212 FILE N.2
```

Run bin.py in the same folder as the interested bin file and it will map the index to the file contents. After that you can automate documentation by running fill.py with a reconst/ folder.