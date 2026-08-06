# DS605 Lab Assignment 1
## Web Scraping and Data Analysis using Scrapy

### Objective
This project scrapes book data from https://books.toscrape.com using Scrapy.

### Dataset
- Website: https://books.toscrape.com
- Pages Scraped: 5
- Total Books: 100

### Extracted Fields
- Title
- Category
- Price
- Rating
- Availability
- Description
- UPC
- Number of Reviews
- Product URL

### Data Preprocessing
- Removed duplicate records
- Filled missing descriptions
- Converted prices to numeric values
- Converted ratings into numerical format
- Extracted stock quantity
- Created new features:
  - Price Band
  - Description Word Count
  - Value Score

### Visualizations
- Price Distribution
- Rating Distribution
- Average Price by Category
- Price vs Rating
- Word Cloud

### Technologies Used
- Python
- Scrapy
- Pandas
- Matplotlib
- WordCloud

### Author
202618029
Ummehani Khatri
DA-IICT(DAU)