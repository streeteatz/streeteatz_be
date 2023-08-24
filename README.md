
[![Contributors](https://img.shields.io/github/contributors/streeteatz/streeteatz_be.svg)](https://github.com/streeteatz/streeteatz_be/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/streeteatz/streeteatz_be.svg)](https://github.com/streeteatz/streeteatz_be/forks)
[![Stargazers](https://img.shields.io/github/stars/streeteatz/streeteatz_be.svg)](https://github.com/streeteatz/streeteatz_be/stargazers)
[![Issues](https://img.shields.io/github/issues/streeteatz/streeteatz_be.svg)](https://github.com/streeteatz/streeteatz_be/issues)

# StreetEatz

![](streeteatz/images/favicon.png)

## About This Project
### Important to Note

This is the back end repository for a full stack application that uses SOA. Here is the link to the StreetEatz organization where both back end and front end repositories can be found:

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/streeteatz)

### Mod 4 Capstone Project

StreetEatz is an app that allows users to find food truck vendors in the area. Food truck owners are also able to join and manage the many different items that they offer to customers. Also allows users to rate and add favorite vendors to their dashboard so they can revisit in the future.

## Purpose

The purpose of the back end for the StreetEatz app is to build APIs and stores the database so that the front end can utilize the data to build the app.

<b><u>Data Management:</u></b>The back end serves as the central hub for storing, organizing, and managing the data associated with user ratings, favorited food trucks, food truck menu items, and food truck information (location, hours, wait time, and a description of what they offer). It provides the necessary infrastructure and databases to efficiently handle the large volume of information generated by the app's food truck vendors.

Overall, the purpose of the back end in the StreetEatz app is to support seamless data management. It plays a vital role in ensuring the app's functionality, enhancing the experience of users searching for available food truck vendors in their area.

## Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
* ![Postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
* ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
* ![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
* [![Miro Board](https://img.shields.io/badge/Miro-050038?style=for-the-badge&logo=Miro&logoColor=white)](https://miro.com/app/board/uXjVM468His=/)
* ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)

## Running On
* Python 3.11.4
* Django 4.2.3

## <b>Getting Started</b>

To get a local copy, follow these simple instructions:

### <b>Installation</b>

1. Fork the project
2. Clone the repo
```
git clone https://github.com/streeteatz/streeteatz_be
```
3. Create a virtual environment
```
python3 -m venv <name of your environment>
```
4. Activate your virtual environment
```
source <name of your environment>/bin/activate
```
5. Install packages
```
pip install -r requirements.txt
```
6. Generate a secret key
```
```
7. Run the migrations
```
python3 manage.py migrate
```
8. Comment the CORS_ALLOWED_ORIGINS in streeteatz_be/settings.py (line 116-122) back in. This is necessary for the front end to access the data

## Endpoints Used

<div style="overflow: auto; height: 200px;">
  <pre>
    <code>
      GET '/vendors' - All Vendors
      GET '/items' - All Vendors' Items
      GET '/vendors/:vendor_id' - Vendor Detail
    </code>
  </pre>
</div>

- Response

<div style="overflow: auto; height: 200px;">
  <pre>
    <code>

    All Vendors
    https://streeteatz-be-b15261620498.herokuapp.com/vendors/

    {
      "data": {
        "attributes": [
          {
          "id": 7,
          "name": "Mac and Noodles",
          "phone_number": "303-204-8782",
          "location": "73.98234, 40.92487",
          "address": "500 E 17th Ave Denver, CO",
          "status": false,
          "hours": "11:00-3:00pm, 5:00-9:00pm",
          "description": "This MacNCheese is to die for!",
          "tags": "#macaroni #cheese #noodles #macncheese",
          "website": "www.macandnoodles.com",
          "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCbkk2SnZiVNK_HNPiPZX9KTlp2tsTNQbWQmxEXiYJzLxlu1MZuLpeO5Iorsor_gV2fSs&usqp=CAU",
          "wait_time": 10,
          "upvote": false,
          "downvote": false,
          "favorited": false,
          "up_rating": 666,
          "down_rating": 12,
          "distanceFromUser": 0
          },

          {
          "id": 10,
          "name": "Deja Roux Cajun & Soul",
          "phone_number": "303-883-3703",
          "location": "70.9837, 38.92847",
          "address": "1911 Sheridan Blvd Edgewater, Co 80214",
          "status": false,
          "hours": "11:00-3:00pm, 5:00-9:00pm",
          "description": "Looking for some delicious soul food? This is the place!",
          "tags": "#cajun #soulfood #delicious",
          "website": "www.dejaroux.com",
          "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfFwFwQQ-zf9O3IFYL4yr6LFoYLk2Cs3tIdQ&usqp=CAU",
          "wait_time": 20,
          "upvote": false,
          "downvote": false,
          "favorited": false,
          "up_rating": 0,
          "down_rating": 0
          },...
        ]
      }
    }

All Vendors' Items
https://streeteatz-be-b15261620498.herokuapp.com/items/

{
  "data": {
    "attributes": [
      {
      "id": 1,
      "name": "Classic Banana",
      "price": "6.00",
      "description": "100% banana, frozen then whipped to perfection! Add your favorite toppings (separate)",
      "vendor": 1
      },
      {
      "id": 2,
      "name": "Mixed Berry Banana",
      "price": "6.00",
      "description": "Banana + strawberry + blackberry frozen then whipped to perfection! Add your favorite toppings (separate)",
      "vendor": 1
      },...
    ]
  }
}

Vendor Details
https://streeteatz-be-b15261620498.herokuapp.com/vendors/1/


{
  "data": {
    "attributes": {
      "id": 1,
      "name": "Ba-Nom-a-nom",
      "phone_number": "970-682-4666",
      "location": "72.37946, -37.87633",
      "address": "2900 Market St Denver, CO 80205",
      "status": false,
      "hours": "5:00-9:00pm",
      "description": "Best desserts you have ever had, and they happen to be vegan!",
      "tags": "#desserts #vegan #healthy #fruit",
      "website": "www.banomanom.com",
      "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3hJWqZUQ1y5-opPj2noXiCtn14Gpz4dSOz5uKKAD2UvTVeWxtld49cOhCwj9O4Mcg0-I&usqp=CAU",
      "wait_time": 20,
      "upvote": false,
      "downvote": false,
      "favorited": false,
      "up_rating": 88,
      "down_rating": 6,
      "distanceFromUser": 0
    }
  }
}
    </code>
  </pre>
</div>

## Schema

![](streeteatz/images/schema.png)

## Authors
* Isaac Thill [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/ithill22) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](www.linkedin.com/in/isaac-thill)
* Reilly Miller [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/rmiller220) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/reilly-miller-6b6131266/)
* Angel Byun [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/angelbyun) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/angel-byun/)
* Patrick Ankiewicz [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/Pma913)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/patrick-ankiewicz/)
* Em Lindvall  [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/emlindvall)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/emlindvall/)
* Devynne Marshall [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/Devynnem)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/devynnemarshall/)
* Jacob McFarlane [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/JacobMacFarlane)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/jacob-macfarlane-052593261/)


### Future Features

1. Allow login for both users and vendors
2. Consume API and utilize geolocation to give a map with accurate distance between user and vendor
3. Create new routes to include ```PATCH```, ```POST```, and ```DELETE``` actions for the vendors to be able to update their menus and any details that pertain to their business. 
4. Create new routes to allow users to add and remove vendors to their favorites. This might be done by creating a new joins table for favorites and removing the favorites attribute from vendors. 