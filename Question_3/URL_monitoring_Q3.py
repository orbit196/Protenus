"""URL_monitoring_Q3: Script will prompt user for a URL and will query the URL every 60 seconds
                      if the HTTP query responds with a status code of 200.
   Author: Yingquan Li
   Date: 8/23/20
   Python version: 2.7.1
   Usage: python URL_monitoring_Q3.py"""

"""
Assumptions:
* URLs entered are using the HTTP protocol
* URLs are publicly accessible and not within a private network
* Assuming that the underlying architecture is based on the RESTful paradigm
* Client-server architecture
* Each GET request is stateless and the server has no idea of the state of previous requests
* Clients should not be able to tell if HTTP requests are routed to servers that serve as proxies
"""

# Imported modules
import urllib2, httplib
import threading
import time

class Monitor:
	"""Objets of class Monitor will ask for a URL. By invoking the fetchURL() method,
	   the URL will be queried every 60 seconds. If the successful, error status code 200
	   will be returned. If not, the appropriate response code will be returned.

	   An message to STDOUT will be printed if the URL is invalid.	
	"""

	def __init__(self, url):
		"""
		Constructor that asks for a URL.
		"""
		self.url = url

	def fetchURL(self):
		"""
		fetch() URL method that will query URL every 60 seconds if it's a valid URL.
		"""
		try: 
			# Open URL connection and record time that it takes to query URL. Print the 
			# HTTP code and the time elapsed.
			start = time.clock()
			req = urllib2.Request(self.url)
			response = urllib2.urlopen(req)
			elapsedTime = time.clock() - start
			print(str(response.getcode()) + "; " + "Request completed in {0:.0f}ms".format(elapsedTime))
			
            # Closing the response
			response.close()

			# Implementing threading to call fetch the URL every 60 seconds
			threading.Timer(60, self.fetchURL).start()
		except urllib2.HTTPError as e:
			# Catching HTTP request errors; prints error code 
			print("HTTP Request Error Code: " + str(e.code))
		except urllib2.URLError as e:
			# Catching errors if the URL cannot be opened or accessed; prints reason why
			print(e.reason)
		except ValueError:
			# Catching an invalid URL value that the user enters; prints user message
			print("URL does not exist!")
		

# Main method
if __name__ == "__main__":
	# Example usage: https://yahoo.com
	URL = raw_input("What is the URL (including https:// or http://) that you would like to fetch? ")
	start = Monitor(URL)
	start.fetchURL()



