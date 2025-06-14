import streamlit as st
import pandas as pd
from src.database import Database
from views.form import render_add_form, render_delete_form
from views.charts import render_pie_chart, render_daily_bar_chart, show_summary_metrics
from views.table import render_data_table

st.title("📊 Household Budget App")

db = Database()
container = db.container("budget_db", "records")
data = db.get_all_records(container)

if data:
    pd_data = pd.DataFrame(data)
    pd_display_data = pd_data[["id", "entry_type", "category", "amount", "memo", "date"]]
else:
    pd_data = pd.DataFrame(columns=["entry_type", "category", "amount", "memo", "date"])
    pd_display_data = pd_data.copy()

st.subheader("📈 Visualization")

if not pd_data.empty:
    show_summary_metrics(pd_data)
    render_pie_chart(pd_data)
    render_daily_bar_chart(pd_data)
else:
    st.info("No records found. Please add some entries.")

render_data_table(pd_display_data)
render_add_form(db, container)
render_delete_form(db, container, pd_data)
