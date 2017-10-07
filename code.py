from selenium import webdriver
import io
import urllib.request
from tkinter import *
from PIL import Image, ImageTk




news_link=[]  #storing the news link
news_images=[]  # storing the news image which we have to read via io library later
news_headline=[]  #storing news headline
news_text=[]      #storing news text
driver=webdriver.Chrome()
browser=driver.get("https://www.facebook.com")
x=driver.find_element_by_css_selector('input[type="email"]')
x.send_keys("example@gmail.com")                                #your email goes here
y=driver.find_element_by_css_selector('input[type="password"]')
y.send_keys("example12345")                                      #your password goes here
z=driver.find_element_by_css_selector('input[value="Log In"]')
z.click()
driver.get("https://www.facebook.com/search/top/?q=fff")
driver.execute_script("document.getElementsByClassName('layerCancel _4jy0 _4jy3 _517h _51sy _42ft')[0].click()")  #if this layer doesn't appear in your chrome instance on facebook remove this line.
xpath1='//*[@id="pagelet_trending_tags_and_topics"]/div/div'
new=driver.find_element_by_xpath(xpath1)
awe=driver.find_elements_by_css_selector('a[class="_4qzh _5v0t _7ge"]')
for i in awe:
    news_link.append(i.get_attribute("href"))




for i in news_link:
    driver.get(i)


    news_image1=driver.find_element_by_xpath('//*[@id="u_ps_0_4_2"]/a/div[1]/div/img')
    news_images.append(news_image1.get_attribute("src"))
    news_headline1=driver.find_element_by_css_selector('div[class ="_4l5g"]')
    news_headline.append(news_headline1.text)
    news_text1=driver.find_element_by_css_selector('div[class="_4l5h"]')
    news_text.append(news_text1.text)




driver.quit()




root=Tk()
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

imager = ImageTk.PhotoImage(file = "a.jpg")

can=Canvas(root)
can.grid(row=0,column=0,sticky='nswe')

hscroll=Scrollbar(root,orient=HORIZONTAL, command=can.xview)
hscroll.grid(row=1,column=0,sticky='we')
vscroll=Scrollbar(root,orient=VERTICAL, command=can.yview)
vscroll.grid(row=0,column=1,sticky='ns')
can.configure(xscrollcommand=hscroll.set, yscrollcommand=vscroll.set)
fram=Frame(can)
can.create_window(0,0,window=fram,anchor='nw')

for s,j,k,l in zip(news_images,news_link,news_headline,news_text):
    r1 = urllib.request.urlopen(s).read()
    im = Image.open(io.BytesIO(r1))
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(fram,image = tkimage)
    texr2 = Label(fram, text=l, wraplength=900, anchor=W, justify=RIGHT, font=("sans-serif", 20),bg = 'Green', fg = 'blue')
    line=Label(fram,text="----------------------------------------------------------------------")

    texr3=Label(fram,text=k,font=("Ariel",30))
    texr1=Label(fram,text=("For more Information",j),bg = 'white', fg = 'blue')

    myvar.image = tkimage


    myvar.pack()
    texr3.pack()
    line.pack()
    print("--------------------------Loading--------------------------------------------")
    texr2.pack(expand=True, fill=BOTH)

    texr1.pack()






fram.update_idletasks()
root.geometry('1000x800')
can.configure(scrollregion=(0, 0, fram.winfo_width(), fram.winfo_height()))

root.mainloop()






