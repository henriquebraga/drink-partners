from aiohttp import web

from drink_partners.backends.pools.partners import PartnersBackendPool


class PartnerView(web.View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.datasource = PartnersBackendPool.get_default()
