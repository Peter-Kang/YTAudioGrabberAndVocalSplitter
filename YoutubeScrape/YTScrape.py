import yt_dlp
import os 

class YTScrape:
    def __init__(self, links, dest):
        self.links = links
        self.dest = dest
        
    def download_audio(self, link):
        with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}) as video:
            info_dict = video.extract_info(link, download = True)
            video_title = info_dict['title']
            print(video_title)
            video.download(link)    
            

    def Scrape(self):
        for link in self.links:
            try:
                #download youtube
               self.download_audio(link)

            except Exception as error:
                print(error)
