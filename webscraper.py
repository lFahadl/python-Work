import requests
import string
from bs4 import BeautifulSoup
import os

def quotes(url):
    r = requests.get(url)
    if r.status_code != 200:
        print()
        return "Invalid quote resource!"
    
    try:
        print()
        return r.json()['content']
    except KeyError:
        return "Invalid quote resource!"

def verify(url):
    r = requests.get(url)
    if r.status_code != 200:
        print()
        return r.status_code


def url_verify(url):
    r = url
    rlist = r.split('/')
    if ('title' not in rlist) or ('www.imdb.com' not in rlist):
        return "\nInvalid movie page!"
    else:
        return ""

def main():
    
    page_num = int(input())
    type_news = input().split()

    loc = f"Page_{page_num}"
    os.mkdir(loc)
    os.chdir(loc)

    for i in range(1, page_num+1):
        url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={str(i)}"
        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        article_list = soup.find_all('article')


        saved_articles = []
        for article in article_list:
            type_article = article.find('span', {'data-test': 'article.type'}).text.split()

            if type_article == type_news:
                a = article.find_all('a', {'data-track-action': 'view article'})
                for i in a:
                    a_string = i.text
                    for character in string.punctuation:
                        a_string = a_string.replace(character, '')
                    file_name = a_string.replace(" ", "_") + '.txt'
                    saved_articles.append(file_name)

                    link = f"https://www.nature.com{i.get('href')}"

                    body = requests.get(link)
                    b_soup = BeautifulSoup(body.content, 'html.parser')
                    print(b_soup.prettify())
                    regular = bytes(b_soup.find('div', {'class': "c-article-body"}).text.strip(), encoding='utf-8')
                    
                    a_file = open(f"{file_name}", 'wb')
                    a_file.write(regular)
                    a_file.close()

    if os.listdir() == []:
        # os.rename(r"C:/Users/pc/Desktop/python/Page_2", r"C:/Users/pc/Desktop/python/Page_1")
        # os.chdir(r"C:/Users/pc/Desktop/python/")
        # os.rename(loc,"Page_1")
        
        os.mkdir(r"C:/Users/pc/PycharmProjects/Web Scraper2/Web Scraper/task/Page_1")

        # with open("File 1", "wb") as file_:
            # file_.write(b'')


        # print(f"Saved articles: {saved_articles}")           
        


    '''
    check = url_verify(url)
    check = verify(url)

    if check:
        print(f"The URL returned {check}!")
    else:
        r = requests.get(url)
        source = open('source.html', 'wb')
        source.write(r.content)
        source.close()
        print("Content saved.")
    '''
    '''
    if check:
        print(check)
    else:
        r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(r.content, 'html.parser')
        movie_info = {"title": soup.find("h1").text, "description": soup.find('span', {'data-testid': 'plot-l'}).text}

        print(movie_info)
    '''  

if __name__ == '__main__':
    main()