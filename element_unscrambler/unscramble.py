# List with most of the elements
import time
start_time = time.time()
elements = ['Hydrogen',
'Helium',
'Lithium',
'Berylium',
'Boron',
'Carbon',
'Nitrogen',
'Oxygen',
'Fluorine',
'Neon', 
'Sodium', 
'Magnesium',
'Aluminium',
'Silicon',
'Phosphorus', 
'Sulphur',
'Chlorine',
'Argon',
'Potassium',
'Calcium',
'Scandium',
'Titanium',
'Vanadium',
'Chromium',
'Manganese',
'Iron',
'Cobalt',
'Nickel',
'Copper',
'Zinc',
'Gallium',
'Germanium',
'Arsenic',
'Selenium',
'Bromine',
'Krypton',
'Rubidium',
'Strontium',
'Yttrium',
'Zirconium',
'Niobium',
'Molybdenum',
'Technetium',
'Ruthenium',
'Rhodium',
'Palladium',
'Silver',
'Cadmium',
'Indium',
'Tin',
'Antimony',
'Tellurium',
'Iodine',
'Xenon',
'Caesium',
'Barium',
'Lanthanum',
'Astatine',
'Americium',
'Actinium',
'Bismuth',
'Bohrium',
'Caesium',
'Copernicium',
'Cerium',
'Curium',
'Californium',
'Dubnium',
'Darmstadtium',
'Dysprosium',
'Europium',
'Einsteinium',
'Francium',
'Fermium',
'Gold',
'Gadolinium'
'Hafnium',
'Hassium',
'Holmium',
'Iridium',
'Lead',
'Lanthanum',
'Lutetium',
'Lawrencium',
'Meitnerium',
'Mendelevium',
'Neodymium']
#Getting input
a = input("Enter your scrambled element:  ")
a = a.lower()
a = list(a)
checkmain = sorted(a)
z = len(elements)
another = True
#Iterating through each element
for i in range(z):
    lower = elements[i].lower()
    lista = list(lower)
    check = sorted(lista)
    if check==checkmain:
        #Join list into a word
        checkb = "".join(lista)
        #Captalize first 
        checkb = checkb.capitalize()
        print(f"Yes, found a match, {checkb}.")
        #Printing runtime
        print("This took:", time.time()-start_time, "seconds")
        #That means a match has been found
        another = False
        break
if another==True:
    #If there is no match
    print("No match found...Maybe a Typo??")
