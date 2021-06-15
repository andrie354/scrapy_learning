import scrapy


class MercedesSpider(scrapy.Spider):
    name = 'mercedes'
    allowed_domains = ['olx.co.id']
    start_urls = ['https://www.olx.co.id/mobil-bekas_c198?filter=make_eq_mobil-bekas-audi']

    def parse(self, response):
        for audis in response.css('div.IKo3_'):
            yield {
                'nama': audis.css('span._2tW1I::text').get(),
                'tahun': audis.css('span._2TVI3::text').get(),
                'harga': audis.css('span._89yzn::text').get().replace('Rp ','')
            }
