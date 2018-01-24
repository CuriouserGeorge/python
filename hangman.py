""" the game is hangman"""
import random
from PIL import Image
path=('/Users/georgetimbrell/Documents/Hanuman.jpg')

pic1 = Image.open(path)
    




words = ("abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachtsman yippee yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac zombie")
words = words.split()
word = random.choice(words)
#print(word)
hints = ['_']*len(word)
print(''.join(hints))


guesses = []

trys = 0
maxTrys = 5
while ''.join(hints) != word and trys < maxTrys:
    guess = input("please guess a letter")
    if guess not in guesses:
        guesses.append(guess)
    print(guesses)

    for i in range(len(word)):
        if word[i] in guesses:
            hints[i] = word [i]
    guesses.sort()
    strGuesses = ','.join(guesses)
    print("current guesses are : %s" % strGuesses)
    trys += 1
    print(''.join(hints))

    
    print ("number of guesses is %d / 5" % trys)


if ''.join(hints) == word:
    print( "well done")

if trys == maxTrys:
    print (" he's dead")
    print ("the word is %s" % word)




    
