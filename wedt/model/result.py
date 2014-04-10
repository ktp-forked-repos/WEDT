# -*- coding: utf-8 -*-
'''
Created on 06-01-2013

@author: Piotr Jastrzębski
'''

from threading import Thread
from Queue import Queue
import math
import threading

class Result:
    hitsNumber = 0
    googleHits = 0
    wikiHits = 0
    pubmedHits = 0
    articleList = None 
    bioToolCheck = None
    semaphore = None
        
    def __init__(self, inputStr):
        from biotool import BioTool
        self.bioToolCheck = BioTool(inputStr)
        self.semaphore = threading.Semaphore()
        
    # Calculate a part of final grade using English Wikipedia 
    # @return: number of articles in english wikipedia
    def getWiki(self):
        tmp = self.bioToolCheck.get_wikipedia_results_count()
        self.semaphore.acquire()
        self.wikiHits += tmp
        self.semaphore.release()
        
    # Calculate a part of final grade using Google web searcher
    # @return: number of articles divided by 1000 in google
    def getGoogle(self):
        tmp = int(math.ceil(self.bioToolCheck.get_google_results_count() / 1000.0))
        self.semaphore.acquire()
        self.googleHits += tmp
        self.semaphore.release()
    
    # Method for a single thread processing single author's h-index
    def checkSingleAuthor(self, singleAuthor, q):
        q.put(singleAuthor.get_h_index())
    
    # Method for a single thread processing single article
    def checkSingleArticle(self, singleArticle, i):
        # Power of the article itself is multiplied by...
        articlePower = 1.0 * (len(self.articleList) - i) / len(self.articleList)
        hIndexSum = 0
        
        q = Queue()
        threads = []
        for singleAuthor in singleArticle.authors:
            tSingle = Thread(target=self.checkSingleAuthor, args=(singleAuthor, q))
            tSingle.start()
            threads.append(tSingle)
            
        for oneThread in threads:
            oneThread.join()

        while(q.empty() != True):    
            hIndexSum += int(q.get())
        # ...a sum of average h-index of all authors and...
        avgHIndex = 1.0 * hIndexSum / len(singleArticle.authors)
        # ...number of citations.
        numOfCitation = singleArticle.get_related_citations_number()
        self.semaphore.acquire()
        self.pubmedHits += int(math.ceil(articlePower * (avgHIndex + numOfCitation)))
        self.semaphore.release()
      
    # Calculate a part of final grade using Articles from PubMed db
    def getFromArticles(self):
        self.articleList = self.bioToolCheck.get_articles()

        i = 0
        threads = []
        for singleArticle in self.articleList:
            # Considering single article
            tSingle = Thread(target=self.checkSingleArticle, name=i, args=(singleArticle, i),)
            i += 1
            tSingle.start()
            threads.append(tSingle)
            
        for oneThread in threads:
            oneThread.join()
            
        # Number of all articles plus sum from all of them
        self.semaphore.acquire() 
        self.pubmedHits += len(self.articleList)
        self.semaphore.release()
        
    # Grade is given as:
    # Total + Sum(i=0 -> Total-1) [(Total-i)/Total]*(hIndexMean+NumberOfCitations)        
    # @return: total grade for a tool
    def getHits(self):
        return self.pubmedHits, self.googleHits, self.wikiHits
