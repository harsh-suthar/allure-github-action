import os
import time

from PIL import Image, ImageDraw, ImageFont


class imageprocess:

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, url, img_type):
        page_name = url.rsplit('/', 1)[-1]
        print(page_name)
        print("Capturing", url, "screenshot as ", page_name + '_' + img_type + '.png')
        self.driver.get(url)
        # self.driver.maximize_window()
        time.sleep(5)
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        if img_type == 'base':
            path = os.path.join(os.getcwd(), 'screenshots/base', page_name + '_' + img_type + '.png')
            print(path)
            self.driver.set_window_size(1920, page_height)
            self.driver.save_screenshot(path)
            self.driver.get_screenshot_as_png()
            print("Done.")
        elif img_type == 'actual':
            path = os.path.join(os.getcwd(), 'screenshots/actual', page_name + '_' + img_type + '.png')
            self.driver.set_window_size(1920, page_height)
            self.driver.save_screenshot(path)
            self.driver.get_screenshot_as_png()
            print("Done.")
        else:
            print("Image type should be Base Or Actual")

    def analyze(self, base_img, actual_img):
        base_path = os.path.join(os.getcwd(), 'screenshots/base', base_img)
        actual_path = os.path.join(os.getcwd(), 'screenshots/actual', actual_img)
        screenshot_base = Image.open(base_path)
        screenshot_actual = Image.open(actual_path)
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot_actual.size
        result = True
        block_width = ((screen_width - 1) // columns) + 1
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height + 1):
            for x in range(0, screen_width, block_width + 1):
                region_actual = self.process_region(screenshot_actual, x, y, block_width, block_height)
                region_base = self.process_region(screenshot_base, x, y, block_width, block_height)

                if region_actual is not None and region_base is not None and region_base != region_actual:
                    draw = ImageDraw.Draw(screenshot_actual)
                    draw.rectangle((x, y, x + block_width, y + block_height), outline="red")
                    result = False

        if not result:
            image1_size = screenshot_actual.size
            output = Image.new('RGB', (2 * image1_size[0], image1_size[1]))
            output.paste(screenshot_actual, (0, 0))
            font = ImageFont.truetype("fonts.ttf", 25)
            screenshot_base = Image.open(base_path)
            draw = ImageDraw.Draw(screenshot_base)
            draw.text((200, 200), "This is Base Image", font=font)
            cache_path = os.path.join(os.getcwd(), 'screenshots/cache', 'homepagecache.png')
            screenshot_base.save(cache_path)
            cache_base = Image.open(cache_path)
            output.paste(cache_base, (image1_size[0], 0))
            output.save("screenshots/result/merged_image.jpg", "JPEG")
            assert False
        else:
            assert True

    def process_region(self, image, x, y, width, height):
        region_total = 0
        factor = 150
        for coordinateY in range(y, y + height):
            for coordinateX in range(x, x + width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel) / 4
                except:
                    return
        return region_total / factor
