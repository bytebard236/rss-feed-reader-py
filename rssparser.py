from typing import Union,List
import xml.etree.ElementTree as ET
from rssnewsobject import RssNewsObject
import requests

class RssParser:
    """This class fetches feeds from RSS feed providers and returns a List of RssNewsObject
        containings new from each feed
    """
    urlList = []
    """ stores list of RSS urls """
    newsReader = []
    """ stores the RssNewsObject returned from the url"""
    
    def __init__(self, url : Union[str,List[str]] = None ) -> None:
        if url is not None:
            self.addUrl(url)

    def addUrl(self, url : Union[str,List[str] ] )  -> None:
        """Function to add RSS Feed URL"""
        if type(url) == str:
            self.urlList.append(url)
        else:
            self.urlList.extend(url) 
    
    def fetchAllNews(self) -> List[RssNewsObject]:
        """This function iterates over all urls
            fetches the RSS feeds, and returns a List of RssNewsObjects read from the urls"""
        if len(self.urlList) > 0:
            for rss_url in self.urlList:
                self.getRSSFeed(rss_url)
        return self.newsReader

    def  getRSSFeed(self, url:str ) -> None:
        """This function takes the url of a RSS feed and parses the feed available into xml"""
        response = requests.get(url)
        if response.status_code == 200: #Request Successful
            xml_data = response.content
            root = ET.fromstring(xml_data)
            self.getNewsItemsFromRSSFeed(root)
        else:
            print(f"Failed to retrieve XML data: from  url '{url}' status code: '{response.status_code}'")

    def getNewsItemsFromRSSFeed(self,root) -> None:
        """This helper function takes the input as the xml of feed and stores all the availble news item into newsReader List"""
        newsItems = root.findall("./channel/item")
        for item in newsItems: # Iterate over the newsItems and add the objects
            newsObject = RssNewsObject()
            for childElm in item:
                if childElm.tag == "title":
                    newsObject.title = childElm.text
                elif childElm.tag == "description":
                    newsObject.description = childElm.text
                elif childElm.tag == "link":
                    newsObject.linkOrg = childElm.text
            self.newsReader.append(newsObject)




