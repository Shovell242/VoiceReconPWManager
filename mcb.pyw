#! python3

# mcb.pyw - save multiple passwords for various websites using keywords and voice recognition

# Usage: <microphone> save <keyword> <microphone>: stores current clipboard to this voice command keyword
#        <microphone> get <keyword> <microphone>: retrieves keywords password from the database and copies it to the clipboard
#        <microphone> list all <microphone>: retrieves all keywords from the database and copies it to the clipboard

import speech_recognition as sr, shelve, pyperclip, re

mcbShelf = shelve.open('mcb')

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say something!')
    audio = r.listen(source)

audioString = r.recognize_google(audio).lower()

openRegex = re.compile(r'(get|save|list|delete)(\s+)(.*)')

mo = openRegex.search(audioString)

command = mo.group(1)
keyword = mo.group(3)

if command == 'save':
    mcbShelf[keyword] = pyperclip.paste()
    print('%s succesfully saved!' % keyword)
elif command == 'delete' and keyword in list(mcbShelf.keys()):
    del mcbShelf[keyword]
    print('%s succesfully deleted' % keyword)
elif command == 'get' and keyword in list(mcbShelf.keys()):
    pyperclip.copy(mcbShelf[keyword])
    print('%s password retrieved!' % keyword)
elif command == 'delete' and keyword == 'all':
    mcbShelf.clear()
    print('All saved passwords have been cleared')
elif command == 'list' and keyword == 'all':
    pyperclip.copy(str(list(mcbShelf.keys())))
    print('All keywords have been copied to the clipboard')
else:
    print('im sorry i dont understand that command')

mcbShelf.close()

