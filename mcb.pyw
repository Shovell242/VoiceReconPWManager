#! python3

# mcb.pyw - save multiple passwords for various websites using keywords and voice recognition

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyboard.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import speech_recognition as sr, shelve, pyperclip, re, os

mcbShelf = shelve.open('mcb')

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say something!')
    audio = r.listen(source)

audioString = r.recognize_google(audio).lower()

openRegex = re.compile(r'(open|save|list)\s+?(.*)?')

mo = openRegex.search(audioString)

if len(mo.groups()) == 2 and mo.group(1) == 'save':



mcbShelf.close()
