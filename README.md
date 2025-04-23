# WikiArt Scrapy Project

This project is a web scraping tool built with Python and Scrapy to collect data from the WikiArt website. It is designed to extract artwork details, artist information, and other related data for art enthusiasts, researchers, or developers working on art-related projects.

## Features

- Scrapes artwork and artist details from WikiArt.
- Utilizes Scrapy, a fast and powerful web scraping framework.
- Modular design with customizable spiders for targeted data extraction.


## Requirements

- Python 3.6 or later
- Scrapy framework

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rjrizani/wikiart_scrapy.git
   cd wikiart_scrapy
2. Create virtual enviroment
3. Install dependencies
4. Usage:
```bash
  cd wikiart
  scrapy crawl gilbert
```

5. commant to get output csv:
```bash
scrapy crawl gilbert -o output2.csv
```

## *Problem from upwork client :

https://www.upwork.com/jobs/~021867433526407762261

I need a list of paintings by the artist Gilbert Stuart.

Here is the website: https://www.wikiart.org/en/gilbert-stuart/james-monroe-1822

You can advance to new paintings by using the white/blue buttons shown in the attached screenshot.

I want the basic facts about each painting and the image address in a Google sheet. I have entered the first six items.  https://docs.google.com/spreadsheets/d/1WetMQYdM9iEDhusA1OKK-gEAuSapBzDxOVzsQ6fIegU/edit?usp=sharing

All of the items have a title, date, and an image address. Some of them also have entries for media, location, and dimensions.

There are a total of 73 artworks.

## *Solution :
Structur html of wikiart like class or id not well-defined so I am use xpath selector to targeting each element then i am using scrapy framework since BeautifulSoup cannot handel xpath.

link github:    
https://github.com/rjrizani/wikiart_scrapy

video:  
https://www.loom.com/share/50644f1aaa0b479c9df0cbdd70ecec64

##Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance this project.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements
- Built using the Scrapy framework.
- Data sourced from WikiArt.



    

