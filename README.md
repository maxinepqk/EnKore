EnKore
======

EnKore is a multilingual keyboard, supporting automatic keboard management when typing in English and Korean.

<img src='https://i.imgur.com/8aYKkcW.gif' width=''/>

GIF created with [LiceCap](http://www.cockos.com/licecap/).

Suppose you are talking to your Korean friend and you wanted to type "I'm now in Pittsburgh" in Korean. 
It is natural that you keep "Pittsburgh" as it is in English and everything else in Korean. Like "핏츠버그"
To do this, you need to type "나는 지금" (tr: "I'm now") in Korean keyboard, switch to English keyboard, type "Pittsburgh", switch back to Korean keyboard and finally, type "에 있어" (tr: "in") in English keyboard.
Anyone who has experienced the situation of typing in the wrong keyboard and ending up deleting and typing it again would understand such frustration.

Our project provides a solution by supporting a keyboard that automatically types the words in your intended language.
When you type a string in English keyboard and the string can be recognized as a valid Korean word, it converts to Korean word right away.

Instruction
-----------

**Everything is in PYTHON3! HEHE**
* Before running, in the console:
```
$ export PYTHONIOENCODING=utf8 
```

Credit
------
* Controlling Keyboards:
 http://pynput.readthedocs.io/en/latest/keyboard.html#controlling-the-keyboard
* Converting Korean <-> English
 http://www.theyt.net/wiki/한영타변환기
* Dictionary
 https://glosbe.com/

Project
------
Tartanhacks 2018
