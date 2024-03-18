# Dependencies
import requests
import time
from dotenv import load_dotenv
import os
import pandas as pd
import json

# Set environment variables from the .env in the local environment
load_dotenv()

nyt_api_key = os.getenv("NYT_API_KEY")
tmdb_api_key = os.getenv("TMDB_API_KEY")

# Set the base URL
url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

# Filter for movie reviews with "love" in the headline
# section_name should be "Movies"
# type_of_material should be "Review"
filter_query = 'section_name:"Movies" AND type_of_material:"Review" AND headline:"love"'

# Use a sort filter, sort by newest
sort = "newest"

# Select the following fields to return:
# headline, web_url, snippet, source, keywords, pub_date, byline, word_count
field_list = "headline,web_url,snippet,source,keywords,pub_date,byline,word_count"

# Search for reviews published between a begin and end date
begin_date = "20130101"
end_date = "20230531"

# Build URL

query_URL = url

# Create an empty list to store the reviews
review_list =[]

# loop through pages 0-19
for page in range(20): # 200 pages or 20 pages??????

    # create query with a page number
    parameters = {
    "api-key" : nyt_api_key,
    "fq" : 'section_name:"Movies" AND type_of_material:"Review" AND headline:"love"', #filter_query,
    "sort" : "newest",
    "f1" : "headline,web_url,snippet,source,keywords,pub_date,byline,word_count",# field_list,
    "begin_date" :"20130101",
    "end_date" : "20230531",
    
}
    # API results show 10 articles at a time

    
    # Make a "GET" request and retrieve the JSON
    response = requests.get(query_URL,params=parameters)
    print (response.status_code)
    reviews = response.json()
    #print ("response json" , reviews)
    # filename = "review_data.json"
    # with open(filename,"w") as file:
    #     json.dump(reviews,file)
    
    
    # Add a twelve second interval between queries to stay within API query limits
    time.sleep(12)
    
    # Try and save the reviews to the reviews_list
    try:
        # loop through the reviews["response"]["docs"] and append each review to the list
        for doc in reviews["response"]["docs"]:
            review_list.append({
                    'headline':doc['headline'],
                    'web_url': doc['web_url'],
                    'snippet' :doc['snippet'],
                    'source' : doc['source'],
                    'keywords':doc ['keywords'],
                    'pub_date' : doc['pub_date'],
                    'byline' :doc['byline'],                    
                    'word_count':doc['word_count']                                
               })

            
        # Print the page that was just retrieved
        print ("Checked page", page)
        # if page == 0:
        #     print(json.dumps(reviews,indent=4))
        # else:
        #     print("Error", response.status_code)

        # Print the page number that had no results then break from the loop
    except Exception as e:
        print('Checked page. No result on page number :', page)
        break

    # Preview the first 5 results in JSON format
first_5_results_list = review_list[:5]
    # Use json.dumps with argument indent=4 to format data]]
json_5_results = json.dumps(first_5_results_list, indent=4)
print(json_5_results)
   
    