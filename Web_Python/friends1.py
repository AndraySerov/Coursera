import requests
import datetime
from operator import itemgetter


def calc_age(uid):

    now = datetime.datetime.now()
    ACCESS_TOKEN = ''   #yoyr token here
    ages = []
    age_and_number = {}

    params_id = {'v': '5.71', 'access_token': ACCESS_TOKEN, 'user_ids': uid}
    id_url = 'https://api.vk.com/method/users.get'
    get_id = requests.get(id_url, params=params_id).json()
    user_id = get_id['response'][0]['id']

    params_friendlist = {'v': '5.71', 'access_token': ACCESS_TOKEN,
                         'user_id': user_id, 'fields': 'bdate'}
    friendlist_url = 'https://api.vk.com/method/audio.get'
    get_friendlist = requests.get(friendlist_url,
                                  params=params_friendlist).json()

    for person in get_friendlist['response']['items']:
        if 'bdate' in person:
            if len(person['bdate'].split('.')[-1]) == 4:
                age = now.year - int(person['bdate'].split('.')[-1])
                ages.append(age)

    for age in ages:
        if age not in age_and_number:
            age_and_number[age] = 1
        else:
            age_and_number[age] += 1

    result = [(k, v) for k, v in age_and_number.items()]
    result2 = sorted(result, key=itemgetter(0))
    result2 = sorted(result2, key=itemgetter(1), reverse=True)

    return result2


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
