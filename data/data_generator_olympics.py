import re
import csv
import sys
import decimal

# A dictionary storing data by country
dataCollection = {}
athletesByCountry = {}
numOfAthletesByCountry = {}

populationByCountry = {}
gdpByCountry = {}

countryByContinent = {}
"""
"americas"
"europe"
"asia"
"australia"
"africa"

"""

countryByContinent['Canada'] = "americas"
countryByContinent['Italy'] = "europe"
countryByContinent['East Germany'] = "europe"
countryByContinent['Mongolia'] = "asia"
countryByContinent['France'] = "europe"
countryByContinent['West Germany'] = "europe"
countryByContinent['Argentina'] = "americas"
countryByContinent['Bolivia'] = "americas"
countryByContinent['Norway'] = "europe"
countryByContinent['Australia'] = "australia"
countryByContinent['United States of America'] = "americas"
countryByContinent['China'] = "asia"
countryByContinent['Soviet Union'] = "asia"
countryByContinent['Netherlands'] = "europe"
countryByContinent['Poland'] = "europe"
countryByContinent['Finland'] = "europe"
countryByContinent['Sweden'] = "europe"
countryByContinent['Switzerland'] = "europe"
countryByContinent['New Zealand'] = "asia"
countryByContinent['Bulgaria'] = "europe"
countryByContinent['Romania'] = "europe"
countryByContinent['United Kingdom'] = "europe"
countryByContinent['Austria'] = "europe"
countryByContinent['Greece'] = "europe"
countryByContinent['Japan'] = "asia"
countryByContinent['Cyprus'] = "europe"
countryByContinent['Turkey'] = "europe"
countryByContinent['San Marino'] = "europe"
countryByContinent['Costa Rica'] = "americas"
countryByContinent['Iceland'] = "europe"
countryByContinent['Belgium'] = "europe"
countryByContinent['Lebanon'] = "asia"
countryByContinent['Chinise Taipei'] = "asia"
countryByContinent['Hungary'] = "europe"
countryByContinent['Morocco'] = "africa"
countryByContinent['Egypt'] = "africa"
countryByContinent['South Koreas'] = "asia"
countryByContinent['Andorra'] = "europe"
countryByContinent['Guatemala'] = "americas"
countryByContinent['Puerto Rico'] = "americas"
countryByContinent['Spain'] = "europe"
countryByContinent['Denmark'] = "europe"
countryByContinent['Monaco'] = "europe"
countryByContinent['Virgin Islands'] = "americas"
countryByContinent['Portugal'] = "europe"
countryByContinent['Mexico'] = "americas"
countryByContinent['Guam'] = "Oceania"
countryByContinent['India'] = "asia"
countryByContinent['Liechtenstein'] = "europe"
countryByContinent['Brazil'] = "americas"
countryByContinent['Lithuania'] = "europe"
countryByContinent['Algeria'] = "africa"
countryByContinent['Slovenia'] = "europe"
countryByContinent['Union of Soviet Socialist Republics'] =  "asia"
countryByContinent['Germany'] = "europe"
countryByContinent['Latvia'] = "europe"
countryByContinent['Croatia'] = "europe"
countryByContinent['North Korea'] =  "asia"
countryByContinent['Czech Republic'] = "europe"
countryByContinent['Georgia'] = "asia"
countryByContinent['Slovakia'] = "asia"
countryByContinent['Uzbekistan'] = "asia"
countryByContinent['Bosnia and Herzegovina'] = "europe"
countryByContinent['Armenia'] = "asia"
countryByContinent['Kazakhstan'] = "europe"
countryByContinent['Ukraine'] = "europe"
countryByContinent['Belarus'] = "europe"
countryByContinent['Russian Federation'] = "europe"
countryByContinent['Estonia'] = "europe"
countryByContinent['Kenya'] = "africa"
countryByContinent['Ireland'] = "europe"
countryByContinent['Israel'] = "asia"
countryByContinent['Venezuela'] = "americas"
countryByContinent['Macedonia'] = "europe"
countryByContinent['Moldova'] = "europe"
countryByContinent['Azerbaijan'] = "asia"
countryByContinent['Trinidad and Tobago'] = "americas"
countryByContinent['Chile'] = "americas"
countryByContinent['Kyrgyzstan'] = "asia"
countryByContinent['Jamaica'] = "americas"
countryByContinent['Tajikistan'] = "asia"
countryByContinent['South Africa'] = "africa"
countryByContinent['Pakistan'] = "asia"
countryByContinent['Peru'] = "americas"
countryByContinent['Colombia'] = "americas"
countryByContinent['Iran'] = "asia"
countryByContinent['Togo'] = "africa"
countryByContinent['Tonga'] = "australia"
countryByContinent['British Virgin Islands'] = "americas"
countryByContinent['Serbia'] = "europe"
countryByContinent['Dominica'] = "americas"
countryByContinent['Montenegro'] = "europe"
countryByContinent['Afghanistan'] = "asia"
countryByContinent['Madagascar'] = "asia"
countryByContinent['Kuwait'] = "asia"
countryByContinent['Nepal'] = "asia"
countryByContinent['Luxembourg'] = "europe"
countryByContinent['Republic of Congo'] = "africa"
countryByContinent['Nigeria'] = "africa"
countryByContinent['Ecuador'] = "americas"
countryByContinent['Benin'] = "africa"
countryByContinent['Cuba'] = "americas"
countryByContinent['Cameroon'] = "africa"
countryByContinent['Zambia'] = "africa"
countryByContinent['Senegal'] = "africa"
countryByContinent['Zimbabwe'] = "africa"
countryByContinent['Dominican Republic'] = "americas"
countryByContinent['Iraq'] = "asia"
countryByContinent['Sierra Leone'] = "africa"
countryByContinent['Uganda'] = "africa"
countryByContinent['Malta'] = "europe"
countryByContinent['Guyana'] = "americas"
countryByContinent['Mali'] = "africa"
countryByContinent['Syria'] = "asia"
countryByContinent['Seychelles'] = "africa"
countryByContinent['Angola'] = "africa"
countryByContinent['Sri Lanka'] = "asia"
countryByContinent['Nicaragua'] = "americas"
countryByContinent['Botswana'] = "africa"
countryByContinent['The Gambia'] = "africa"
countryByContinent['Swaziland'] = "africa"
countryByContinent['Ghana'] = "africa"
countryByContinent['Saudi Arabia'] = "asia"
countryByContinent['Oman'] = "asia"
countryByContinent['Samoa'] = "australia"
countryByContinent['United Arab Emirates'] = "asia"
countryByContinent['Solomon Islands'] = "australia"
countryByContinent['Rwanda'] = "africa"
countryByContinent['Somalia'] = "africa"
countryByContinent["Cote d'Ivoire"] = "africa"
countryByContinent['Singapore'] = "asia"
countryByContinent['Indonesia'] = "asia"
countryByContinent["Central African Republic"] = "africa"
countryByContinent["Mauritius"] = "africa"
countryByContinent['Brunei Darussalam'] = "asia"
countryByContinent["Niger"] = "africa"
countryByContinent['Malasya'] = "asia"
countryByContinent['Panama'] = "americas"
countryByContinent['Bahamas'] = "americas"
countryByContinent['Bangladesh'] = "asia"
countryByContinent['El Salvador'] = "americas"
countryByContinent['Thailand'] = "asia"
countryByContinent['Hong Kong'] = "asia"
countryByContinent['Philippines'] = "asia"
countryByContinent['Grenada'] = "americas"
countryByContinent['Belize'] = "americas"
countryByContinent['Chad'] = "africa"
countryByContinent['Uruguay'] = "americas"
countryByContinent['Equatorial Guinea'] = "africa"
countryByContinent['Tunisia'] = "africa"
countryByContinent['Bermuda'] = "americas"
countryByContinent['Barbados'] = "americas"
countryByContinent['Qatar'] = "asia"
countryByContinent['Bhutan'] = "asia"
countryByContinent['Sudan'] = "africa"
countryByContinent['Suriname'] = "americas"
countryByContinent['Netherlands Antilles'] = "americas"
countryByContinent['Papua New Guinea'] = "australia"
countryByContinent['Malawi'] = "africa"
countryByContinent['Jordan'] = "asia"
countryByContinent['Mauritania'] = "africa"
countryByContinent['Honduras'] = "americas"
countryByContinent['Congo'] = "africa"
countryByContinent['Paraguay'] = "americas"
countryByContinent['Fiji'] = "australia"
countryByContinent['Guinea'] = "africa"
countryByContinent['Tanzania'] = "africa"
countryByContinent['Gabon'] = "africa"
countryByContinent['Saint Vincent and the Grenadines'] = "americas"
countryByContinent['Vanuatu'] = "australia"
countryByContinent['Vietnam'] = "asia"
countryByContinent['Haiti'] = "americas"
countryByContinent['Maldives'] = "asia"
countryByContinent['Ethiopia'] = "africa"
countryByContinent['Aruba'] = "americas"
countryByContinent['Yemen'] = "asia"
countryByContinent['Albania'] = "europe"
countryByContinent['Libya'] = "africa"
countryByContinent['Namibia'] = "africa"
countryByContinent['Turkmenistan'] = "asia"
countryByContinent['Lao PDR'] = "asia"
countryByContinent['Cape Verde'] = "africa"
countryByContinent['Saint Lucia'] = "americas"
countryByContinent['Saint Kitts and Nevis'] = "americas"
countryByContinent['Brunei'] = "asia"
countryByContinent['Guinea Bissau'] = "africa"
countryByContinent['Comoros'] = "africa"
countryByContinent['Liberia'] = "africa"
countryByContinent['Eritrea'] = "africa"
countryByContinent['Mozambique'] = "africa"
countryByContinent['Palau'] = "australia"
countryByContinent['Myanmar'] = "asia"
countryByContinent['Sao Tome and Principe'] = "africa"
countryByContinent['Micronesia'] = "australia"
countryByContinent['Timor-Leste'] = "asia"
countryByContinent['Nauru'] = "australia"
countryByContinent['American Samoa'] = "australia"
countryByContinent['Tuvalu'] = "australia"
countryByContinent['Marshall Islands'] = "australia"
countryByContinent['Cambodia'] = "asia"
countryByContinent['Cook Islands'] = "australia"
countryByContinent['Kiribati'] = "australia"
countryByContinent['Burundi'] = "africa"
countryByContinent['Djibouti'] = "africa"
countryByContinent['Cayman Islands'] = "americas"



def parce_data(search_year, search_seasson):

  dataIn = open("cleaned_athletes_pop_gdp-merged.txt")
  firstLine = True

  for record in dataIn.readlines():
    if firstLine:
      firstLine = False
      continue

    gold = 0
    silver = 0
    bronze = 0
    gdp = 0
    population = 0

    try:
      (name,
       sex,
       age,
       height,
       weight,
       team,
       country_code,
       country_name,
       games,
       year,
       season,
       city,
       sport,
       event,
       medal,
       population,
       gdp ) = record.replace('"', '').replace('\n', '').split('\t')

      """
      print (" >>>> Just Finished split")
      print (name,
       sex,
       age,
       height,
       weight,
       team,
       country_code,
       country_name,
       games,
       year,
       season,
       city,
       sport,
       event,
       medal,
       population,
       gdp )
       """

      if year == search_year and season == search_seasson:

        #countryByContinent[country_name] = 'tbd';

        if medal == "Gold":
          gold = 1
        elif medal == "Silver":
          silver = 1
        elif medal == "Bronze":
          bronze = 1

        # Tracks athletes by country
        if name not in athletesByCountry.keys():
          athletesByCountry[name] = {
            "country_name" : country_name,
            "athlete_part_count" : 1
          }
        else:
          athletesByCountry[name]["country_name"] = country_name
          athletesByCountry[name]["athlete_part_count"] += 1


        if country_name not in populationByCountry.keys():
          populationByCountry[country_name] = population

        if country_name not in gdpByCountry.keys():
          gdpByCountry[country_name] = gdp

        if country_name in dataCollection.keys():
          dataCollection[country_name]["gold"] += gold
          dataCollection[country_name]["silver"] += silver
          dataCollection[country_name]["bronze"] += bronze
        else:

            try:
              if 'E' in gdp:
                gdpInFloat = float(gdp)
              elif gdp == '':
                gdpInFloat = 0
              else:
                gdpInFloat = float(gdp)
            except:
              e = sys.exc_info()[0]

              print ("Error: %s" % e)
              print (gdp)

              gdpInFloat = 0
              pass

            dataCollection[country_name] = {
              "gold" : gold,
              "silver": silver,
              "bronze": bronze,
              "population" : float(population),
              "gdp" : gdpInFloat
            }
    except:
      e = sys.exc_info()[0]

      print (">>>>>>>>>>>>>>>")
      print ("Error: %s" % e)
      print (record)
      pass

  athletesCountByCountry = {}

  for name, athlete_count in athletesByCountry.items():
    if athletesByCountry[name]['country_name'] in athletesCountByCountry.keys():
      athletesCountByCountry[athletesByCountry[name]['country_name']] += athletesByCountry[name]['athlete_part_count']
    else:
      athletesCountByCountry[athletesByCountry[name]['country_name']] = athletesByCountry[name]['athlete_part_count']

  for country_name, stats in dataCollection.items():
    #print country_name
    #print dataCollection[country_name]
    #print athletesCountByCountry[country_name]
    dataCollection[country_name]["num_athletes"] = athletesCountByCountry[country_name]
    dataCollection[country_name]["medal_count"] = dataCollection[country_name]['gold'] +  dataCollection[country_name]['silver'] + dataCollection[country_name]['bronze']


  fileOut  = open('olympic-data-' + search_year + '-' + search_seasson + '.csv', 'wb')
  columns = ['name','Continent','GDP', 'MedalCount', 'Gold', 'Silver', 'Bronze','AthletesCount', "Population"]
  writer = csv.DictWriter(fileOut, fieldnames=columns)
  writer.writeheader()

  for country_name, stats in dataCollection.items():
    print (country_name)
    print (dataCollection[country_name])
    print (countryByContinent[country_name])
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    try:
      writer.writerow({'name'     : country_name,
                       'Continent'   : countryByContinent[country_name],
                       'GDP'         : dataCollection[country_name]['gdp'],
                       'MedalCount'  : dataCollection[country_name]['medal_count'],
                       'Gold'        : dataCollection[country_name]['gold'],
                       'Silver'      : dataCollection[country_name]['silver'],
                       'Bronze'      : dataCollection[country_name]['bronze'],
                       'AthletesCount' : dataCollection[country_name]['num_athletes'],
                       'Population'  : dataCollection[country_name]['population']
                       })
    except:
      print (">>> MISSING COUNTRY <<<<")
      print (country_name)
      pass

def main():
  print ("**** Data Generator ****")
  parce_data("1980", "Winter")

  print (countryByContinent['Canada'])
  #print dataCollection
  #print athletesByCountry['Lieuwe de Boer']


if __name__ == "__main__":
  main()
