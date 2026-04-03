# 🔧 Бинарная классификация для предиктивного обслуживания оборудования

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)

---

## 🎯 Что делает проект

Обучает модель машинного обучения предсказывать отказы оборудования (`1` — поломка, `0` — исправная работа) и предоставляет удобный веб-интерфейс для тестирования.

---

## 📊 Данные

| Параметр | Значение |
|----------|----------|
| **Источник** | UCI AI4I 2020 Predictive Maintenance Dataset |
| **Объём** | 10 000 записей |
| **Параметры** | температура, механические нагрузки, скорость вращения, износ инструмента |
| **Цель** | `Machine failure` (факт отказа) |

> ⚠️ **Дисбаланс классов:** отказы составляют ~3.4% выборки

---

## ⚙️ Технологии

| Компонент | Технология |
|-----------|------------|
| **Модель** | Random Forest (class_weight='balanced') |
| **Метрики** | Accuracy, ROC-AUC, Confusion Matrix, Precision, Recall, F1 |
| **Предобработка** | удаление лишних признаков, кодирование категорий, нормализация (StandardScaler) |
| **Веб-интерфейс** | Streamlit |

---

## 💻 Возможности приложения

- 📁 Загрузка своего CSV-файла
- 🔄 Обучение модели с визуализацией
- 📊 Отображение метрик и матрицы ошибок
- ⭐ Анализ важности признаков
- 🔮 Ручной ввод параметров для прогноза

---

## 🚀 Быстрый старт

```bash
git clone https://github.com/ROMPEL2000/predictive_maintenance_project 
cd predictive_maintenance_project
pip install -r requirements.txt или py -m pip install -r requirements.txt
streamlit run app.py или py -m streamlit run app.py
```
## Видео-демонстрация
[Ссылка на видео](demo.mp4)
