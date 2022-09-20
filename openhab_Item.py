class Item(object):
    def __init__(self, type:str = None, name:str = None, tags:list = None, groups:list = None):
        self.type = type
        self.name = name
        self.tags = tags
        self.groups = groups
    
    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
    
    def getTags(self):
        return self.tags
    
    def getGroups(self):
        return self.groups
    
    def setType(self, type:str):
        self.type = type
        
    def setName(self, name:str):
        self.name = name
        
    def setTags(self, tags:list):
        self.tags = tags
        
    def setGroups(self, groups:list):
        self.groups = groups
        
class StringItem(Item):
    def __init__(self, type:str = None, name:str = None, state:str = None, tags:list = None, groups:list = None):
        super().__init__(type, name, tags, groups)
        self.state = state
    
    def getState(self):
        return self.state
    
    def setState(self, state:str):
        self.state = state
