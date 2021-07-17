from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

def scrap(a):
    print("Scrap jalan")
    myprofile = webdriver.FirefoxProfile('/Users/irenegloriia/Library/Application Support/Firefox/Profiles/egc4m9xh.stockbitScrap')
    PATH = "/opt/homebrew/Cellar/geckodriver/0.29.0/bin/geckodriver"
    driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)
    
    driver.get(a)
    # print('isi dari A : ',a)


    if ("Bisnis.com" in a or "bisnis.com"  in a):
        link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
        a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, link))).get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(a)
        try:
            time = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[2]/div/span").text
            title = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/h1").text
            link = driver.current_url
            box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[5]/div/div[1]")
            paragraf = box.find_elements_by_xpath("./child::*")
            teksPosting = []
            for a in paragraf:
                if (a.tag_name == "p" or a.tag_name == "table"):
                    if not (a.text[:7]=="Sumber:" or a.text[7:]=="Editor :"):
                        a = a.text.split("\n")
                        a = " ".join(a)
                        teksPosting.append(a)

            teksPosting = " ".join(teksPosting)
        except:
            time = "Bisnis.com Error"
            title = "Bisnis.com Error"
            teksPosting = "Bisnis.com Error"
            link = "Bisnis.com Error"

        # print('Waktu', time)
        # print('Judul', title)
        # print(link)
        # print(teksPosting) 
        # print("=======================================================================================================================")
        driver.close()
        return teksPosting

    elif ("ipotnews.com" in a):
        print(dateTime)
        link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
        a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, link))).get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(a)
        box = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl')
        paragraf = box.find_elements_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/article')
        title = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/dt').text
        time = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/div/small').text
        link = driver.current_url

        # print('Judul = ' +title)
        # print('Waktu = ' +time)
        # print(link)
        teksPosting = ''
        for n in range(len(paragraf)):
            teksPosting = teksPosting + paragraf[n].text + ' '
        for match in re.finditer('Sumber', teksPosting):
            sumber = match.start()
        teksPosting = teksPosting[:sumber]
        # print(teksPosting)
        # print("=======================================================================================================================")
        driver.close()
        return teksPosting

    elif ("cnbcindonesia.com" in a):
        try :
            link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
            a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(a)
            box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article')
            nampung = box.find_element_by_xpath(".//div[@class='detail_text']")
            paragraf = nampung.find_elements_by_tag_name('p')
            time = driver.find_element_by_xpath(".//div[@class='date']").text
            link = driver.current_url

            if (len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/article/div[3]/div/div/h2")) > 0 ): 
                title = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[3]/div/div/h1").text
            else : 
                title = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[1]/div/div/h1").text
            
            teksPosting = ''
            if (len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/article/div[7]/a/i")) > 0):
                for n in range(len(paragraf)):
                    if not ("NEXT:" in paragraf[n].text[:5]):
                        teksPosting = teksPosting + paragraf[n].text
                next = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[7]/a/i")
                driver.execute_script("arguments[0].scrollIntoView(true);", next )
                next.click()
                box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article')
                nampung = driver.find_element_by_xpath(".//div[@class='detail_text']")
                paragraf = nampung.find_elements_by_tag_name('p')

                for i in range(len(paragraf)):
                    if not ("NEXT:" in paragraf[i].text[:5]):
                        teksPosting = teksPosting + paragraf[i].text 
            else :
                for i in range(len(paragraf)):
                    if not ("NEXT:" in paragraf[i].text[:5]):
                        teksPosting = teksPosting + paragraf[i].text
        except :
            time = 'error cnbc'
            title = 'error cnbc'
            teksPosting = 'error cnbc'
            link = 'error cnbc'
        teksPosting = teksPosting.replace('Jakarta, CNBC Indonesia - ','')
        teksPosting = teksPosting.replace('TIM RISET CNBC INDONESIA','')   
        # print('Judul = ' +title)
        # print('Waktu = ' +time)
        # print(link)
        # print(teksPosting)
        # print("=======================================================================================================================")
        driver.close()
        return teksPosting

    elif ("kontan.co.id" in a):
        print('Jalan kontan')
        artikel = driver.find_element_by_class_name('tmpt-desk-kon')
        isi = artikel.find_elements_by_tag_name('p')
        title = driver.find_element_by_class_name('detail-desk').text
        #time = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div[2]').text
        #time = driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/div[1]/div[2]').text
        # if (len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]")) > 0 ): 
        #     time = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]").text
        # else : 
        #     time = driver.find_element_by_xpath("html/body/div[2]/div[2]/div[1]/div[1]/div[2]").text
        #                                         /html/body/div[1]/div[2]/div/div[1]/div[2]                                 
        link = driver.current_url
        teksPosting = ''
        for n in range(1, len(isi)):
            if(isi[n].text[:9] != "Baca Juga"):
                teksPosting= teksPosting + isi[n].text + ' '
        # print('Judul = ' +title)
        # print('Waktu = ' +time)
        # print(link)
        # print(teksPosting)
        # print("=======================================================================================================================")
        driver.close()
        isi = [
            title,teksPosting
        ]
        return isi
    elif ("kompas.com" in a):
        try :
            link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
            a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(a)
            if (len(driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div[7]/div/div[3]")) > 0):
                showAll = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div[7]/div/div[3]')
                driver.execute_script("arguments[0].scrollIntoView(true);", showAll )
                showAll.click()
                time.sleep(10)
            box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div[2]/div[1]')
            paragraf = box.find_elements_by_tag_name('p')
            title = driver.find_element_by_xpath("//h1[@class='read__title']").text
            time = driver.find_element_by_xpath("//div[@class='read__time']").text
            link = driver.current_url
            teksPosting = ''
            for n in range(len(paragraf)):
                if not ("Baca jug" in paragraf[n].text[:9]):
                    teksPosting = teksPosting + paragraf[n].text + ''
        except :
            time = 'error kompas'
            title = 'error kompas'
            teksPosting = 'error kompas'
            link = 'error'
# driver.close()
        return teksPosting

    elif ("indotelko.com" in a):
        try :
            link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
            a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(a)
            teksPosting = driver.find_element_by_xpath("//div[@id='font_news']").text
            teks2 = teksPosting.find_element_by_xpath('//*[@id="box_bj"]')
            title = driver.find_element_by_xpath('//*[@id="title"]').text
            time = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[4]').text
            link = driver.current_url

            if (len(driver.find_elements_by_xpath("/html/body/div[1]/div[4]/div[1]/div[4]")) > 0 ): 
                time = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[4]").text
            else : 
                time = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[5]/div[1]/div[4]").text
            
        except :
            time = 'indotelko error'
            title = 'indotelko error'
            teksPosting = 'indotelko error'
            link = 'indotelko error'
        driver.close()
        return teksPosting

    elif ("neraca.co.id" in a):
        link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
        a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, link))).get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(a)
        box = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div')
        paragraf = box.find_elements_by_tag_name('p')
        title = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/h1').text
        time = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/span[2]').text
        link = driver.current_url

        # print('Judul = ' +title)
        # print('Waktu = ' +time)
        # print(link)
        teksPosting = ''
        for n in range(len(paragraf)):
            teksPosting = teksPosting + paragraf[n].text + ' '
        # print(teksPosting)
        # print("=======================================================================================================================")
        driver.close()
        return teksPosting