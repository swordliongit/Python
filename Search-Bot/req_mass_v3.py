import asyncio
from aiohttp import ClientSession
from requests.exceptions import HTTPError






class SearchBotProviderSearchBots(models.Model):
    _name = 'tourism.providers.search_bots'
    _description = 'Search Bot Provider'

    name = fields.Char('Search Bot Name')
    provider = fields.Selection(
        string='Provider',
        selection=[
            ('coraltravel', 'CoralTravel'),
            ('tatilbudur', 'TatilBudur.com'),
            ('tatilcom', 'Tatil.com'),
            ('jollytur', 'Jollytur.com'),
            ('etstur', 'EtsTur.com'),
            ('tatilsepeti.com', 'Tatilsepeti.com'),
            ('odamax.com', 'Odamax.com'),
            ('otelz.com', 'Otelz.com'),
            ('setur', 'Setur'),
            ('local', 'Local'),
        ],
    )
    detail = fields.Char('Detail')
    bot_detail_id = fields.Many2one(
        'tourism.providers.search_bot.detail', string='Search Bot Details'
    )
    
    URLS = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1,101)]
    RESULTS = []    
    
    async def get(self, url, session):
        try:
            response = await session.request(method='GET', url=url)
            response.raise_for_status()
            # print(f"Response status ({url}): {response.status}")
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error ocurred: {err}")
        response_json = await response.json()
        return response_json


    async def run_program(self, url, session):
        try:
            response = await self.get(url, session)
            self.RESULTS.append(response)
        except Exception as err:
            print(f"Exception occured: {err}")
            pass


    async def main(self):
        async with ClientSession() as session:
            await asyncio.gather(*[self.run_program(url, session) for url in self.URLS])
            
    def run_async(self):
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        s = time.perf_counter()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())

        elapsed = time.perf_counter() - s

        print(f"Completed {len(self.URLS)} requests with {len(self.RESULTS)} results")
        for i in self.RESULTS:
            print(str(i))
        print(elapsed)

    def get_provider_detail(self):
        bag = {
            'urls': {
                'coraltravelZena': "https://www.coraltatil.com/Ajax/Hotel2.ashx?get=hotellist&name=Zena+Resort+Hotel",
                'coraltravelAres': "https://api.tatil.com/autocomplete?q=Ares%20Dream",
                'tatilbudur': "https://www.tatilbudur.com/hotel/search?term=Quadas%20Hotel",
                'tatilcom': '',
                'jollytur': "https://www.jollytur.com/Shared/Search?type=HotelPlanner&key=emily%20&_=1694593478310",
                'etstur': "https://www.etstur.com/Otel/ajax/autocomplete?pagetype=SEARCH&q=Ares%20Dream%20Hotel",
                'tatilsepeti': "",
                'odamax': "",
                'otelz': "",
                'setur': "",
            },
            'proxies': {
                'http': "http://snapproxy:DsQWzRwjVM@89.43.67.180:3128",
                'https': "http://snapproxy:DsQWzRwjVM@89.43.67.180:3128",
            },
            'proxies_ovh': {
                'http': "http://snapproxy:DsQWzRwjVM@188.165.56.45:3128",
                'https': "http://snapproxy:DsQWzRwjVM@188.165.56.45:3128",
            },
            'headers': {
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
                'Content-Type': 'application/json',
            }
        }
        
        if self.provider == "coraltravel":
            self.process_provider(bag, 'coraltravel')
        elif self.provider == "tatilbudur":
            self.process_provider(bag, 'tatilbudur')
        elif self.provider == "tatilcom":
            pass
        elif self.provider == "jollytur":
            self.process_provider(bag, 'jollytur')
        elif self.provider == "etstur":
            # self.protothread()
            t = threading.Thread(target=self.run_async)
            t.start()
            
        elif self.provider == "tatilsepeti.com":
            pass
        elif self.provider == "odamax.com":
            pass
        elif self.provider == "otelz.com":
            pass
        elif self.provider == "setur":
            pass