from amoCrm import AmoCrm


class Lead:
    @staticmethod
    @AmoCrm.request
    def create(pipeline_id: int, name: str = None, responsible: int = 0, budget: int = 0):
        data = dict()
        data['method'] = "POST"
        data['url'] = "api/v4/leads"
        data['json'] = [{
            "pipeline_id": pipeline_id,
            "responsible_user_id": responsible,
            # "pipeline_id": 6992723,
            "name": name,
            'price': budget
        }]
        return data

    @staticmethod
    @AmoCrm.request
    def read():
        data = dict()
        data['method'] = "GET"
        data['url'] = "amo/leads"
        return data

    @staticmethod
    @AmoCrm.request
    def delete(id: int):
        data = dict()
        data['method'] = "DELETE"
        data['url'] = f"objects/{id}"
        return data

    @staticmethod
    @AmoCrm.request
    def update(id: int):
        data = dict()
        data['method'] = "DELETE"
        data['url'] = f"objects/{id}"
        return data

    @staticmethod
    @AmoCrm.request
    def read_one(id: int):
        data = dict()
        data['method'] = "GET"
        data['url'] = f"amo/leads{id}"
        return data

    @staticmethod
    @AmoCrm.request
    def add_tag(lead_id: int, tag_name: list):
        data = dict()
        data['method'] = "PATCH"
        data['url'] = f"api/v4/leads"
        tags = []
        for name in tag_name:
            tags.append({
                            "name": name
                        })
        data['json'] = [
            {
                "id": lead_id,
                "_embedded": {
                    "tags": tags
                }
            },
        ]
        return data
