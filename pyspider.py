#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

from pattern.web import Spider
# import requests
# from pyquery import PyQuery as pq

class Spiderling(Spider):
    def visit(self, link, source=None):
        print 'visited: ', repr(link.url), 'from: ', link.referrer
        # print self.history
        # print self.visited
        # p = pq(requests.get(link.url).text)
        # for i in p('img')[1:]:
            # print pq(i).attr('src')
        if len(self.visited) > 10:
            self.done = True
    def fail(self, link):
        print 'failed: ', repr(link.url)

# Gather our code in a main() function
def main():
    method = 'BREADTH'
    if sys.argv[2]:
        method = sys.argv[2]
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    s = Spiderling(links=[sys.argv[1]], delay=5)
    while not s.done:
        s.crawl(method=method, cached=False, throttle=5)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
