import requests
import os
import pathlib

data_urls = {'https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat':'routes'
            ,'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat':'airlines'
            ,'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat':'airports'
}

data_headers = {'airports':'Airport_ID,City,Country,IATA,ICAO,Latitude,Longitude,Altitude,Timezone,DST,Tz_db,Type,Source'
                ,'airlines':'Airline_ID,Name,Alias,IATA,ICAO,Callsign,Country,Active'
                ,'routes':'Airline,Airline_ID,Source_Airport,Source_Airport_ID, Destination_Airport,Destination_Airport_ID,Codeshare,Stops,Equipment'
}

directory = 'ABC_Supply_Tableau_Homework'

def data_dir_create():
    path = pathlib.Path.cwd() / 'Data'

    path.mkdir(exist_ok=True)

def get_data():
    for url in data_urls.items():
        resp = requests.get(url[0])
        file_name = './Data/' + url[1] + '.csv'
        header = data_headers[url[1]]

        with open(file_name, 'w', encoding='UTF-8', newline='\n') as data_file:
            data_file.write(header + "\n")
            data_file.write(resp.text)


if __name__ == "__main__":
    print('Creating folder to house data.')
    data_dir_create()
    print('Getting data for homework.')
    get_data()

