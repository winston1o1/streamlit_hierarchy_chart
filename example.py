import streamlit as st
import pandas as pd

from streamlit_hierarchy_chart import hierarchy_chart
from utils import cx_credit_mtree

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

st.subheader("Component with constant args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.

df = pd.read_csv('test.csv')
main_dt = '2025-01-01'
comparator_dt = '2025-02-01'

cx_credit_mtree_res = cx_credit_mtree(df,main_dt,comparator_dt)

data = cx_credit_mtree_res[0]
metric_keys = cx_credit_mtree_res[1]
selected_metric_key = hierarchy_chart(data=data)


st.write(selected_metric_key)
selected_metric = metric_keys.get(selected_metric_key)
if selected_metric:
    st.write(selected_metric)