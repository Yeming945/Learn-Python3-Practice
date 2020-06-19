""" 练习 39. 字典，可爱的字典 """

# create a mapping of state to abbreviation
# 创建一些州的缩写
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# create a basic set of states and some cities in them
# 创建一些基本的州和它们的城市
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# add some more cities
# 添加更多城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
# 打印出一些城市
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])


# print some states
# 打印一些州
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviate {abbrev}")


# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
# sately get abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
