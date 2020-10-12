import logging

from flask import request
from flask import Response
from flask_restplus import Resource
from restplus import api

from restplus import api
from url_parsing import URLParsing 

log = logging.getLogger(__name__)

ns = api.namespace('demo/', description='URL Analyzer')


@ns.route("/url_title/",methods=['GET'])
class UrlDescription(Resource):
    def get(self):
        url_link = request.args.get("url_link")
        url = URLParsing(url_link)
        return url.get_tittle()

@ns.route("/statistics_url/",methods=['GET'])
class StatisticsURL(Resource):

    def get(self):
        url_link = request.args.get("url_link")
        url = URLParsing(url_link)
        return {"keyword_in_tittle": url.kw_in_tittle(),
                "unique_keywords" : url.unique_kw(),
                "frequency_keyword":url.frequency_kw()
                }