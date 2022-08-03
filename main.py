from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

City = input(str("Enter City: \n"))
Max_Rent = input(str("Enter Max Rent : \n"))
Max_Credit = input(str("Enter Max Credit : \n"))
url = "https://divar.ir/s/"

url = url + City + '/rent-residential?credit=-' + Max_Credit + '&rent=-' + Max_Rent
# print(url)
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
# soup = BeautifulSoup(page.content, 'html5lib')
posts = soup.find("div", { "class" : "browse-post-list" })
# print(len(posts))

def get_posts(posts):
    post_datas = []
    for post in posts:
        post_description = post.find_all("div", { "class" : "kt-post-card__description" })
        # print(type(post_description))
        post_description = list(post_description)
        post_credit = post_description[0].text.strip()
        post_rent = post_description[1].text.strip()
        post_credit = post_credit.replace("تومان", "").replace("ودیعه:", "").strip().replace(",", "")
        post_rent = post_rent.replace("تومان", "").replace("اجارهٔ ماهانه:", "").strip().replace(",", "")
        post_title = post.find("h2", { "class" : "kt-post-card__title" }).text.strip()
        post_link = post.find("a")['href']
        post_link = 'https://divar.ir' + post_link
        post_data = {
            'title': post_title,
            'credit' : post_credit,
            'rent' : post_rent,
            'link' : post_link,
        }
        post_datas.append(post_data)
        # print(post_credit)
        # print(post_rent)
        # print(post_title)
        # print(post_link, '\n')
        # break
    return post_datas
        
last_post = None
all_posts = None
idx = 0
while(True):
    if idx == 0 :
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        all_posts = get_posts(posts=posts)
        last_post = {
            'title': all_posts[0]['title'],
            'credit' : all_posts[0]['credit'],
            'rent' : all_posts[0]['rent'],
            'link' : all_posts[0]['link'],
        }
    print(last_post)
    time.sleep(900)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    all_posts = get_posts(posts=posts)
    temp_post = {
            'title': all_posts[0]['title'],
            'credit' : all_posts[0]['credit'],
            'rent' : all_posts[0]['rent'],
            'link' : all_posts[0]['link'],
        }
    
    if temp_post['title'] != last_post['title']  :
        last_post = {
            'title': all_posts[0]['title'],
            'credit' : all_posts[0]['credit'],
            'rent' : all_posts[0]['rent'],
            'link' : all_posts[0]['link'],
        }
        print(last_post)
    idx += 1
