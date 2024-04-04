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

 