EnKore
======

EnKore is a multilingual keyboard, supporting automatic keboard management when typing in English and Korean.

Suppose you are talking to your Korean friend and you wanted to type "I'm in Pittsburgh" in Korean. 
It is natural that you keep "Pittsburgh" as it is in English and everything else in Korean. Like ""
To do this, you need to type "" Korean keyboard, switch to English keyboard, type "Pittsburgh", switch back to Korean keyboard and finally, type "" in English keyboard.
Anyone who has been experiencing (constantly) the situation or typing in the wrong keyboard and ending up deleting and typing it again,would understand such fructration.

Our project provides a solution by supporting a keyboard that automaticly types the words in your intended language.
When you type a string in English keyboard and the string can be recognized as a valid Korean typing, it converts to Korean word right away.

Instruction
-----------

**Everything in PYTHON3! HEHE**
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

