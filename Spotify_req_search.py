# APIs often reffered to the third party services on respective servers to which developers purposefully connected 
# to download or request those services from server to their (user's/developer's server, or  local program or worskpace) 
# to incorcorate those services and APis to their program.

#for requesting those services & APIs from the server , we have request module in python , which is used for HTTP request to specified URL
# this request module takes web-url as a argument and in returns gives us the several info of that web-page on specified url like jason format of that page along 
# with there're several operations we can do that on web data on specified web url by methods like:-
'''
- GET:	GET method is used to retrieve information from the given server using a given URL.


- POST:	POST request method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it.

- PUT:	The PUT method requests that the enclosed entity be stored under the supplied URL. If the URL refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.

- DELETE:	The DELETE method deletes the specified resource

- HEAD:	The HEAD method asks for a response identical to that of a GET request, but without the response body.

- PATCH:	It is used for modify capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource
''' 

#To play with web, Python Requests is must. Whether it be hitting APIs, 
# downloading entire social media pages, and much more cool stuff, 
# one will have to make a request to the URL.

 
 
 # packages :
from requests import post , get
import sys
import os
import json
import base64
from dotenv import load_dotenv 
import cowsay

def main():
    
    # now going to fetch client-id and client-secret
    load_dotenv() # loading environment file , for loading environment variable
    
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    
    token = get_token(client_id=client_id, client_secret=client_secret)
    
    
     
    
    
    if len(sys.argv) > 3 :  # if user enter beyound country code alongwith artist-name  
      sys.exit(cowsay.tux("Too many args: please enter Artist-name alongwith Country-code only"))
         
    elif len(sys.argv) < 2 : # if user not even enter the artist-name for basic-search by artist-name(atleast). 
      sys.exit(cowsay.tux("Too few args: please enter either Artist-name \nalongwith Country-code \nor simply enter artist-name (atleast)"))
    
    elif len(sys.argv) == 2 : # if user only enter artist_name but not country-code
      print("you enter the Artist-name only [Basic-search for top-tracks will be initiated; with default-Country-code set as :IN(INDIA)]")
      art_name = sys.argv[1].title() # converting first letter to caps for better aesthetics and search fluency.
      print(f"Artist-name: {art_name}")
      
      searched_art = search_for_artist(token=token, artist_name=art_name)  # here country code not passed as it's not mentioned by user
      # creating exception for handling  None returned by search_for_artist (none will be retuend by function here if entered artist_name not found on spotify) 
      # if none returned then we can't continue procedure of fetching id by supplying key as 'id' 
      # as program gona be terminated by Error-"NoneType object not suscriptable"
      if searched_art == None:  
          sys.exit("Exit From Main: Try to search another Artist")
      
      else:
        
          searched_art_id = searched_art["id"]  # specifically fetching artist -id from json_file [which is in python dictionary format] ;here we're passing "id" as key
          searched_art_name = searched_art["name"]  # similarly fetching artist name
          print(f"Here we successfuly found Artist with name: {searched_art_name} \nAnd gona retrive top-tracks [in country bydefault: IN] for Artist-id: {searched_art_id}")
                        

      
      
    else: # if user entered artist-name with country code ; then its all fine
      print("you're all fine for further procedure [Precise-search for top-tracks will be initiated]")
      art_name = sys.argv[1].title() # converting first letter to caps for better aesthetics and search fluency.
      cntry_c = sys.argv[2].upper()# as country code in uppercase will be aceepted while searching 
      print(f"Artist-name: {art_name} \nCountry-code(Default-IN): {cntry_c}")
      
      searched_art = search_for_artist(token=token, artist_name=art_name, Country_code=cntry_c)  # here country code passed as it's mentioned by user
      # creating exception for handling  None returned by search_for_artist (none will be retuend by function here if entered artist_name not found on spotify) 
      # if none returned then we can't continue procedure of fetching id by supplying key as 'id' 
      # as program gona be terminated by Error-"NoneType object not suscriptable"
      if searched_art == None:  
          sys.exit("Exit From Main: Try to search another Artist")
          
      else:       
          searched_art_id = searched_art["id"]  # specifically fetching artist -id from json_file [which is in python dictionary format] ;here we're passing "id" as key
          searched_art_name = searched_art["name"]  # similarly fetching artist name
          print(f"Here we successfuly found Artist with name: {searched_art_name} \nAnd gona retrive top-tracks [in Country: {cntry_c}] for Artist-id: {searched_art_id}")
        
  


  
   
# defining function used for posting reuest to spotify-account-services for access-token 
def get_token(client_id, client_secret):
    # passing client-id & client secret as parameter to function for posting request
    base_url = "https://accounts.spotify.com/api/token" 
    
    # now converting authentication string [format:client-id:client-seceret] to base64 encoded with utf=8 type
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf=8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    #preparing format of headers as prescribed
    headers = {
        "Authorization": "Basic " + auth_base64,             # screenshot:[ref: SS:P]
        "Content-Type": "application/x-www-form-urlencoded"   # screenshot:[ref: SS:P]
    
    }
    
    #preparing for data-format(as prescribed):
    data = {"grant_type": "client_credentials"}
    
    # now going to post request 
    
    result =  post(url=base_url, headers= headers, data=data)
    json_result = json.loads(result.content)
    token= json_result["access_token"]  # fething specifically access-token from jsonfile(result in python dictionary format) 
                                        #by passing access _token as key
    return token                                    
    
def get_auth_header(token):
    
    #this header will be used for any search on spotify platfrom, its format will be same 
                                 #that's why building the dedicated function in the name of it just to call it simply whenever we need it.
    return {"Authorization": "Bearer " + token} #header fromat for search as given [ref: SS:a] 
                             
# now defining function for searching artist for fetching artist-id
def search_for_artist(token, artist_name , Country_code= "IN"):  #bydefault country-code will be IN(INDIA) if not pass by user
    #base url for search
    url = "https://api.spotify.com/v1/search"
    
    headers = get_auth_header(token=token)
    
    # now in query where we're going to search by artist name and type of search as artist
    query= f"?q={artist_name}&type=artist&market={Country_code}&limit=1"
    
    query_url = url + query
    # geting result through search -api for searcing artist by artist-name
    result = get(url= query_url, headers= headers)
    json_result = json.loads(result.content)['artists']['items']  # here we fetching important info only here its 'artist and items' info by their respective keys.
    #print(json_result) can print the json result for analysing the result for fetching several attributes
    
    # here if entered artist name not found then what will happen or reurned after this functiona call 
    # for that here we're creating exception 
    if len(json_result) == 0:
        cowsay.tux("No artist with this name exist on spotify...")
        return None
    
    else:
        return json_result[0]  # fetching artist info only from python dictionary format of jason file..... 
 
    
    
    
main()