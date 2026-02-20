import streamlit as st
import requests

# Настройки (те же, что были)
TOKEN = "6812156683:AAH_qpMTsHxFmwRLhVadfoqa3n73EJ2BcTM"
CHAT_ID = "314412076"

# Функция отправки
def send_tg(message):
    url = f"https://api.telegram.org{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

# Адаптация под мобильный экран Mini App
st.set_page_config(page_title="Dress App", layout="centered")

st.write("### 👗 Аренда платьев")

# Данные
dresses = [
    {"name": "Облако нежности", "size": "110", "price": 1500, "img": "img/1.jpg"},
    {"name": "Золотая искра", "size": "122", "price": 2000, "img": "img/2.jpg"}
]

# Компактный выбор
option = st.selectbox("Выберите категорию", ["Все платья", "Размер 110", "Размер 122"])

for dress in dresses:
    # Простая логика фильтра
    if option == "Все платья" or dress["size"] in option:
        with st.container(border=True):
            st.image(dress["img"])
            st.subheader(dress["name"])
            st.write(f"Размер: {dress['size']} | {dress['price']} руб.")
            if st.button(f"Записаться", key=dress['name'], use_container_width=True):
                st.session_state.selected = dress['name']

# Всплывающее окно записи (стиль Mini App)
if 'selected' in st.session_state:
    st.info(f"Оформляем: {st.session_state.selected}")
    with st.form("mini_form"):
        name = st.text_input("Имя")
        phone = st.text_input("Телефон")
        if st.form_submit_button("Подтвердить", use_container_width=True):
            send_tg(f"Заявка из Mini App!\n{st.session_state.selected}\n{name}: {phone}")
            st.success("Отправлено! Закройте приложение.")

