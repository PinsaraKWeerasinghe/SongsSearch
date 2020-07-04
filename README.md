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
```
scrapy crawl sinhala_songs_lyrics_spider  -o data.json
```
It will crate a .json file that include all scraped data.

#2. Json converting
JSON converter Scraped result is with unicode and it is not capable of using for the BULK API of the Elasticsearch. Therefore according to the reqired format of the BULK API the lyrics document file is genrated by running "bulk_unicode_converter.py" of the SongsSearch/ScrapeSongsComponent/BulkJsonGenerator/ directory.
```
python bulk_unicode_converter.py
```
#3. Indexing
The index creating mapping and settings are in the "settings.json" file in the SongsSearch/SongsSearchComponent/ directory. Use kibana to create index by copying and pasting the command of the "settings.json". You can simply add all song documents by running  the folowing command within the SongsSearch/ScrapeSongsComponent/BulkJsonGenerator/ directory. The index name is "map_v5"
```
curl -H "Content-Type: application/json" -XPOST "localhost:9200/map_v5/_bulk?pretty&refresh" --data-binary "@bulk_lyrics_objects.json"
```
# 4. Searching
Searching Before run the flask app the "singling" library should be installed in the computer. For that, download the library from the followin URL and add the path of the root directory of the library to the PYTHONPATH as mentioned in the library's repo readme. For run the library there are few dependencies ahould be installed ; "emoji","nltb" python libraries. https://github.com/ysenarath/sinling

Now run the flask app in SongsSearch/SongsSearchComponent/ derectory.

Search and enjoy Sinhala lyrics from "http://localhost:5000/".
