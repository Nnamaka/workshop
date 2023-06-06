# testing sharzam api endpoints.
# Assuming you have your rapidapi key stored in a .env file in the same
# directory as this file
# please visit https://rapidapi.com/tipsters/api/shazam-core to see the 
# available endpoints

import requests
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')
rapid_api_key = os.getenv('RAPIDAPI_API_KEY')

URL1 = "https://shazam-core7.p.rapidapi.com/charts/get-top-songs-in-world"
URL2 = "https://shazam-core7.p.rapidapi.com/songs/get_details"

# get top world songs
HEADERS = {
	"X-RapidAPI-Key": rapid_api_key,
    "X-RapidAPI-Host": "shazam-core7.p.rapidapi.com"
}

querytops = {"term":"Sorry"}
response = requests.get(URL1, headers=HEADERS, params=querytops).json()

# get details of a song
queryparams = {'id':take['key']}
response = requests.get(URL2, headers=HEADERS, params=queryparams).json()
