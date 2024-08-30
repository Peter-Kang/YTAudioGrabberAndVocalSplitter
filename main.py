from FileIO.ReadLinks import ReadLinks 
from YoutubeScrape.YTScrape import YTScrape

def main():
    print("Reading Links")
    links = ReadLinks().ReadIn();
    print(f"Pulled in [{len(links)}] Links")
    print("Pulling Data")
    scrape = YTScrape(links).Scrape();
    print("Splitting Vocals from Instrumental")

main()