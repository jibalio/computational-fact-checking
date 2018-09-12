bestMovies = '''1927-28	Seventh Heaven	Frank Borzage
1927-28	Two Arabian Knights	Lewis Milestone
1928-29	The Divine Lady	Frank Lloyd
1934	It Happened One Night	Frank Capra
1935	The Informer	John Ford
1937	The Awful Truth	Leo McCarey
1939	Gone with the Wind	Victor Fleming
1942	Mrs Miniver	William Wyler
1943	Casablanca	Michael Curtiz
1945	The Lost Weekend	Billy Wilder
1948	The Treasure of the Sierra Madre	John Huston
1949	A Letter to Three Wives	Joseph L. Mankiewicz
1951	A Place in the Sun	George Stevens
1953	From Here to Eternity	Fred Zinnemann
1954	On the Waterfront	Elia Kazan
1955	Marty	Delbert Mann
1957	The Bridge on the River Kwai	David Lean
1958	Gigi	Vincente Minnelli
1964	My Fair Lady	George Cukor
1967	The Graduate	Mike Nichols
1968	Oliver	Carol Reed
1969	Midnight Cowboy	John Schlesinger
1970	Patton	Franklin J. Schaffner
1971	The French Connection	William Friedkin
1973	The Sting	George Roy Hill
1974	The Godfather Part II	Francis Ford Coppola
1976	Rocky	John G. Avildsen
1977	Annie Hall	Woody Allen
1978	The Deer Hunter	Michael Cimino
1979	Kramer vs Kramer	Robert Benton
1980	Ordinary People	Robert Redford
1981	Reds	Warren Beatty
1982	Gandhi	Richard Attenborough
1983	Terms of Endearment	James L. Brooks
1984	Amadeus	Miloš Forman
1985	Out of Africa	Sydney Pollack
1986	Platoon	Oliver Stone
1987	The Last Emperor	Bernardo Bertolucci
1988	Rain Man	Barry Levinson
1990	Dances with Wolves	Kevin Costner
1991	The Silence of the Lambs	Jonathan Demme
1992	Unforgiven	Clint Eastwood
1994	Forrest Gump	Robert Zemeckis
1995	Braveheart	Mel Gibson
1996	The English Patient	Anthony Minghella
1997	Titanic	James Cameron
1998	Saving Private Ryan	Steven Spielberg
1999	American Beauty	Sam Mendes
2000	Traffic	Steven Soderbergh
2001	A Beautiful Mind	Ron Howard
2002	The Pianist	Roman Polanski
2003	The Lord of the Rings The Return of the King	Peter Jackson
2005	Brokeback Mountain	Ang Lee
2006	The Departed	Martin Scorsese
2007	No Country for Old Men	Joel and Ethan Coen
2008	Slumdog Millionaire	Danny Boyle
2009	The Hurt Locker	Kathryn Bigelow
2011	The Artist	Michel Hazanavicius
2013	Gravity	Alfonso Cuarón
'''

def filterMovies(bestMovies):
    filteredMovies = []
    data = [line.split('\t') for line in bestMovies.splitlines()]
    for item in data:
        filteredMovies.append(item[1])
    file = open("t4_x_movie.txt", "a")
    file.write('\n'.join(filteredMovies))

def filterDirectors(bestMovies):
    filteredDirectors = []
    data = [line.split('\t') for line in bestMovies.splitlines()]
    for item in data:
        filteredDirectors.append(item[2])
    file = open("t4_y_director.txt", "a")
    file.write('\n'.join(filteredDirectors))

filterDirectors(bestMovies)
filterMovies(bestMovies)
