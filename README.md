# Predictive Maintenance

Учебное веб-приложение для прогноза отказа оборудования по рабочим параметрам. Модель Random Forest обучается на загруженном CSV, а интерфейс Streamlit показывает оценку и позволяет проверить отдельный набор параметров.

**Python · pandas · scikit-learn · Streamlit · Matplotlib · Seaborn**

[Видеодемонстрация](demo.mp4) · [Код модели](analysis_and_model.py)

## Возможности

- Загрузка CSV с данными оборудования.
- Обучение Random Forest и разделение данных на обучающую и тестовую выборки 80/20.
- Оценка Accuracy и ROC-AUC, визуализация матрицы ошибок.
- Ручной ввод параметров: тип оборудования, температуры, скорость вращения, крутящий момент и износ инструмента.
- Прогноз класса и вероятности отказа.

## Запуск

Рекомендуемая среда — Python 3.10 с отдельным виртуальным окружением. Версии библиотек заданы в `requirements.txt`.

```bash
git clone https://github.com/ROMPEL2000/predictive_maintenance_project.git
cd predictive_maintenance_project
python -m venv .venv
```

Активируйте окружение:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Установите зависимости и запустите приложение:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Данные

Приложение рассчитано на CSV со схемой **AI4I 2020 Predictive Maintenance**. Датасет не включён в репозиторий: подготовьте файл и загрузите его в интерфейсе.

Ожидаемые столбцы:

```text
UDI, Product ID, Type, Air temperature [K], Process temperature [K],
Rotational speed [rpm], Torque [Nm], Tool wear [min], Machine failure,
TWF, HDF, PWF, OSF, RNF
```

`Type` принимает значения `L`, `M`, `H`; целевой признак `Machine failure` — `0` или `1`. Идентификаторы и отдельные признаки видов отказа исключаются перед обучением.

## Структура

| Файл | Назначение |
| --- | --- |
| `app.py` | Точка входа и навигация Streamlit |
| `analysis_and_model.py` | Подготовка данных, обучение, оценка и прогноз |
| `presentation.py` | Презентация проекта внутри приложения |
| `requirements.txt` | Зависимости |
| `demo.mp4` | Видеодемонстрация |

## Ограничения

Это учебная реализация. Модель обучается заново при работе с загруженным набором данных; сохранение модели и автоматическая проверка схемы CSV пока не реализованы. Текущая предобработка масштабирует данные до разделения выборки; перед использованием результатов для сравнения моделей её следует перенести в Pipeline и обучать только на тренировочной части.
