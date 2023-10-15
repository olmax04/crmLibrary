from .amoCrm import AmoCrm


class Connect:

    @staticmethod
    @AmoCrm.request
    def create(source_id: int, source_type: str, target_id: [int, str], target_type: [int, str],
               metadata: dict = {"is_main": True}) -> dict:
        data = dict()
        data['url'] = f"api/v4/{target_type}/{target_id}/link"
        data['method'] = 'POST'
        data['json'] = [
            {
                "to_entity_id": source_id,
                "to_entity_type": source_type,
                "metadata": metadata
            }
        ]
        return data
