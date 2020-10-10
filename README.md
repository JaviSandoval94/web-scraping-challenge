# Mission to Mars
![mission-to-mars](https://github.com/JaviSandoval94/web-scraping-challenge/blob/master/Missions_to_Mars/pictures/mission_to_mars.png)
Welcome to this mission to Mars! This is a web scraping project which uses BeautifulSoup, Selenium, Splinter, MongoDB and the Pymongo library to scrape the web and retrieve news, facts and pictures of our red neighbor from different web sources. The results are displayed in a web application made using HTML.

## Step 1
The code uses Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to scrape through the data sources and retrieve the following information:
  * NASA Mars News
  * JPL Mars Space Images - Featured Image
  * Mars Weather
  * Mars Hemispheres Images
The scraping code was first tested in the `mission_to_mars.ipynb` Jupyter Notebook and afterwards captured in the `scrape` function of the `scrape_mars.py` Python file. The final results are returned by the function in a dictionary called `mars_data`, which contains all the scraped information and is imported into the Flask server during the next step.
 ## Step 2
 A web application was created using MongoDB and Flask in the `app.py` Python file. The `scrape_mars.py` file is imported into this file to run the scrape function from the Flask server. To run this step, a database was created using MongoDB to save the scrape results.
 ## Step 3
 Finally, the scraped data was visualized in an HTML file which responds to the Flask request. The following screenshot shows the code results after the last commit of the current project:
 ![mars-scrape](https://github.com/JaviSandoval94/web-scraping-challenge/blob/master/Missions_to_Mars/pictures/Mars-web-app-1-updated.PNG)
 ![mars-scrape-hemispheres](https://github.com/JaviSandoval94/web-scraping-challenge/blob/master/Missions_to_Mars/pictures/Mars-web-app-2-updated.PNG)
 
 ## Data sources
 All the data from this project was scraped from the following sites:
 ### Nasa Mars News Site
 This site contains news related to Mars expeditions and observations.
 * [Nasa Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
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
 
 ## Technical details
Please note that this project requires installation of MongoDB and the creation of a database to save the srape results. Also make sure to install the [Splinter web driver](https://splinter.readthedocs.io/en/latest/drivers/chrome.html) and have the `chromedriver.exe` file in your working directory.
