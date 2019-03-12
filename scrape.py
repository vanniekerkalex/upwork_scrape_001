import requests
from bs4 import BeautifulSoup
from csv import writer
from csv import reader


# response = requests.get('http://codedemos.com/sampleblog/')
# soup = BeautifulSoup(response.text, 'html.parser')
# posts = soup.find_all(class_='post-preview')

empty = ""
entries = 0
link_count = 0

data = []
header = ['Full Name', 'First Name', 'Last Name', 'Title', 'Phone', 'Mobile	Email', 'Agency', 'Address',
          'City', 'State', 'Postcode', 'Page URL']

f = open('links.txt', 'r')
links = f.readlines()
f.close()

# a = "https://www.raywhite.com/contact/?type=People&target=people&suburb=ABBA+RIVER%2C+WA+6280&radius=50&firstname=&lastname=&_so=contact"

with open('data.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(header)

    for link in links:

        link_count += 1
        response = requests.get(link, headers={'User-agent': 'your bot 0.1'})
        soup = BeautifulSoup(response.text, 'html.parser')
        raw_data = soup.find_all(class_='list-group')

        for post in raw_data:

            # Get all the agency information
            agency = post.find(class_='no-text-transform').get_text().strip()
            # Get the address info from the agency information
            address = post.find(
                'address').next_element.replace('·', '').strip()
            # Split the address into a list by removing the commas
            address = address.rsplit(', ', 2)
            # Split the territory and postcode
            temp = address[-1].rsplit(' ', 1)
            # Removes the territory and postcode as it's a single string
            del address[-1]
            # Appends to the address list the territory and postcode
            address.append(temp[0])
            address.append(temp[1])

            city = address[1]
            state = address[2]
            postcode = address[3]

            agents = post.find_all(class_='card horizontal-split vcard')

            for agent in agents:

                try:
                    agent_fullname = agent.find(
                        class_='agent-name').get_text().strip()
                    agent_firstname = (agent_fullname.split())[0]
                    agent_lastname = (agent_fullname.split())[-1]
                except:
                    agent_fullname = empty
                    agent_firstname = empty
                    agent_lastname = empty

                try:
                    agent_role = agent.find(
                        class_='agent-role').get_text().strip()
                except:
                    agent_role = empty

                try:
                    agent_mobile_data = agent.find(class_='agent-mobile')
                    try:
                        agent_mobile = agent_mobile_data.find('a').get_text()
                    except:
                        agent_mobile = empty
                except:
                    agent_mobile = empty

                try:
                    agent_officenum_data = agent.find(class_='agent-officenum')
                    try:
                        agent_officenum = agent_officenum_data.find(
                            'a').get_text()
                    except:
                        agent_officenum = empty
                except:
                    agent_officenum = empty

                try:
                    agent_email_data = agent.find(class_='email')
                    try:
                        agent_email = agent_email_data.find(
                            'a', href=True).get('href').replace('mailto:', '')
                    except:
                        agent_email = empty
                except:
                    agent_email = empty

                data.append([agent_fullname, agent_firstname, agent_lastname, agent_role,
                             agent_officenum, agent_mobile, agency, address[0], city, state, postcode, link.strip()])

                csv_writer.writerow([agent_fullname, agent_firstname, agent_lastname, agent_role,
                                     agent_officenum, agent_mobile, agency, address[0], city, state, postcode, link.strip()])

                entries += 1
                print("Links: " + str(link_count) +
                      " Entries: " + str(entries))

            # header = ['Full Name', 'First Name', 'Last Name', 'Title', 'Phone', 'Mobile	Email', 'Agency', 'Address',
            #           'City', 'State', 'Postcode', 'Page URL']

# print(data)
# print(len(data))

# with open('data.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = header
#     csv_writer.writerow(headers)

    # for each in data:
    #     csv_writer.writerow(each)
