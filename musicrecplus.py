#Steven Munson
#I pledge my honor to have abided by the Stevens Honor System

def read_preferences(filename):
    dictionary = {}
    with open(filename, "r") as f:
        if f == '':
            return ''
        for line in f:
            [username, artists] = line.strip().split(":")
            artistList = artists.split(",")
            dictionary[username] = artistList
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

def choices():
    choice = input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")
    choices = ['e', 'r', 'p', 'h', 'm', 'q']
    while choice not in choices:
        choice = input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")
    if choice == 'e': e()
    if choice == 'r': r()
    if choice == 'p': p()
    if choice == 'h': h()
    if choice == 'm': m()
    if choice == 'q': q()

try:
    with open('musicrecplus_ex2_b.txt', 'x') as f:
        f.write('')
except FileExistsError:
    f = read_preferences("musicrecplus_ex2_b.txt")

name_artists = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")


if name_artists not in f:
    a = {name_artists: []}
    print(a)
    f.update(appArtists(a, name_artists))
    print(f)
    choices()
    
else:
    choices()

























