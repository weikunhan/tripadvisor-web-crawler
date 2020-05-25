# -*- coding: utf-8 -*-
from tripadvisor import Tripadvisor
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tripadvisor Web crawler.')
    parser.add_argument('-q', '--place_name', type=str, required=True, help='Crawling tartget place informaiton based on a string query')
    parser.add_argument('-s', '--section_name', type=str, required=True, help='Crawling urls of section based on the search result for one place')
    args = parser.parse_args()

    # scrape urls of places
    if args.place_name:
        crawler = Tripadvisor()
        urls = crawler.get_urls(args.place_name, args.section_name)
        print(urls)