def greet_user(): #def informs python that youre defing function
    """ Display a simple greeting."""# any indented lines that follow def(): make up the body of the function
    print("hello!") # is only a code in the body

greet_user() # b/s no information is needed here, calling our function is simple

print("\n****passing information to a function****")

def greet_user(username): # (username) is a parameter
    """Display simple greeting"""
    print("Hello,"+ username.title()+ "!")

greet_user('Jackie') # jackie is an argument in here

print(" -----------8-1------------")
def display_message():
    """I am learning Function in Python"""
    print("Hi, I am learning function in Python")

display_message()

print(" -----------8-2------------")

def favorite_book(book_title):
    print(f"My favortite book is '{book_title.title()}'")

favorite_book("the sun also rises")

print("\n***Passing Argument ***")

def describe_husband(race, husband='John'):
    """Display information about my husband."""
    print(f" I have a {husband} and he is {race.title()}")

describe_husband('blue','John')
describe_husband('mix','son')
describe_husband('more asian','middle son')

print("----------8-3----------")
def make_shirt(shirt_size, text_message):
    print(f"I would like to order a shirt size {shirt_size} and text message on the shirt '{text_message.title()}'")

make_shirt('small','be happy')
make_shirt(text_message ='be happy',shirt_size = 'small') # keyword arguments( the order of the keyword argument
# dosent matter becouse python know where each value should go.


print("----------8-4----------")

def make_shirt(shirt_size = 'large', text_message='I love python'):
    print(f"I would like to order a shirt size {shirt_size} and text message on the shirt '{text_message.title()}'")

make_shirt()
make_shirt(shirt_size = 'medium')
make_shirt(shirt_size = 'extra small', text_message= 'life is Good')

print("----------8-5----------")
def describe_city(city_name,country = 'Kyrgyzstan'):
    print(f" The city of {city_name} is in the {country} ")

describe_city('osh')
describe_city('bishkek')
describe_city('Moscow', 'Russia')

print("\n***********returning a value**********")
def get_name(first, last):
    """Return Full name, neatly formated"""
    full = first + ' '+last
    return full.title()
programmer = get_name('jackie','ashyrova')
print(programmer)

print("\n***while loop*******")
#while True:
    #print("\nPlease tell me your name:")
    #print("(enter 'q' at any time to quite)")

    #first = input("first: ")
    #if first == 'q':
       # break

    #last = input("last: ")
    #if last == 'q':
        #break
    #name = get_name(first, last)
    #print("\nhello " + name)

print("\n****making an argument optional in function***")
def get_name(first, last, middle):
    """Return Full name, neatly formated"""
    full = first + ' '+ last + ' ' + middle
    return full.title()
programmer = get_name('jackie','ashyrova','aman')
print(programmer)


print("\n*******to make some variables optional********")
def get_name(first, last, middle=''):
    """Return Full name, neatly formated"""
    if middle:
        full = first + ' '+last + ' ' + middle
    else:
        full = first + ' ' + last
    return full.title()
programmer = get_name('jackie','ashyrova')
print(programmer)
programmer = get_name('jackie','ashyrova','aman')
print(programmer)

print("\nhomework 8-6")

def city_country(city, country):
    return(city.upper() + ", " + country.upper())

city = city_country('nyc', 'usa')
print(city)

city = city_country('Bishkek', 'Kyrgyzstan')
print(city)

city = city_country('tokyo', 'japan')
print(city)

print("\nHomework 8-7-------")

def make_album(artist_name, music_album, tracks=0):
    artists = {'name': artist_name.title(),
               'album': music_album.title(),
               }
    if tracks:
        artists['tracks'] = tracks
    return artists

musician = make_album('John_Lenon','Avbey Road')
print(musician)

musician = make_album('Lady_gaga','Joanne')
print(musician)

musician = make_album('The_Beatles', 'Revolver')
print(musician)

tracks = make_album('me', 'you', tracks=8)
print(tracks)

print("\nhomework8-8")

def make_album(artist_name, music_album, tracks=0):
    artists = {'name': artist_name.title(),
               'album': music_album.title(),
               }
    if tracks:
        artists['tracks'] = tracks
    return artists

artist_name = "\n what album do you want?"
music_album ="whos the artist"

print("enter 'q' at any time yu want to stop")

while True:
    artist = input(artist_name)
    if artist == 'q':
        break
    album = input(music_album)
    if album == 'q':
        break

album= make_album(artist_name,music_album)
print(album)
print("\nthanks for responding")