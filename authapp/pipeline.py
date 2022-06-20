from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile, ShopUser


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse((
        'https',
        'api.vk.com',
        '/method/users.get',
        None,
        urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_200')),
                              access_token=response['access_token'],
                              v='5.131'
                              )),
        None
    ))
    # api_url = urlunparse(('https',
    #                       'api.vk.com',
    #                       '/method/users.get',
    #                       None,
    #                       urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
    #                                             access_token=response['access_token'],
    #                                             v='5.131')),
    #                       None
    #                       ))

    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    print(data)
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.about_me = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        print(age, user.age)
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.age = age

    if data['photo_200']:
        user.avatar = data['photo_200']

    user.save()
