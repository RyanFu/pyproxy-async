from src.app.ip_get import IPGet, SiteResponse
from src.lib.structs import SiteData, SiteResponseData

key = 'jiangxianli'


@IPGet.config(key)
def config():
    site = SiteData()
    site.name = '免费代理IP库'
    site.pages = ['http://ip.jiangxianli.com/?page=%d' % i for i in range(1, 5)]
    return site


@IPGet.parse(key)
def parse(resp: SiteResponse):
    items = resp.xpath('//tr')[1:]
    for item in items:
        try:
            res = SiteResponseData()
            res.ip = item.xpath('.//td[2]//text()')[0]
            res.port = item.xpath('.//td[3]//text()')[0]
            yield res
        except Exception:
            continue


if __name__ == '__main__':
    from src.lib.func import run_until_complete

    runner = IPGet.test_crawl(key)
    run_until_complete(runner)
