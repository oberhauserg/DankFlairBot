import praw
import sqlite3


import time
import ThreadedServices
from DatabaseManager import DatabaseManager
from RedditManager import RedditManager
from ruamel.yaml import YAML
import threading
import Rule
from RulesManager import RulesManager

SUBREDDIT = "dankmemes"

def main():

    DatabaseManager.init_connection('test.sqlite')

    DatabaseManager.create_tables()

    RedditManager.login_threads_from_file("config.yml")

    RedditManager.get_messages()

#    ThreadedServices.setup_threads(SUBREDDIT)

    ThreadedServices.setup_threads("OnionHate")

    while True:
        time.sleep(0)


if __name__ == "__main__":
    main()