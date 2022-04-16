'''
def xor(a, b):
    # Write your code here
   return not ((a and b) or (not (a or b)))

print(xor("", ["7", 5]))
'''
'''
def wrong_password(password):
    a = (password == "" or (not password and real_password))
    return a or password != real_password
'''
'''
import requests

from bs4 import BeautifulSoup

index = int(input())
url = input()

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
soup.prettify()

subtitles = soup.find_all('h2')

print(subtitles[index].text)
'''
'''
import requests

from bs4 import BeautifulSoup

url = input()

r = requests.get(url)

soup = BeautifulSoup(r, 'html.parser')
soup.prettify()

print(soup.find('h1').text)
'''
'''
import requests

from bs4 import BeautifulSoup

index = int(input()) - 1
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')
print(links[index].get('href'))
'''
'''
import requests

from bs4 import BeautifulSoup

index = int(input()) - 1
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')

#print(links[index].get('href'))
#print(f"#act{index}")

#for i in links:
#    print(i.get('href'))
'''
# import requests

# from bs4 import BeautifulSoup

'''
r = requests.get('https://newsineasyenglish.com/2018/05/13/air-pollution/')

print(r.status_code) 
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
'''
'''
# grinning face
print("\U0001f600")
 
# grinning squinting face
print("\U0001F606")
 
# rolling on the floor laughing
print("\U0001F923")
'''
'''
a = int(input())
a_ = chr(a)
b = int(input())
b_ = chr(b)
c = int(input())
c_ = chr(c)
d = int(input())
d_ = chr(d)
print(a_ + b_ + c_ + d_)
'''
'''
#obj = input()
integer = int(input())

final = (integer).to_bytes(2, byteorder='big')
print(final[0] + final[1])
'''
'''
r_animals = open("animals.txt", "r", encoding='utf-8')
w_animals = open("animals_new.txt", "w", encoding='utf-8')
for i in r_animals:
    w_animals.write(i)
r_animals.close()
w_animals.close()
'''
'''
color_list = ['cyan', 'magenta', 'yellow', 'key color']

cymk_file = open('animals.txt', 'w', encoding='utf-8')
cymk_file.writelines(color_list)
cymk_file.close()
'''
'''
import string
import os

story = "Legendary Arecibo telescope will close forever — scientists are reeling"

na_string = '!hi. wh?at is the weat[h]er lik?e.'

new_string = story.replace('—', '').replace('  ', ' ').replace(' ', '_')
print(new_string)

#new_string = new_string.replace(" ", "_")

#print(story)

os.mkdir('folderrrrrrr')
'''
import os
import sys

# args = sys.argv

# if len(args) > 1:
#     directory = args[1]
#     for root, dirs, files in os.walk(directory, topdown=False):
#         for name in files:
#             print(os.path.join(root, name))
# else:
#     print('Directory is not specified')
 

args = sys.argv
if not len(args) > 1:
    print("Directory is not specified")
else:
    for root, dirs, files in os.walk(args[1], topdown=False):
        # for name in dirs:
        #     if not name:
        #         print(os.path.join(root, name))
        for name in files:
            print(os.path.join(root, name))


