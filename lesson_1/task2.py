capitals = {
    'Canada' : 'Ottawa',
    'Ukraine' : 'Kiev',
    'USA' : 'Washington'
}

countries = ['Canada', 'Ukraine', 'USA', 'China',]

for country in countries:
    if country in capitals:
        print(capitals.get(country))