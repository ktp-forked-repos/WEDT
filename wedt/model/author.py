# -*- coding: utf-8 -*-
import httplib, urllib, re
from BeautifulSoup import BeautifulSoup
import constval

'''
Created on 23-13-2012

@author: Piotr Król
'''

class Author(object):
    name = None
    surname = None
    __h_index = None
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    # Gets H index or if it is not stored, calls a method to calculate
    def get_h_index(self):
        if self.__h_index is None:
            self.__h_index = self.__calculate_h_index()
        return self.__h_index
    
    # Calculate H_index of an author using PubMed db (Backup method)
    # @return: h-index value
    def __calculate_h_index_pubmed(self):
        from article import Article
        
        cites = []
        for art in Article.get_articles(self.name + " " + self.surname):
            for auth in art.authors:
                if auth.name == self.name and auth.surname == self.surname:
                    cites.append(art.get_related_citations_number())

        cites.sort()
        cites.reverse()
        
        h = 0
        for cite in cites:
            if cite > h:
                h += 1
            else:
                break

        return h
    
    # Calculate H_index of an author using Google Scholar
    # @return: h-index value
    def __calculate_h_index(self):
        limit = constval.H_LIMIT

        if self.name is not None and self.surname is not None:
        	query = self.name + ' ' + self.surname
        if self.name is None and self.surname is not None:
        	query = self.surname
        if self.name is not None and self.surname is None:
        	query = self.name
        else:
        	query = ''

        params = urllib.urlencode( {
                                'q': query,
                                'num': limit 
                                } )
        headers = {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        url = '/scholar' + "?" + params
        conn = httplib.HTTPConnection( 'scholar.google.com' )
        conn.request( "GET", url, "", headers )

        resp = conn.getresponse()
        cites = []
        if resp.status == 200:
            html = resp.read()
            html = html.decode( 'ascii', 'ignore' )
            soup = BeautifulSoup( html )

            for record in soup( 'div', { 'class': 'gs_fl' } ):
                match = re.search( "Cited by ([^<]*)", str( record ) )
                
                if match is not None:
                    cite = int( match.group( 1 ) )
                    cites.append( cite )
    
            cites.sort()
            cites.reverse()
    
            h = 0
            for cite in cites:
                if cite > h:
                    h += 1
		else:
                    break

        else:
            h=0
        return h
    
    def __repr__(self):
        return self.surname + ', ' + self.name
