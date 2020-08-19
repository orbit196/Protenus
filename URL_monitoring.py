# Takes a URL as an argument.

# Fetches the URL once per minute.

# Prints a record of the attemp with the HTTP response code and time it took to return (if successful).

# Display help information to the user and catches errors as appropriate.

# Please list any assumptions in either code comments or an additional Markdown file. 

#### 

import urllib2, httplib
import threading
import time

class Monitor:
	def __init__(self, url):
		self.url = url
		# print(self.url)

	def fetchURL(self):
		try: 
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
			print("HTTP Request Error Code: " + str(e.code))
		except urllib2.URLError as e:
			print(e.reason)
		except ValueError:
			print("URL does not exist!")
		

if __name__ == "__main__":
	URL = raw_input("What is the URL (including https:// or http://) that you would like to fetch? ")
	start = Monitor(URL)
	start.fetchURL()

####


