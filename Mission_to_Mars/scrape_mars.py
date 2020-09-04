from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from webdriver_manager.chrome import ChromeDriverManager
import time

def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #News
    nasa_mars="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(nasa_mars)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_list = soup.find('ul', class_='item_list')
    news = news_list.find('li')
    news_title = news.find("div",class_="content_title").text
    news_p = news.find("div",class_="article_teaser_body").text

    
    #Photo
    jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl)
    time.sleep(1)

    html2 = browser.html
    soup_img = bs(html2, 'html.parser')

    imgs_list = soup_img.find('ul', class_='articles')
    imgs = imgs_list.find('li')
    featured_image = imgs.find("a",class_="fancybox")["data-fancybox-href"]
    featured_image_url =f"https://www.jpl.nasa.gov{featured_image}"

    browser.quit()

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}]
    
    mars = {
        "news_title":news_title,
        "news_p":news_p,
        "img":featured_image_url,
        "hemisphere":hemisphere_image_urls
    }
    return mars

