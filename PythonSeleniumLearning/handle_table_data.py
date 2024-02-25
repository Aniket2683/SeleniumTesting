from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class handle_table_data_demo():
    def table_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()

        print("\n\n\nTable data in Full Table : ")
        table_data = driver.find_elements(By.XPATH,"//table[@id='table1']//td")

        for data in table_data:
            print(data.text)

        print("\n\n\nTable data in First Row : ")
        table_firstrow = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]/td")

        for first_data in table_firstrow:
            print(first_data.text)

        # similar can be done for each row .By changing the tr[n th row] in the XPATH


        #now for a specific cell
        print("\n\n\nTable data in Third Row Second column :")
        table_3row2column = driver.find_element(By.XPATH, "//table[@id='table1']//tr[3]/td[2]")
        print(table_3row2column.text)

        # now for data in 3rd column
        print("\n\n\nTable all data in Third column :")
        table_3column = driver.find_elements(By.XPATH, "//table[@id='table1']//td[3]")
        for data_3 in table_3column:
            print(data_3.text)


        #Number od rows and columns of table
        print("\n\nSize of table : ")
        rows = driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
        print("Rows : ",len(rows))
        cols = driver.find_elements(By.XPATH, "//table[@id='table1']//th")
        print("Cols : ", len(cols))

        driver.quit()
demo1 = handle_table_data_demo()
demo1.table_demo()


