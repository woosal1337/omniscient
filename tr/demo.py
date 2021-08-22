from googletrans import Translator

translator = Translator()

translation = translator.translate("""
[Paroles de "Polémique" ft. Central Cee]

[Intro : Freeze Corleone, Central Cee & tag]
S/o le Flem
Allô ? Cee ? C'est comment ? T'as déjà quitté London ?
Yo Freeze, we're doing one ten through the country dumpin'
Vas-y, carré, fais-moi signe dès qu't'arrives à Paris
I'll be like in thirty minute my bro, I'll bill it, can you pattern some Cali ?
Sans stress, on a les connec', quand t'es là, on s'connecte
Say less, ekip, ekip
Yo

[Couplet 2 : Freeze Corleone]
Fais des grosses liasses avec des polémiques (Cash)
Dieu avec moi comme si j'bois que de l'eau bénite (Han)
Dakar comme la place de l'obélisque (Ekip)
Mixe Fanta exotique avec la codéine (Lin)
Faut transférer tout le cash au pays (Cash)
Dieu et le fer, négro, pas de protéines (Paw)
Corleone, Central Cee (Central Cee)
Lambo' orange, Maybach anthracite (Sku)
Fuck un colon, fuck la Françafrique
Chen Zen A.K.A. machine à scorer (Cash)
Yeuz’ bridés comme la Chine, la Corée (Han)
Pas d'pas d'danse dans les clips, pas d'choré'
Et y a que Dieu que j'peux adorer (Que j'peux adorer)
Dans la maison piège, trouve-moi dans la kitchen (Trouve-moi dans la kichten)

[Couplet 3 : Central Cee]
How they hate on man when I don't even know they're existing? (How?)
They talk too much, they tweet too much, gotta keep my distance
Cee don't be in the mix, one wish, my G's get freed out the system
Link with Freeze, it's lean that he drinkin'
Sippin', throwin' up Cs not crippin'
Keep on bitchin', think that you're Mitch
Until bro come and cut off your fingers
Fuck what you're thinking, fuck your opinion
That mixtape made me a million (Haha)

[Couplet 4 : Freeze Corleone]
Yeuz comme des litchis, loin d'eux comme les Fidji
CEO, compte en banque avec six chiffres (Cash)
Allume les big shit, découpe comme Geechi
Il m'faut le biff de Lionel Richie (Cash)
Six sur six, s/o à Central
Fume de ouf comme une cheminée d'la centrale
Grosse Cali comme à South Central
J'arrive New York à fond comme le parc central (Ekip)
Movie, bienvenue dans le film
S/o 22Gz, un trou dans l'muffin
Chen Zen chasse les vampires comme dans Buffy, ekip
""", dest="en")

print(translation.text)