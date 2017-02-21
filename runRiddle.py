def riddle(word, infile=False, displayFalse=False):
	#Local constants
	if os.path.exists(infile):
		# if a file location is given, convert that file to TLIST
		# any string will be accepted here, but may not work
		TUBELIST = []

		# open file for reading
		f = open(infile, 'r')

		# loop over file, append each line (minus \n to list)
		for line in f:
			TUBELIST.append(line.rstrip('\n'))

		# clean up, close file
		f.close()
	
	else:
		# if no infile list is given, TLIST is the default
		TUBELIST = ['Acton Town', 'Aldgate East', 'Aldgate', 'Alperton', 'Amersham', 
			'Angel', 'Archway', 'Arnos Grove', 'Arsenal', 'Baker Street', 
			'Balham', 'Bank', 'Barbican', 'Barking', 'Barkingside', 
			'Barons Court', 'Bayswater', 'Becontree', 'Belsize Park', 
			'Bermondsey', 'Bethnal Green', 'Blackfriars', 'Blackhorse Road', 
			'Bond Street', 'Borough', 'Boston Manor', 'Bounds Green', 
			'Bow Road', 'Brent Cross', 'Brixton', 'Bromley-by-Bow', 
			'Buckhurst Hill', 'Burnt Oak', 'Caledonian Road', 'Camden Town',
			'Canada Water', 'Canary Wharf', 'Canning Town', 'Cannon Street', 
			'Canons Park', 'Chalfont & Latimer', 'Chalk Farm', 'Chancery Lane', 
			'Charing Cross', 'Chesham', 'Chigwell', 'Chiswick Park', 
			'Chorleywood', 'Clapham Common', 'Clapham North', 'Clapham South', 
			'Cockfosters', 'Colindale', 'Colliers Wood', 'Covent Garden', 
			'Croxley', 'Dagenham East', 'Dagenham Heathway', 'Debden', 
			'Dollis Hill', 'Ealing Broadway', 'Ealing Common', "Earl's Court", 
			'East Acton', 'East Finchley', 'East Ham', 'East Putney', 
			'Eastcote', 'Edgware Road', 'Edgware', 'Elephant & Castle', 
			'Elm Park', 'Embankment', 'Epping', 'Euston Square', 'Euston', 
			'Fairlop', 'Farringdon', 'Finchley Central', 'Finchley Road', 
			'Finsbury Park', 'Fulham Broadway', 'Gants Hill', 'Gloucester Road', 
			'Golders Green', 'Goldhawk Road', 'Goodge Street', 'Grange Hill', 
			'Great Portland Street', 'Green Park', 'Greenford', 'Gunnersbury', 
			'Hainault', 'Hammersmith', 'Hampstead', 'Hanger Lane', 'Harlesden', 
			'Harrow & Wealdstone', 'Harrow-on-the-Hill', 'Hatton Cross', 
			'Heathrow T123', 'Heathrow T4', 'Heathrow T5', 'Hendon Central', 
			'High Barnet', 'High Street Kensington', 'Highbury & Islington', 
			'Highgate', 'Hillingdon', 'Holborn', 'Holland Park', 'Holloway Road', 
			'Hornchurch', 'Hounslow Central', 'Hounslow East', 'Hounslow West', 
			'Hyde Park Corner', 'Ickenham', 'Kennington', 'Kensal Green', 
			'Kensington (Olympia)', 'Kentish Town', 'Kenton', 'Kew Gardens', 
			'Kilburn Park', 'Kilburn', "King's Cross/St Pancras", 'Kingsbury', 
			'Knightsbridge', 'Ladbroke Grove', 'Lambeth North', 
			'Lancaster Gate', 'Latimer Road', 'Leicester Square', 'Leyton', 
			'Leytonstone', 'Liverpool Street', 'London Bridge', 'Loughton', 
			'Maida Vale', 'Manor House', 'Mansion House', 'Marble Arch', 
			'Marylebone', 'Mile End', 'Mill Hill East', 'Monument', 'Moor Park', 
			'Moorgate', 'Morden', 'Mornington Crescent', 'Neasden', 
			'New Cross Gate', 'New Cross', 'Newbury Park', 'North Acton', 
			'North Ealing', 'North Greenwich', 'North Harrow', 'North Wembley', 
			'Northfields', 'Northolt', 'Northwick Park', 'Northwood Hills', 
			'Northwood', 'Notting Hill Gate', 'Oakwood', 'Old Street', 
			'Osterley', 'Oval', 'Oxford Circus', 'Paddington', 'Park Royal', 
			'Parsons Green', 'Perivale', 'Piccadilly Circus', 'Pimlico', 
			'Pinner', 'Plaistow', 'Preston Road', 'Putney Bridge', 
			"Queen's Park", 'Queensbury', 'Queensway', 'Ravenscourt Park', 
			'Rayners Lane', 'Redbridge', "Regent's Park", 'Richmond', 
			'Rickmansworth', 'Roding Valley', 'Rotherhithe', 'Royal Oak', 
			'Ruislip Gardens', 'Ruislip Manor', 'Ruislip', 'Russell Square', 
			'Seven Sisters', 'Shadwell', "Shepherd's Bush", 
			"Shepherd's Bush Market", 'Sloane Square', 'Snaresbrook', 
			'South Ealing', 'South Harrow', 'South Kensington', 'South Kenton', 
			'South Ruislip', 'South Wimbledon', 'South Woodford', 
			'Southfields', 'Southgate', 'Southwark', "St James's Park", 
			"St John's Wood", "St Paul's", 'Stamford Brook', 'Stanmore', 
			'Stepney Green', 'Stockwell', 'Stonebridge Park', 'Stratford', 
			'Sudbury Hill', 'Sudbury Town', 'Surrey Quays', 'Swiss Cottage', 
			'Temple', 'Theydon Bois', 'Tooting Bec', 'Tooting Broadway', 
			'Tottenham Court Road', 'Tottenham Hale', 'Totteridge & Whetstone', 
			'Tower Hill', 'Tufnell Park', 'Turnham Green', 'Turnpike Lane', 
			'Upminster Bridge', 'Upminster', 'Upney', 'Upton Park', 'Uxbridge', 
			'Vauxhall', 'Victoria', 'Walthamstow Central', 'Wanstead', 
			'Wapping', 'Warren Street', 'Warwick Avenue', 'Waterloo', 
			'Watford', 'Wembley Central', 'Wembley Park', 'West Acton', 
			'West Brompton', 'West Finchley', 'West Ham', 'West Hampstead', 
			'West Harrow', 'West Kensington', 'West Ruislip', 
			'Westbourne Park', 'Westminster', 'White City', 'Whitechapel', 
			'Willesden Green', 'Willesden Junction', 'Wimbledon Park', 
			'Wimbledon', 'Wood Green', 'Wood Lane', 'Woodford', 'Woodside Park']
	falseList = []

	for station in TUBELIST:
		for letter in word.lower(): #i = letter within word
			if letter in station.lower(): #if any of given letters are in name, add to false
				falseList.append(station) #append station keeping cases
				
	#Determine trueList, remove all false answers from fullList
	# breaks with duplicates?
	trueList = set(TUBELIST) - set(falseList)
	trueList = list(trueList)

	if displayFalse.upper() == "Y":
		print("False: ")
		print(falseList)
	print("True: ")
	print(trueList)
