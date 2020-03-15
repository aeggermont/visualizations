"""
Cleaning and consolidation data script
"""

import re
import csv
import sys

# Historial Athletes data sets
historical_athletes_data     = "source-athlete_events-tab.txt"

# Country code data sets
country_codes_iso_data            = "source-country_codes_iso-tab.txt"
historical_country_codes_iso_data = "source-country_codes_iso-historical-tab.txt"

# Population datasets
population_by_country_data         = "source-population_by_country.txt"

# Place holders
country_names_collection = {}
athletes_historical_data_compiled = {}

"""
Generating GDP Historical Country GDP
"""
def gdp_historical_country_gdp():

    print ("Getting historical country gdp")
    index = 0

    columns = ['country_name', 'country_code', 'indicator_name', 'indicator_code', '1960', '1961', '1962', '1963',
               '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976',
               '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
               '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
               '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
               '2016', '2017', '2018', '2019']

    dataIn =  open("source-gdp-by-country.txt")
    dataOut = open('cleaned-source-gdp-by-country.csv', 'wb')

    writer = csv.DictWriter(dataOut, fieldnames=columns)
    writer.writeheader()


    for countryRecord in dataIn:
        if index < 1:
            index += 1
            continue

        index += 1
        fields = countryRecord.replace('"', '').replace('\n', '').split('\t');
        #fields = countryRecord.split('\t')

        try:
             writer.writerow({'country_name': country_names_collection[fields[1]],
                             'country_code': fields[1],
                             'indicator_name': fields[2] ,
                             'indicator_code': fields[3],
                             '1960': fields[4] ,
                             '1961': fields[5],
                             '1962': fields[6],
                             '1963': fields[7],
                             '1964': fields[8],
                             '1965': fields[9],
                             '1966': fields[10],
                             '1967': fields[11],
                             '1968': fields[12],
                             '1969': fields[13],
                             '1970': fields[14],
                             '1971': fields[15],
                             '1972': fields[16],
                             '1973': fields[17],
                             '1974': fields[18],
                             '1975': fields[19],
                             '1976': fields[20],
                             '1977': fields[21],
                             '1978': fields[22],
                             '1979': fields[23],
                             '1980': fields[24],
                             '1981': fields[25],
                             '1982': fields[26],
                             '1983': fields[27],
                             '1984': fields[28],
                             '1985': fields[29],
                             '1986': fields[30],
                             '1987': fields[31],
                             '1988': fields[32],
                             '1989': fields[33],
                             '1990': fields[34],
                             '1991': fields[35],
                             '1992': fields[36],
                             '1993': fields[37],
                             '1994': fields[38],
                             '1995': fields[39],
                             '1996': fields[40],
                             '1997': fields[41],
                             '1998': fields[42],
                             '1999': fields[43],
                             '2000': fields[44],
                             '2001': fields[45],
                             '2002': fields[46],
                             '2003': fields[47],
                             '2004': fields[48],
                             '2005': fields[49],
                             '2006': fields[50],
                             '2007': fields[51],
                             '2008': fields[52],
                             '2009': fields[53],
                             '2010': fields[54],
                             '2011': fields[55],
                             '2012': fields[56],
                             '2013': fields[57],
                             '2014': fields[58],
                             '2015': fields[59],
                             '2016': fields[60],
                             '2017': fields[61],
                             '2018': fields[62],
                             '2019': fields[63]})
        except:
            print ("Missing country name: %s: %s " % (fields[0], fields[1]))



def get_historical_country_population(year=1990):

    print ("Getting population for year: %s" % year)

    dataIn = open(population_by_country_data)
    dataOut =  open('cleaned-population_by_country_data.csv', 'wb')
    index = 0

    columns = ['country_name', 'country_code', 'indicator_name', 'indicator_code', '1960', '1961', '1962', '1963',
               '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976',
               '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
               '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
               '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
               '2016', '2017', '2018', '2019']

    writer = csv.DictWriter(dataOut, fieldnames=columns)
    writer.writeheader()

    for countryRecord in dataIn:

        if index < 1:
            index += 1
            continue

        index += 1
        fields = countryRecord.split('\t')

        try:
            writer.writerow({'country_name': country_names_collection[fields[1]],
                            'country_code': fields[1],
                            'indicator_name': fields[2] ,
                            'indicator_code': fields[3],
                            '1960': fields[4] ,
                            '1961': fields[5],
                            '1962': fields[6],
                            '1963': fields[7],
                            '1964': fields[8],
                            '1965': fields[9],
                            '1966': fields[10],
                            '1967': fields[11],
                            '1968': fields[12],
                            '1969': fields[13],
                            '1970': fields[14],
                            '1971': fields[15],
                            '1972': fields[16],
                            '1973': fields[17],
                            '1974': fields[18],
                            '1975': fields[19],
                            '1976': fields[20],
                            '1977': fields[21],
                            '1978': fields[22],
                            '1979': fields[23],
                            '1980': fields[24],
                            '1981': fields[25],
                            '1982': fields[26],
                            '1983': fields[27],
                            '1984': fields[28],
                            '1985': fields[29],
                            '1986': fields[30],
                            '1987': fields[31],
                            '1988': fields[32],
                            '1989': fields[33],
                            '1990': fields[34],
                            '1991': fields[35],
                            '1992': fields[36],
                            '1993': fields[37],
                            '1994': fields[38],
                            '1995': fields[39],
                            '1996': fields[40],
                            '1997': fields[41],
                            '1998': fields[42],
                            '1999': fields[43],
                            '2000': fields[44],
                            '2001': fields[45],
                            '2002': fields[46],
                            '2003': fields[47],
                            '2004': fields[48],
                            '2005': fields[49],
                            '2006': fields[50],
                            '2007': fields[51],
                            '2008': fields[52],
                            '2009': fields[53],
                            '2010': fields[54],
                            '2011': fields[55],
                            '2012': fields[56],
                            '2013': fields[57],
                            '2014': fields[58],
                            '2015': fields[59],
                            '2016': fields[60],
                            '2017': fields[61],
                            '2018': fields[62],
                            '2019': fields[63]})
        except:
            print ("Missing country name: %s: %s " % (fields[0], fields[1]))

        #country_code = re.sub("[^a-z0-9]+", "", countryRecord.split('\t')[1], flags=re.IGNORECASE)
        #print ("%s : (%s, %s)  " % (country_code, countryRecord.split('\t')[0],  countryRecord.split('\t')[21]))







def get_historical_and_current_country_codes():
    """
    Produces a list of current and historical 3 character country codes
    and corresponding names
    """
    myFile = open('cleaned-historical_and_current_country_codes.csv', 'wb')
    columns = ['country_code', 'country_name']
    writer = csv.DictWriter(myFile, fieldnames=columns)
    writer.writeheader()

    for country_code, country_name in country_names_collection.items():
        print (" %s, %s " % (country_code, country_name))

        writer.writerow({'country_code': country_code,
                         'country_name': country_name })


"""
Gets countries population by year           1             2             3              4     5 
"""
def get_country_population(country=None, year=None):

    year = int(year)-1956
    for record in open('cleaned-population_by_country_data.csv', 'r').readlines():
        countrStats =  record.split(',')
        if ( country == countrStats[0]):
            #print(">>> STATS <<<")
            #print(countrStats[0])
            #print(countrStats[year])
            return countrStats[year]

"""
Gets medal counts per country, number of athletes and population by year
"""
def get_historical_athletes_data(year=None):

    index = 0;
    #year = "1960"

    country_stats_per_year = {}

    for record in open('cleaned-historical_athletes_dataset.csv', 'r').readlines():
        event  = record.replace('"', '').replace('\n', '').split(',')
        if (len(event) > 1):
            if (str(event[9]) == str(year)):

                if event[7] in country_stats_per_year:

                    # Get athletes
                    current_athletes = country_stats_per_year[event[7]]['athletes']
                    current_athletes.append(event[0])

                    # Get medal counts
                    print("Medal: %s " % (event[14]))

                    bronce_medals = country_stats_per_year[event[7]]['bronce_medals']
                    silver_medals = country_stats_per_year[event[7]]['silver_medals']
                    gold_medals   = country_stats_per_year[event[7]]['gold_medals']
                    other_medals  = country_stats_per_year[event[7]]['other_medals']

                    if event[14] == "Bronze":
                        bronce_medals += 1
                    elif event[14] == "Gold":
                        gold_medals += 1
                    elif event[14] == "Silver":
                        silver_medals += 1
                    elif event[14] == "NA":
                        pass
                    else:
                        other_medals += 1

                    totalMedalCount = bronce_medals + gold_medals + silver_medals + other_medals

                    country_stats_per_year[event[7]] = { 'athletes' : current_athletes,
                                                         'bronce_medals' : bronce_medals,
                                                         'silver_medals': gold_medals,
                                                         'gold_medals': silver_medals,
                                                         'other_medals': other_medals,
                                                         'totalMedalCount' : totalMedalCount }
                else:
                    athletes = []
                    bronce_medals = 0
                    silver_medals = 0
                    gold_medals   = 0
                    other_medals  = 0

                    athletes.append(event[0])

                    print("Medal: %s " % (event[14]))

                    if event[14] == "Bronze":
                        bronce_medals = 1
                    elif  event[14] == "Gold":
                        gold_medals = 1
                    elif event[14] == "Silver":
                        silver_medals = 1
                    elif event[14] == "NA":
                        pass
                    else:
                        other_medals = 1

                    totalMedalCount = bronce_medals + gold_medals + silver_medals + other_medals


                    country_stats_per_year[event[7]] = {'athletes': athletes,
                                                        'bronce_medals': bronce_medals,
                                                        'silver_medals': gold_medals,
                                                        'gold_medals': silver_medals,
                                                        'other_medals': other_medals,
                                                        'totalMedalCount' : totalMedalCount}
                index += 1


    # Create CSV file

    fileOut  = open('olympic-data-1998.csv', 'wb')
    columns = ['name','GDP', 'MedalCount', 'AthletesCount', "Population"]
    writer = csv.DictWriter(fileOut, fieldnames=columns)
    writer.writeheader()

    for country in country_stats_per_year.items():

        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print (country[0])
        population = get_country_population(country[0], year)
        #print (set(country[1]['athletes']))
        print ("Num of Athletes: %s " % len(set(country[1]['athletes'])))
        print ("Bronce Medals: %s " % country[1]['bronce_medals'])
        print ("Silver Medals: %s " % country[1]['silver_medals'])
        print ("Gold Medals: %s " % country[1]['gold_medals'])
        print ("Other Medals: %s " % country[1]['other_medals'])
        print ("Total Medal Count: %s " % country[1]['totalMedalCount'])
        print (" Population: %s " % population )

        writer.writerow(
                        {
                         'name'          : country[0],
                         'GDP'           : 0,
                         'MedalCount'    : country[1]['totalMedalCount'],
                         'AthletesCount' : len(set(country[1]['athletes'])),
                         'Population'    : population,
                         })

def clean_historical_athletes_data():
    """
    Produces historical lust of athlete events in alympics since 1960
    """

    myFile = open('cleaned-historical_athletes_dataset.csv', 'wb')

    firstLine = False
    index = 0

    with myFile:
        myFields = ['name', 'sex', 'age', 'height', 'weight', 'team', 'country_code', 'country_name', 'games', 'year', 'season', 'city', 'sport', 'event', 'medal']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        for record in open("source-historical-olympics-athletes-tab.txt").readlines():
            #if index > 100:
            #    break
            index += 1
            (id, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, medal ) =  record.split('\t')

            medal = medal.replace('"', '').replace('\n', '')

            if not firstLine:
                firstLine = True
                continue

            country_code = re.sub("[^a-z0-9]+","", noc, flags=re.IGNORECASE)

            try:
                writer.writerow({'name': name ,
                                 'sex': sex,
                                 'age': age,
                                 'height': height,
                                 'weight': weight,
                                 'team': team,
                                 'country_code': country_code,
                                 'country_name': country_names_collection[country_code],
                                 'games': games,
                                 'year': year,
                                 'season': season,
                                 'city': city,
                                 'sport': sport,
                                 'event': event,
                                 'medal': medal })

            except:
                e = sys.exc_info()[0]
                print ("Error: %s" % e)
                print("===========================================")

                #" Missing country code: %s" % record.split('\t')[7])
                pass

def country_codes_iso():

    print ("*** Country codes ***")

    index = 0

    for country in open(country_codes_iso_data):

        country_code = re.sub("[^a-z0-9]+", "", country.split('\t')[1], flags=re.IGNORECASE)

        country_name = country.split('\t')[0].strip()
        country_names_collection[country_code] = country_name

        #if  country.split('\t')[1].strip() in country_names_collection.keys():
        #    print ("Country already in list: %s -> %s" % ( country_code, country_names_collection[country_code] ))

        index += 1

    print (" Total Count: %d" % index)


def historical_country_codes_iso():

    print("*** Historical Country Codes ***")

    for country in open(historical_country_codes_iso_data):

        try:
            country_code = re.sub("[^a-z0-9]+", "", country.split('\t')[1], flags=re.IGNORECASE)
            #country_code = country.strip().split('\t')[1].strip()
            country_name = country.strip().split('\t')[0].strip()
            country_names_collection[country_code] = country_name

            #if country.split('\t')[1].strip() in country_names_collection.keys():
            #    print("Country already in list: %s -> %s" % (country_code, country_names_collection[country_code]))

        except:
            pass


def generateHistoricalCountriesList():
    country_codes_iso()
    historical_country_codes_iso()



def getHistoricalDataByYear():

    for country_code, country_name in country_names_collection.items():
        print (" %s, %s " % (country_code, country_name))

def main():

    print ("*** Olympics Historical Data ***")
    country_codes_iso()
    gdp_historical_country_gdp()

    #clean_historical_athletes_data()
    #generateHistoricalCountriesList()
    #get_historical_athletes_data( 1998)


    #get_historical_athletes_data()
    #get_historical_athletes_data()
    #get_historical_and_current_country_codes()
    #get_historical_country_population()
    # get_historical_country_population(2019)





if __name__ == "__main__":

    main()