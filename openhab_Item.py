class Item(object):
    def __init__(self, type:str = None, name:str = None, tags:list = None, groups:list = None):
        self.setType(type)
        self.setName(name)
        self.setTags(tags)
        self.setGroups(groups)
        self.__itemTypes = ["Color", "Contact", "DateTime", "Dimmer", "Group", "Image", "Location", "Number", "Player", "Rollershutter", "String", "Switch"]
        
    def __checkItemType(self, type:str):
        if type in self.__itemTypes:
            return True
        return False
    
    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
    
    def getTags(self):
        return self.tags
    
    def getGroups(self):
        return self.groups
    
    def setType(self, type:str):
        self.type = self.__checkItemType(type)
        
    def setName(self, name:str):
        self.name = name
        
    def setTags(self, tags:list):
        self.tags = tags
        
    def setGroups(self, groups:list):
        self.groups = groups

class ColorItem(Item):
    def __init__(self, type:str = None, name:str = None, state = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
    
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
        
class ContactItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        
    def __checkContactValue(self, value):
        if isinstance(value, str):
            if value == "OPEN" or value == "CLOSED":
                return True
            return False
        return False
        
class DateTimeItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        
    def __checkDateTimeValue(self, value):
        if isinstance(value, str):
            if value != datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%dT%H:%M:%SZ'):
                return True
            return False
        return False
        
class DimmerItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        
    def __checkDimmerValue(self, value):
        if isinstance(value, str):
            if value == "ON" or value == "OFF" or value == "INCREASE" or value == "DECREASE":
                return True
            return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False
        
class GroupItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)
    
    def getState(self):
        return self.state
    
    def setState(self, state:str):
        if self.__checkGroupValue(state):
            self.state = state
        
    def __checkGroupValue(self, value):
        if isinstance(value, str):
            return True
        return False
        
class ImageItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        
    def __checkImageValue(self, value):
        if base64.b64decode(value, validate=True) == True:
            return True
        return False
        
class LocationItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        
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
        
class NumberItem(Item):
    def __init__(self, type:str = None, name:str = None, state = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        if self.__checkNumberValue(state):
            self.state = state
        
    def __checkNumberValue(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False
        
class PlayerItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        
    def __checkPlayerValue(self, value):
        if value == "PLAY" or value == "PAUSE" or value == "NEXT" or value == "PREVIOUS" or value == "REWIND" or value == "FASTFORWARD":
            return True
        return False
        
class RollershutterItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        
    def __checkRollershutterValue(self, value):
        if isinstance(value, str):
            if value == "UP" or value == "DOWN" or value == "STOP" or value == "MOVE":
                return True
            return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False
        
class StringItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)
    
    def getState(self):
        return self.state
    
    def setState(self, state:str):
        if self.__checkStringValue(state):
            self.state = state
        
    def __checkStringValue(self, value):
        if isinstance(value, str):
            return True
        return False

class SwitchItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.setState(state)
    
    def getState(self):
        return self.state
    
    def setState(self, state:str):
        if self.__checkSwitchValue(state):
            self.state = state
        
    def __checkSwitchValue(self, value):
        if value == "ON" or value == "OFF":
            return True
        return False
