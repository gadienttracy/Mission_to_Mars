#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[30]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[31]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[32]:


#set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[33]:


#id the parent element and create a variable to hold it
slide_elem.find('div', class_='content_title')


# In[34]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[35]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[36]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[37]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[38]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[39]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[40]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[41]:


#table scraping
#create a new df from html table read_html() searches for and returns a list of tables found in html 0=pull first table it finds
df = pd.read_html('https://galaxyfacts-mars.com')[0]
#assign columns to the new df
df.columns=['description', 'Mars', 'Earth']
#turn description column into the df index
df.set_index('description', inplace=True)
df


# In[42]:


#convert df back to html
df.to_html()


# In[53]:


# 1. Use browser to visit the URL 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[54]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

site = browser.find_by_css("a.product-item h3")
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for item in range(len(site)):
    hemispheres = {}
    
    browser.find_by_css("a.product-item h3")[item].click()
    
    sample_element = browser.find_link_by_text("Sample").first
    hemispheres["image_url"] = sample_element["href"]
    
    hemispheres["title"] = browser.find_by_css("h2.title").text
    
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
    


# In[55]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[56]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




