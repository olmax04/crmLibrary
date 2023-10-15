from .rieltorModule import RieltorModule
from .utils.realEstate import *
from .types.realEstate import RealEstateObject


class RealEstate:

    @staticmethod
    @RieltorModule.request
    def create(realEstate: RealEstateObject, responsibleId: int, leadId: int):
        data = dict()
        data['method'] = "POST"
        data['url'] = "objects"
        data['json'] = {
            "cluster_id": 2088,
            "name": Name.get_name(realEstate.address),
            "responsible_id": responsibleId,
            "category_id": 1,
            "parent_id": None,
            "type_id": 96646,
            "deal_type_id": 1,
            "lead_id": leadId,
            "price": realEstate.price + realEstate.communal,
            "price_in_currency": 0,
            "currency": "PLN",
            "export_website": False,
            "description_public": description(realEstate.deposit, realEstate.roomsCount, realEstate.bedroomsCount),
            "description_inner": description_inner(realEstate.description),
            "params": [
                link(realEstate.url),
                state("Poland"),
                representative(realEstate.ownerType),
                bedrooms(realEstate.bedroomsCount),
                rooms(realEstate.roomsCount),
                kaucja(realEstate.deposit, realEstate.price, realEstate.communal),
                czynsz(realEstate.communal),
                city(realEstate.address),
                floor(realEstate.currentFloor),
                floors_count(realEstate.floorCount),
                district(realEstate.address),
                parking(realEstate.parking),
                area(realEstate.area),
                address(realEstate.address),
                second_czynsz(realEstate.communal),
                animals(realEstate.parking),
                children()
            ]
        }
        return data

    @staticmethod
    @RieltorModule.request
    def read():
        data = dict()
        data['method'] = "GET"
        data['url'] = "objects"
        return data

    @staticmethod
    @RieltorModule.request
    def delete(id: int):
        data = dict()
        data['method'] = "DELETE"
        data['url'] = f"objects/{id}"
        return data

    @staticmethod
    @RieltorModule.request
    def update(id: int, fields: dict):
        data = dict()
        data['method'] = "PATCH"
        data['url'] = f"objects/{id}"
        data['json'] = fields
        return data
