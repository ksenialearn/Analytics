#Searches apartments on Streeteasy by specified price, number of bedrooms, and neighborhood.
#Outputs a CSV file with apartment links and Available date.

from bs4 import BeautifulSoup
import urllib

#Adjust these variables for your selection
pricemin = 2800 #minimum price of the apartment
pricemax = 3300 #maximum price of the apartment
beds = 1 #number of bedrooms
hood = 'manhattan' #neighborhood. Some other options: 'nyc' - all NYC, 'manhattan', 'uws', 
#'uws','midtown-all', 'downtown', 'ues', 'brooklyn', 'queens'
#_________________________________________


def package_url_rent(page):
    return 'http://streeteasy.com/for-rent/'+hood+'/price:'+str(pricemin)+ \
            '-'+str(pricemax)+'%7C'+str(beds)+':'+str(beds)+'?page='+page


def getDate(url):
    page = urllib.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    details = soup.find_all('div', {'class':'details_info'})
    for line in details:
        
        h = line.find('h6')
        if h is not None:
            description = unicode(h.string)
            desc = description.split()
            for word in desc:
                if word == 'Availability' or 'Available':
                    listt= line.contents
                    lengg= len(listt)
                    av = listt[lengg-1].strip()
                    return av
                    
                   
with open('listings.csv', 'w') as f:
    for x in range(1,10): #loop through 100 pages
        url=package_url_rent(str(x))
        print url
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('div', {'class': 'details-title'})
    
        for title in titles:
            urlLink= title.find('a')['href']
            fullLink= 'http://streeteasy.com' + urlLink
            print fullLink
            avail = getDate(fullLink)
            print avail        
            f.write( fullLink + ',' + avail + '\n')
        
