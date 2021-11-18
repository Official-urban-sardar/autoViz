import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import os
import plotly.express as px
import matplotlib.pyplot as plt

os.getcwd()
st.set_page_config(layout='wide')


st.header('Performing Visualization')
st.subheader('Upload file here')
dataset = st.file_uploader("",type=['csv'])

if dataset is not None:
    df = pd.read_csv(dataset)
    df = pd.DataFrame(df)
    st.subheader('Data set')
    st.dataframe(df, 3000,150)

    # finding the null values
    # a=df.isnull().sum()
    # st.write(a)
    num_df = df.select_dtypes(include=np.number)
    # num_df.dropna(axis=1)
    # st.write(num_df)
    st.sidebar.header('Select Type Visualization')
    Activities = ["Line chart", "Bar chart","Box plot","Scatter plot","Heat map","Pie chart"]
    choice = st.sidebar.selectbox("", Activities)
    st.subheader('Visualization')



    if choice is not None:
        if choice == "Line chart":
            st.sidebar.header('Select values to plot Line chart')
            col_x = st.sidebar.selectbox("Select  column For x axis", df.columns)
            col_y = st.sidebar.multiselect("Select  columns For y axis", num_df.columns)
            x = df[col_x]
            y = df[col_y]
            y = y.columns.tolist()
            fig = px.line(df, x=x, y=y, width=1400, height=400)
            fig.update_xaxes(type='category')
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="#D3D3D3",
            )
            st.plotly_chart(fig)
        elif choice == "Bar chart":
            st.sidebar.header('Select values to Bar chart')
            col_x = st.sidebar.selectbox("Select  column For x axis", df.columns)
            col_y = st.sidebar.multiselect("Select  columns For y axis", num_df.columns)
            x = df[col_x]
            y = df[col_y]
            y = y.columns.tolist()
            fig = px.bar(df, x=x, y=y, width=1400, height=400)
            fig.update_xaxes(type='category')
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="#D3D3D3",
            )
            st.plotly_chart(fig)
        elif choice == "Box plot":
            st.sidebar.header('Select values to plot Box plot')
            col_x = st.sidebar.selectbox("Select  column For x axis", df.columns)
            col_y = st.sidebar.multiselect("Select  columns For y axis", num_df.columns)
            x = df[col_x]
            y = df[col_y]
            y = y.columns.tolist()
            fig = px.box(df, x=x, y=y, width=1400, height=400)
            fig.update_xaxes(type='category')
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="#D3D3D3",
            )
            st.plotly_chart(fig)
        elif choice== "Scatter plot":
            st.sidebar.header('Select values to plot Scatter plot')
            col_x = st.sidebar.selectbox("Select  column For x axis", df.columns)
            col_y = st.sidebar.multiselect("Select  columns For y axis", num_df.columns)
            x = df[col_x]
            y = df[col_y]
            y = y.columns.tolist()
            fig = px.scatter(df, x=x, y=y, width=1400, height=400)
            fig.update_xaxes(type='category')
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="#D3D3D3",
            )
            st.plotly_chart(fig)

        elif choice== "Heat map":
            st.sidebar.header('Select values to plot Heatmap')
            col_x = st.sidebar.multiselect("", num_df.columns)
            x = num_df[col_x]
            x = x.columns.tolist()
            if len(x) > 1:
                col1, col2, col3 = st.beta_columns([2, 6, 3])
                with col1:
                    st.write("")
                with col2:
                    fig, ax = plt.subplots()
                    r=sns.heatmap(num_df[x].corr(), ax=ax, cmap="Blues",linewidths=.4)
                    st.write(fig)
                with col3:
                    st.write("")
            else:
                st.sidebar.error("Please select at least 2 variables")

        else:
            st.sidebar.header('Select values to plot pie chart')
            col_a = st.sidebar.selectbox("Select the values", num_df.columns)
            col_b = st.sidebar.selectbox("select the label ", df.columns)
            a = df[col_a]
            b = df[col_b]
            fig = px.pie(df, values=a, names=b, width=700, height=700)
            fig.update_xaxes(type='category')
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor="#D3D3D3",
            )
            st.header("Pie chart")
            st.plotly_chart(fig)
















