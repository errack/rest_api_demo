import logging
import warnings

from analyzer import Analyzer

log = logging.getLogger(__name__)

class URLParsing:
    def __init__(self, url_link):
        self.url_link = url_link
        self.tittle = None
        self.keywords = None
        log.info("set new url {}".format(self.url_link))
        self.parsing()

    def parsing(self):
        """
            This method makes use of a parser to consult the 
            URL and in case of being able to access, obtain the 
            HTML text and access the configured information

        """
        if Analyzer.check_url(self.url_link):
            info = Analyzer.find_elements(self.url_link,['keywords'])
            self.tittle = info.get("tittle",None)
            self.keywords = info.get("keywords",None)


    def __parsing_keywords(self, info):
        """
            This method summarizes the keywords and 
            returns a dict that contains the keyword 
            and the amount for each one as a key.

            Param: text wiht keyword

            Return: {'keyword_n':'n'}
        """
        keywords = {}
        if info is not None:
            for key in info.split(" "):
                cls_key = key.replace(",","").lower()
                if keywords.get(cls_key,None) is None:
                    keywords[cls_key] = 1
                else:
                    temp_count = keywords.get(cls_key)
                    keywords[cls_key] = temp_count + 1
        return keywords

    def get_keywords(self):
        return {"keywords":self.keywords,"url":self.url_link} if self.keywords is not None else None
    
    def get_tittle(self):
        return {"tittle":self.tittle,"url":self.url_link} if self.tittle is not None else None


    def unique_kw(self):
        kw = self.__parsing_keywords(self.keywords)
        return {"keyword":[x.strip() for x in kw.keys()]}
    
    def kw_in_tittle(self):
        kw = [x.replace(",","").lower() for x in self.keywords.split(" ")]
        kw_tittle = [x.lower() for x in self.__parsing_keywords(self.tittle).keys()]
        total = [x for x in kw if x in kw_tittle]
        return {"total_kewords":len(total),"keywords":total,"tittle": self.tittle}

    def frequency_kw(self):
        return self.__parsing_keywords(self.keywords)