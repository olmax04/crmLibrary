import re

import thefuzz.fuzz


class Name:
    @staticmethod
    def state(value: str = None):
        return value or "Warszawa"

    @staticmethod
    def district(value: str):
        temp = check_district(value)['value']
        array = temp.split(" ")
        return f"#{array[2]}"

    @staticmethod
    def street(value: str):
        array = value.split(",")
        for item in array:
            if 'ul' in item:
                return item.replace(" ", "")

    @staticmethod
    def get_name(adress: str):
        return f"{Name.state('Warszawa')}, {Name.district(adress)}, {Name.street(adress)}"


def children(value: str = None):
    return {
        "param_id": 448516,
        "param_alias": "children",
        "param_type": 3,
        "values": [
            {
                "value": "Возможно",
                "enum_id": "vozm"
            }
        ]
    }


def link(value: str):
    return {
        "param_id": 478004,
        "param_alias": "link_to_object",
        "param_type": 8,
        "values": [
            {
                "value": value
            }
        ]
    }


def kaucja(value: int, price: int, czynsz: int):
    if value == 0 or value is None:
        return {
            "param_id": 447419,
            "param_alias": "kaucja",
            "param_type": 2,
            "values": [
                {
                    "value": price
                }
            ]
        },

    else:
        return {
            "param_id": 447419,
            "param_type": 2,
            "values": [
                {
                    "value": value
                }
            ]
        }


def second_czynsz(value: int):
    return {
        "param_id": 447421,
        "param_alias": "administracyjny",
        "param_type": 2,
        "values": [
            {
                "value": value
            }
        ]
    }


def czynsz(value: int):
    return {
        "param_id": 447421,
        "param_alias": "administracyjny",
        "param_type": 2,
        "values": [
            {
                "value": value
            }
        ]
    },


def description(kaucja: int = 0, rooms: int = 0, bedrooms: int = 0):
    if rooms == 1 or rooms < 1:
        bedrooms = 1
        rooms = 1
    else:
        bedrooms -= 1
    return (
        f"Кауция: {kaucja}<br>Кол-во комнат: {rooms}<br>Кол-во спален: {bedrooms}<br>Кондиционер:<br>Животные: Возможно<br>Паркинг: Возможно")


def description_inner(value: str):
    edited_value = value
    target = ['garaż', 'garaz', 'miejsce postojowe', 'miejsce parkingowe', 'parking', 'komorka',
              'komórka lokatorska',
              'dzieci', 'dziecko', 'zwierzęta', 'zwierzeta', 'zwierzętom', 'kaucja', 'depozyt', 'media', 'liczniki',
              'czynsz administracyjny', 'cena', 'zaliczka', 'zaliczki', 'koszt', 'dostepne', 'balkon', 'wanna',
              'prysznic',
              'klimatyzacja', 'klima', 'oplaty', 'AC', 'obcokrajowcy', 'najem okazjonalny', 'zwierzętom',
              'plac zabaw',
              'płace zabaw', 'osiedlu', 'kaucja', 'czynsz najmu', "prąd", 'opłaty', "kwota", "CENA",
              'tarasem', 'taras', 'miejsca postojowe']
    numbers = re.findall(r'\d+', value)
    for number in numbers:
        if number in edited_value:
            edited_value = edited_value.replace(number, f"<strong>{number}</strong>")
    for item in target:
        if item in edited_value:
            edited_value = edited_value.replace(item, f"<strong>{item}</strong>")
    return edited_value


def address(value: str):
    return {
        "param_id": 425521,
        "values": [
            {
                "value": value,
            }
        ]
    }


def area(value: int):
    return {
        "param_id": 425520,
        "param_alias": "total_square",
        "param_type": 2,
        "values": [
            {
                "value": value
            }
        ]
    }


def city(value: str):
    return {
        "param_id": 447416,
        "param_type": 3,
        "values": [
            {
                "value": "Варшава",
                "enum_id": "varshava"
            }
        ]
    }


def district(value: str):
    return {
        "param_id": 447417,
        "param_type": 3,
        "values": [
            check_district(value)
        ]
    }


def check_district(value: str):
    districts = {
        "bemowo": {
            "value": "Варшава - Бемово",
            "enum_id": "Bemovo"
        },
        "ochota": {
            "value": "Варшава - Охота",
            "enum_id": "Hunting"
        },
        "ursynów": {
            "value": "Варшава - Урсунов",
            "enum_id": "Ursunov"
        },
        "bielany": {
            "value": "Варшава - Беляны",
            "enum_id": "Belyans"
        },
        "wola": {
            "value": "Варшава - Воля",
            "enum_id": "Will"
        },
        "Żoliborz": {
            "value": "Варшава - Жолибож",
            "enum_id": "Zholibozh"
        },
        "mokotów": {
            "value": "Варшава - Мокотув",
            "enum_id": "Mokotuv"
        },
        "wilanów": {
            "value": "Варшава - Вилянув",
            "enum_id": "Vilyanuv"
        },
        "białołęka": {
            "value": "Варшава - Бялоленка",
            "enum_id": "Byalolenka"
        },
        "powisle": {
            "value": "Варшава - Повисле",
            "enum_id": "Povisle"
        },
        "praga-południe": {
            "value": "Варшава - Прага-Полудне",
            "enum_id": "Prague-afternoon"
        },
        "praga-północ": {
            "value": "Варшава - Прага-Пулноц",
            "enum_id": "Prague-Pulnots"
        },
        "targówek": {
            "value": "Варшава - Таргувек",
            "enum_id": "Targouk"
        },
        "rembertów": {
            "value": "Варшава - Рембертув",
            "enum_id": "Rembertov"
        },
        "śródmieście": {
            "value": "Варшава - Средместье",
            "enum_id": "Sredmest"
        },
        "wesoła": {
            "value": "Варшава - Весола",
            "enum_id": "Vesol"
        },
        "wawer": {
            "value": "Варшава - Вавер",
            "enum_id": "Vaver"
        },
        "włochy": {
            "value": "Варшава - Влохи",
            "enum_id": "Volokhi"
        },
        "ursus": {
            "value": "Варшава - Урсус",
            "enum_id": "Ursus"
        },
    }
    array = value.lower().split(",")
    greatest = None
    for item in array:
        for district in districts.items():
            key, value = district[0], district[1]
            match = thefuzz.fuzz.ratio(item, key)
            if greatest is None:
                greatest = {"score": match, "value": value}
            elif greatest['score'] < match:
                greatest = {"score": match, "value": value}
            if match > 80:
                return value
    return greatest['value']


def floor(value: int):
    return {
        "param_id": 425518,
        "param_type": 2,
        "values": [
            {
                "value": value
            }
        ]
    }


def floors_count(value: int):
    return {
        "param_id": 425519,
        "param_type": 2,
        "values": [
            {
                "value": value
            }
        ]
    }


def animals(value: str):
    return {
        "param_id": 448517,
        "param_alias": "animals",
        "param_type": 3,
        "values": [
            {
                "value": "Возможно",
                "enum_id": "vozm"
            }
        ]
    }


def parking(value: str):
    if value is not None:
        return {
            "param_id": 448519,
            "param_alias": "parking",
            "param_type": 3,
            "values": [
                {
                    "value": "Подземный",
                    "enum_id": "podz"
                }
            ]
        }
    else:
        return {
            "param_id": 448519,
            "param_alias": "parking",
            "param_type": 3,
            "values": [
                {
                    "value": "Возможно",
                    "enum_id": "vozm"
                }
            ]
        }


def rooms(value: int):
    if value <= 1:
        return {
            "param_id": 425643,
            "param_alias": "BedroomsCount",
            "param_type": 2,
            "values": [
                {
                    "value": value
                }
            ]
        }
    else:
        return {
            "param_id": 425643,
            "param_alias": "BedroomsCount",
            "param_type": 2,
            "values": [
                {
                    "value": value - 1
                }
            ]
        }


def bedrooms(value: int):
    param_id = 448514
    return {
        "param_id": param_id,
        "param_type": 2,
        "values": [
            {
                "value": value
            }
        ]
    }


def state(value: str):
    return {
        "param_id": 447415,
        "values": [
            {
                "value": "Польша",
                "enum_id": "poland"
            }
        ]
    }


def representative(value: str):
    values = {
        "prywatny": {
            "param_id": 447410,
            "values": [
                {
                    "value": "Собственник",
                    "enum_id": "owner"
                }
            ]
        },
        "Oferta prywatna": {
            "param_id": 447410,
            "values": [
                {
                    "value": "Собственник",
                    "enum_id": "owner"
                }
            ]
        },
        "użytkownik": {
            "param_id": 447410,
            "values": [
                {
                    "value": "Собственник",
                    "enum_id": "owner"
                }
            ]
        },
        "biuro nieruchomości": {
            "param_id": 447410,
            "values": [
                {
                    "value": "Посредник",
                    "enum_id": "mediator"
                }
            ]
        },
        "osoba prywatna": {
            "param_id": 447410,
            "values": [
                {
                    "value": "Собственник",
                    "enum_id": "owner"
                }
            ]
        },
        "agent nieruchomości": {
            "param_id": 447410,
            "values": [
                {
                    "value": "Посредник",
                    "enum_id": "mediator"
                }
            ]
        }}
    if value in values:
        return values[value]
    return values['biuro nieruchomości']
