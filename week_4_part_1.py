# Assignment 1
print('---------- Assignment 1 ----------')
import requests

get_activity = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities')
assert get_activity.status_code == 200

activity = get_activity.json()
for i in range(len(activity)):
    if not activity[i]['completed']:
        print(activity[i]['id'])


# Assignment 2
print('---------- Assignment 2 ----------')
import json

user_info = {
  "username": "admin",
  "password": "password"
}

session = requests.session()
post_login = session.post('https://automationintesting.online/auth/login', json = user_info)

get_room_list = session.get('https://automationintesting.online/room/')
checkin = "2024-03-09"
checkout = "2024-03-10"
first_room = get_room_list.json()['rooms'][0]['roomid']

booking_info = {
    'bookingdates': {
        'checkin': '%s' % checkin,
        'checkout': '%s' % checkout
    },
    'depositpaid': 'true',
    'firstname': 'First',
    'lastname': 'Last',
    'roomid': '%s' % first_room,
    'totalprice': '100'
}
post_booking = session.post('https://automationintesting.online/booking/', json = booking_info)
assert post_booking.status_code == 201

id = post_booking.json()['bookingid']
booking_result = {
    'bookingid': id, 
    'booking': {
        'bookingid': id, 
        'roomid': first_room, 
        'firstname': 'First', 
        'lastname': 'Last', 
        'depositpaid': True, 
        'bookingdates': {
            'checkin': '%s' % checkin, 
            'checkout': '%s' % checkout
        }
    }
}
assert json.dumps(post_booking.json()) == json.dumps(booking_result)


# Assignment 3
print('---------- Assignment 3 ----------')
def single_number(nums):
    newlist = []

    for i in nums:
        if i in newlist:
            newlist.remove(i)
        else:
            newlist.append(i)
    return newlist.pop()
    
print(single_number([2, 2, 1])) # Should be 1
print(single_number([4, 1, 2, 1, 2])) # Should be 4
print(single_number([1])) # Should be 1
