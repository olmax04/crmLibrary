class RealEstateObject:
    def __init__(self, source, url):
        self.source: str = source
        self.url: str = url
        self.images: list = list()
        self.address: str = None
        self.ownerType: str = None
        self.owner: dict = None
        self.price: int = None
        self.description: str = None
        self.currentFloor: int = None
        self.floorCount: int = None
        self.roomsCount: int = None
        self.bedroomsCount: int = None
        self.area: int = None
        self.parking: str = None
        self.deposit: int = None
        self.communal: int = None

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        self.url = url

    def getImages(self):
        return self.images

    def setImages(self, images):
        self.images = images

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getOwnerType(self):
        return self.ownerType

    def setOwnerType(self, ownerType):
        self.ownerType = ownerType

    def getOwner(self):
        return self.owner

    def setOwner(self, owner):
        self.owner = owner

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getCurrentFloor(self):
        return self.currentFloor

    def setCurrentFloor(self, currentFloor):
        self.currentFloor = currentFloor

    def getFloorCount(self):
        return self.floorCount

    def setFloorCount(self, floorCount):
        self.floorCount = floorCount

    def getRoomsCount(self):
        return self.roomsCount

    def setRoomsCount(self, roomsCount):
        self.roomsCount = roomsCount

    def getBedroomsCount(self):
        return self.bedroomsCount

    def setBedroomsCount(self, bedroomsCount):
        self.bedroomsCount = bedroomsCount

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getArea(self):
        return self.area

    def setArea(self, area):
        self.area = area

    def getParking(self):
        return self.parking

    def setParking(self, parking):
        self.parking = parking

    def getDeposit(self):
        return self.deposit

    def setDeposit(self, deposit):
        self.deposit = deposit

    def getCommunal(self):
        return self.communal

    def setCommunal(self, communal):
        self.communal = communal
