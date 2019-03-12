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

    # Get all the agency information
    agency = post.find(class_='no-text-transform').get_text().strip()
    # Get the address info from the agency information
    address = post.find('address').next_element.replace('·', '').strip()
    # Split the address into a list by removing the commas
    address = address.rsplit(', ', 2)
    # Split the territory and postcode
    temp = address[-1].rsplit(' ', 1)
    # Removes the territory and postcode as it's a single string
    del address[-1]
    # Appends to the address list the territory and postcode
    address.append(temp[0])
    address.append(temp[1])

    print(agency)
    print(address)

    agents = post.find_all(class_='card horizontal-split vcard')

    for agent in agents:
        agent_name = agent.find(class_='agent-name').get_text().strip()
        agent_role = agent.find(class_='agent-role').get_text().strip()
        agent_mobile = agent.find(class_='agent-mobile')
        agent_mobile2 = agent_mobile.find('a').get_text()
        # agent_officenum = agent.find(
        #     class_='agent-officenum').next_element.get_text().strip()
        # agent_email = agent.find(class_='agent-email')

        # li = soup.find('li', {'class': 'text'})
        # children = li.findChildren("a", recursive=False)

        print(agent_name)
        print(agent_role)
        print(agent_mobile2)
        # print(agent.prettify())

# with open('posts.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['Title', 'Link', 'Date']
#     csv_writer.writerow(headers)

#     for post in posts:
#         title = post.find(class_='post-title').get_text().replace('\n', '')
#         link = post.find('a')['href']
#         date = post.select('.post-date')[0].get_text()
#         csv_writer.writerow([title, link, date])
