from bs4 import BeautifulSoup as bs
import requests

def scrap(a):
    if ("cnbcindonesia.com" in a):
        teks = ''
        while a != "kosong":
            # print("masuk2")
            src = requests.get(a)
            document = bs(src.content , "lxml")
            # print(src.status_code)

            content = document.find("div",attrs={"class":"jdl"})
            title2 = content.find_all("h1")
            for b in title2:
                print(b.text)
                title = b.text

            berita = document.find("div",attrs={"class":"detail_text"})
            baca = berita.find("div",attrs={"class":"lihatjg"})
            teks2 = berita.text  
            if (baca != None ) :
                bacajg = baca.text
                teks2 = teks2.replace(bacajg,"") 
            teks = teks + teks2 + "\n\n"
            nextpage = document.find("div",attrs={"class":"long-cta text_right"})
            if (nextpage != None):
                a = nextpage.find("a",attrs={"class":"btn btn_inline gtm_button_indeks_newsfeed"})['href']
            else :
                a = "kosong"

            # print(b)
        return [title,teks]
    
    elif ("indotelko.com" in a):
        src = requests.get(a)
        document = bs(src.content , 'lxml')

        title2 = document.find("div",attrs={"id":"box_left"})
        judul = title2.find("div",attrs={"id":"title"})
        tes = judul.find_all("h1")
        print(judul.text)
        title = judul.text
        isi = document.find("div",attrs={"id":"font_news"})
        baca = isi.find("div",attrs={"id":"box_bj"})
        teks = isi.text
        bacajg = baca.text
        teks = teks.replace(bacajg,"")
        return [title,teks]

    elif ("ipotnews.com" in a or "indopremier.com" in a):
        src = requests.get(a)
        document = bs(src.content , 'lxml')
        # print(src.status_code)
        title2 = document.find("dl",attrs={"class":"listNews"})
        content = title2.find("dt") 
        print(content.text)
        isi = document.find("article")
        print(isi.text)
        title = content.text
        teks = isi.text
        return [title,teks]

    elif ("kompas.com" in a):
        src = requests.get(a)
        document = bs(src.content,'lxml')

        title2 = document.find("div",attrs={"class":"col-bs10-10"})
        content = title2.find("h1")
        title = content.text
        print(content.text)

        isi = document.find("div",attrs={"class":"read__content"})
        teks = isi.text
        return [title,teks]

    elif ("kontan.co.id" in a):
        src = requests.get(a)
        document = bs(src.content,'lxml')
        #print(src.status_code)

        title2 = document.find("div",attrs={"class":"bag-kiri"})
        content = title2.find("h1")
        title = content.text
        print(content.text)

        isi = document.find("div",attrs={"class":"tmpt-desk-kon"})
        berita = isi.find_all("p")

        teks = ''
        for i,a in enumerate(berita):
            if i > 0 :
                print(a.text)
                teks = teks + a.text
        return [title,teks]