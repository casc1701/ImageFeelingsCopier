# ImageFeelingsCopier
Copies the PNG tEXt chunk data and renames files for SillyTavern

SillyTavern uses something called Expressions, those are PNG files named as admiration,amusement,anger,annoyance,approval,caring,confusion,curiosity,desire,disappointment,disapproval,disgust,embarrassment,excitement,fear,gratitude,grief,joy,love,nervousness,neutral,optimism,pride,realization,relief,remorse,sadness & surprise, all with a PNG extension.

It's easy to create those files using Stable Diffusion, but to manually rename them is sometimes messy.

This script reads the original prompt, stored in the PNG and tries to find the original expression. If it succeeds, it renames a copy of the file as the expression.

USAGE: put the script in a folder, create two subfolders, INPUT and OUTPUT. Put the files you want to rename in the INPUT, run python ImageFeelingsCopier.py and watch the magic happens. 
