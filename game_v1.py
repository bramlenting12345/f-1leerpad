import os

aantal_loden_kettingen = 0

intro_verhaal = """--------------------------------escape from prisson------------------------------------

U bent op een mysterieus eiland en weet niet waar. Als je om je heen kijkt zie je betonnen muren en tralies voor de ramen.
Op de muur staat van alles gekrast. Leuke poppetjes, strepen waaruit je kan afleiden hoelang iemand hier al is geweest. 
Ok veel tekst en getallen. Een soort van kruis met daaronder het getal 1977 RIP Elvis.
Ook de deur is voorzien van enige traliewerk. Er zit een groot hangslot op de deur.
Na enig zoekwerk in de ruimte vind u de volgende spullen :

- Een groot oud stuk zeil
- Dik stuk ijzerdraad
- Dun klosje touw
- Een strip boek van Dagobert Duck

LET OP u krijgt bij ieder fout antwoord een loden ketting om. bij 2 loden kettingen zinkt u.

"""
print(intro_verhaal)
input("druk op enter om door te gaan ")
print(" ")
os.system("cls")





#------------------------------------ontsnappen uit cel------------------------

ontsnap_uit_cel = """--------------------------------ontsnap uit cel--------------------------------------------

welke item denk u te kunnen gebruiken om de cel deur open te maken ? 
a = een vijl
b = dun klosje touw
c = een dun stuk ijzerdraad
d = een C4 bom 
e = kern raket
f = dik stuk ijzerdraad
g = sleutel 

"""
print(ontsnap_uit_cel)
ontsnap_cel_item =input("maak u keuze ")

if ontsnap_cel_item=="f":
   print("dit was het juiste antwoord u bent ontsnap uit de cel  ")
   print(" ")
   
   input("druk enter om verder te gaan ")
   os.system("cls")

else:
   print("dit was niet het juiste antwoord u krijgt een loden ketting ")
   aantal_loden_kettingen = aantal_loden_kettingen + 1
   print("  ")
   print("u heeft " , aantal_loden_kettingen , "ketting")

   input("druk enter om verder te gaan ")
   os.system("cls")


# kies items----------------------------------------------------

kies_items = """--------------------kies items om mee te nemen-------------------
   
   voor dat u uw cel verlaat mag u nog twee items mee nemen.
   kies verstandig wand door de juiste keuze te maken komt u levend van het eiland af,
   maak u keuze 

   a = mobiekle telefoon
   b = dun klosje touw 
   c = dik klosje touw 
   d = pakje sigaretten
   e = een groot oud stuk zeil 
   f = dik stuk ijzerdraad 
   g = kern raket 
   
   """

print(kies_items)
   
kies_item_1 = input("maak u eerste keuze ")
print("  ")
kies_item_2 = input("maak u tweede keuze ")

if kies_item_1=="b" or kies_item_1=="e":
      if kies_item_2=="b" or kies_item_2=="e":
         print("subliem dit was de goede combinatie ")
         input("druk enter om verder te gaan ")
         os.system("cls")


      else:
         print("dit was niet het juiste antwoord u krijgt een loden ketting ")
         aantal_loden_kettingen = aantal_loden_kettingen + 1
         print("  ")
         print("u heeft " , aantal_loden_kettingen , "ketting")
         input("druk enter om verder te gaan ")
         os.system("cls")
         
else: 
     print("dit was niet het juiste antwoord u krijgt een loden ketting ")
     aantal_loden_kettingen = aantal_loden_kettingen + 1
     print("  ")
     print("u heeft " , aantal_loden_kettingen , "ketting")     
     input("druk enter om verder te gaan ")
     os.system("cls")

# open buiten deur----------------------------------------------------

open_buiten_deur = """----------------------open buiten deur---------------------

u heeft 2 middelen mee genomen waar van u denkt dat u er mee van het eiland af kan komen
maar voor dat u het eiland verder kan ontdekken moet u eerst een deur open maken die 
u naar buiten leid. Dit is een deur met een cijfer cominatie. In het hek werk staat
de tekst RIP Elvis gekrast. Denk goed terug voor dat u de cominatie in voert u heeft 
maar een kans om de code goed in te voeren.

dit zijn de invoer codes waar uit u kunst kiezen 

a = 1977
b = 1820
c = 1930
d = 1967
e = 1989
f = 2021
g = 1830

"""
print(open_buiten_deur )

open_buiten_deur_1 = input("maak u keuze ")
if open_buiten_deur_1=="a":
    print("u bent geweldig dit was het goeie antwoord ")
    input("druk enter om verder te gaan ")
    os.system("cls")

else: 
   print("dit was niet het juiste antwoord u krijgt een loden ketting ")
   aantal_loden_kettingen = aantal_loden_kettingen + 1
   print("  ")
   print("u heeft " , aantal_loden_kettingen , "ketting")     
   input("druk enter om verder te gaan ")
   os.system("cls")



het_eiland_af="""---------------------het eiland af------------------------------------

u loopt door de buiten deur om u heen ziet u een prachtig eiland met palmbomen en een mooi
wit strand. Maar ondanks dat het een prachtige vakantie bestemming zou kunne zijn 
wilt u zo snel mogelijk van het eiland af. U loopt naar het strand en kijkt treurig naar de zee 
je ziet niks alleen maar water,water en nog is water. Je bedenkt dat de enige oplossing die je hebt 
is om een vlot te bouwen en op deze manier van het eiland af te komen.

Tip   als u bij de tweede vraag de juiste spullen heeft mee genomen dan kunt u daar een vlot van bouwen 

u kunt kiezen uit de volgende spullen voor het maken van een vlot.

a = een opblaas boot 
b = een oud stuk zeil 
c = een dik stuk touw 
d = een roei spaan 
e = dun stuk touw 
f = een pakje sigaretten 
g = een pomp


"""
print(het_eiland_af)

red_middel_1=input("maak u keuze ")
red_middel_2=input("maak u tweede keuze ")


if red_middel_1=="b" or red_middel_1=="e":
   if red_middel_2=="b" or red_middel_2=="e":
      print("amazing hiermee kunt u een vlot bouwen")

   else:
      print("dit was niet het juiste antwoord u krijgt een loden ketting ")
      aantal_loden_kettingen = aantal_loden_kettingen + 1
      print("  ")
      print("u heeft " , aantal_loden_kettingen , "ketting")
      input("druk enter om verder te gaan ")
      os.system("cls")

else:
    print("dit was niet het juiste antwoord u krijgt een loden ketting ")
    aantal_loden_kettingen = aantal_loden_kettingen + 1
    print("  ")
    print("u heeft " , aantal_loden_kettingen , "ketting")
    input("druk enter om verder te gaan ")
    os.system("cls")



   
het_einde="""--------------------het einde------------------------------

als u het spel goed heeft gespeeld en u heeft de juist antwoorden gekozen dan bent u nu onderweg 
op een zelf gebouwen vlot. en na 3 dagen op zee rond gezworven te hebben bent u opgepikt 
door een vrachtschip die je naar huis heeft gebracht.
heeft u door te veel fouten antwoorden meer dan 3 sleutels 
dan bent u gezonken met vlot en al en opgegeten door
haaien. 
"""
print(het_einde)