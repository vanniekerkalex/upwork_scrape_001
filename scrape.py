import requests
from bs4 import BeautifulSoup
from csv import writer
from csv import reader


# response = requests.get('http://codedemos.com/sampleblog/')
# soup = BeautifulSoup(response.text, 'html.parser')
# posts = soup.find_all(class_='post-preview')


data = []
header = ['Full Name', 'First Name', 'Last Name', 'Title', 'Phone', 'Mobile	Email', 'Agency', 'Address',
          'City', 'State', 'Postcode', 'Page URL']

f = open('links.txt', 'r')
links = f.readlines()
f.close()

a = "https://www.raywhite.com/contact/?type=People&target=people&suburb=ABBA+RIVER%2C+WA+6280&radius=50&firstname=&lastname=&_so=contact"

# for link in links:
#response = requests.get(a)

response = requests.get(a, headers={'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(response.text, 'html.parser')
raw_data = soup.find_all(class_='list-group')

for post in raw_data:
    agency = post.find(class_='no-text-transform').get_text().replace('\n', '')
    address = post.find('address').next_element.replace('\n', '')

    print(agency)
    print(address)

# with open('posts.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['Title', 'Link', 'Date']
#     csv_writer.writerow(headers)

#     for post in posts:
#         title = post.find(class_='post-title').get_text().replace('\n', '')
#         link = post.find('a')['href']
#         date = post.select('.post-date')[0].get_text()
#         csv_writer.writerow([title, link, date])
