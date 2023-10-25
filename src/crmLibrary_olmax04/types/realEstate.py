class RealEstateObject:
    def __init__(self, source, url):
        self.source: str = source
        self.url: str = url
        self.images: list = list()
        self.address: str = None
        self.ownerType: str = None
        self.owner: dict = None
        self.price: int = 0
        self.description: str = None
        self.currentFloor: int = 0
        self.floorCount: int = 0
        self.roomsCount: int = 0
        self.bedroomsCount: int = 0
        self.area: int = 0
        self.parking: str = None
        self.animals: str = None
        self.deposit: int = 0
        self.communal: int = 0

    def __str__(self):
        return (f"RealEstate[url: {self.url}]\n"
                f"  Address: {self.address}\n"
                f"  Owner type: {self.ownerType}\n"
                f"  Price: {self.price}\n"
                f"  Description: {self.description}\n"
                f"  Current floor: {self.currentFloor}\n"
                f"  Floor count: {self.floorCount}\n"
                f"  Rooms count: {self.roomsCount}\n"
                f"  Bedrooms count: {self.bedroomsCount}\n"
                f"  Area: {self.area} m^2\n"
                f"  Parking: {self.parking}\n"
                f"  Animals: {self.animals}\n"
                f"  Deposit: {self.deposit}\n"
                f"  Communal: {self.communal}\n")

    def getUrl(self):
        return self.url

    def setUrl(self, url: str):
        self.url = url

    def getAnimals(self):
        return self.animals

    def setAnimals(self, animals: str):
        self.animals = animals

    def getImages(self):
        return self.images

    def setImages(self, images: list):
        self.images = images

    def getAddress(self):
        return self.address

    def setAddress(self, address: str):
        self.address = address

    def getOwnerType(self):
        return self.ownerType

    def setOwnerType(self, ownerType: str):
        self.ownerType = ownerType

    def getOwner(self):
        return self.owner

    def setOwner(self, owner: dict):
        self.owner = owner

    def getPrice(self):
        return self.price

    def setPrice(self, price: int):
        self.price = price

    def getCurrentFloor(self):
        return self.currentFloor

    def setCurrentFloor(self, currentFloor: int):
        self.currentFloor = currentFloor

    def getFloorCount(self):
        return self.floorCount

    def setFloorCount(self, floorCount: int):
        self.floorCount = floorCount

    def getRoomsCount(self):
        return self.roomsCount

    def setRoomsCount(self, roomsCount: int):
        self.roomsCount = roomsCount

    def getBedroomsCount(self):
        return self.bedroomsCount

    def setBedroomsCount(self, bedroomsCount: int):
        self.bedroomsCount = bedroomsCount

    def getDescription(self):
        return self.description

    def setDescription(self, description: str):
        self.description = description

    def getArea(self):
        return self.area

    def setArea(self, area: int):
        self.area = area

    def getParking(self):
        return self.parking

    def setParking(self, parking: [str, None]):
        self.parking = parking

    def getDeposit(self):
        return self.deposit

    def setDeposit(self, deposit: int):
        self.deposit = deposit

    def getCommunal(self):
        return self.communal

    def setCommunal(self, communal: int):
        self.communal = communal
