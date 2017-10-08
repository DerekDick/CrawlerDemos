from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.sse.com.cn/assortment/stock/list/share/")

print("sleeping...")
time.sleep(3)

for page_index in range(2, 7):
    table = driver.find_element_by_css_selector("#tableData_ > div.table-responsive.sse_table_T01.tdclickable > table")
    rows = table.find_elements_by_tag_name("tr")
    print(len(rows))
    for i in range(1, len(rows)):
        print(rows[i].find_elements_by_tag_name("td")[1].text)

    input_page_index = driver.find_element_by_css_selector("#ht_codeinput")
    input_page_index.send_keys("%d\n" % page_index)
    print("sleeping...")
    time.sleep(3)
