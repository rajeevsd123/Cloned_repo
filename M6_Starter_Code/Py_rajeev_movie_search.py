
# Dependencies
import requests
import time
from dotenv import load_dotenv
import os
import pandas as pd
import json
from pandas import json_normalize

tmdb_api_key = "1aa6d32f206e0d460fb9da911b4db70a"
base_url = "https://api.themoviedb.org/3"
# titles = ['The Attachment Diaries',
#  'What’s Love Got to Do With It?’ Probably a Lo',
#  'You Can Live Forever',
#  'A Tourist’s Guide to Love',
#  'Other People’s Children',
#  'One True Loves',
#  'The Lost Weekend: A Love Story',
#  'A Thousand and One',
#  'Your Place or Mine',
#  'Love in the Time of Fentanyl',
#  'Pamela, a Love Story',
#  'In From the Side',
#  'After Love',
#  'Alcarràs',
#  'Nelly & Nadine',
#  'Lady Chatterley’s Lover',
#  'The Sound of Christmas',
#  'The Inspection',
#  'Bones and All',
#  'My Policeman',
#  'About Fate',
#  'Waiting for Bojangles',
#  'I Love My Dad',
#  'A Love Song',
#  'Alone Together',
#  'Art of Love',
#  'The Wheel',
#  'Thor: Love and Thunder',
#  'Both Sides of the Blade',
#  'Fire of Love',
#  'Love & Gelato',
#  'Stay Prayed Up',
#  'Benediction',
#  'Dinner in America',
#  'In a New York Minute',
#  'Anaïs in Love',
#  'I Love America',
#  'See You Then',
#  'La Mami',
#  'Love After Love',
#  'Deep Water',
#  'Lucy and Desi',
#  'Cyrano',
#  'The In Between',
#  'Book of Love',
#  'Lingui, the Sacred Bonds',
#  'The Pink Cloud',
#  'A Journal for Jordan',
#  'West Side Story',
#  'Aulcie',
#  'Love Is Love Is Love',
#  'Love Hard',
#  'Bergman Island',
#  'Hard Luck Love Song',
#  'South of Heaven',
#  'Wife of a Spy',
#  'Happier Than Ever',
#  'Together',
#  'Annette',
#  'Resort to Love',
#  'Woodstock 99: Peace, Love and Rage',
#  'Casanova, Last Love',
#  'Running Against the Wind',
#  'Asia',
#  'Undine',
#  'This Town',
#  'Tu Me Manques',
#  'Monday',
#  'Ride or Die',
#  'Future People',
#  'Luz',
#  'Happily',
#  'This Is the Life',
#  'To All the Boys: Always and Forever',
#  'Young Hearts',
#  'Little Fish',
#  'Two of Us',
#  'Atlantis',
#  'Preparations to Be Together',
#  'Your Name Engraved Herein',
#  'Sylvie’s Love',
#  'Ariana Grande: Excuse Me, I Love You',
#  'Museum Town',
#  'Wild Mountain Thyme',
#  'My Psychedelic Love Story',
#  '69: The Saga of Danny Hernandez',
#  'Ammonite',
#  'Love and Monsters',
#  'Dick Johnson Is Dead',
#  'Love, Guaranteed',
#  'Feel the Beat',
#  'Babyteeth',
#  'Spelling the Dream',
#  'A Secret Love',
#  'Love Wedding Repeat',
#  'Almost Love',
#  'Hope Gap',
#  'All the Bright Places',
#  'The Photograph',
#  'You Go to My Head',
#  'Ordinary Love',
#  'To All the Boys: P.S. I Still Love You',
#  'The Woman Who Loves Giraffes',
#  'Queen & Slim',
#  'Marriage Story',
#  'Cyrano, My Love',
#  'Pretenders',
#  'First Love',
#  'Loro',
#  'Falling Inn Love',
#  'Hot Air',
#  'Love, Antosha',
#  'Leto',
#  'The Tomorrow Man',
#  'Asako I & II',
#  'The Sun Is Also a Star',
#  'Shéhérazade',
#  'Long Shot',
#  'Clara',
#  'Kalank',
#  'Rafiki',
#  'Diane',
#  'Five Feet Apart',
#  'Ash Is Purest White',
#  'Gloria Bell',
#  'Black Mother',
#  'The Hole in the Ground',
#  'How to Train Your Dragon: The Hidden World',
#  'A Tuba to Cuba',
#  'Fighting With My Family',
#  'Sorry Angel',
#  'Berlin, I Love You',
#  'Untogether',
#  'Cold War',
#  'If Beale Street Could Talk',
#  'Asher',
#  'The Party’s Just Beginning',
#  'The Great Pretender',
#  'Sicilian Ghost Story',
#  'The New Romantic',
#  'Pimp',
#  'In a Relationship',
#  'They’ll Love Me When I’m Dead’ Documents Orson Welles’s Last Fil',
#  'Burning,’ Love Ignites a Divided Worl',
#  'After Everything,’ a Young Love Blooms in Crisi',
#  'Quincy’ Captures a Lifelong Love Affair With Musi',
#  'Love, Gilda,’ a Portrait of a Brief and Brilliant Caree',
#  'Tea With the Dames,’ Four Legends Dish on Acting and Lov',
#  'Bel Canto,’ Music Is the Food of Love and Rebellio',
#  'The Citizen,’ an Immigrant Picks a Bad Time to Fall in Lov',
#  'Love, Cecil,’ an Aesthete Ahead of His Tim',
#  'How to Talk to Girls at Parties',
#  'Rogers Park,’ Life and Love in a Chicago Neighborhoo',
#  'Love & Bananas,’ Uncovering the Plight of the Asian Elephan',
#  'Godard Mon Amour',
#  'Submergence,’ a Love Story Sunk by Geopolitic',
#  'Love After Love,’ an Unflinching Look at Extended Grie',
#  'Outside In',
#  'Love, Simon,’ a Glossy Teen Romance, the Hero Has a Secre',
#  'Keep the Change,’ Two People With Autism Find Lov',
#  'The Party',
#  'The Housemaid,’ Twisted Love and Angry Ghosts in Vietna',
#  'Forever My Girl,’ a Romance Resumes After a Long Brea',
#  'Kangaroo: A Love-Hate Story’ Exposes a Wildlife Massacr',
#  'Lover for a Day',
#  'Youth,’ the People’s Dance Troupe, in Love and Wa',
#  'Killing for Love’ Revisits a Virginia Murder Cas',
#  'The Shape of Water’ Is Altogether Wonderfu',
#  'Love Beats Rhymes,’ a Hip-Hop Artist Transformed by Poetr',
#  'Cuba and the Cameraman’ Lavishes Love on a Country … and Castr',
#  'On the Beach at Night Alone’ Zooms in on a Love Affai',
#  'Thelma,’ a Woman in Love Can Burn Down the Worl',
#  'Hello Again,’ a Movie Musical Ode to Love and Lust Over Decade',
#  'It Happened in L.A.,’ All That Questing After Lov',
#  'God’s Own Country',
#  'The Mountain Between Us',
#  'Dina,’ a Differently Abled Love Stor',
#  'In Search of Fellini',
#  'Woodpeckers,’ a Tale of Love and Agonizing Penal Confinemen',
#  'I Do ... Until I Don’t,’ Love and Loathing in Florid',
#  'Tales of an Immoral Couple’: Love Means Having to Grow U',
#  'After Love’ and Regretting Every Momen',
#  'The Last Face',
#  'Women Who Kill,’ and May Be in Love With On',
#  'False Confessions,’ the Play’s Not Quite the Thin',
#  'Review: Those Movies, Himself — Bertrand Tavernier’s Tour of French Cinem',
#  'The Big Sick,’ Comedy Is Hard, Love Harde',
#  'Lost in Paris',
#  'Vincent N Roxxy,’ Love Is in the Air, N So Is Fea',
#  'Everything, Everything’ Pits Love Against Diseas',
#  'Hounds of Love’ Is Tense and Deadly Down Unde',
#  'Harold and Lillian’ Introduces a Hollywood Power Coupl',
#  'The Happiest Day in the Life of Olli Maki,’ Love and Life on the Rope',
#  'The Promise’ Finds a Love Triangle in Constantinopl',
#  'Frantz,’ a Mysterious Frenchman and the Wounds of Wa',
#  'The Other Half',
#  'The Ottoman Lieutenant',
#  'Love & Taxes',
#  'Everybody Loves Somebody,’ a Rom-Com With Bit',
#  'Kedi,’ Rekindling a ‘Love of Life']
titles = ['The Attachment Diaries',
 'What’s Love Got to Do With It?’ Probably a Lo',
 'You Can Live Forever',
 'A Tourist’s Guide to Love',
 'Other People’s Children'
 ]
# Create an empty list to store the results
tmdb_movies_list = []

# Create a request counter to sleep the requests after a multiple
# of 50 requests
request_counter = 1
try :
# Loop through the titles
    for title_item in titles:
            # Check if we need to sleep before making a request
        #    if request_counter%50 == 0:
        #     time.sleep(1)

            # Add 1 to the request counter
        # request_counter = request_counter+1
            
            # Perform a "GET" request for The Movie Database
            search_url = f"{base_url}/search/movie"
            search_param = {"api_key":tmdb_api_key, "query" :title_item}
            #url= url+title_item+tmdb_key_string
            #print (url)
            movie_search_resonse = requests.get(search_url, params=search_param)
            movie_search_json = movie_search_resonse.json()

            if movie_search_json['total_results'] > 0:

            # Include a try clause to search for the full movie details.
            # Use the except clause to print out a statement if a movie
            # is not found.
                
                    # Get movie id
                    movie_id = movie_search_json['results'][0]['id']
                    ####### increment request counter  #### reivew
                    # Add 1 to the request counter
                    request_counter = request_counter+1
                    # Make a request for a the full movie details
                    full_movie_details_url = f"{base_url}/movie/{movie_id}"
                    full_movie_detail_param = {"api_key":tmdb_api_key}
                    # Execute "GET" request with url
                    full_movie_details_response = requests.get(full_movie_details_url, full_movie_detail_param)
                    full_movie_details_json =  full_movie_details_response.json()
                    
                    # Extract the genre names into a list
                    genres = [genre["name"] for genre in full_movie_details_json['genres']]
                    

                    # Extract the spoken_languages' English name into a list
                    spoken_languages = [spoken_language["name"] for spoken_language in full_movie_details_json["spoken_languages"]]

                    # Extract the production_countries' name into a list

                    production_countries = [production_country["name"] for production_country in full_movie_details_json ["production_countries"]]
                    # Add the relevant data to a dictionary and
                    # append it to the tmdb_movies_list list
                    movie_details_dict = {
                        'title': full_movie_details_json['title'],
                        'original_title' :full_movie_details_json['original_title'],
                        'budget' :full_movie_details_json['budget'],
                        'genres' :full_movie_details_json['genres'],
                        'original_language' :full_movie_details_json['original_language'],
                        'spoken_languages' :full_movie_details_json['spoken_languages'],
                        'homepage':full_movie_details_json['homepage'],
                        'overview' :full_movie_details_json['overview'],
                        'popularity' :full_movie_details_json['popularity'],
                        'runtime' :full_movie_details_json['runtime'],
                        'revenue' :full_movie_details_json['revenue'],
                        'release_date' :full_movie_details_json['release_date'],
                        'vote_average' :full_movie_details_json['vote_average'],
                        'vote_count' :full_movie_details_json['vote_count'],
                        'production_countries' :full_movie_details_json['production_countries'],
                    }
                    tmdb_movies_list.append(movie_details_dict)

                    #### reqeust_coutter is mutliple of 50
                    if request_counter % 50 == 0:
                        print ( "Application is sleeping for 1 sec")
                        time.sleep(1)

            # Print out the title that was found
                    print("Found", title_item)
            else: 
                print (title_item, "not found")
except Exception  as e:
    print(f"An error occured,  {e}")
