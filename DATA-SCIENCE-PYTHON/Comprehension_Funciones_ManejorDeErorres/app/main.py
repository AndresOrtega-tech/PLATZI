import utils

data = [
        {
            'Country':'Colombia',
            'Populaiton': 300
        },
        {
            'Country':'Bolivia',
            'Populaiton': 400
        }
    ]

def run():
    keys, values = utils.getPopulation()
    print(keys, values)

    country = input('Type country: ')

    result = utils.populationByCountry(data, country)
    print(result)

if __name__ == '__main__':
    run()