import urllib.request
import logging
import lxml

from bs4 import BeautifulSoup


log = logging.getLogger(__name__)


class Analyzer:

    @staticmethod
    def find_elements(url_link, config):
        try:
            data = {'url': url_link}
            status = 0
            r = urllib.request.Request(url_link)
            response = urllib.request.urlopen(r)
            html = response.read().decode("utf8").replace("\r","").replace("\t","").replace("\n","")
            status = response.status
            if status == 200:
                log.info("[{}]-{}".format(url_link,"Status 200"))
                soup = BeautifulSoup(html,'html',None, None, None)
                print("[{}] - {}".format(url_link,soup.title.string))
                data["tittle"]=soup.title.string
                meta_list = soup.find_all("meta")
                for meta in meta_list:
                    if 'name' in meta.attrs:
                        name = meta.attrs['name']
                        if name in config:
                            data[name.lower()] = meta.attrs['content']
        except Exception as a:
            log.error("URL: [{}] - Reason {}".format(url_link,a))
        return data

    @staticmethod
    def check_url(url_link):
        try:
            r = urllib.request.Request(url_link)
            response = urllib.request.urlopen(r)
            if response.status == 200:
                return True
            else:
                return False
        except Exception as e:
            log.error('Could not load page [{}]. Reason: {}'.format(url_link, str(e)))
            return False