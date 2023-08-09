# LetterboxdCrawler - A Movie Information Web Crawler

LetterboxdCrawler is a web crawler written in Python using Scrapy that extracts movie information from Letterboxd, a popular movie database and social networking site for film enthusiasts. This project allows you to gather valuable data such as movie name, year, director, genres, themes, IMDb ID, TMDB ID, and an interesting feature - histogram data.

## Features

- Extracts movie information: The crawler collects movie details such as name, year of release, director, and length from the Letterboxd website.
- Retrieves genres and themes: The crawler also captures movie genres and themes associated with each film, providing insight into the movie's content and style.
- IMDb and TMDB IDs: The crawler fetches the IMDb ID and TMDB ID, allowing you to cross-reference additional information from these popular movie databases.
- Histogram data: One of the standout features of this project is its ability to store histogram data, which indicates the distribution of ratings for each movie.

## Installation

To use this movie information web crawler, follow these steps:

1. Install Python: Make sure you have Python 3.x installed on your system.
2. Install Scrapy: You can install Scrapy using pip by running `pip install scrapy`.
3. Clone the repository: Clone this GitHub repository to your local machine using `git clone https://github.com/behzadsabeti/LetterboxdCrawler.git`.
4. Navigate to the project directory: Use the `cd LetterboxdCrawler` command to change to the project directory.

## Usage

To run the spider and extract movie information, open a terminal or command prompt and navigate to the project directory. Use the following commands:

1. To save the data in JSON format, run:
   `scrapy crawl MovieDetail -o data_letterboxd.json`
2. To save the data in CSV format, run:
   `scrapy crawl MovieDetail -o data_letterboxd.csv`
   
The extracted movie information will be stored in the respective output file (data_letterboxd.csv) in the project directory.

## Sample Data

```json
{
    "name": "Fight Club",
    "year": "1999",
    "director": "David Fincher",
    "length": "139",
    "genres": [
        "drama"
    ],
    "themes": [
        "Intense violence and sexual transgression",
        "Politics and human rights",
        "future, sci-fi, technology, action or technological",
        "political, democracy, documentary, president or propaganda",
        "sexuality, sex, disturbed, unconventional or challenging",
        "violence, shock, disturbing, brutal or graphic",
        "boxing, fighting, champion, sports or fighter"
    ],
    "imdb_id": "tt0137523",
    "tmdb_id": "550",
    "histogram": [
        2481,
        6415,
        3220,
        21273,
        17610,
        116291,
        126030,
        475883,
        285577,
        663782
    ]
}
```
## Contributing
Contributions to this project are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

## License
This project is licensed under the MIT License. 

## Acknowledgments
Special thanks to the Scrapy community and the Letterboxd website for providing valuable movie information.
