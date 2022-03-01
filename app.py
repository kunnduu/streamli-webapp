import streamlit as st  # web development
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts


# read csv from a github repo
df = pd.read_csv(
    "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")


st.set_page_config(
    page_title='Real-Time Data Science Dashboard',
    page_icon='📊',
    layout='wide'
)


# dashboard title

st.title("Real-Time / Live Data Science Dashboard")
placeholder1 = st.empty()

# top-level filters
with placeholder1.container():
    col1, col2 = st.columns(2)
    with col1:
        job_filter = st.selectbox("Select the Job", pd.unique(df['job']))
    with col2:
        filter = st.selectbox("Loan Taken?", pd.unique(df['loan']))

# creating a single-element container.
placeholder = st.empty()

# dataframe filter

df = df[df['job'] == job_filter]
df=df[df['loan']==filter]
df['age_new'] = df['age'] 
df['balance_new'] = df['balance'] 
# creating KPIs
avg_age = np.mean(df['age_new'])

count_married = int(df[(df["marital"] == 'married')]
                    ['marital'].count() )

# near real-time / live feed simulation


balance = np.mean(df['balance_new'])
with placeholder.container():
    # create three columns
    kpi1, kpi2, kpi3 = st.columns(3)

# fill in those three columns with respective metrics or KPIs
kpi1.metric(label="Avg Age ⏳", value=round(avg_age))
kpi2.metric(label="Married Count 💍", value=int(
    count_married))
kpi3.metric(label="Avg A/C Balance ＄",
            value=f"$ {round(balance,2)} ")

# create two columns for charts

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.markdown("### First Chart")
    fig = px.scatter(data_frame=df, x='age_new', y='balance')
    st.write(fig)
with fig_col2:
    st.markdown("### Second Chart")
    fig2 = px.histogram(data_frame=df, x='age_new',marginal='box',
                        color_discrete_sequence=['red'],)
    fig2.update_layout(bargap=0.5)                    
    st.write(fig2)
st.markdown("### Detailed Data View")
st.dataframe(df)
#placeholder.empty()
