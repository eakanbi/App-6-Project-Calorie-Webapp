from bs4 import BeautifulSoup
import requests

class Temperature:
    """ Represent a temperature value extracted 
from the timeanddate.com/weather webpage"""

    headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'


    def __init__(self, country, city):

        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')

    def _build_url(self):
        """Builds the url string adding country and city"""
        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        """Builds the url string adding country and city"""
        url = self._build_url()
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        temperature_element = soup.find("div", class_="h2").text.strip().replace("°F", "")
        return float(temperature_element)


    def get(self):
        """Cleans the out of scrape"""
        if self._scrape():
        # Extract the temperature text
            temperature = self._scrape()
            return temperature
        
    
if __name__ == '__main__':
    temperature =Temperature(country="usa", city="san francisco")
    print(temperature.get())
    # print(temperature._scrape())