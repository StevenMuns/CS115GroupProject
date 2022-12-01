#Steven Munson and Emma Millet
#I pledge my honor that I have abided by the Stevens Honor System



def read_preferences(filename):
    '''Returns the plain text of filename to a dictionary containing users and their aritist preferences
    Steven Munson'''
    dictionary = {}
    with open(filename, "r") as f:
        if f == '':
            return ''
        for line in f:
            [username, artists] = line.strip().split(":")
            artistList = artists.split(",")
            dictionary[username] = artistList

    global globalDict
    globalDict = dictionary
    return dictionary

def appArtists(d, u):
    '''Asks for the user to enter their artist preferences
    Steven Munson, edited by Emma Millet'''
    a = input("Enter an artist that you like (Enter to finish): ")
    if a == '':
        b = {u:[]}
        b[u] = sorted(d[u])
        return b
    y = a[0].capitalize() + a[1:]
    if y in d[u]:
        return appArtists(d, u)
    d[u].append(y)
    return appArtists(d, u)

def e():
    '''Updates the users artist preferences
    Steven Munson'''
    f.pop(name_artists)
    a = {name_artists: []}
    f.update(appArtists(a, name_artists))
    choices()

def r():
    """ prints recommended artists to the user.
        if no recommendations are found, prints "no preferences available at this time"
        Emma Millet
    """
    dictionary = globalDict
    username = globalUsername

    if len(dictionary.keys()) == 1:
        return print("No preferences available at this time.")
    prefs = dictionary.get(username)
   
    best = -1
    prefs = dictionary.get(username)

    bestUser = ""
    for user in dictionary.keys():
        if user[-1] == "$":
            continue
        else:
            score = numMatches(prefs, dictionary[user])
            if score > best and username != user:
                best = score
                bestUser = user
   
    rec = []
    for item in dictionary.get(bestUser):
        if ((item in prefs) != True):
            rec += [item]
   
    if (rec == []):
        return print("No preferences available at this time.")
    for artist in rec:
        print(artist)

def edit(list1, list2):
    """returns a new list that contains only the elements in list2 not in list1
        Emma Millet
    """
    newL = []
    for item in list2:
        if ((item in list1) != True):
            newL += [item]
    return newL

def numMatches(list1, list2):
    """ return the num of elements that match between two sorted lists
         taken from textbook ; Emma Millet
    """
    matches, i, j = 0, 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def popDictMaker():
    ''' Returns a dictionary sorted by lowest frequently occuring artists to highest frequently returning artists 
    choices()

def r():
    """ prints recommended artists to the user.
        if no recommendations are found, prints "no preferences available at this time"
        Emma Millet
    """
    dictionary = globalDict
    username = globalUsername

    if len(dictionary.keys()) == 1:
        return print("No preferences available at this time.")
    prefs = dictionary.get(username)
   
    best = -1
    prefs = dictionary.get(username)

    bestUser = ""
    for user in dictionary.keys():
        if user[-1] == "$":
            continue
        else:
            score = numMatches(prefs, dictionary[user])
            if score > best and username != user:
                best = score
                bestUser = user
   
    rec = []
    for item in dictionary.get(bestUser):
        if ((item in prefs) != True):
            rec += [item]
   
    if (rec == []):
        return print("No preferences available at this time.")
    for artist in rec:
        print(artist)

def edit(list1, list2):
    """returns a new list that contains only the elements in list2 not in list1
        Emma Millet
    """
    newL = []
    for item in list2:
        if ((item in list1) != True):
            newL += [item]
    return newL

def numMatches(list1, list2):
    """ return the num of elements that match between two sorted lists
         taken from textbook ; Emma Millet
    """
    matches, i, j = 0, 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def popDictMaker():
    ''' Returns a dictionary sorted by lowest frequently occuring artists to highest frequently returning artists 
    Steven Munson, edited by Emma Millet'''
    a = []
    for key in globalDict:
        if key[-1] != '$':
            a.append(key)

    L = []
    for x in a:
        for b in f[x]:
            L.append(b)
   
    y = []
    for x in L:
        if x not in y:
            y.append(x)
   
    d = {}
    for x in y:
        d.update({x: L.count(x)})
        L.remove(x)
   
    c = dict(sorted(d.items(), key=lambda item: item[1]))
    return c

def p():
    '''Shows the top 3 most popular artists by how frequently each show up in each users preferences; "Sorry, no user found." otherwise
    Steven Munson'''
    c = popDictMaker()
    if len(c) == 0:
        print("Sorry , no artists found.")
        return choices()

    elif len(c) < 3:
        w = list(c.keys())
        for x in range(len(c)):
            print(w[x])
        return choices()
    else:
        w = list(c.keys())
        for x in range(3):
            print(w[-1])
            w = w[:-1]
        return choices()

def h():
    '''Prints number of likes the most popular artist recieved. If there are no artists found, prints "Sorry, no artists found."
    Emma Millet'''
    c = popDictMaker()
    biggest = -1

    if c != {}:
        for artist in c:
            if c[artist] >= biggest:
                biggest = c[artist]
        print(biggest)
    else:
        print("Sorry, no artists found.")
    return choices()

def m():
    '''
       Prints the full name of the user who likes the most artists; "Sorry, no user found." otherwise
       Steven Munson
    '''
    x = 0
    arist = ''
    c = popDictMaker()
    if c == {}:
        print("Sorry, no user found.")
        return choices()
    for key in globalDict:
        if len(globalDict[key]) > x:
            x = len(globalDict[key])
            artist = key
    print(artist)
    return choices()
   
def choices():
    '''Provides menu options and handles user input
    Written by Steven Munson, Modified by Emma Millet '''

    choice = input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")
   
    while choice != 'q':
        if choice == 'e': e()
        if choice == 'r': r()
        if choice == 'p': p()
        if choice == 'h': h()
        if choice == 'm': m()
        else:
            choice = input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")

    with open('musicrecplus.txt', "r+") as file:
            for user in globalDict:
                file.truncate()
                file.seek(0)
                file.write(str(user) + ":" + ",".join(globalDict[user]) +
                        "\n")
            for user in globalDict:
                
                file.write(str(user) + ":" + ",".join(globalDict[user]) +
                        "\n")
    file.close()

try:
    with open('musicrecplus.txt', 'x') as f:
        f.write('')
except FileExistsError:
    f = read_preferences("musicrecplus.txt")

    pass

f = read_preferences("musicrecplus.txt")


name_artists = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
global globalUsername
globalUsername = name_artists


if name_artists not in f:
    a = {name_artists: []}
    print(a)
    f.update(appArtists(a, name_artists))
    print(f)
    choices()
   
else:
    choices()
