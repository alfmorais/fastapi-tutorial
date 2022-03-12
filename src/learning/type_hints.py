from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple, Union

from pydantic import BaseModel


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name


print(get_full_name('john', 'doe'))


def get_name_with_age(name: str, age: int):
    name_with_age = name + 'is this old: ' + str(age)
    return name_with_age


# Simple Types
def get_items(
    item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes
):
    return item_a, item_b, item_c, item_d, item_e


def process_items(items: List[str]):
    for item in items:
        print(item)


# def process_tuple_set(items_t: Tuple(int, int, str), items_s: Set[bytes]):
#     return items_s, items_t


def process_dict(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item(item: Union[int, str]):
    print(item)


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'Hey {name}!')
    else:
        print('Hello World')


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2017-06-01 12:22',
    'friends': [1, '2', b'3'],
}
user = User(**external_data)

print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]

print(user.id)
# > 123
