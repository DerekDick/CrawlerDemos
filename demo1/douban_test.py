#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }
    
    HEADERS = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cookie': 'bid=r-9irkkroVk; ps=y; dbcl2="139284813:PuHSQombjdM"; ck=KaCw; _pk_id.100001.8cb4=0f59c258b581bf92.1507266171.1.1507266315.1507266171.; push_noty_num=0; push_doumail_num=0; __utma=30149280.40088825.1507266172.1507266172.1507266172.1; __utmc=30149280; __utmz=30149280.1507266172.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.13928'
}

    
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.douban.com/people/163296676/rev_contacts', callback=self.index_page, headers=self.HEADERS, validate_cert=False)

    
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        count = 0
        for each in response.doc('dd > a').items():
            print("each.html() = \"%s\"" % each.html())
            count += 1
            print(count)
            self.crawl(each.attr.href, callback=self.detail_page, headers=self.HEADERS, validate_cert=False)
            
        self.crawl(response.doc('.next > a').attr.href, callback=self.index_page, headers=self.HEADERS, validate_cert=False)

    
    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
