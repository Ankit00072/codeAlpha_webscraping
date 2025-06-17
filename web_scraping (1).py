{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5fec57d4-feef-426d-a5c6-c0076f28ec0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Scraping complete. Data saved to books_data.csv\n",
      "Products found: 100\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# Base URL\n",
    "base_url = 'http://books.toscrape.com/catalogue/page-{}.html'\n",
    "\n",
    "books = []\n",
    "\n",
    "# Scrape first 5 pages (you can increase this)\n",
    "for page in range(1, 6):\n",
    "    url = base_url.format(page)\n",
    "    response = requests.get(url)\n",
    "    soup = BeautifulSoup(response.content, 'html.parser')\n",
    "\n",
    "    items = soup.find_all('article', class_='product_pod')\n",
    "\n",
    "    for item in items:\n",
    "        title = item.h3.a['title']\n",
    "        price = item.find('p', class_='price_color').text[2:]  # Remove '£'\n",
    "        availability = item.find('p', class_='instock availability').text.strip()\n",
    "        rating_class = item.find('p')['class'][1]  # e.g., 'Three'\n",
    "        \n",
    "        books.append({\n",
    "            'Title': title,\n",
    "            'Price (£)': price,\n",
    "            'Availability': availability,\n",
    "            'Rating': rating_class\n",
    "        })\n",
    "\n",
    "# Save to CSV\n",
    "df = pd.DataFrame(books)\n",
    "df.to_csv('books_data.csv', index=False)\n",
    "print(\"✅ Scraping complete. Data saved to books_data.csv\")\n",
    "print(\"Products found:\", len(books))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de5d96fa-94b4-4d61-b290-55a5b89758f6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
