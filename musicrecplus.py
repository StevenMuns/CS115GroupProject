#Steven Munson and Emma Millet
#I pledge my honor that I have abided by the Stevens Honor System



def read_preferences(filename):
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
    a = input("Enter an artist that you like (Enter to finish): ")
    if a == '':
        b = {u:[]}
        b[u] = sorted(d[u])
        return b
    x = a[1:].casefold()
    y = a[0].capitalize() + x
    if y in d[u]:
        return appArtists(d, u)
    d[u].append(y)
    return appArtists(d, u)

def e():
    f.pop(name_artists)
    a = {name_artists: []}
    f.update(appArtists(a, name_artists))
    print(f)
    choices()

def r():
    """ 
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
         taken from textbook
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

def p():
    a = []
    for key in f:
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

def choices():
    choice = input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")
    choices = ['e', 'r', 'p', 'h', 'm']

    while choice != 'q':
        if choice == 'e': e()
        if choice == 'r': r()
        if choice == 'p': p()
        if choice == 'h': h()
        if choice == 'm': m()
        else:
            choice = input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")

try:
    with open('musicrecplus_ex2_b.txt', 'x') as f:
        f.write('')
except FileExistsError:
    f = read_preferences("musicrecplus_ex2_b.txt")

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























