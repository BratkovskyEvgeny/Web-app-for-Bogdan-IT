



import streamlit as st
from PIL import Image
import time

#@st.cache(suppress_st_warning=True)
def object_main():
    
    st.sidebar.title("Веб-приложение для поздравления Богдана Игоря Тадеушевича")
    st.sidebar.image('dr.jpg', width=300)
    
    st.markdown("<h1 style='text-align: center; '>Поздравление от отдела аналитики и управления данными</h1>", unsafe_allow_html = True)
    st.write("Поздравляем с днём рождения, **Игорь Тадеушевич!** :sunglasses: Желаем крепкого здравия, попутного ветра на пути к своим целям, нереального везения и энергии для реализации идей ! Per aspera ad astra !!!")
    
    if st.button("Запускай праздничную анимацию!"):
        time.sleep(2)
        st.balloons()
        time.sleep(2)
        st.balloons()
        time.sleep(2)
        st.snow()
    
    st.image('logo.jpg')
    
    #st.markdown(
           # "Ниже размещены памятные фотографии для хорошего настроения не только в этот праздничный день.")
   # image = Image.open('jawa.jpg')
   # st.image(image, caption='На Яве. Май 2022 года.')
    
   # image=Image.open('royal.jpg')
    #st.image('royal.jpg')
   # st.image(image, caption='На Royal Enfield')
    
   # image=Image.open('both.jpg')
    #st.image(image, caption='Весеннее мотопутешествие')

if __name__ == '__main__':
    object_main()
