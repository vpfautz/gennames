# Random name generator

This script uses pwgen and converts the output to best looking usernames. This
is done by evaluating 3grams of english nouns, with given count of these nouns
in some sample text.
So for each random string from pwgen, we use a sliding window, to get all
3grams, rate them and multiply the results. This value is compared to a current
maximum and the best words will be displayed.

## Requirements
```
pip2 install pwgen
```

## Usage
```
./gennames.py
```

## Output
```
perive 875672059651200
bather 492604881874560
cortan 175907029831680
unte55 87497119016112
l1c3s3 530283768803712
atence 688265924875776
firess 173507029522000
t1nere 214486394777312
l1tart 139879470302208
```

## Improvements

You could replace the `top1500_nouns.txt` file by another language to get nicknames, that sounds better in your language.
Syntax is:

```
word;count in some source;description
```
