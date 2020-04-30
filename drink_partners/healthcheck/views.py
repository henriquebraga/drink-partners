from aiohttp import web


class HealthCheckView(web.View):
    async def get(self):
        return web.json_response(data={'status': 'OK'})
