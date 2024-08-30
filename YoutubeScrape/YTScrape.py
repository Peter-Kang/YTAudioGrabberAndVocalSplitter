import pytube
import os 

class YTScrape:
    def __init__(self, links):
        self.links = links
        
    def Scrape(self):
        for link in self.links:
            try:
                yt = pytube.YouTube( link )
                # extract only audio 
                video = yt.streams.filter(only_audio=True)
                print(video)
            except Exception as error:
                print(error)
