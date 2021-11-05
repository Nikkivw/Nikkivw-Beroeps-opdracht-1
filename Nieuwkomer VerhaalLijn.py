# Slow typing
import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     #time.sleep(3./90)

# Begin of the story
def Begin():
    sprint("Je woont in Kabul de hoofdstad van Afghanistan de taliban is binnengedrongen en dreigt iedereen neerschieten die niet bij de Taliban wilt aan sluiten. Je besluit te vluchten.")
    Begin = input("Hoe wil je vluchten? \na. Lopen \nb. Met de auto naar het dichts bij zijnde buurland Pakistan \nc. Smokkelaar\n") # A = senario1_1, B = Senario1_2, C = Senario1_3,
    if Begin == 'a':
        print('\n')
        Senario1_1()
    elif Begin == 'b':
        print('\n')
        Senario2_1()
    else:
        Begin == 'c'
        print('\n')
        Senario3_1() 

def Senario1_1(): # 50/50 chance question
    sprint ("Je hebt gekozen om lopend naar turkije te gaan maar je had niet genoeg tijd om de reis voor te bereiden waardoor je niet genoeg voedsel en water mee heb kunnen nemen.")
    vraag50_50 = input("Druk op enter om verder te kijken") 
    if vraag50_50 == '': #Enter imput for 50/50 
        sprint("Test")

def Senario1_2(): # Good ending 50/50
    sprint("Je hebt de reis overleeft en bent aangekomen in turkije je bent alleen heel erg verhongerd en uitgedroogd. Direct nadat je bent aangekomen in turkije ben je naar het ziekenhuis gebracht.")

def Senario1_3(): # Bad ending 50/50
    sprint("Je was verder terug al iemand tegengekomen die vroeg om voedsel en water. Wellicht had je dat niet moeten delen.")

def Senario2_1(): 
    sprint ("Je hebt besloten om naar het dichts bij zijnde buurland te vluchten (Pakistan) Met de auto.\nMaar door de chaos in de stad is de auto stuk.Je hebt nog maar twee opties, kijken of je iemand kan vinden om mee te rijzen of een smokkelaar vragen om je over de grens te brengen.")
    Vraag_1  = input("Je hebt nog maar twee opties.\na.kijken of je iemand kan vinden om mee te rijzen.\nb.Smokkelaar vragen om je over de grens te brengen.\n")
    if Vraag_1 == 'a':
        print('\n')
        Senario2_2()
    elif Vraag_1 == 'b':
        print('\n')
        Senario3_1()

def Senario2_2():
    sprint ("Je hebt een familie gevonden die ook naar Pakistan willen vluchten. Je mag van de familie mee rijden, maar midden in de rijs stopt de auto er mee. Je gaat kijken en ziet dat de motor over verhit is. Je kan de motor laten af koelen en dan over hopelijk een dag verder gaan of het laatste stuk gaan lopen.")

def Senario3_1(): 
    sprint ("Test") 
Begin()

