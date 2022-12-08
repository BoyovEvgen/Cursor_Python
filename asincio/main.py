import asyncio
import aiohttp
import requests
import time
BASE_URL = "https://pokeapi.co/api/v2/"
POKEMONS_URL = BASE_URL + "pokemon/"
TYPE_URL = BASE_URL + "type/"


def get_list_of_pokemons(type_pok=None):
    """
    виконується запрос за типом з якого парсятся імена,
    якщо тип не передається то виконується запрос на перші 20 обїєктів.
    :param type_pok:
    :return:
    """
    if type_pok:
        res = requests.get(TYPE_URL + type_pok)
        pokemons_lst = [data.get('pokemon') for data in res.json()['pokemon']]
    else:
        res = requests.get(POKEMONS_URL)
        pokemons_lst = res.json()['results']
    names_lst = [poc.get('name') for poc in pokemons_lst]
    return names_lst


def get_info_pokemon():
    """
    реалізіція першого завдання без asincio для порівняння швикості виконання.
    Виконання більше 4х секунд.
    """
    names = get_list_of_pokemons()
    start = time.time()
    for name in names:
        res = requests.get(POKEMONS_URL + name)
        data_dict = res.json()
        # print(res.json())
        print(f"{name.title()} has a weight of {data_dict.get('weight')} and a height of {data_dict.get('height')}")
    print(time.time() - start)


async def get_info_pokemon_async(session, name):
    resp = await session.get(POKEMONS_URL + name)
    data_dict = await resp.json()
    print(f"{name.title()} has a weight of {data_dict.get('weight')} and a height of {data_dict.get('height')}")
    return {'id': data_dict.get('id'),
            'name': name.title(),
            'weight': data_dict.get('weight'),
            'height': data_dict.get('height')}


async def main(name_lst):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        res = await asyncio.gather(*[get_info_pokemon_async(session, name) for name in name_lst])
    print(time.time() - start)  # виконання біля 0.2 секунди
    return res


def get_all_type():
    """реалізував спочатку отримання типів,так ях хто знає які вони там є ..."""
    res = requests.get(TYPE_URL)
    type_lst = [t['name'] for t in res.json()['results']]
    return type_lst


def chose_type():
    """ту робимо бибір типу з завантажених з get_all_type"""
    types = get_all_type()
    print(types)
    while True:
        type_pok = input('Введіть один тип Покемона з наданих вище: ')
        if type_pok in types:
            return type_pok


if __name__ == '__main__':
    # 1.
    get_info_pokemon() # розблокувати для отримання інфо перших 20 покемонів без asincio
    # 2.
    name_list = get_list_of_pokemons()  # розблокувати для отримання інфо перших 20 покемонів з asincio
    # 3.
    # name_list = get_list_of_pokemons(chose_type())  # розблокувати для отримання інфо покемонів за вибраним Типом з asincio


    print(asyncio.run(main(name_list)))







# main_loop = asyncio.get_event_loop() # створює петлю в якій виконуються задачі
# main_loop.create_task(my_func)  # створює задачц
# main_loop.run_until_complete(main())  #працює поки не виконаються завдання
# main_loop.run_forever()  #працюєє незкінченно
