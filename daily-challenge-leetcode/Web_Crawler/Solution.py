# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from collections import deque


class Solution:

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        ans = set()
        domain = startUrl.split('/')[2]
        que = deque([startUrl])
        while que:
            curr = que.popleft()
            if curr not in ans and domain == curr.split('/')[2]:
                ans.add(curr)
                for url in htmlParser.getUrls(curr):
                    que.append(url)
        return ans
