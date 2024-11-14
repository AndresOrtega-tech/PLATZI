def getPopulation():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values

def populationByCountry(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result

[
    {
        'Country':'Colombia',
        'Populaiton': 300
    },
    {
        'Country':'Bolivia',
        'Populaiton': 400
    }
]