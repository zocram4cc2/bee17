# 
## Gameplay patch for Pro Evolution Soccer 2017

 is the gameplay patch developed for the [4chan cup](https://implyingrigged.info/) for its use in PES2017. This is achieved like the previous PES2021 patch by changing the binary constants file Konami left in the game's data packs. 
**Current patch notes:**

- match/pesSmart: 
  
  - Buffed defence mark calc approach rate 10%. Should help shore up the defence.

  - Greatly diminished GK Press rates (1.7/1.5/1.3 to 1.2/1.0/0.8 Def. GK/No Playstyle/Of. GK) - should help keepers behave more aggressively toward the ball (this is a reverse value, no idea why).

  - Slightly more stamina loss (+1 to all values)

- player/gk:

  - Buffed all catch/deflect angle constants 10% and cut wait times 10% for a slight buff.

  - Buffed Base Pos Rate for both GK styles (def/no style and offensive) from 0.8/1.2 to 1.2/1.4 - should help keepers behave more aggressively toward the ball.


- team/basePosition:

  Imported some values from 17: 

  **DO NOTE: THIS WILL NOT MAKE THE GAME BEHAVE LIKE PES17. IT'S JUST A VERY SLIGHT STEP TOWARDS IT.**
  
   - spaceCoverRate and adjustSpaceCoverRate changed from 0.4 and 0.2 to 0.43 and 0.23 which will help teams cover space better.

   - dfLineWidth 3 4 and 5 were 20, 24 and 28 in 16 and were changed to their 17 values of 16, 20 and 24. This will make defenses narrower, helping avoid *some* throughballs for their respective defenses.

   - ballSideMaxRate_strategy_defensive was changed from 0.3 to 0.6. Not sure what this does exactly but the "rates" are very effective usually and this sounds like it helps the team reshape around the ball when out of possession (this is what _strategy_defensive means).

   - closeRate_DF_FW_Retreat was changed from 40 to 42. This will help the 3 to 5 defensive players close better on "Retreat" situations (presumably counterattacks). closeRate_DF_FW was also changed from 45 to 49 (not from 17).

   - lastLineCloseMaxRate was changed from 0.6 to 0.8. This is a 20% boost to the base rate defensive players close down on the ball.

   - lengthDf and lengthDf_retreat changed from 40 and 35 to 35 and 30. This will help the defence be more compact length of the pitch wise (AKA more in a horizontal line than spread out) both in normal and in retreating situations.

  Further changes to basePosition:

    - minDist_MF_DF changed from 8 to 7 and minDist_MF_DF_strategy_defensive from 4 to 3.8. This will help the midfield close down better into its own defence, granting a slight numbers advantage to the defending team.

    - minDist_MF_FW changed from 1.5 to 1.33. This will help the midfield join the attack better.

    - all slides values changed: slideDistMax 25->35; slideDistMin 8->4; slideJudgeWidthMargin 10->20; slideWidth 3->5. This will hopefully provoke funnier and deadlier slide tackles. :)

    - wideRate 0.3 -> 0.33 for a slight help to wide buildup.

- team/defenceMark:
   
  - **all** of this file received an around 10% buff, this means +1 on all INT values, +10% on all angles and zones, and -10% on wait times. This should help defences keep their marks without being slurpy.

- team/lineBreak:

  - checkAreaScore, checkAreaScore_line_Breaker, checkInterceptScore and checkInterceptScore_line_Breaker all nerfed 5. This will either make the AI make slightly lower quality chances or lower the quality of those chances. I'm not exactly sure, AFAIR it's the first. Will remember in testing.

- team/pairAnime:

  - Stamina min/med/max effect bumped 10%.

- team/spaceRun:

  - checkScore, checkScore_good, checkScore_flow all lowered by 10. This will make the strikers slightly less precise.

  - checkInterceptScore and checkInterceptScore_good set to 80 and 70 (from 0 and 10). This will make first timers and headers better.



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