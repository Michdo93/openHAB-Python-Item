class Item(object):
    def __init__(self, type:str = None, name:str = None, state = None, tags:list = None, groups:list = None):
        self.__itemTypes = ["Color", "Contact", "DateTime", "Dimmer", "Group", "Image", "Location", "Number", "Player", "Rollershutter", "String", "Switch"]
        self.setType(type)
        self.setName(name)
        self.setState(state)
        self.setTags(tags)
        self.setGroups(groups)
        
    def __checkItemValue(self, type:str, value):
        bool = False

        if type == self.__itemTypes[0]:
            bool = self.__checkColorValue(value)
        elif type == self.__itemTypes[1]:
            bool = self.__checkContactValue(value)
        elif type == self.__itemTypes[2]:
            bool = self.__checkDateTimeValue(value)
        elif type == self.__itemTypes[3]:
            bool = self.__checkDimmerValue(value)
        elif type == self.__itemTypes[4]:
            bool = self.__checkGroupValue(value)
        elif type == self.__itemTypes[5]:
            bool = self.__checkImageValue(value)
        elif type == self.__itemTypes[6]:
            bool = self.__checkLocationValue(value)
        elif type == self.__itemTypes[7]:
            bool = self.__checkNumberValue(value)
        elif type == self.__itemTypes[8]:
            bool = self.__checkPlayerValue(value)
        elif type == self.__itemTypes[9]:
            bool = self.__checkRollershutterValue(value)
        elif type == self.__itemTypes[10]:
            bool = self.__checkStringValue(value)
        elif type == self.__itemTypes[11]:
            bool = self.__checkSwitchValue(value)

        return bool


    def __checkColorValue(self, value):
        if isinstance(value, str):
            if value == "ON" or value == "OFF" or value == "INCREASE" or value == "DECREASE":
                return True
            else:
                value = value.replace(" ", "")
                splitted = value.split(",")
                hue = float(splitted[0])
                saturation = float(splitted[1])
                brightness = float(splitted[2])
                if isinstance(hue, float) or isinstance(saturation, float) or isinstance(brightness, float):
                    if (0 <= hue <= 360.0) and (0 <= saturation <= 255.0) and (0 <= brightness <= 255.0):
                        return True
                    return False
                return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False
        return False

    def __checkContactValue(self, value):
        if isinstance(value, str):
            if value == "OPEN" or value == "CLOSED":
                return True
            return False
        return False

    def __checkDateTimeValue(self, value):
        if isinstance(value, str):
            if value != datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%dT%H:%M:%SZ'):
                return True
            return False
        return False

    def __checkDimmerValue(self, value):
        if isinstance(value, str):
            if value == "ON" or value == "OFF" or value == "INCREASE" or value == "DECREASE":
                return True
            return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False

    def __checkGroupValue(self, value):
        if isinstance(value, str):
            return True
        return False

    def __checkImageValue(self, value):
        if base64.b64decode(value, validate=True) == True:
            return True
        return False

    def __checkLocationValue(self, value):
        if isinstance(value, str):
            value = value.replace(" ", "")
            splitted = value.split(",")
            latitude = float(splitted[0])
            longitude = float(splitted[1])
            altitude = float(splitted[2])
            if isinstance(latitude, float) or isinstance(longitude, float) or isinstance(altitude, float):
                return True
            return False
        return False

    def __checkNumberValue(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False

    def __checkPlayerValue(self, value):
        if value == "PLAY" or value == "PAUSE" or value == "NEXT" or value == "PREVIOUS" or value == "REWIND" or value == "FASTFORWARD":
            return True
        return False

    def __checkRollershutterValue(self, value):
        if isinstance(value, str):
            if value == "UP" or value == "DOWN" or value == "STOP" or value == "MOVE":
                return True
            return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False

    def __checkStringValue(self, value):
        if isinstance(value, str):
            return True
        return False

    def __checkSwitchValue(self, value):
        if value == "ON" or value == "OFF":
            return True
        return False
    
    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
    
    def getState(self):
        return self.state
    
    def getTags(self):
        return self.tags
    
    def getGroups(self):
        return self.groups
    
    def setType(self, type:str):
        if self.__checkItemType(type):
            self.type = type
        
    def setName(self, name:str):
        self.name = name
        
    def setState(self, state):
        if self.__checkItemValue:
            self.state = state
        
    def setTags(self, tags:list):
        self.tags = tags
        
    def setGroups(self, groups:list):
        self.groups = groups

class ColorItem(Item):
    def __init__(self, type:str = None, name:str = None, state = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
    
    def __checkColorValue(self, value):
        return super().__checkColorValue(value)
        
class ContactItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state:str):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkContactValue(self, value):
        return super().__checkContactValue(value)
        
class DateTimeItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state:str):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkDateTimeValue(self, value):
        return super().__checkDateTimeValue(value)
        
class DimmerItem(Item):
    def __init__(self, type:str = None, name:str = None, state:int = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state:int):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkDimmerValue(self, value):
        return super().__checkDimmerValue(value)
        
class GroupItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkGroupValue(self, value):
        return super().__checkGroupValue(value)
        
class ImageItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state:str):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkImageValue(self, value):
        return super().__checkImageValue(value)
        
class LocationItem(Item):
    def __init__(self, type:str = None, name:str = None, state = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkLocationValue(self, value):
        return super().__checkLocationValue(value)
        
class NumberItem(Item):
    def __init__(self, type:str = None, name:str = None, state = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkNumberValue(self, value):
        return super().__checkNumberValue(value)
        
class PlayerItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkPlayerValue(self, value):
        return super().__checkPlayerValue(value)
        
class RollershutterItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkRollershutterValue(self, value):
        return super().__checkRollershutterValue(value)
        
class StringItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkStringValue(self, value):
        return super().__checkStringValue(value)

class SwitchItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def __checkSwitchValue(self, value):
        return super().__checkSwitchValue(value)
