# main module of entire program (starting point)
import threading
from queue import Queue
from spider import Spider
from general import *
from domain import *

# The idea is create multiple threads (Spider) to crawl multiple web pages simultinuously
# Create 2 files
# queue.txt: containing links in the waiting list
# crawled.txt: containing crawled paths

# global variables
PROJECT_NAME = 'teamdatascience'
HOMEPAGE = 'https://www.teamdatascience.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

# each element in queue is a job
queue = Queue()
# create first Spider
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_workers():
    # create multiple threads, with each thread as a worker
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work, daemon=True)
        t.start()


def work():
    # threads work until no longer job
    while True:
        url = queue.get() # get element in the queue
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def crawl():
    # if there are links in queue, add job into queue
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


def create_jobs():
    # Add job into queue
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    # Blocks until all items in the queue have been processed
    queue.join()


create_workers()
crawl()