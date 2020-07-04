# SongsSearch
There are many search engines for search Songs lyrics for people who love the music. All of
them are in the English language. Currently, no implementation to **Sinhala language**. This
project aims to build a simple lyrics retrieval system using IR and NLP concepts on the phrase
of lyrics or Metadata of lyrics.
This project is based on [elastic](https://www.elastic.co/ "elastic") search. [Kibana](https://www.elastic.co/kibana "Kibana") is used to explore the data in here. In below show the fields of the Songs in retrival data.
- lyrics: Lyrics of the song that each line separate by \n
- artist: List of Artist(s) of the song
- movie: If the songs belong to a movie that movie containing here
- name: Name of the song
- genere: List of genres of the song
- views: no of views for the song in the original site
- shares: Number of Shares of the song in the original site
- lyrics by: List of Lyrics writer(s) of the song
- music by: List of music director(s) of the song

# System Architecture
![System Architecture](https://github.com/PinsaraKWeerasinghe/SongsSearch/blob/master/System_Architecture.png "System Architecture")

#Four main steps in the project
1. Scraping - Scrapy 
2. Json converting - Python
3. Indexing - Elasticsearch and Kibana  
4. Searching - Flask 

#1. Scraping
Scraping is doing in SongsSearch/ScrapeSongsComponent/Scrape_Scrapy/ directory. in here using [SinhalaSongbook.com](https://sinhalasongbook.com/ "SinhalaSongbook.com") website to scrape data. move your comand line derectory to above derectory and run follwing command.
`scrapy crawl sinhala_songs_lyrics_spider  -o data.json`
It will crate a .json file that include all scraped data.
