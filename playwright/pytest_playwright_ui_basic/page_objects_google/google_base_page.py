from playwright import sync_api

class GooglePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = "input[name='q']"

    async def goto(self):
        await self.page.goto("https://www.google.com")

    async def get_title(self):
        return await self.page.title()

    async def is_search_box_visible(self):
        return await self.page.is_visible(self.search_input)