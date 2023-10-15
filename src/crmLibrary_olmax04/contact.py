from .amoCrm import AmoCrm


class Contact:
    @staticmethod
    @AmoCrm.request
    def create(link: str, name: str = "Unnamed", phone: str = None) -> dict:
        data = dict()
        data['url'] = "api/v4/contacts"
        data['method'] = "POST"
        data['json'] = [{
            "first_name": name,
            "last_name": "",
            "custom_fields_values": [
                {
                    "field_id": 1354502,
                    "values": [
                        {
                            "value": f"{link}"
                        }
                    ]
                },
                {
                    "field_id": 350880,
                    "values": [
                        {
                            "value": f"{phone}"
                        }
                    ]
                },
            ]
        }]
        return data
