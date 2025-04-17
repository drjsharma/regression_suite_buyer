import pytest
import time
from selenium.webdriver.common.by import By
from setup.login_buyer import login  # Import login function
from setup.setup_driver import setup  # Import setup fixture
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("setup")
class TestRFQWizard:

    def test_login(self, setup):
        """Logs in before running filter tests"""
        driver = setup  # Use the fixture WebDriver
        login(driver)  # Reusable login


    def test_rfq_wizard_request_form(self,setup):
        driver=setup
        wait=WebDriverWait(driver,10)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiButton-contained > .MuiTypography-root")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".MuiButton-contained > .MuiTypography-root"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiFormControlLabel-root:nth-child(2) > .MuiButtonBase-root")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".MuiFormControlLabel-root:nth-child(2) > .MuiButtonBase-root"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-1j4vbtd")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-1j4vbtd"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-175s3hj")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-175s3hj"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".rfq-wizard")))

    
    def test_rfq_wizard_mandatory_elements_check(self,setup):
        driver=setup
        wait=WebDriverWait(driver,10)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-1ofqig9 > .MuiFormHelperText-root")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".css-1ofqig9 > .MuiFormHelperText-root"),"Invalid RFQ name"))

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiBox-root:nth-child(2) > span > .MuiFormHelperText-root")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".MuiBox-root:nth-child(2) > span > .MuiFormHelperText-root"),"Invalid bid end date"))

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiBox-root:nth-child(3) > span > .MuiFormHelperText-root")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".MuiBox-root:nth-child(3) > span > .MuiFormHelperText-root"),"Invalid expected delivery date"))

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiFormHelperText-root:nth-child(1)")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".MuiFormHelperText-root:nth-child(1)"),"Invalid RFQ items"))

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-13p9ov9")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-13p9ov9"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-175s3hj")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-175s3hj"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiTableCell-root:nth-child(1) > .MuiFormHelperText-root")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".MuiTableCell-root:nth-child(1) > .MuiFormHelperText-root"),"Invalid item name"))

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiTableCell-root:nth-child(4) > .MuiFormHelperText-root")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".MuiTableCell-root:nth-child(4) > .MuiFormHelperText-root"),"Invalid UOM"))

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".MuiTableCell-root:nth-child(5) > .MuiFormHelperText-root")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".MuiTableCell-root:nth-child(5) > .MuiFormHelperText-root"),"Invalid quantity"))



    def test_bid_end_date(self,setup):
        driver=setup
        wait=WebDriverWait(driver,10)

        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[2]/span/div/div/div/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[2]/span/div/div/div/button"))).click()

        today_timestamp = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today = int(today_timestamp.timestamp() * 1000)
        one_day = int((today_timestamp + timedelta(days=1)).timestamp() * 1000)
        two_day = int((today_timestamp + timedelta(days=2)).timestamp() * 1000)
        three_day = int((today_timestamp + timedelta(days=3)).timestamp() * 1000)

        print(today)
        print(one_day)
        print(two_day)
        print(three_day)

        # Selectors
        selector0 = f'[data-timestamp="{today}"]'
        selector1 = f'[data-timestamp="{one_day}"]'
        selector2 = f'[data-timestamp="{two_day}"]'
        selector3 = f'[data-timestamp="{three_day}"]'

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector0)))
        assert not EC.element_to_be_clickable((By.CSS_SELECTOR, selector0))(driver), "❌ Today SHOULD NOT be clickable"

        # 1 Day Ahead - should NOT be clickable
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector1)))
        assert not EC.element_to_be_clickable((By.CSS_SELECTOR, selector1))(driver), "❌ 1 day ahead SHOULD NOT be clickable"

        # 2 Day Ahead - should be clickable
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector2)))
        assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector2))), "❌ 2 day ahead SHOULD be clickable"

        # 3 Day Ahead - should be clickable
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector3)))
        assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector3))), "❌ 3 day ahead SHOULD be clickable"




    '''def test_expected_delivery_date(self,setup):
        driver=setup
        wait=WebDriverWait(driver,10)

        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[2]/span/div/div/div/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[2]/span/div/div/div/button"))).click()

        today_timestamp = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today = int(today_timestamp.timestamp() * 1000)
        two_days = int((today_timestamp + timedelta(days=2)).timestamp() * 1000)
        three_days= int((today_timestamp + timedelta(days=3)).timestamp() * 1000)

        selector1 = f'[data-timestamp="{two_days}"]'
        selector2 = f'[data-timestamp="{three_days}"]'

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,selector1)))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selector1))).click()




        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[3]/span/div/div/div/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[3]/span/div/div/div/button"))).click()
        
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector1)))
        assert not EC.element_to_be_clickable((By.CSS_SELECTOR, selector1))(driver)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector2)))
        assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector2)))


        driver.find_element(By.ID,':rt:').clear()'''



        

    def test_rfq_name(self,setup):
        driver=setup
        wait = WebDriverWait(driver,10)

        wait.until(EC.presence_of_element_located((By.ID,":rr:")))
        wait.until(EC.element_to_be_clickable((By.ID,":rr:"))).send_keys("testds@123")

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-175s3hj")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-175s3hj"))).click()

        time.sleep(1)

        assert not EC.text_to_be_present_in_element((By.CSS_SELECTOR,".css-1ofqig9 > .MuiFormHelperText-root"),"Invalid RFQ name")(driver)

        driver.find_element(By.ID,":rr:").clear()



    def test_rfq_terms(self,setup):
        driver=setup
        wait=WebDriverWait(driver,10)

        wait.until(EC.presence_of_element_located((By.ID,":r12:")))
        wait.until(EC.text_to_be_present_in_element((By.ID,":r12:"),"60 DAYS"))

        driver.find_element(By.ID,":r12:").clear()

        time.sleep(1)

        driver.find_element(By.ID,":r12:").send_keys("60 DAYS")

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-175s3hj")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-175s3hj"))).click()

        time.sleep(1)

        wait.until(EC.presence_of_element_located((By.ID,":r12:")))
        wait.until(EC.visibility_of_element_located((By.ID,":r12:")))

        driver.find_element(By.ID,":r12:").clear()

    
    def test_rfq_wizard_create(self,setup):
        driver=setup
        wait=WebDriverWait(driver,10)

        wait.until(EC.presence_of_element_located((By.ID,":rr:")))
        wait.until(EC.element_to_be_clickable((By.ID,":rr:"))).send_keys("testds@123")



        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[2]/span/div/div/div/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[2]/span/div/div/div/button"))).click()

        today_timestamp = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today = int(today_timestamp.timestamp() * 1000)
        two_day = int((today_timestamp + timedelta(days=2)).timestamp() * 1000)
        selector1 = f'[data-timestamp="{two_day}"]'

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector1)))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector1))).click()




        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[3]/span/div/div/div/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div[3]/span/div/div/div/button"))).click()
        
        three_days= int((today_timestamp + timedelta(days=3)).timestamp() * 1000)
        selector2 = f'[data-timestamp="{three_days}"]'

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector2)))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector2))).click()



        '''wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-13p9ov9")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-13p9ov9"))).click()'''

        wait.until(EC.presence_of_element_located((By.ID,":r14:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r14:"))).send_keys("Bulb")

        wait.until(EC.presence_of_element_located((By.ID,":r15:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r15:"))).send_keys("SYSKA")

        wait.until(EC.presence_of_element_located((By.ID,":r16:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r16:"))).send_keys("LED")

        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[5]/div/div/table/tbody/tr[1]/td[4]/div/div")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[5]/div/div/table/tbody/tr[1]/td[4]/div/div"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[data-value="NOT_APPLICABLE"]')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-value="NOT_APPLICABLE"]'))).click()

        wait.until(EC.presence_of_element_located((By.ID,":r18:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r18:"))).send_keys(2)



        '''driver.find_element(By.CSS_SELECTOR,".css-1v6qxbp").click()
        wait.until(EC.presence_of_element_located((By.ID,":r19:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r19:"))).send_keys("Tubelight")

        wait.until(EC.presence_of_element_located((By.ID,":r1a:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r1a:"))).send_keys("PHILIPS")

        wait.until(EC.presence_of_element_located((By.ID,":r1b:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r1b:"))).send_keys("WALLMOUNT")

        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[5]/div/div/table/tbody/tr[2]/td[4]/div/div")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"root\"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[5]/div/div/table/tbody/tr[2]/td[4]/div/div"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[data-value="NOT_APPLICABLE"]')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-value="NOT_APPLICABLE"]'))).click()

        wait.until(EC.presence_of_element_located((By.ID,":r1d:")))
        wait.until(EC.element_to_be_clickable((By.ID,":r1d:"))).send_keys(1)'''

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".css-175s3hj")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".css-175s3hj"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".ackBtn > .MuiTypography-root")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".ackBtn > .MuiTypography-root"))).click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".message")))
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".message")))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".message"),"RFQ created successfully"))

        time.sleep(5)


if __name__=="__main__":
    pytest.main(["-v","--tb=short",__file__])
