import os

def BandNameGenerator():
    '''Takes the City name and Pet name returns Band Name A
    which is concatinated by City & Pet name'''

    os.system('cls') # os.system('clear') for Mac or linux

    print("Welcome to Band Name Generator.")    
    city = input("What's name of city you grew up in? :")
    pet_name = input("What's your pet's name? :")
    band_name = city.title() + " " + pet_name.title()
    # title() or capitalize() --> for first letter capital
    # Upper() --> for full of capital 
    # lower() --> for Full of lower case
    print("Your band name could be %s" %band_name)   
    # %d for Numeric and %s for String

BandNameGenerator()


