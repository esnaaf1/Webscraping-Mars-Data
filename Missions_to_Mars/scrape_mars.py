import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # set the path for chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_all():
    browser = init_browser()

    #*****************SCRAPE THE HEADLINE NEEWS******************
    # visit the Mission To Mars news url
    news_url = 'http://mars.nasa.gov/news'
    browser.visit(news_url)
    time.sleep(1)

    # Get the results into html
    html = browser.html
    # use BeautifulSoup to parse the html
    soup = bs(html, 'html.parser')
    
    # Get the first headline title
    news = soup.find('div', class_="content_title")
    news_title = news.find('a').get_text()
    
    # Get the dscription for the first headline
    # Get the dscription for the first headline
    news_detail=soup.find('div', class_="article_teaser_body").get_text()

    #*****************SCRAPE THE FEATURED IMAGE******************
    # Visit the Mars images url
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    base_url ="https://www.jpl.nasa.gov"
    browser.visit(img_url)
    time.sleep(1)

    # Look for the full_image tag
    full_image = browser.find_by_id('full_image')
    # Click on the "Full Imge Button"
    full_image.click()
    
    # Click for more information
    browser.is_element_present_by_text('more info', wait_time=2)
    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()
    
    # grab the html and scrape the full image link
    soup = bs(browser.html, 'html.parser')
    featured_img = soup.find('img', class_='main_image')['src']
    featured_img_url = f'{base_url}{featured_img}'

    #****************SCRAPE THE TWITTER FOR WEATHER***************
    # Vist the Mars Twitter website
    twitter_url = 'https://twitter.com/marswxreport/'
    browser.visit(twitter_url)
    time.sleep(1)

    # Get the html
    html=browser.html
    soup=bs(html,'html.parser')

    # look for the container with tag div and class js-twee-text-container
    container=soup.find('div', class_='js-tweet-text-container')
    # look for the paragraph tag p and get the text element
    mars_weather=container.find('p').get_text()

    #****************SCRAPE THE MARS FACTS*************************
    # Visit the Mars facts url
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    time.sleep(1)

    # Get the Mars Fact table and convert it to a html string
    html = browser.html
    tables = pd.read_html(facts_url)
    mars_facts_html = tables[0].to_html(header=False, index=False)

    #**************** SCRAPE HEMISPHERE IMAGES **********************
    # Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemisphers.
    # hemispheres_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Using alternate website because the url posted in the homework does not work anymore
    hemispheres_url= 'https://web.archive.org/web/20181114171728/https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    time.sleep(1)

    # loop through each link and find the image uril and the title
    hemisphere_image_urls=[]
    url_links = browser.find_by_css('a.product-item h3')

    for i in range(len(url_links)):
        
        # create an empty dictionary for each hemisphe
        hemisphere={}
        browser.find_by_css('a.product-item h3')[i].click()
        
        #get hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
        
        #next find the sample image anchor tag and get href
        sample_elem = browser.find_link_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']

    
        #Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)

        #Finally navigate back to start again on loop
        browser.back()
    
    #*************** CREATE A DICTOIONARY *********************
    mars_info={}
    mars_info['news_title'] = news_title
    mars_info['news_detail'] = news_detail
    mars_info['featured_img_url'] = featured_img_url
    mars_info['mars_weather'] = mars_weather
    mars_info['mars_facts_html'] = mars_facts_html
    mars_info['hemisphere_image_urls'] = hemisphere_image_urls

    # Close the browser
    browser.quit()

    # Return results
    return mars_info
