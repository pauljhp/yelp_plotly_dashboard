import streamlit as st
import plotly.graph_objects as go
import plotly
import plotly.express as px
import pandas as pd
import numpy as np

side_bar_options = (
    "users",
    "businesses"
)

st.set_page_config(
    page_title="Yelp dataset visualization - COMP7507",
    layout="wide")

with st.sidebar:
    radio_selected = st.radio("select an option",
                      side_bar_options)

if radio_selected == "users":
    user_df = pd.read_csv("./data/user_data.csv", index_col=0, header=0)
    # st.write(user_df.head())
    corr_mat = user_df.corr(numeric_only=True)
    corr_mat = pd.DataFrame(np.tril(corr_mat, k=-1),
                            index=corr_mat.index, columns=corr_mat.columns)\
                            .replace(0., np.nan)
    corr_fig = px.imshow(corr_mat, height=600, width=600 ,color_continuous_scale='RdBu_r')
    corr_fig.update_layout(title="correlation heatmap - user attributes")

    def get_histogram(attribute):
        fig = px.histogram(user_df, x=attribute, histnorm='probability density')
        fig.update_layout(title=f"histogram - {attribute}")
        return fig

    left, right = st.columns([1.5, 0.5])
    with left.container():
        st.plotly_chart(corr_fig)

    with right.container():
        attribute_selected = st.selectbox(
            label="select an attribute",
            options=user_df.columns,
            index=21)
        histogram = get_histogram(attribute_selected)
        st.plotly_chart(histogram)


