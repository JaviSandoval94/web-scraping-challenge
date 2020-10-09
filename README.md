# Mission to Mars
![mission-to-mars](https://github.com/JaviSandoval94/web-scraping-challenge/blob/master/Missions_to_Mars/pictures/mission_to_mars.PNG)
Welcome to this mission to Mars! This is a web scraping project which uses BeautifulSoup, Selenium, Splinter, MongoDB and the Pymongo library to scrape the web and retrieve news, facts and pictures of our red neighbor from different web sources. The results are displayed in a web application made using HTML.

## Step 1
The code uses Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to scrape through the data sources and retrieve the following information:
  * NASA Mars News
  * JPL Mars Space Images - Featured Image
  * Mars Weather
  * Mars Hemispheres Images
  
 ## Step 2
 A web application was created using MongoDB and Flask to render the scraped information using HTML.<br>
 The following screenshot shows the code results after the last commit of the current project:
 ![mars-scrape](https://github.com/JaviSandoval94/web-scraping-challenge/blob/master/Missions_to_Mars/pictures/Mars-web-app-1-updated.PNG)
 ![mars-scrape-hemispheres](https://github.com/JaviSandoval94/web-scraping-challenge/blob/master/Missions_to_Mars/pictures/Mars-web-app-2-updated.PNG)
 
 ## Data sources
 All the data from this project was scraped from the following sites:
 ### Nasa Mars News Site
 This site contains news related to Mars expeditions and observations.
 [Nasa Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
 ### Jet Propulsion Laboratory NASA
 This site was accessed to retrieve the Mars featured image of the day.
 * [Mars Featured Image - Jet Propulsion Laboratory NASA](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
 ### Twitter
 Get information from the Mars Weather account to retrieve weather data from the Martian surface.
 * [Mars Weather Twitter account](https://twitter.com/marswxreport?lang=en)
 ### Space Facts
 This page was used to retrieve facts from Mars.
 * [Space Facts - Mars Facts](https://space-facts.com/mars/)
 ### USGS Astrogeology site
 Four pictures of the Martian hemispheres were retrieved from this website.
 * [Mars Hemispheres Images](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
 
 ## Code explanation
An initial test for the scraping was made in the `mission_to_mars.ipynb` file. This code is replicated in the `scrape_mars.py` file, which is called from the Flask application contained in the `app.py` file to render the results in the `index.html` template. Please note that this project requires installation of MongoDB to save the srape results. Also make sure to install the [Splinter web driver](https://splinter.readthedocs.io/en/latest/drivers/chrome.html) and have the `chromedriver.exe` file in your working directory.
