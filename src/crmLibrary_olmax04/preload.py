from .rieltorModule import RieltorModule


class Preload:
    @staticmethod
    def preload_handler(list):
        preload_data = {}
        for i, file in enumerate(list):
            preload_data[f"file{i}"] = file
        return preload_data

    @staticmethod
    @RieltorModule.request
    def create(files_urls) -> dict:
        data = dict()
        data['url'] = "preloads/object_photo/"
        data['headers'] = {'Accept': "*/*"}
        data['method'] = "POST"
        data['files'] = Preload.preload_handler(files_urls)
        return data
