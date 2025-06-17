# Import required libraries
import requests                   # For sending HTTP requests to the website
from bs4 import BeautifulSoup     # For parsing HTML content
import pandas as pd               # For storing and exporting data as CSV

# Define the base URL of the website (books.toscrape.com)
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# Initialize an empty list to store data about books
books = []

# Loop through the first 5 pages of the site (you can increase the range)
for page in range(1, 6):
    # Format the URL with the current page number
    url = base_url.format(page)

    # Send a GET request to the page and get the response
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all book containers on the page
    items = soup.find_all('article', class_='product_pod')

    # Loop through each book container to extract details
    for item in items:
        # Get the book title from the 'title' attribute of the <a> tag inside <h3>
        title = item.h3.a['title']

        # Get the book price (removing the '£' symbol using slicing)
        price = item.find('p', class_='price_color').text[2:]

        # Get availability status (strip() removes unwanted spaces/newlines)
        availability = item.find('p', class_='instock availability').text.strip()

        # Get the rating by extracting the second class (e.g., 'Three') from the <p> tag
        rating_class = item.find('p')['class'][1]

        # Append the extracted data as a dictionary to the books list
        books.append({
            'Title': title,
            'Price (£)': price,
            'Availability': availability,
            'Rating': rating_class
        })

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(books)

# Save the DataFrame as a CSV file
df.to_csv('books_data.csv', index=False)

# Print confirmation
print("✅ Scraping complete. Data saved to books_data.csv")
