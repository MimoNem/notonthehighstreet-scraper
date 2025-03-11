# notonthehighstreet-scraper
Parser for Not On The High Street using Scrapy framework

This repository contains a web scraper for the website "Not On The High Street," built using the Scrapy framework. The scraper is designed to extract detailed product information from the site.

You can find an article dedicated to this scraper on - [LinkedIn](https://www.linkedin.com/pulse/data-collection-web-scraping-real-world-order-example-korenevskis-cc4re/) -

## Features

- Extracts product details such as title, price, description, and more.
- Handles pagination to scrape multiple pages.
- Stores scraped data in a structured format (e.g., JSON, CSV).
- Configurable settings for ease of use and customization.

## Requirements

- Python 3.x
- Scrapy

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/MimoNem/notonthehighstreet-scraper.git
    cd notonthehighstreet-scraper
    ```

2. Create and activate a virtual environment (recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:

    ```sh
    cd notonthehighstreet-scraper
    ```

2. Run the scraper:

    ```sh
    scrapy crawl categories
    ```
    ```sh
    scrapy crawl product_links
    ```
    ```sh
    scrapy crawl product_spider
    ```

3. The scraped data will be saved in the output format specified in the Scrapy settings.

## Configuration

You can customize the scraper settings by modifying the `settings.py` file in the Scrapy project. This includes settings for user-agents, download delays, pipelines, and more.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Scrapy](https://scrapy.org/) - An open-source and collaborative web crawling framework for Python.
