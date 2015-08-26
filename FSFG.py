#/bin/python
#########################
##
## Fake Sensitive File Generator
## v0.1
## 
## Coded by Th3R3g3nt
##
#########################

import random
import argparse
import glob
import sys
from argparse import RawTextHelpFormatter

# US Common Names http://www.behindthename.com/top/lists/us/2013/100 && http://names.mongabay.com/most_common_surnames.htm
def namegen():

	f_names = ["Aaron","Adam","Adrian","Aiden","Alexander","Andrew","Angel","Anthony","Austin","Ayden","Benjamin","Bentley","Blake","Brandon","Brayden","Brody","Caleb","Camden","Cameron","Carson","Carter","Charles","Chase","Christian","Christopher","Colton","Connor","Cooper","Damian","Daniel","David","Dominic","Dylan","Easton","Eli","Elijah","Ethan","Evan","Gabriel","Gavin","Grayson","Henry","Hudson","Hunter","Ian","Isaac","Isaiah","Jace","Jack","Jackson","Jacob","James","Jase","Jason","Jaxon","Jaxson","Jayden","Jeremiah","John","Jonathan","Jordan","Jose","Joseph","Joshua","Josiah","Juan","Julian","Justin","Kayden","Kevin","Landon","Levi","Liam","Lincoln","Logan","Lucas","Luis","Luke","Mason","Matthew","Michael","Nathan","Nathaniel","Nicholas","Noah","Nolan","Oliver","Owen","Parker","Robert","Ryan","Samuel","Sebastian","Thomas","Tristan","Tyler","William","Wyatt","Xavier","Zachary","Aaliyah","Abigail","Addison","Alexa","Alexandra","Alexis","Allison","Alyssa","Amelia","Anna","Annabelle","Aria","Ariana","Arianna","Ashley","Aubree","Aubrey","Audrey","Autumn","Ava","Avery","Bella","Brianna","Brooklyn","Camila","Caroline","Charlotte","Chloe","Claire","Elizabeth","Ella","Ellie","Emily","Emma","Eva","Evelyn","Faith","Gabriella","Genesis","Gianna","Grace","Hailey","Hannah","Harper","Isabella","Jocelyn","Julia","Katherine","Kayla","Kaylee","Kennedy","Khloe","Kylie","Lauren","Layla","Leah","Lillian","Lily","London","Lucy","Lydia","Mackenzie","Madeline","Madelyn","Madison","Makayla","Maya","Melanie","Mia","Mila","Morgan","Naomi","Natalie","Nevaeh","Nicole","Nora","Olivia","Paisley","Penelope","Peyton","Piper","Riley","Ruby","Sadie","Samantha","Sarah","Savannah","Scarlett","Serenity","Skylar","Sofia","Sophia","Sophie","Stella","Sydney","Taylor","Victoria","Violet","Zoe","Zoey"]
	l_names = ["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson","Garcia","Martinez","Robinson","Clark","Rodriguez","Lewis","Lee","Walker","Hall","Allen","Young","Hernandez","King","Wright","Lopez","Hill","Scott","Green","Adams","Baker","Gonzalez","Nelson","Carter","Mitchell","Perez","Roberts","Turner","Phillips","Campbell","Parker","Evans","Edwards","Collins","Stewart","Sanchez","Morris","Rogers","Reed","Cook","Morgan","Bell","Murphy","Bailey","Rivera","Cooper","Richardson","Cox","Howard","Ward","Torres","Peterson","Gray","Ramirez","James","Watson","Brooks","Kelly","Sanders","Price","Bennett","Wood","Barnes","Ross","Henderson","Coleman","Jenkins","Perry","Powell","Long","Patterson","Hughes","Flores","Washington","Butler","Simmons","Foster","Gonzales","Bryant","Alexander","Russell","Griffin","Diaz","Hayes","Myers","Ford","Hamilton","Graham","Sullivan","Wallace","Woods","Cole","West","Jordan","Owens","Reynolds","Fisher","Ellis","Harrison","Gibson","Mcdonald","Cruz","Marshall","Ortiz","Gomez","Murray","Freeman","Wells","Webb","Simpson","Stevens","Tucker","Porter","Hunter","Hicks","Crawford","Henry","Boyd","Mason","Morales","Kennedy","Warren","Dixon","Ramos","Reyes","Burns","Gordon","Shaw","Holmes","Rice","Robertson","Hunt","Black","Daniels","Palmer","Mills","Nichols","Grant","Knight","Ferguson","Rose","Stone","Hawkins","Dunn","Perkins","Hudson","Spencer","Gardner","Stephens","Payne","Pierce","Berry","Matthews","Arnold","Wagner","Willis","Ray","Watkins","Olson","Carroll","Duncan","Snyder","Hart","Cunningham","Bradley","Lane","Andrews","Ruiz","Harper","Fox","Riley","Armstrong","Carpenter","Weaver","Greene","Lawrence","Elliott","Chavez","Sims","Austin","Peters","Kelley","Franklin","Lawson","Fields","Gutierrez","Ryan","Schmidt","Carr","Vasquez","Castillo","Wheeler","Chapman","Oliver","Montgomery","Richards","Williamson","Johnston","Banks","Meyer","Bishop","Mccoy","Howell","Alvarez","Morrison","Hansen","Fernandez","Garza","Harvey","Little","Burton","Stanley","Nguyen","George","Jacobs","Reid","Kim","Fuller","Lynch","Dean","Gilbert","Garrett","Romero","Welch","Larson","Frazier","Burke","Hanson","Day","Mendoza","Moreno","Bowman","Medina","Fowler","Brewer","Hoffman","Carlson","Silva","Pearson","Holland","Douglas","Fleming","Jensen","Vargas","Byrd","Davidson","Hopkins","May","Terry","Herrera","Wade","Soto","Walters","Curtis","Neal","Caldwell","Lowe","Jennings","Barnett","Graves","Jimenez","Horton","Shelton","Barrett","Obrien","Castro","Sutton","Gregory","Mckinney","Lucas","Miles","Craig","Rodriquez","Chambers","Holt","Lambert","Fletcher","Watts","Bates","Hale","Rhodes","Pena","Beck","Newman","Haynes","Mcdaniel","Mendez","Bush","Vaughn","Parks","Dawson","Santiago","Norris","Hardy","Love","Steele","Curry","Powers","Schultz","Barker","Guzman","Page","Munoz","Ball","Keller","Chandler","Weber","Leonard","Walsh","Lyons","Ramsey","Wolfe","Schneider","Mullins","Benson","Sharp","Bowen","Daniel","Barber","Cummings","Hines","Baldwin","Griffith","Valdez","Hubbard","Salazar","Reeves","Warner","Stevenson","Burgess","Santos","Tate","Cross","Garner","Mann","Mack","Moss","Thornton","Dennis","Mcgee","Farmer","Delgado","Aguilar","Vega","Glover","Manning","Cohen","Harmon","Rodgers","Robbins","Newton","Todd","Blair","Higgins","Ingram","Reese","Cannon","Strickland","Townsend","Potter","Goodwin","Walton","Rowe","Hampton","Ortega","Patton","Swanson","Joseph","Francis","Goodman","Maldonado","Yates","Becker","Erickson","Hodges","Rios","Conner","Adkins","Webster","Norman","Malone","Hammond","Flowers","Cobb","Moody","Quinn","Blake","Maxwell","Pope","Floyd","Osborne","Paul","Mccarthy","Guerrero","Lindsey","Estrada","Sandoval","Gibbs","Tyler","Gross","Fitzgerald","Stokes","Doyle","Sherman","Saunders","Wise","Colon","Gill","Alvarado","Greer","Padilla","Simon","Waters","Nunez","Ballard","Schwartz","Mcbride","Houston","Christensen","Klein","Pratt","Briggs","Parsons","Mclaughlin","Zimmerman","French","Buchanan","Moran","Copeland","Roy","Pittman","Brady","Mccormick","Holloway","Brock","Poole","Frank","Logan","Owen","Bass","Marsh","Drake","Wong","Jefferson","Park","Morton","Abbott","Sparks","Patrick","Norton","Huff","Clayton","Massey","Lloyd","Figueroa","Carson","Bowers","Roberson","Barton","Tran","Lamb","Harrington","Casey","Boone","Cortez","Clarke","Mathis","Singleton","Wilkins","Cain","Bryan","Underwood","Hogan","Mckenzie","Collier","Luna","Phelps","Mcguire","Allison","Bridges","Wilkerson","Nash","Summers","Atkins","Wilcox","Pitts","Conley","Marquez","Burnett","Richard","Cochran","Chase","Davenport","Hood","Gates","Clay","Ayala","Sawyer","Roman","Vazquez","Dickerson","Hodge","Acosta","Flynn","Espinoza","Nicholson","Monroe","Wolf","Morrow","Kirk","Randall","Anthony","Whitaker","Oconnor","Skinner","Ware","Molina","Kirby","Huffman","Bradford","Charles","Gilmore","Dominguez","Oneal","Bruce","Lang","Combs","Kramer","Heath","Hancock","Gallagher","Gaines","Shaffer","Short","Wiggins","Mathews","Mcclain","Fischer","Wall","Small","Melton","Hensley","Bond","Dyer","Cameron","Grimes","Contreras","Christian","Wyatt","Baxter","Snow","Mosley","Shepherd","Larsen","Hoover","Beasley","Glenn","Petersen","Whitehead","Meyers","Keith","Garrison","Vincent","Shields","Horn","Savage","Olsen","Schroeder","Hartman","Woodard","Mueller","Kemp","Deleon","Booth","Patel","Calhoun","Wiley","Eaton","Cline","Navarro","Harrell","Lester","Humphrey","Parrish","Duran","Hutchinson","Hess","Dorsey","Bullock","Robles","Beard","Dalton","Avila","Vance","Rich","Blackwell","York","Johns","Blankenship","Trevino","Salinas","Campos","Pruitt","Moses","Callahan","Golden","Montoya","Hardin","Guerra","Mcdowell","Carey","Stafford","Gallegos","Henson","Wilkinson","Booker","Merritt","Miranda","Atkinson","Orr","Decker","Hobbs","Preston","Tanner","Knox","Pacheco","Stephenson","Glass","Rojas","Serrano","Marks","Hickman","English","Sweeney","Strong","Prince","Mcclure","Conway","Walter","Roth","Maynard","Farrell","Lowery","Hurst","Nixon","Weiss","Trujillo","Ellison","Sloan","Juarez","Winters","Mclean","Randolph","Leon","Boyer","Villarreal","Mccall","Gentry","Carrillo","Kent","Ayers","Lara","Shannon","Sexton","Pace","Hull","Leblanc","Browning","Velasquez","Leach","Chang","House","Sellers","Herring","Noble","Foley","Bartlett","Mercado","Landry","Durham","Walls","Barr","Mckee","Bauer","Rivers","Everett","Bradshaw","Pugh","Velez","Rush","Estes","Dodson","Morse","Sheppard","Weeks","Camacho","Bean","Barron","Livingston","Middleton","Spears","Branch","Blevins","Chen","Kerr","Mcconnell","Hatfield","Harding","Ashley","Solis","Herman","Frost","Giles","Blackburn","William","Pennington","Woodward","Finley","Mcintosh","Koch","Best","Solomon","Mccullough","Dudley","Nolan","Blanchard","Rivas","Brennan","Mejia","Kane","Benton","Joyce","Buckley","Haley","Valentine","Maddox","Russo","Mcknight","Buck","Moon","Mcmillan","Crosby","Berg","Dotson","Mays","Roach","Church","Chan","Richmond","Meadows","Faulkner","Oneill","Knapp","Kline","Barry","Ochoa","Jacobson","Gay","Avery","Hendricks","Horne","Shepard","Hebert","Cherry","Cardenas","Mcintyre","Whitney","Waller","Holman","Donaldson","Cantu","Terrell","Morin","Gillespie","Fuentes","Tillman","Sanford","Bentley","Peck","Key","Salas","Rollins","Gamble","Dickson","Battle","Santana","Cabrera","Cervantes","Howe","Hinton","Hurley","Spence","Zamora","Yang","Mcneil","Suarez","Case","Petty","Gould","Mcfarland","Sampson","Carver","Bray","Rosario","Macdonald","Stout","Hester","Melendez","Dillon","Farley","Hopper","Galloway","Potts","Bernard","Joyner","Stein","Aguirre","Osborn","Mercer","Bender","Franco","Rowland","Sykes","Benjamin","Travis","Pickett","Crane","Sears","Mayo","Dunlap","Hayden","Wilder","Mckay","Coffey","Mccarty","Ewing","Cooley","Vaughan","Bonner","Cotton","Holder","Stark","Ferrell","Cantrell","Fulton","Lynn","Lott","Calderon","Rosa","Pollard","Hooper","Burch","Mullen","Fry","Riddle","Levy","David","Duke","Odonnell","Guy","Michael","Britt","Frederick","Daugherty","Berger","Dillard","Alston","Jarvis","Frye","Riggs","Chaney","Odom","Duffy","Fitzpatrick","Valenzuela","Merrill","Mayer","Alford","Mcpherson","Acevedo","Donovan","Barrera","Albert","Cote","Reilly","Compton","Raymond","Mooney","Mcgowan","Craft","Cleveland","Clemons","Wynn","Nielsen","Baird","Stanton","Snider","Rosales","Bright","Witt","Stuart","Hays","Holden","Rutledge","Kinney","Clements","Castaneda","Slater","Hahn","Emerson","Conrad","Burks","Delaney","Pate","Lancaster","Sweet","Justice","Tyson","Sharpe","Whitfield","Talley","Macias","Irwin","Burris","Ratliff","Mccray","Madden","Kaufman","Beach","Goff","Cash","Bolton","Mcfadden","Levine","Good","Byers","Kirkland","Kidd","Workman","Carney","Dale","Mcleod","Holcomb","England","Finch","Head","Burt","Hendrix","Sosa","Haney","Franks","Sargent","Nieves","Downs","Rasmussen","Bird","Hewitt","Lindsay","Le","Foreman","Valencia","Oneil","Delacruz","Vinson","Dejesus","Hyde","Forbes","Gilliam","Guthrie","Wooten","Huber","Barlow","Boyle","Mcmahon","Buckner","Rocha","Puckett","Langley","Knowles","Cooke","Velazquez","Whitley","Noel","Vang"]
	return[f_names[random.randint(0, len(f_names)-1)],l_names[random.randint(0, len(l_names)-1)]]

# US Phone Number
def phonegen(format=1):

	number = ""
	# 123-123-1234	
	if format == 1:
		number = number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('123456789')
		number = number+"-"
		for i in range(3):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# 123 123 1234
	if format == 2:
		number = number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(3):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# 1231231234
	if format == 3:
		number = number+random.choice('123456789')
		for i in range(9):
			number = number+random.choice('1234567890')
		return number

	# 123-1234-123
	if format == 4:
		number = number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(4):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(3):
			number = number+random.choice('1234567890')
		return number


	# 123 1234 123
	if format == 5:
		number = number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(4):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(3):
			number = number+random.choice('1234567890')
		return number

	# (123)-123-1234
	if format == 6:
		number = "("+number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+")-"
		for i in range(3):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# (123) 123 1234
	if format == 7:
		number = "("+number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+") "
		for i in range(3):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# (123)1231234
	if format == 8:
		number = "("+number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+")"
		for i in range(7):
			number = number+random.choice('1234567890')
		return number



# US SSN format
def ssngen(format=1):
	number = ""
	# 123-12-1234
	if format == 1:
		number = number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# 123 12 1234
	if format == 2:
		number = number+random.choice('123456789')
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(2):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# 123456789
	if format == 3:
		number = number+random.choice('123456789')
		for i in range(8):
			number = number+random.choice('1234567890')
		return number

# US Driver Licence
def dlgen():
	number = ""
	number = number+random.choice('123456789')
	for i in range(7):
		number = number+random.choice('1234567890')
	return number

# Citizenship
def citgen():

	citlist = ["Afghan","Albanian","Algerian","Andorran","Angolan","Argentinian","Armenian","Australian","Austrian","Azerbaijani","American","Bahamian","Bahraini","Bangladeshi","Barbadian","Belarusian","Belgian","Belizean","Beninese","Bhutanese","Bolivian","Bosnian","Tswana","Brazilian","Briton","Bruneian","Bulgarian","Burkinese","Burmese","Burundian","Cambodian","Cameroonian","Canadian","Cape Verdean","Chadian","Chilean","Chinese","Colombian","Congolese","Costa Rican","Croat or a Croatian","Cuban","Cypriot","Czech","Dane","Djiboutian","Dominican","Dominican","Ecuadorean","Egyptian","Salvadorean","English","Eritrean","Estonian","Ethiopian","Fijian","Finn","French","Gabonese","Gambian","Georgian","German","Ghanaian","Greek","Grenadian","Guatemalan","Guinean","Guyanese","Haitian","Dutch","Honduran","Hungarian","Icelander","Indian","Indonesian","Iranian","Iraqi","Irish","Italian","Jamaican","Japanese","Jordanian","Kazakh","Kenyan","Kuwaiti","Laotian","Latvian","Lebanese","Liberian","Libyan","Liechtensteiner","Lithuanian","Luxembourger","Macedonian","Malagasy","Malawian","Malaysian","Maldivian","Malian","Maltese","Mauritanian","Mauritian","Mexican","Moldovan","Monacan","Mongolian","Montenegrin","Moroccan","Mozambican","Namibian","Nepalese","Dutch","New Zealander","Nicaraguan","Nigerien","Nigerian","North Korean","Norwegian","Omani","Pakistani","Panamanian","Papua New Genuinean","Paraguayan","Peruvian","Filipino","Pole","Portuguese","Qatari","Romanian","Russian","Rwandan","Saudi Arabian","Scot","Senegalese","Serb or a Serbian","Seychellois","Sierra Leonian","Singaporean","Slovak","Slovene","Solomon Islander","Somali","South African","South Korean","Spaniard","Sri Lankan","Sudanese","Swazi","Swede","Swiss","Syrian","Taiwanese","Tajik","Tanzanian","Thai","Togolese","Trinidadian","Tobagan","Tunisian","Turk","Turkmen","Tuvaluan","Ugandan","Ukrainian","Emirati","Briton","US citizen","Uruguayan","Uzbek","Vanuatuan","Venezuelan","Vietnamese","Welsch","Western Samoan","Yemeni","Yugoslav","Zairean","Zambian","Zimbabwean"]
	return citlist[random.randint(0, len(citlist)-1)]

# Birth date
def bdaygen(format = 1):
	number = ""
	#23/12/1985
	if format == 1:
		number = ""
		number = number+str(random.randint(1, 31))
		number = number+"/"
		number = number+str(random.randint(1, 12))
		number = number+"/"
		number = number+str(random.randint(1930, 2014))
		return number

	#23-12-1985
	if format == 2:
		number = ""
		number = number+str(random.randint(1, 31))
		number = number+"-"
		number = number+str(random.randint(1, 12))
		number = number+"-"
		number = number+str(random.randint(1930, 2014))
		return number

	#12/23/1985
	if format == 3:
		number = ""
		number = number+str(random.randint(1, 12))
		number = number+"/"
		number = number+str(random.randint(1, 31))
		number = number+"/"
		number = number+str(random.randint(1930, 2014))
		return number

	#12-23-1985
	if format == 4:
		number = ""
		number = number+str(random.randint(1, 12))
		number = number+"-"
		number = number+str(random.randint(1, 31))
		number = number+"-"
		number = number+str(random.randint(1930, 2014))
		return number

	#1985/12/23
	if format == 5:
		number = ""
		number = number+str(random.randint(1930, 2014))
		number = number+"/"
		number = number+str(random.randint(1, 12))
		number = number+"/"
		number = number+str(random.randint(1, 31))
		return number

	#1985-12-23
	if format == 6:
		number = ""
		number = number+str(random.randint(1930, 2014))
		number = number+"-"
		number = number+str(random.randint(1, 12))
		number = number+"-"
		number = number+str(random.randint(1, 31))
		return number


# Financial Infomation - Bank Account number
def bangen():
	number = ""
	# 0123456789012
	number = number+random.choice('123456789')
	for i in range(12):
		number = number+random.choice('1234567890')
	return number

# Financial Infomation - Bank Account routing number
def rougen(format=1):
	number = ""
	# 0123456789
	number = number+random.choice('123456789')
	for i in range(8):
		number = number+random.choice('1234567890')
	return number


# Financial Infomation - Credit Card number
def ccgen(format=1):
	number = ""
	# 1234-123456-12345
	if format == 1:
		number = number+random.choice('3456')
		for i in range(3):
			number = number+random.choice('123456789')
		number = number+"-"
		for i in range(6):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(5):
			number = number+random.choice('1234567890')
		return number

	# 1234 123456 12345
	if format == 2:
		number = number+random.choice('3456')
		for i in range(3):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(6):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(5):
			number = number+random.choice('1234567890')
		return number

	# 123412345612345
	if format == 3:
		number = number+random.choice('3456')
		for i in range(14):
			number = number+random.choice('1234567890')
		return number

	# 1234-1234-1234-1234
	if format == 4:
		number = number+random.choice('3456')
		for i in range(3):
			number = number+random.choice('123456789')
		number = number+"-"
		for i in range(4):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(4):
			number = number+random.choice('1234567890')
		number = number+"-"
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# 1234 1234 1234 1234
	if format == 5:
		number = number+random.choice('3456')
		for i in range(3):
			number = number+random.choice('123456789')
		number = number+" "
		for i in range(4):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(4):
			number = number+random.choice('1234567890')
		number = number+" "
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

	# 1234 1234 1234 1234
	if format == 6:
		number = number+random.choice('3456')
		for i in range(3):
			number = number+random.choice('123456789')
		for i in range(4):
			number = number+random.choice('1234567890')
		for i in range(4):
			number = number+random.choice('1234567890')
		for i in range(4):
			number = number+random.choice('1234567890')
		return number

#Easy (consistent formatting, CSV, one record per line, includes header info)
def easy(args):
	delim = ","
	print "First name,Last name,Birthday,Phone Number,Social Security Number,Driver License Number,Citizenship,Bank Routing Number,Bank Account Number,Credit Card Number"
	for i in range(args.number[0]):
		name = namegen() 
		bday = bdaygen()
		phone = phonegen()
		ssn = ssngen()
		dl = dlgen()
		cit = citgen()
		rou = rougen()
		ban = bangen()
		cc = ccgen()
		print name[0] + delim + name[1] + delim + bday + delim + phone + delim + ssn + delim + dl + delim + cit + delim + rou + delim + ban + delim + cc

#Normal (random formatting, CSV, one record per line)
def medium(args):
	delim = ","
	for i in range(args.number[0]):
		name = namegen() 
		bday = bdaygen(random.randint(1, 6))
		phone = phonegen(random.randint(1, 7))
		ssn = ssngen(random.randint(1, 3))
		dl = dlgen()
		cit = citgen()
		rou = rougen()
		ban = bangen()
		cc = ccgen(random.randint(1, 6))
		print name[0] + delim + name[1] + delim + bday + delim + phone + delim + ssn + delim + dl + delim + cit + delim + rou + delim + ban + delim + cc

#Hard (random formatting, random delimiter, no new line)
def hard(args):
	for i in range(args.number[0]):
		delim = random.choice("~!@#$%^&*=_+[]{}|;':\",.<>?")
		name = namegen() 
		bday = bdaygen(random.randint(1, 6))
		phone = phonegen(random.randint(1, 7))
		ssn = ssngen(random.randint(1, 3))
		dl = dlgen()
		cit = citgen()
		rou = rougen()
		ban = bangen()
		cc = ccgen(random.randint(1, 6))
		print name[0] + delim + name[1] + delim + bday + delim + phone + delim + ssn + delim + dl + delim + cit + delim + rou + delim + ban + delim + cc,

#Medium + Ceaser cipher for easy decode and readability
def obfuscated(args):
	ofile = open("test_plain.txt","w")
		
	delim = ","
	for i in range(args.number[0]):
		name = namegen() 
		bday = bdaygen(random.randint(1, 6))
		phone = phonegen(random.randint(1, 7))
		ssn = ssngen(random.randint(1, 3))
		dl = dlgen()
		cit = citgen()
		rou = rougen()
		ban = bangen()
		cc = ccgen(random.randint(1, 6))
		plain = name[0] + delim + name[1] + delim + bday + delim + phone + delim + ssn + delim + dl + delim + cit + delim + rou + delim + ban + delim + cc
		ofile.write(plain+"\n")
		cipher = ""
		decrypt = ""
		for i in plain:
			cipher = cipher + chr(ord(i)-4)
		print cipher

	
def decrypt(args):
	encrypted_file = ""
	try:
		encrypted_file = open(args.file)
	except:
		print "Error opening file! Exiting\n"

	for i in encrypted_file:
		decrypt = ""
		for j in i:
			decrypt = decrypt + chr(ord(j)+4)
		print decrypt

def main():

	#Read the command line arguments
	parser = argparse.ArgumentParser(description='Fake Sensitive File Generator by Th3R3g3nt', formatter_class=RawTextHelpFormatter)
	parser.add_argument('-d','--difficulty', nargs="+", type=str, default="easy", help='Difficulty to detect for a DLP solution. Possible values are:\n Easy (consisten formatting, CSV, one record per line, includes header info)\n Normal (random formatting, CSV, one record per line)\n Hard (random formatting, random delimiter, no new line)\n Obfuscated (Medium + Ceaser cipher for easy decode and readability)\n\n')
	parser.add_argument('-n','--number', nargs="+", type=int, default=10, help="The number of records should be created")
	parser.add_argument('-f','--file', type=str, help="Obfuscated file to demangle")

	args = parser.parse_args()

	if len(sys.argv) < 2:
		print parser.print_help()
		exit()

	if args.file is not None:
		decrypt(args)
		exit()

	if type(args.number) == int:
		args.number = [10]
	

	if args.difficulty[0] == "Easy" or args.difficulty[0] == "easy":
		easy(args)
		exit()

	if args.difficulty[0] == "Medium" or args.difficulty[0] == "medium":
		medium(args)
		exit()

	if args.difficulty[0] == "Hard" or args.difficulty[0] == "hard":
		hard(args)
		exit()

	if args.difficulty[0] == "Obfuscated" or args.difficulty[0] == "obfuscated":
		obfuscated(args)
		exit()

	print "Invalid difficulty selected. \nExiting\n"
	exit()	

if __name__ == "__main__":
	main()