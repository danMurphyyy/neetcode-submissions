class SiteNode:

    def __init__(self, site, prev = None, next = None):
        self.site = site
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = SiteNode(homepage)

    def visit(self, url: str) -> None:
        self.node.next = SiteNode(url, self.node)
        self.node = self.node.next

    def back(self, steps: int) -> str:
        while self.node.prev and steps > 0:
            self.node = self.node.prev
            steps -= 1
        return self.node.site

    def forward(self, steps: int) -> str:
        while self.node.next and steps > 0:
            self.node = self.node.next
            steps -= 1
        return self.node.site


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)