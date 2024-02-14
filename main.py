from rssparser import RssParser


def main():
    """Driver function"""
    myRssParser = RssParser()

    """
    Adding sample rss website urls
    myRssParser.addUrl(r"https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    myRssParser.addUrl(r"https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    
    """

    while(True):
        usrInp = handleUserInput()
        if(usrInp == 1):
            rssUrl = input("Enter URL: ")
            myRssParser.addUrl(rssUrl)
        elif usrInp == 2:
            rssFeeds = myRssParser.fetchAllNews()
            for news in rssFeeds:
                print(f"Tile: {news.title}")
                print(f"Description: {news.description}")
                print(f"Link: {news.linkOrg}")
        elif usrInp == 3:
            break
        else:
            print("Invalid input Recieved. Please retry")


def handleUserInput():
    print("1. Add URL")
    print("2. Fetch and Display Latest news")
    print("3. Exit")
    usrInput = input("Enter your choice: ")
    return int(usrInput)
    
if __name__ == "__main__":
    main()