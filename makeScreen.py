import asyncio
from pyppeteer import launch

try:
    from PIL import Image
except ImportError:
    import Image

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.goto('https://www.google.com/')
    await page.screenshot({'path': 'screen1.png', 'fullPage': True})

    await page.goto('https://www.google.com/search?q=11')
    await page.screenshot({'path': 'screen2.png', 'fullPage': True})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())


background = Image.open("screen1.png")
overlay = Image.open("en.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

# new_img = Image.blend(background, overlay, 0.5)
# new_img.save("new.png","PNG")\

back = Image.open("screen1.png")
width, height = back.size
image1 = Image.open("en.png")
width1, height1 = image1.size
image1 = image1.convert("RGBA")
back.paste(image1, (width - width1, 5))
back.save("screen1_auth.png", quality=95)