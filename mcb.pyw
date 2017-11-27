#! python3

# mcb.pyw - save multiple passwords for various websites using keywords and voice recognition

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyboard.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import speech_recognition as sr, shelve, pyperclip, re

mcbShelf = shelve.open('mcb')

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say something!')
    audio = r.listen(source)

audioString = r.recognize_google(audio).lower()

openRegex = re.compile(r'(get|save|list)(\s+)(.*)')

mo = openRegex.search(audioString)

command = mo.group(1)
keyword = mo.group(3)

if command == 'save':
    mcbShelf[keyword] = pyperclip.paste()
    print('%s succesfully saved!' % keyword)
elif command == 'get':
    pyperclip.copy(mcbShelf[keyword])
    print('%s password retrieved!' % keyword)
elif command == 'list' and keyword == 'all':
    pyperclip.copy(str(list(mcbShelf.keys())))
else:
    print('im sorry i dont understand that command')
mcbShelf.close()

