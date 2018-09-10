#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO: CHECK TRUTH VALUES NA. COMPARE REGULAR BL METHOD, VS TFIDF/COSSIM, just normalize the values find the sweet spot. regularize cosine sim ksi duol lng difference. 0.1 and 0.3 must make difference. raise to ^-1/2 lng ok na.

"""
Truth.py (Alfafara, Ibalio)
This is the core of the project. This takes in a csv file of paths, and converts each path into two
truth values (metric and ultrametric closure). The entities traversed by the paths will be saved into
a sqlite3 database, to minimize the number of API calls.
"""

from wikipedia import WikipediaPage, page
from scrapers.request import get_response, get_path
from scrapers.wiki_datahandler import DataHandler
from scrapers.logger import log, errorlog
import time
import math
import urllib
import wikipedia
from PathFinder import retrieve_path
from nlp import LemTokens, LemNormalize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

TOKEN = ""
dh = DataHandler('wiki.sqlite3')

class Page ():
    backlinkcount = None
    pagecontent = None
    pageid = None
    """
    Calls constructor of WikipediaPage. No extra overhead since content is lazy-loaded.
    View source code of WikipediaPage:
    https://github.com/goldsmith/Wikipedia/blob/master/wikipedia/wikipedia.py
    """
    def __init__(self, title=None, pageid=None, redirect=True, preload=False, original_title='', backlinksonly = False):
        start_time = time.time()
        log("Truth.page: Creating page object for {}".format(title))
        # Try to get the data from the database first.
        # If record does not exist, value will be None.
        # If none, then run the WikipediaPage constructor and save the data.
        page_db_rows = dh.get_page(title)

        if not page_db_rows:    # if the page does not exist in the database
            log("Truth.page: No existing data found for {} in the database. Retrieving from API.".format(title))
            d = page(title=title, pageid=pageid, auto_suggest=True, redirect=True, preload=False)   # load a WikipediaPage object and just assign its attributes to self. (hax)
            self.title = title
            self.pageid = d.pageid
            self.backlinkcount = self.api_retrievebacklinkcount()   # retrieve backlinks using dispenser's API
            if not backlinksonly:   # if user wants all content to be loaded (not backlinks only)
                self.pagecontent = d.content    # retrieve from API (this uses lazy loading)
            else:
                self.pagecontent=None   # do not retrieve data
            self.remember() # save the data to the database

        else:   #if the data doesnt EXISTS in the database
            log("Truth.page: Data for {} found in database. Retrieving from database.".format(title))
            self.title = page_db_rows[0][0]
            if not backlinksonly:   # if user wants all the data then,
                if not page_db_rows[0][1]:  # if page is present, but content is NULL (e.g. page was previously loaded but backlinksonly=True)
                    log("Retrieving Content (Page is in DB, but content is not loaded).")
                    d = page(title=title, pageid=pageid, auto_suggest=True, redirect=True, preload=False)   # load a wikipage object and assign its atrributes to self
                    self.pageid = d.pageid
                    self.pagecontent = d.content
                    self.update()   # remember the downloaded content in the database
                else:   # else if content is present then just simply set the content row to self.pagecontent.
                    self.pagecontent = page_db_rows[0][1]   
            else:
                self.pagecontent = None # if user wants backlinks only then set pagecontent to NULL.
            self.backlinkcount = page_db_rows[0][2] # load backlink count from db
        log("Truth.page: Successfully created "+repr(self) + ", finished {:.5f}s".format(time.time() - start_time))

    def api_retrievebacklinkcount(self):
        # API by dispenser
        requrl = "https://dispenser.info.tm/~dispenser/cgi-bin/backlinkscount.py?title={}".format(
            urllib.parse.quote(self.title)     # quote the url to replace special characters (e.g. unicode) to url safe chars
        )
        return float(get_response(requrl))

    def remember(self):
        dh.insert_page(self)
        log("Truth.page: Remembered page {} in database.".format(self.title))

    def update(self):
        dh.update(self)
        log("Truth.page: Remembered page {} in database".format(self.title))

    def __repr__(self):
        if self.pagecontent:
            content = self.pagecontent[:45]
        else:
            content = "... Content was explicitly not loaded"
        return "["+self.title+"]: " +content+"... ["+repr(len(self.pagecontent or ''))+" characters, "+repr(self.backlinkcount)+" backlinks]"

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

class Path:


    pathstring = ""
    nodes = []
    cosine_similarity = 0.00

    def __init__(self, source, dest, pathonly=False):
        
        page_db_rows = dh.get_path(source, dest)

        if not page_db_rows:    # query if it is not in database
            log(f"Querying '{source}' -> '{dest}' from API.")
            self.titles = [x.replace('_',' ') for x in get_path(source.strip(),dest.strip(), TOKEN)]

            # Catch the possible errors
            if len(self.titles) == 1:   # Error No. 1: Page doesn't exist.
                errorlog(self.titles[0])
                raise(Exception(self.titles[0]))
            elif len(self.titles) == 0: # Error No. 2: Access token is invalid.
                errorlog("invalid access token")
                raise(Exception("Invalid Access token"))

            
            self.pathstring = ">".join(self.titles)
            self.nodes = []

            log(f"Found nodes {self.titles}")
            self.source = self.titles[0]
            self.dest = self.titles[len(self.nodes)-1]
            self.remember()
        else:
            log("Truth.Path: Path Found in database. Loading from DB.")
            self.source = page_db_rows[0][0]
            self.dest = page_db_rows[0][1]
            self.pathstring = page_db_rows[0][2]
            self.cosine_similarity = page_db_rows[0][3]
            self.titles = self.pathstring.split('>')
        if not pathonly:
                for idx, x in enumerate(self.titles):
                    if idx == 0 or idx==len(self.titles)-1:
                        self.nodes.append(Page(x, backlinksonly=False))
                    else:
                        self.nodes.append(Page(x, backlinksonly=True))
        log(repr(self))


    def __repr__(self):
        a = []
        for x in self.titles:
            a.append(f"[{x}]")
        a  = " -> ".join(a)
        return f"<Path> {a}"
        

            
            # primitive implementation.
            # get count of next article title in the current article.
            
    
    def remember(self):
        dh.insert_path(self)
        log("Remembering path {} in database.".format(self.pathstring))
        pass







#----------------------------------------------------------
# TRUTH VALUE METHODS
#- --------------------------------------------------------
tfs = {}      
def get_truth_value(path_taken):
    #print(path_taken)
    # slice the path
    path = [Page(d) for d in path_taken.split('>')]
    source = path[0] # get the first element of the path
    dest = path[len(path)-1] # get the last element of the path
    #----------------------------------------------------------------------
    documents = [source.pagecontent, dest.pagecontent]
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    def cos_similarity(textlist):
        tfidf = TfidfVec.fit_transform(textlist)
        return (tfidf * tfidf.T).toarray()
    if path_taken not in tfs.keys():
        cos_sim = cos_similarity(documents)
        tfs[path_taken] = cos_sim
    else:
        cos_sim = tfs[path_taken]
    # ---------------------------------------------------------------------
    cos_sim = cos_sim[0][1]
    truthvalue = 1.00
    for x in path[1:]:
        #print(f"{x.backlinkcount}*{cos_sim}")
        truthvalue+=math.log(x.backlinkcount*cos_sim)
    # ---------------------------------------------------------------------
    truthvalue = 1/truthvalue
    truthvalue*=0.5
    truthvalue+=cos_sim*0.5
    return truthvalue

def get_truth_value_old(path_taken):
    # slice the path
    path = [Page(d) for d in path_taken.split('>')]
    source = path[0] # get the first element of the path
    dest = path[len(path)-1] # get the last element of the path
    truthvalue = 1.00
    for x in path[1:]:
        truthvalue+=math.log(x.backlinkcount)
    # ---------------------------------------------------------------------
    truthvalue = 1/truthvalue
    return truthvalue
    
def get_utfidf(path_taken):
    # slice the path
    path = [Page(d) for d in path_taken.split('>')]
    source = path[0] # get the first element of the path
    dest = path[len(path)-1] # get the last element of the path
    #----------------------------------------------------------------------
    documents = [source.pagecontent, dest.pagecontent]
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    def cos_similarity(textlist):
        tfidf = TfidfVec.fit_transform(textlist)
        return (tfidf * tfidf.T).toarray()
    if path_taken not in tfs.keys():
        cos_sim = cos_similarity(documents)
        tfs[path_taken] = cos_sim
    else:
        cos_sim = tfs[path_taken]
    # ---------------------------------------------------------------------
    cos_sim = cos_sim[0][1]
    truthvalue = 1.00
    bl = max([x.backlinkcount for x in path[1:]])
    truthvalue+=math.log(bl*cos_sim)
    # ---------------------------------------------------------------------
    truthvalue = 1/truthvalue
    truthvalue*=0.5
    truthvalue+=cos_sim*0.5
    return truthvalue















if __name__ == '__main__':

    TOKEN = "1535217730|c9905d277d1239eebdf7555f5af79cd1"
    a = Path('Japan', 'Tokyo', pathonly=True)
    print(a.nodes)

    """
    log("Truth.py started.")
    fa = open('nice.txt','w')
    ideologies = "1981 Irish hunger strike; 9/11 Truth movement; Abertzale; Abolished monarchy; African nationalism; African socialism; Afrikaner nationalism; Agorism; Agrarianism; Agrarian socialism; Ahlus Sunnah wal Jamaah (organisation); Albanians in the Republic of Macedonia; Alexander Lukashenko; Alsace; Alter-globalization; American nationalism; Anarchism; Anarchist communism; Anarcho-capitalism; Anarcho-syndicalism; Andalusian nationalism; Anglo-Irish Treaty; Anglophile; Animal rights; Animal welfare; Anti-Americanism; Anti-capitalism; Anti-Catholicism in the United Kingdom; Anti-clericalism; Anti-communism; Anti Communism; Anti-corporate activism; Anti-Corruption; Anti-Esotericism; Anti-fascism; Anti-Federalism; Antifeminism; Anti-globalization movement; Anti-imperialism; Anti-Islamism; Anti-Judaism; Anti-Leninism; Anti-LGBT; Anti-liberal; Antimilitarism; Anti-nationalism; Anti-Polish sentiment; Anti-Revisionism; Antisemitism; Anti-Sovietism; Anti-Stalinist left; Anti-statism; Anti-taxation; Anti-war movement; Antiziganism; Anti-Zionism; António Ramalho Eanes; Apartheid in South Africa; Aragon; Armenian nationalism; Assyrian nationalism; Austrofascism; Authoritarianism; Autonomism; Awoism; Azerbaijani nationalism; Ba’athism; Balanced budget; Baloch nationalism; Bangladeshi nationalism; Basque nationalism; Bavaria; Bavarian independence; Bavarian Regionalism; Beauty; Beijing; Belarus; Bengali nationalism; Berberism; Berber people; Beta Israel; Big tent; Black Consciousness Movement; Black nationalism; Black supremacy; Bolivarianism; Bolivarian Revolution; Bolivia; Bosniaks; Bosnianism; Brahmin; Breton nationalism; Breton people; British Empire; British Fascism; British nationalism; Buddhism; Buddhist socialism; Bulgaria; Burmese Way to Socialism; Business; Caliphate; Cambodia; Canadian nationalism; Canarian nationalism; Cantonalism; Capitalism; Carinthian Slovenes; Castilian nationalism; Castroism; Catalan nationalism; Catalan separatism; Catholic Church; Catholic social teaching; Centralisation; Central Powers; Centre-left; Centre-right; Centrism; Chaldean Christians; Cham issue; Cham people (Asia); Chardal; Chavismo; Chinese nationalism; Chinese reunification; Chinese socialism; Christian communism; Christian democracy; Christian ethics; Christian humanism; Christianity; Christian left; Christian right; Christian socialism; Citizenship; Civil and political rights; Civil liberties; Classical liberalism; Classical Marxism; Clerical fascism; Clericalism; Colonialism; Communism; Communist Party of China; Communitarianism; Community politics; Conflict management; Congress of Verona (1943); Conservatism; Conservatism in Australia; Conservatism in Canada; Conservatism in Germany; Conservatism in the United States; Conservative Democrat; Conservative liberalism; Constitutionalism; Constitutional monarchy; Consumerism; Consumer protection; Cooperative; Co-operative economics; Cooperative federalism; Copyright; Cornerstone Group; Cornish Assembly; Cornish Autonomy; Cornish nationalism; Corporatism; Corsican nationalism; Cosmopolitanism; Côte d’Ivoire; Council communism; Creationism; Criticism of Islam; Croatian nationalism; Croats of Boka Kotorska; Croats of Vojvodina; Cultural conservatism; Cultural liberalism; Danish Realm; Decentralization; Decolonization; Degar; Degrowth; Demarchy; Democracy; Democratic liberalism; Democratic security; Democratic socialism; Democratic Struggle; Democratization; Deng Xiaoping Theory; Departments of Bolivia; Developmentalism; Development criticism; Devizes; Devolution; Devolved English parliament; Dictatorship of the proletariat; Direct democracy; Direct rule; Disputed status of Gibraltar; Distributism; Doi Moi; Dominant minority; Dominionism; Drug policy reform; Druze; Early Malay nationalism; Eastern Orthodox Church; Ecology; Ecology movement; Economic liberalism; Economic nationalism; Economic rationalism; Eco-socialism; Ecosociality; E-democracy; Education; Egalitarianism; Egyptian nationalism; Éire Nua; Electoral reform; Electoral reform in New Zealand; Elitism; English independence; English nationalism; Environmentalism; Equal justice under law; Equal opportunity; Equal rights; Eritrea; Especifismo; Ethnic-minority; Ethnic nationalism; Ethnocentrism; Ethnopluralism; Eurasianism; Euro; Eurocommunism; European integration; European People’s Party; Euroscepticism; Expansionism; Experimental projects; Factions in the Democratic Party (United States); Fair trade; Falangism; Family values; Far-left politics; Faroe Islands; Far right in the United Kingdom; Far-right politics; Fascism; Fathers’ rights movement; Federalism; Federalism in China; Federalist; Federation; Feminism; Feudalism; Filipino nationalism; Finland; Fiscal conservatism; Fiscal federalism; Flemish Movement; Fourth International Posadist; Francisco de Sá Carneiro; Francoist Spain; Francophile; Francophone; Franjo Tu ̄ dman; Freedom of information; Freedom of speech; Free love; Free market; Free trade; French Community of Belgium; French First Republic; French nationalism; Friesland; Frivolous political party; Fujimorism; Fundamentalism; Gaels; Gag rule; Galicianism (Galicia); Galician nationalism; Gaullism; Georgism; Gerald Götting; German Emperor; German language; German nationalism; Good governance; Goulash Communism; Grassroots; Grassroots democracy; Greater Armenia (political concept); Greater Israel; Greater Somalia; Greek nationalism; Green anarchism; Green conservatism; Greenland; Green liberalism; Green libertarianism; Green party; Green politics; Gross national happiness; Guerrilla warfare; Guevarism; Gwynedd; Halakha; Haredi Judaism; Harm reduction; Hazara people; Hindutva; Ho Chi Minh Thought; Holism; Honduras; House of Grimaldi; Hoxhaism; Hugo Chávez; Humanism; Humanist Movement; Human rights; Hungarian nationalism; Hungarians in Romania; Hungarians in Slovakia; Husakism; Hutu Power; Idealism; Imperial Preference; Impossibilism; Independence; Independent (politician); Indian nationalism; Indigenism; Indigenous rights; Individualism; Industrialisation; Integral humanism; Integralism; Intellectual property; Internal resistance to South African apartheid; Internationalism; Internationalism (politics); International Socialist Tendency; Internet censorship; Iranian nationalism; Iranian reform movement; Iraqi nationalism; Iraqi Turkmens; Irish nationalism; Irish republicanism; Iron Guard; Islam; Islamic democracy; Islamic fundamentalism; Islamic republic; Islamism; Islamophobia; Isolationism; Israeli–Palestinian conflict; Istria; Italian nationalism; Italy–Malta relations; Ivoirité; Jadid; James Madison; Japanese militarism; Japanese nationalism; J. B. Danquah; Jeffersonian democracy; Juche; Justice; Justicialist Party; Kahanism; Katarismo; Kemalist ideology; Ketuanan Melayu; Keynesian economics; Kham; Khatim an-Nabuwwah; Khmer people; Kidderminster; Kirchnerism; Korean nationalism; Kuomintang; Kurdish nationalism; Kurdish people; Kwame Nkrumah; Kyrgyz nationalism; Laborer; Labor rights; Labor Zionism; Labour movement; Laïcité; Laissez-faire; Land of Israel; Latvia; Latvian people; Law and order (politics); Lebanese nationalism; Left centrism; Left communism; Left-libertarianism; Left–right politics; Left-wing nationalism; Left-wing politics; Legality of cannabis; Leninism; Liberal conservatism; Liberal democracy; Liberalism; Liberalism in Australia; Liberalism in Colombia; Liberalism in South Korea; Liberalism in the United States; Liberal movements within Islam; Liberal nationalism; Liberal socialism; Liberation theology; Liberism; Libertarian conservatism; Libertarian Democrat; Libertarianism; Libertarian Marxism; Libertarian socialism; Lieberman Plan; Lists of active separatist movements; Lithuania; Localism; Localism (politics); Luxemburgism; Macedonian nationalism; Malta–United Kingdom relations; Maltese; Maoism; Market liberalism; Market socialism; Martinique; Marxism; Marxism–Leninism; Masculism; Mass politics; Megali Idea; Metaxism; Microeconomic reform; Militant; Militarism; Millî Görü ̧s; Minarchism; Minority rights; Miraism; Mixed economy; Mizrahi Jews; Mobutism; Moderate; Moderate Islamism; Moderation; Modernization; Modern Orthodox Judaism; Monarchism; Monarchy; Monarchy of Australia; Monetary reform; Montenegrin nationalism; Morality; Moravism; Morocco; Movement for the unification of Romania and Moldova; Multiculturalism; Multiethnic society; Muslim; Nacionalismo (Argentine political movement); Naga Nationalism; Nasserism; National Bolshevism; National Catholicism; National communism; National conservatism; Nationalism; Nationalization; National liberalism; National Liberation (historical); National Reconciliation; National syndicalism; Nativism (politics); Natural Capitalism: Creating the Next Industrial Revolution; Nazism; Neocolonialism; Neoconservatism; Neoconservatism (disambiguation); Neo-fascism; Neoliberalism; Neo-Nazism; Netherlands; Network neutrality; Neutrality (international relations); Nevis; New Democrats; New Left; New Nationalism; New Right; None of the above; Non-interventionism; Nonpartisan; Nonsectarian; Nonviolence; Non-violent resistance; Non-voting; Nordic agrarian parties; Norse religion; Norwegian romantic nationalism; Objectivism (Ayn Rand); One country, two systems; One nation conservatism; Open government; Opposition (politics); Opposition to immigration; Oromo people; Pacifism; Pakistani nationalism; Paleoconservatism; Paleolibertarianism; Palestinian nationalism; Palestinian sovereignty; Pan-Africanism; Panama; Pan-Americanism; Pan-Arabism; Pañcas ̄ ila; Pancasila (politics); Pan-European identity; PanEuropean nationalism; Pan-Germanism; Pan-Iranism; Pan-Islamic awakening; Pan-Islamism; Pan-Latin Americanism; Pan-Slavism; Pan-Turkism; Paraguay; Parliamentary system; Participatory democracy; Participatory politics; Partition of Belgium; Pashtun people; Patent; Patriotism; Peace; Peace movement; Pensioner; Pensioners’ Party; People of Ethiopia; Peronism; Personalism; Peru; Peter Kropotkin; Pim Fortuyn; Pim Fortuyn List; Platformism; Pochvennichestvo; Poles in Lithuania; Political corruption; Political freedom; Political parties of minorities; Political positions of David Cameron; Political radicalism; Political satire; Politics of Israel; Popolarismo; Popular front; Popular Socialism; Populism; Portuguese nationalism; Portuguese people; Pragmatism; Presentation program; President of the United States; President of Ukraine; Privacy; Pro-Europeanism; Progressive Christianity; Progressive Democrats of America; Progressivism; Progressivism in the United States; Protectionism; Protest; Protestantism; Protest vote; Proto-fascism; Proxy voting; Publicly funded health care; Puerto Rican independence movement; Quebec sovereignty movement; Qutbism; Racialism; Radical; Radicalism (historical); Rakhine people; Rankovi ́cism; Redistribution of wealth; Reform; Reformism; Reform movement; Regional development; Regionalism (politics); Regions of Ethiopia; Reintegrationism; Religion; Religious denomination; Religious nationalism; Religious Zionism; Republicanism; Republicanism in Australia; Republicanism in New Zealand; Republicanism in the United Kingdom; Republicanism in the United States; Revisionism (Marxism); Revisionist Zionism; Revolutionary socialism; Rhodesia; Right-libertarianism; Rights; Right-wing politics; Right-wing populism; Royalist; Ruhollah Khomeini; Rule of law; Russia; Russian immigration to Israel in the 1990s; Russian nationalism; Russians in Estonia; Russians in Latvia; Russians in Lithuania; Russo-centrism; Russophilia; Sahrawi people; Salafi; Sami people; Sandinismo; Satire; Savoy; Scientific development concept; Scientific socialism; Scottish independence; Scottish Labour Party; Scottish national identity; Scottish nationalism; Secluarism; Secular humanism; Secularism; Secularism in Pakistan; Secularity; Self-determination; Senior citizen; Separatism; Sephardic Haredim; Serbia; Serbian–Montenegrin unionism; Serbian nationalism; Serbian progressivism; Serbs of Montenegro; Sex-positive movement; Shia Islam; Sindhi nationalism; Single-issue politics; Sinhalese Buddhist nationalism; Slavic nationalism; Slavonia; Slovaks; Slovenian nationalism; Small government; Social change; Social conservatism; Social Conservatism; Social conservatism in the United States; Social corporatism; Social Credit; Social democracy; Social ecology; Social humanism; Social Individualism; Socialism; Socialism and Islam; Socialism of the 21st century; Socialist economics; Socialist feminism; Social Justce; Social justice; Social liberalism; Social market economy; Social republicanism; Social sphere; Solidarism; Somalia; Songun; South Africa; South Sudan; Souverainism; Sovereignty; Spain; Spanish nationalism; Spiritualism; Spirituality; Sri Lankan Tamil nationalism; Stalinism; State Peace and Development Council; State Shinto; States’ rights; Statism; Statism in Sh ̄ owa Japan; Strasserism; Structuralism; Sudan; Šumadija; Sunni Islam; Sunshine Policy; Sustainable development; Sweden; Swedish-speaking Finns; Syncretic politics; Syndicalism; Syrian nationalism; Syrmia; Szeged Idea; Taiwanese nationalism; Taiwan independence; Taiwanization; Tamil nationalism; Technocracy; Temperance movement; Tertium quids; Thatcherism; Third camp; Third Position; Third Way; Third Way (centrism); Third Way (United Kingdom); Three Principles of the People; Three Represents; Tigray-Tigrinya people; Titoism; Torah; Trade union; Traditionalism; Traditionalist conservatism; Transcendental Meditation; Transnistria; Transparency (behavior); Treaty of Lisbon; Tribalism; Triple Entente; Tripuri nationalism; Trotskyism; Truth and reconciliation commission; Turkic nationalism; Turkish nationalism; Two-Nation Theory; Two-state-solution; Ujamaa; Ukrainian nationalism; Ulster loyalism; Ulster nationalism; Ultramontanism; Unification Church; Unilateral Declaration of Independence; Unionism in Ireland; Unionism in Scotland; Unionism in the United Kingdom; Union of European Federalists; Union State; Unitarisation; United Ireland; United States Congress; Urban design; Uribism; Uruguay; Uzbekistan; Valencian nationalism; Venetian nationalism; Venizelism; Vietnam; Vojvodina; Völkisch movement; Volksgemeinschaft; Voluntaryism; Walloon Movement; Warsaw; Wars of national liberation; Weapons Rights; Welfare; Welfare State; Welsh independence; Welsh nationalism; Wessex; Western conservatism; Western world; Whiggism; White nationalism; White separatism; White supremacy; Solidarity; Women’s rights; Workerism; Xenophobia; Yalkut Yosef; Youth rights; Zionism; Zulu people".split("; ")
    for idx, x in enumerate(ideologies):
        try:
            a = Page(x)
            fa.write(a.title+";"+repr(a.backlinkcount)+"\n")
            #fa.write("Error getting "+a.title)
        except wikipedia.exceptions.DisambiguationError:
            fa.write("DisambiguationError for " + x);
            log("DisambuiguationError for "+x+".Error is ignored.\n")
        except wikipedia.exceptions.PageError:
            fa.write("PageError for " + x);
            log("PageError for "+x+".Error is ignored.\n")
        except:
            fa.write("Generic error for " + x);
            log("Generic Error for "+x+".Error is ignored.\n")
    fa.close()
    """