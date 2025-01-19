
# cities = ["antalya",'istanbul']
# plates =['07','34']
# print(plates[cities.index('istanbul')])

plates = {'antalya' : '07', 'istanbul' : '34'}
print(plates['istanbul'])

plates['ankara'] = '06'
print(plates)

print("*******************")

users = {
    'user1' :{
        'age' : 25,
        'address' : 'antalya',
        'phone' : '1111111'
    },
      'user2' :{
        'age' : 25,
        'address' : 'bolu',
        'phone' : '1111111'
    }
}
print(users)
print(users['user2']['address'])