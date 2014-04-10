# -*- coding: utf-8 -*-
from Bio import Entrez, Medline
from httplib import HTTPException
import constval

'''
Created on 23-13-2012

@author: Piotr Król
'''

class Article(object):
    pmid = None
    authors = None
    
    __authors_cache = {}
    
    # Mail address given to Entrez db
    __user_email = constval.USER_MAIL 

    def __init__(self, pmid, authors):
        self.pmid = pmid
        self.authors = authors
    
    @staticmethod
    def clear_cache():
        Article.__authors_cache = {}
    
    # Gets from PubMed certain given number of articles
    #
    # @param query: phrase it is looked for
    # @param retmax: max number of returned values
    #
    # @return: List consisted of
    # <i>retmax</i> articles as a response for <i>query</i> 
    @staticmethod
    def get_articles(query):
        articles_ids = Article.__get_article_ids(query, constval.MAX_RET)
        return Article.__get_articles_by_ids(articles_ids)
    
    # Gets citations form PubMed 
    # @return: List of citations
    def get_related_citations(self):
        article_ids = self.__get_related_citations_ids()
        return self.__get_articles_by_ids( article_ids )
    
    # Gets from PubMed number of citations
    # @return: Number of citations
    def get_related_citations_number(self):
        return len(self.__get_related_citations_ids())
    
    # Gets from PubMed certain given number of ids
    #
    # @param query: phrase it is looked for
    # @param retmax: max number of returned values
    #
    # @return: List of ids
    @staticmethod
    def __get_article_ids(query, retmax):
        Entrez.email = Article.__user_email

        handle = Entrez.esearch( db = 'pubmed',
                                 term = query,
                                 retmax = retmax
                                 )
        record = Entrez.read( handle )
        return record['IdList']

    # Gets from PubMed certain given number of cited ids
    #
    # @param query: phrase it is looked for
    # @param retmax: max number of returned values
    #
    # @return: List of cited ids
    def __get_related_citations_ids(self):
        Entrez.email = Article.__user_email
        handle = Entrez.elink( dbfrom = 'pubmed',
                               id = self.pmid,
                               linkname = 'pubmed_pubmed'
                               )
        records = Entrez.read( handle )
        
        article_ids = [ 
            link["Id"] for link in records[0]["LinkSetDb"][0]["Link"]
            ]

        return article_ids
    
    # Gets from PubMed articles with certain id
    #
    # @param article_ids: List of ids
    # @param retmax: max number of returned values
    #
    # @return: List of articles
    @staticmethod
    def __get_articles_by_ids(article_ids):
        if article_ids is None or len(article_ids) == 0:
            return []
        
        Entrez.email = Article.__user_email        
        handle = Entrez.efetch( db = 'pubmed',
                                id = article_ids,
                                rettype = 'medline',
                                retmode = 'text'
                                )
             
        records = Medline.parse( handle )

        articles = []
        for record in records:
            pmid = record['PMID']
            authors = None
            
            if 'FAU' in record:
                authors = record['FAU']
            else:
                authors = ['CN']
            
            authors_objs = []
            for author in authors:
                name = author
                surname = None
                
                if ', ' in author:
                    [surname, name] = str.split(author, ', ')
                
                from author import Author
                
                if name is not None and surname is not None:
                    author_str = name + ' ' + surname
                elif name is not None and surname is None:
                    author_str = name
                elif name is None and surname is not None:
                    author_str = surname
                else:
                    author_str = ''
                    
                if(author_str not in Article.__authors_cache):
                    authors_objs.append( Author(name, surname) )
                else:
                    authors_objs.append( Article.__authors_cache[author_str])

            articles.append( Article( pmid, authors_objs ) )

        return articles