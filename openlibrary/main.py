from bs4 import BeautifulSoup
import requests
from connection_db import AppContext
from functions import soup_response


list_categories_url = "https://openlibrary.org/subjects"
list_books_per_category = "https://openlibrary.org/search?subject="
end_point = "https://openlibrary.org"

# Récupération de la liste des catégories


soup = soup_response(list_categories_url)

subject = soup.find('div', id="subjectsPage")


categories = BeautifulSoup(str(subject), 'html.parser').find_all('li')
categories = [category.get_text() for category in categories][:-9]



for i in range(len(categories)):
    categories[i] = f'{list_books_per_category}{categories[i].strip()}&page=1'


books_link_detail_page = []


# Récupération des livres par catégorie
for category in categories[:1]:
    soup = soup_response(category)
    attributes = {
        "class":"results",
        "itemprop": "url"
    }

    book_link_detail_page = [f"{end_point}{link['href'].strip()}" for link in soup.find_all('a', attrs=attributes)]
    books_link_detail_page.extend(book_link_detail_page)

for link in books_link_detail_page:
    data = []
    soup=soup_response(link)
    attribute_title = {
        "class":"work-title",
        "itemprop": "name"
    }
    attribute_isbn = {
        "class":"work-title",
        "itemprop": "name"
    }
    attribute_author = {
        "class":"edition-byline",
        "itemprop": "author"
    }
    
    attribute_descrition  = {
        "class":"book-description-content",
        
    }
    
    attribute_theme = {
        "class":"work-title",
        "itemprop": "name"
    }
    
    attribute_genre = {
        "class":"clamp",
    }
    attribute_annee_publication = {
        "class":"edition-omniline-item",
        "itemprop": "datePublished"
    }
    attribute_nbre_editions = {
        "class":"work-title",
        "itemprop": "name"
    }
    attribute_langue = {
        "class":"language",
        "itemprop": "inLanguage"
    }
    attribute_avg_rate = {
        "class":"avg-ratings",
        "itemprop": "ratingValue"
    }
    attribute_nbre_rate = {
        "class":"readers-stats__review-count",
        "itemprop": "reviewCount"
    }
    title = soup.find('h1',attrs=attribute_title).get_text
    isbn = soup.find('dd', attrs=attribute_isbn).get_text
    author = soup.find('h2', attrs=attribute_author).get_text
    description = soup.find('p', attrs=attribute_descrition).get_text
    themes = soup.find_all('a', attrs=attribute_theme).get_text
    #genre = soup.find('span', class="reviews__value").get_text
    annee_publication = soup.find('span', attrs=attribute_annee_publication).get_text
    #enbre_editions = soup.find('dd', attrs=attribute_nbre_editions).get_text
    langue = soup.find('span', attrs=attribute_langue).get_text
    avg_rating = soup.find('span', attrs=attribute_avg_rate).get_text
    nbre_rate = soup.find('span', attrs=attribute_nbre_rate).get_text





