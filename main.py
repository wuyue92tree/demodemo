# encoding=utf8
from crwy.spider import Spider


class Runner(Spider):
    def __init__(self):
        super(Runner, self).__init__()

    def crawl(self):
        self.logger.info('start crawl.')
        url = 'http://example.com/'
        # 基于requests封装
        res = self.html_downloader.download(url)
        return res

    def parse(self, content):
        self.logger.info('start parse')
        # 基于beautifulsoup封装
        soups = self.html_parser.parser(content)
        return soups

    def executor(self):
        res = self.crawl()
        title = self.parse(res.text).find('title').text
        self.logger.info(f'site title is: {title}')

def main():
    runner = Runner()
    runner.executor()


if __name__ == '__main__':
    main()