"""
A Simple Prototype of a typing system for Candian
Aboriginal (Cree) Syllabics.

David Baker, dab498
5/18/2022

Notes:
Some fonts do not recognize Syllabic Characters. You may have to
save the file using option (c) then view the text file in another
font if you can't see them in the app.
"""

#Sets up menu for user
def menu():
    end=False
    while(end==False):
        print('Welcome, please select a letter:')
        print('a) new string')
        print('b) view strings')
        print('c) save strings')
        print('d) exit')

        selection=input('enter letter:')
        if selection=='a':
            roman=stringbuilder()
            crscript=cree(roman)
            page.append(crscript)
        elif selection=='b':
            stringviewer()
        elif selection=='c':
            stringsaver()
        elif selection=='d':
            print('Have a nice day :)')
            end=True
        else:
            print('sorry, that is not a valid input')
    

#Takes input from user in typing system,
#Transcribes it in Latin alphabet transcription of Cree.
def stringbuilder():
    st=input('please type your string:')
    syl=''
    for i in range(len(st)):
        try:
            syl=syl+maps[st[i]]
        except(KeyError):
            print('A character was not recognized. Try again')
            stringbuilder()
    return syl


def stringviewer():
    for i in range(len(page)):
        print(page[i])
    return

#Saves to a .txt file in the document in the current directory.
def stringsaver():
    name=input('File name?')
    f=open(name+'.txt','w',encoding='UTF-8')
    for i in range(len(page)):
        f.write(page[i]+'\n')
    return


#Takes a Latin Alphabet Transcription and turns it into
#Syllabics Characters.
def cree(roman):
    crscript=''
    slice=0
    try:
        while(slice<len(roman)):
            if roman[slice:slice+2] in syllables:
                crscript+=syllables[roman[slice:slice+2]]
                slice+=2
            else:
                crscript+=plains[roman[slice:slice+1]]
                slice+=1

        print(crscript)
        return crscript
    except:
        print('Sorry, there was an unexpected error')
        return ''


page=[] #list of every string created for viewing

#map input to proper latin characters for easy transfer to syllabics
maps={'a':'p',"s":'t',"d":'c',"f":'k',
'r':'m','w':'l','v':'r','c':'s','x':'w','z':'y',
'q':'h','e':'n',

'k':'e','i':'i','l':'o','j':'a',
' ':' ','.':'.'}

#solo vowels + syllable final consonants
plains={'e':'ᐁ',
'i':'ᐃ',
'o':'ᐅ',
'a':'ᐊ',
'p':'ᑊ',
't':'ᐟ','c':'ᐨ','k':'ᐠ',
'm':'ᒼ','n':'ᐣ','l':'ᐪ',
'r':'ᕑ','s':'ᐢ','w':'ᐤ','y':'ᐧ','h':'ᐦ',

' ':' ','.':'.'}

#Cons+vowel compounds
syllables={
'pe':'ᐯ','pi':'ᐱ','po':'ᐳ','pa':'ᐸ',
'te':'ᑌ','ti':'ᑎ','to':'ᑐ','ta':'ᑕ',
'ce':'ᒉ ','ci':'ᒋ','co':'ᒍ','ca':'ᒐ',
'ke':'ᑫ','ki':'ᑭ','ko':'ᑯ','ka':'ᑲ',
'me':'ᒣ','mi':'ᒥ','mo':'ᒧ','ma':'ᒪ',
'ne':'ᓀ','ni':'ᓂ','no':'ᓄ','na':'ᓇ',
'le':'ᓓ ','li':'ᓕ','lo':'ᓗ','la':'ᓚ',
're':'ᕃ','ri':'ᕆ','ro':'ᕈ','ra':'ᕋ',
'se':'ᓭ','si':'ᓯ','so':'ᓱ','sa':'ᓴ',
'we':'ᐍ','wi':'ᐏ','wo':'ᐓ','wa':'ᐗ',
'ye':'ᔦ','yi':'ᔨ','yo':'ᔪ','ya':'ᔭ'}


menu()