Demo2: Selenium
========
- [Official Website](http://www.seleniumhq.org/)
- [Github Repository](https://github.com/SeleniumHQ/selenium)
- [Documentation](http://www.seleniumhq.org/docs/)

Installation for Python
--------
- `pip install selenium`
- Add the executable web driver(Chrome is a good choice) to the Scripts folder of the Python installation folder.

Run the demo2 project
--------
- Visit the website to be crawled in Chrome and turn on the Chrome DevTools(F12 on Windows).
- Find the xpath or the css selector of the element you want to crawl or manipulate.
- Call the function `WebDriver.find_element_by_xpath()` or `WebDriver.find_element_by_css_selector()` to get the elements.
- Call the function `WebElement.click()` to perform the click action, so the content of the web page will be updated for the following crawling.