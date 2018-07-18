import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"  # 识别蜘蛛。它在项目中必须是唯一的

    def start_requests(self):  # 必须返回Spider将开始爬行的可迭代请求
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # 该parse()方法通常解析响应，将抽取的数据提取为dicts，并查找要遵循的新URL并Request从中创建新的request（）。
    def parse(self, response):  # 将调用一个方法来处理为每个请求下载的响应。响应参数是TextResponse保存页面内容的实例，并具有处理它的其他有用方法
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)