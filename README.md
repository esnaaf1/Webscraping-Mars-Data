# WEBSCAPING-MARS-DATA
In this project, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following websites were used:

- NASA Mars News https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

- JPL Mars Space Images https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

- Mars Weather https://twitter.com/marswxreport?lang=en

- Mars Hemispheres https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

I used MongoDB to store all the information scraped from above websites.

I used FLASK templating to ceate a new HTML page to display all information from the MongoDB database.

