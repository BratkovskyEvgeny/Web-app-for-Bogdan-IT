
#pip install streamlit  == 1.17.0
#pip install Pillow == 9.4.0
#pip install numpy == 1.21.6
#pip install matplotlib == 3.5.5


import streamlit as st
#import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image
import time

#@st.cache(suppress_st_warning=True)
def object_main():
    #st.sidebar.image('logo.jpg', width=300)
    #st.markdown("<h1 style='text-align: center; color: black;'>Веб-приложение для демонстрации развёртывания модели компьютерного зрения</h1>", unsafe_allow_html = True)
    #st.sidebar.title("Веб-приложение для демонстрации модели компьютерного зрения (проект для базового потока Deep Learning School)")
    #st.sidebar.info("Веб-приложение для (проект для базового потока Deep Learning School). Создано Братковским Евгением Викторовичем (User ID (Stepik.org): 528271325).")
    #st.title("Поздравление от отдела аналитики и управления данными")
    #st.write('Hello, *World!* :sunglasses:')
    #st.write("<h6 style='text-align: center;'>YOLO или You Only Look Once — это популярная архитектура CNN, которая используется для распознавания объектов на изображении. В проекте использована YOLOv3 — усовершенствованная версия архитектуры YOLO. Основная особенность YOLOv3 состоит в том, что на выходе есть три слоя, каждый из которых расчитан на обнаружение объектов разного размера. </h6>", unsafe_allow_html = True)
    #st.image('yolo_1.png', width=350)
    #choice = st.radio("", ("Пример для демонстрации", "Выбрать изображение из коллекции"))
    #st.write()
    
    #video_file = open('myvideo.mp4', 'rb')
    #video_bytes = video_file.read()
    #st.sidebar.button("Перейти к поздравлению")
    #st.video(video_bytes)
    #st.snow()
    #st.balloons()
    st.sidebar.title("Веб-приложение для поздравления Богдана Игоря Тадеушевича")
    st.sidebar.image('dr.jpg', width=300)
    
    st.markdown("<h1 style='text-align: center; '>Поздравление от отдела аналитики и управления данными</h1>", unsafe_allow_html = True)
    st.write("Поздравляем с днём рождения, **Игорь Тадеушевич!** :sunglasses: Желаем крепкого здравия, попутного ветра на пути к своим целям, нереального везения и энергии для реализации идей ! Per aspera ad astra !!!")
    
    if st.button("Запускай праздничную анимацию!"):
        time.sleep(2)
        st.balloons()
        st.balloons()
        st.balloons()
        time.sleep(3)
        st.snow()
        st.snow()
    
    
    
    
    
    st.image('logo.jpg')
    
    
    
     
    st.markdown(
            "Ниже размещены памятные фотографии для хорошего настроения не только в этот праздничный день.")
    image = Image.open('jawa.jpg')
    st.image(image, caption='На Яве. Май 2022 года.')
    
    image=Image.open('royal.jpg')
    #st.image('royal.jpg')
    st.image(image, caption='На Royal Enfield')
    
    image=Image.open('both.jpg')
    st.image(image, caption='Весеннее мотопутешествие')
    
    
    
    
    
    #st.sidebar.title("Веб-приложение для кредитного скоринга и анализа данных")
    #st.sidebar.button("Начать кредитный скоринг") 
    st.sidebar.info("Разработчик приложения — Братковский Евгений Викторович.")
    #st.markdown(
           # "Добро пожаловать в веб-приложение!   Для начала официальная часть.")
    #time.sleep(0.5)  # simulate a computation
           
    #st.balloons()
    #st.image('scoring.jpg', width=750)   
    #if st.sidebar.button("Перейти к поздравлению"):
        
                #st.image('dr.jpeg', width=300)
                #st.snow()
                #st.sidebar.success("**Добро пожаловать, {}**".format(username))
                #st.image('royal.jpeg', width=750)
                #st.write("Поздравляем с днём рождения, *Игорь Тадеушевич!* :sunglasses:")
                #st.balloons()

if __name__ == '__main__':
    object_main()
