class RssNewsObject:
    """ Container class to hold RSS news attributes"""
    title=None
    description=None
    linkOrg=None

    def __init__(self,title:str='',description:str='',linkOrg:str='') -> None:
        self.__setattr__("title",title)
        self.__setattr__("description",description)
        self.__setattr__("linkOrg",linkOrg)
    
    def __str__(self) -> str:
        if self.title is None:
            self.title = 'N/A'
        if self.description is None:
            self.description = 'N/A'
        if self.linkOrg is None:
            self.linkOrg = 'N/A'
        return "[title='"+self.title+"', Description='"+self.description+"', Link='"+self.linkOrg+"']"