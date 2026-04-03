import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


def analysis_and_model_page():
    st.title("Бинарная классификация для предиктивного обслуживания")

    uploaded_file = st.file_uploader("Загрузите CSV-файл", type="csv")
    if not uploaded_file:
        st.info(
            "Ожидается загрузка файла с колонками: Type, Air temperature [K], Process temperature [K], Rotational speed [rpm], Torque [Nm], Tool wear [min], Machine failure")
        return

    # Загрузка и предобработка
    data = pd.read_csv(uploaded_file)
    drop_cols = ['UDI', 'Product ID', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF']
    data = data.drop(columns=[c for c in drop_cols if c in data.columns])
    data['Type'] = data['Type'].map({'L': 0, 'M': 1, 'H': 2})

    num_cols = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]',
                'Tool wear [min]']
    scaler = StandardScaler()
    data[num_cols] = scaler.fit_transform(data[num_cols])

    # Разделение и обучение
    X = data.drop(columns=['Machine failure'])
    y = data['Machine failure']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)

    # Оценка
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    st.subheader("Результаты оценки модели")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Precision", f"{precision_score(y_test, y_pred):.3f}")
    col2.metric("Recall", f"{recall_score(y_test, y_pred):.3f}")
    col3.metric("F1-Score", f"{f1_score(y_test, y_pred):.3f}")
    col4.metric("ROC-AUC", f"{roc_auc_score(y_test, y_proba):.3f}")

    # Матрица ошибок
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Норма', 'Отказ'], yticklabels=['Норма', 'Отказ'])
    ax.set_xlabel("Предсказано")
    ax.set_ylabel("Реально")
    st.pyplot(fig)

    # Важность признаков
    fig, ax = plt.subplots(figsize=(6, 4))
    imp = pd.DataFrame({'Признак': X.columns, 'Важность': model.feature_importances_}).sort_values('Важность')
    ax.barh(imp['Признак'], imp['Важность'])
    ax.set_xlabel("Важность")
    st.pyplot(fig)

    # Форма для прогноза
    st.subheader("Прогноз для нового оборудования")
    with st.form("pred_form"):
        cols = st.columns(3)
        type_val = cols[0].selectbox("Тип", ['L', 'M', 'H'])
        air_temp = cols[0].number_input("Температура воздуха [K]", value=300.0)
        proc_temp = cols[1].number_input("Температура процесса [K]", value=310.0)
        rot_speed = cols[1].number_input("Скорость вращения [rpm]", value=1500.0)
        torque = cols[2].number_input("Крутящий момент [Nm]", value=40.0)
        tool_wear = cols[2].number_input("Износ инструмента [min]", value=100.0)
        submitted = st.form_submit_button("Сделать прогноз")

    if submitted:
        input_df = pd.DataFrame([{
            'Type': {'L': 0, 'M': 1, 'H': 2}[type_val],
            'Air temperature [K]': air_temp,
            'Process temperature [K]': proc_temp,
            'Rotational speed [rpm]': rot_speed,
            'Torque [Nm]': torque,
            'Tool wear [min]': tool_wear
        }])
        input_df[num_cols] = scaler.transform(input_df[num_cols])
        pred = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0][1]

        if pred == 1:
            st.error(f"⚠️ ОТКАЗ ОБОРУДОВАНИЯ (вероятность: {proba:.2%})")
        else:
            st.success(f"✅ НОРМАЛЬНАЯ РАБОТА (вероятность отказа: {proba:.2%})")


if __name__ == "__main__":
    analysis_and_model_page()