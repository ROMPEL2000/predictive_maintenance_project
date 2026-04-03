import streamlit as st
from analysis_and_model import analysis_and_model_page
from presentation import presentation_page

# Настройка страницы
st.set_page_config(
    page_title="PdM: Бинарная классификация",
    page_icon="🔧",
    layout="wide"
)

# Кастомный CSS для боковой панели
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# Боковая панель
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    st.markdown("## 🔧 PdM System")
    st.markdown("---")

    # Навигация
    pages = {
        "📊 Анализ и модель": analysis_and_model_page,
        "📑 Презентация": presentation_page
    }

    selected_page = st.radio(
        "Выберите раздел",
        options=list(pages.keys()),
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.caption("ВКР: Бинарная классификация для предиктивного обслуживания")
    st.caption("© 2026")

# Загрузка выбранной страницы
pages[selected_page]()