# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from article import Article
from result import Result
from threading import Thread
import httplib
import re
import time
import urllib

'''
Created on 23-13-2012

@author: Piotr Król, Piotr Jastrzębski
'''

class BioTool(object):
    name = None
    __rank_points = None
    __google_points = None
    __wiki_points = None
    __pubmed_points = None
    __articles = None
    __query_sufix = 'bioinformatics'
    
    def __init__(self, name):
        self.name = name
        
    # Comparator used in ranking process
    @staticmethod
    def compare(first_tool, second_tool):
        first_tool_rank = first_tool.get_rank_points()
        second_tool_rank = second_tool.get_rank_points() 
        
        if first_tool_rank == second_tool_rank:
            return 0
        elif first_tool_rank < second_tool_rank:
            return 1
        return -1
    
    # If points are not calculated already calls a function to get them
    def get_rank_points(self):
        if self.__rank_points is None:
            self.__pubmed_points, self.__google_points, self.__wiki_points = self.__calculate_rank_points()
            self.__rank_points = self.__pubmed_points + self.__google_points + self.__wiki_points
        return self.__rank_points
    
    # If points are not calculated already calls a function to get them from Google
    def get_google_points(self):
        if self.__google_points is None:
            self.__pubmed_points, self.__google_points, self.__wiki_points = self.__calculate_rank_points()
        return self.__google_points
    
    # If points are not calculated already calls a function to get them from Wikipedia
    def get_wiki_points(self):
        if self.__wiki_points is None:
            self.__pubmed_points, self.__google_points, self.__wiki_points = self.__calculate_rank_points()
        return self.__wiki_points
    
    # If points are not calculated already calls a function to get them from PubMed
    def get_pubmed_points(self):
        if self.__pubmed_points is None:
            self.__pubmed_points, self.__google_points, self.__wiki_points = self.__calculate_rank_points()
        return self.__pubmed_points
        
    # Gets articles from PubMed
    def get_articles(self):
        if self.__articles is None:
            self.__articles = Article.get_articles(self.name) 
        return self.__articles
    
    # Gets and returns number of hits from Google 
    def get_google_results_count(self):        
        query = self.name + ' ' + self.__query_sufix

        params = urllib.urlencode({
                                    'q' : query,
                                    'hl' : 'en',
                                    })
            
        headers = {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        
        url = '/search' + "?" + params
        conn = httplib.HTTPConnection('www.google.com')
        conn.request("GET", url, "", headers)

        resp = conn.getresponse()
        
        if resp.status == 200:
            html = resp.read()
            html = html.decode('ascii', 'ignore')
            soup = BeautifulSoup(html)
            
            for result in soup('font', { 'size' : str(-1) }):
                match = re.match('.*Results *' + 
                                 '< *b *> *[0-9,]*[0-9] *</ *b *>' + 
                                 ' *- *' + 
                                 '< *b *> *[0-9,]*[0-9] *</ *b *>' + 
                                 ' *of about *' + 
                                 '< *b *> *[0-9,]*[0-9] *</ *b *>.*',
                                 str(result))
                
                if match is not None:
                    tag = result('b')[2]

                    match = re.search('[0-9,]*[0-9]',
                                       str(tag))
                    
                    if match is not None:
                        results_count_str = str(match.group(0))
                        results_count_str = results_count_str.replace(',', '')
                        results_count_str = results_count_str.replace(' ', '')
                        return int(results_count_str)
                    
        return 0
    
    # Gets and returns number of articles from Wikipedia
    def get_wikipedia_results_count(self):
        query = self.name + ' ' + self.__query_sufix

        params = urllib.urlencode({
                                    'search' : query
                                    })
        headers = {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        
        url = '/w/index.php' + "?" + params
        conn = httplib.HTTPConnection('en.wikipedia.org')
        conn.request("GET", url, "", headers)

        resp = conn.getresponse()
        
        if resp.status == 200:
            html = resp.read()
            html = html.decode('ascii', 'ignore')
            soup = BeautifulSoup(html)
            
            for result in soup('div', { 'class' : 'results-info'}):
                match = re.match('.*Results *' + 
                                  '< *b *> *[0-9,]*[0-9] *</ *b *>' + 
                                  ' *of *' + 
                                  '< *b *> *[0-9,]*[0-9] *</ *b *>' + 
                                  ' for.*',
                                  str(result)
                                  )
                
                tag = result('b')[1]
                match = re.search('[0-9,]*[0-9]', str(tag))
                
                if match is not None:
                    wiki_results_count_str = str(match.group(0))
                    wiki_results_count_str = wiki_results_count_str.replace(',', '')
                    wiki_results_count_str = wiki_results_count_str.replace(' ', '')
                    return int(wiki_results_count_str)

        return 0
    
    # Method used for rank points calculation
    # It is called in separately thread for each tool   
    # @return: Final grade for an article         
    def __calculate_rank_points(self):
        start = time.time()
        test = Result(self.name)    
        
        tWiki = Thread(target=test.getWiki)
        tArticles = Thread(target=test.getGoogle)
        tGoogle = Thread(target=test.getFromArticles) 
        
        tWiki.start()
        tArticles.start()
        tGoogle.start()
        
        tWiki.join()
        tArticles.join()
        tGoogle.join()
        
        print self.name + ": " + (str)(time.time() - start) + "s"
        
        return test.getHits()