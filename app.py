from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')

# 프로젝트 관련 함수(이름)으로 바꿈
def get_beer():
    # 요청할 정보의 api를 가져옴
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    # api 를 -> json(javaScript Object Notation) 으로 파씽해주는 방법
    beerjson = r.json()
    # beer 라는 객체에 api에서 가져오고 json으로 바꿔준 정보를 저장함
    beer = {
        'name': beerjson[0]['name'],
        'abv': beerjson[0]['abv'],
        'desc': beerjson[0]['description'],
        'foodpair': beerjson[0]['food_pairing'][0]
    }

    # 왜? [0]['name'] ? = 보면 리스트안에 {} 라고 0번째 리스트에서 [name] 을 찾겠다는 거임
#     [
#   {
#     "id": 192,
#     "name": "Punk IPA 2007 - 2010",
#     "tagline": "Post Modern Classic. Spiky. Tropical. Hoppy.",
#     "first_brewed": "04/2007",
#     "description": "Our flagship beer that kick started the craft beer revolution. This is James and Martin's original take on an American IPA, subverted with punchy New Zealand hops. Layered with new world hops to create an all-out riot of grapefruit, pineapple and lychee before a spiky, mouth-puckering bitter finish.",
#     "image_url": "https://images.punkapi.com/v2/192.png",
#     "abv": 6.0,
#     "ibu": 60.0,
#     "target_fg": 1010.0,
#     "target_og": 1056.0,
#     "ebc": 17.0,
#     "srm": 8.5,
#     "ph": 4.4,
#     "attenuation_level": 82.14,
#     "volume": {
#       "value": 20,
#       "unit": "liters"
#     },
#     "boil_volume": {
#       "value": 25,
#       "unit": "liters"
#     },
#     "method": {
#       "mash_temp": [
#         {
#           "temp": {
#             "value": 65,
#             "unit": "celsius"
#           },
#           "duration": 75
#         }
#       ],
#       "fermentation": {
#         "temp": {
#           "value": 19.0,
#           "unit": "celsius"
#         }
#       },
#       "twist": null
#     },
#     "ingredients": {
#       "malt": [
#         {
#           "name": "Extra Pale",
#           "amount": {
#             "value": 5.3,
#             "unit": "kilograms"
#           }
#         }
#       ],
#       "hops": [
#         {
#           "name": "Ahtanum",
#           "amount": {
#             "value": 17.5,
#             "unit": "grams"
#            },
#            "add": "start",
#            "attribute": "bitter"
#          },
#          {
#            "name": "Chinook",
#            "amount": {
#              "value": 15,
#              "unit": "grams"
#            },
#            "add": "start",
#            "attribute": "bitter"
#          },
#          ...
#       ],
#       "yeast": "Wyeast 1056 - American Ale™"
#     },
#     "food_pairing": [
#       "Spicy carne asada with a pico de gallo sauce",
#       "Shredded chicken tacos with a mango chilli lime salsa",
#       "Cheesecake with a passion fruit swirl sauce"
#     ],
#     "brewers_tips": "While it may surprise you, this version of Punk IPA isn't dry hopped but still packs a punch! To make the best of the aroma hops make sure they are fully submerged and add them just before knock out for an intense hop hit.",
#     "contributed_by": "Sam Mason <samjbmason>"
#   }
# ]
      
    #print(beer)
    return render_template('index.html', beer=beer)
    # beer = beer 뜻 : 앞의 beer 라는 객체는 html 파일에서 {{beer.~~}}만들고 값을 전달해주는 키 값
    # 뒤의 beer는 랜더링된 페이지에 포함하기 위해 템플릿에 전달해주는 value 값
     
 
#set FLASK_ENV=development
#flask run
#flask 종료 : ctrl+c