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