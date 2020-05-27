# Import dependencies
import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs

def scrape():
    # Get the path to the chromedriver.exe and run the browser.
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', executable_path, headless=False)

    # Access the Mars news URL
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Get the latest title from the item list in the Mars news site.
    news_title = soup.find('ul', class_ = 'item_list').\
                find('div', class_ = 'content_title').text

    # Get the latest article teaser from the item list in the Mars news site.
    news_p = soup.find('ul', class_ = 'item_list').\
                find('div', class_='article_teaser_body').text

    # Specify the space images URL and visit page using the browser. Parse content as HTML
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Using BeautifulSoup on the browser HTML, get the latest featured image URL and save it as a string.
    img_url_short = soup.find('ul', class_ = 'articles').\
            find('li', class_ = 'slide').find('a')['data-fancybox-href']

    featured_image_url = 'https://www.jpl.nasa.gov' + img_url_short

    # Get response from Mars Weather Twitter page
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    # Get reference to the featured image in the latest tweet.
    mars_weather_img = soup.find('div', class_ = 'js-tweet-text-container').find('p').find('a').text

    # Remove reference to the image in the tweet text and save as a string.
    mars_weather = soup.find('div', class_ = 'js-tweet-text-container').find('p').text.replace(mars_weather_img, '')

    # Gather the tables at the Mars facts site.
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    # Extract the stats table and save as HTML.
    mars_table = tables[0].rename(columns = {0:'description', 1:'value'}).to_html().replace('\n', '')

    # Specify the Mars astrogeology URL and visit page using the browser. Parse content as HTML
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Create a list with the hemisphere names and an empty list to save data dictionaries.
    hemisphere_image_urls = []
    hemispheres = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']

    # Iterate through the hemispheres list.
    for hemisphere in hemispheres:
    
        # Create an empty dictionary for each hemisphere and save its name in the 'title' entry.
        hemisphere_dict = {}
        hemisphere_dict['title'] = hemisphere + ' Hemisphere'
    
        # Navigate through the browser and get the image URL.
        browser.click_link_by_partial_text(hemisphere)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = soup.find('div', class_ = 'container').\
            find('div', class_ = 'wide-image-wrapper').\
            find('img', class_ = 'wide-image')['src']
    
        # Store the image URL in the hemisphere dictionary.
        hemisphere_dict['img_url'] = 'https:astrogeology.usgs.gov' + img_url
        hemisphere_image_urls.append(hemisphere_dict)
        browser.back()

        mars_data = {'news_title': news_title, 'news_p': news_p, 'featured_image_url': featured_image_url, 'mars_weather': mars_weather, 'mars_table': mars_table, 'hemisphere_image_urls': hemisphere_image_urls}

    browser.quit()

    return mars_data