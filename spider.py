# this module defines Spider class to crawl web
from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider():

    # class variables
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set() # store the queue links
    crawled = set() # store the crawled links

    # A web page's URL cannot be in both the queue file and the crawled file at the same time
    # make sure not to crawl the same link twice => use set
    
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        # the first Spider create files
        # and add link into set
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')

            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)

        except:
            print("Error: cannot crawl page")
            return set()
        
        return finder.page_links()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue or url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)
    
    @staticmethod
    def update_files():
        # update queue and crawled set
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
