import requests
import json
import pandas as pd

HLKZ_API_BASE = 'https://hlkz.sourceruns.org'
HLKZ_API_MAPS = '/api/maps'

def maps_url(page):
    return f'{HLKZ_API_BASE+HLKZ_API_MAPS}?page={page}'


def get_maps():
    maps = {
        'name': [],
        'players': [],
        'pure_wr': [],
        'pro_wr': [],
    }

    i = 1
    while True:
        url = maps_url(i)
        print(f'page: {i}\trequesting: {url}')
        request = requests.get(url)
        response = request.json()
        data = response['data']
        if data == []:
            break
        for _map in data:
            print(_map)
            maps['name'].append(_map['name'])
            if _map['playersTotal'] == None:
                maps['players'].append(-1)
            else:
                maps['players'].append(_map['playersTotal'])
            if _map['pure_wr'] == None:
                maps['pure_wr'].append(-1)
            else:
                maps['pure_wr'].append(_map['pure_wr'])
            if _map['pro_wr'] == None:
                maps['pro_wr'].append(-1)
            else:
                maps['pro_wr'].append(_map['pro_wr'])
        i += 1

    df = pd.DataFrame(maps)

    return df

if __name__ == '__main__':
    maps = get_maps()
    maps.head()
    maps.to_csv('maps.csv', index=False)
    maps.to_excel('maps.xlsx', index=False)
    