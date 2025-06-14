import streamlit as st
from datetime import date
from typing import get_args
from src.models import Record

def render_add_form(db, container):
    st.subheader("Add a Record")

    with st.form("entry_form"):

        col1, col2 = st.columns(2)
        with col1:
            entry_type_options = get_args(Record.model_fields["entry_type"].annotation)
            entry_type = st.selectbox("Type", entry_type_options)
        with col2:
            entry_category = get_args(Record.model_fields["category"].annotation)
            category = st.selectbox("Category", entry_category)

        amount = st.number_input("Amount", min_value=0, step=100)
        memo = st.text_input("Note (optional)")
        entry_date = st.date_input("Date", value=date.today())

        submitted = st.form_submit_button("Add")

        if submitted:
            record = Record(
                entry_type=entry_type,
                category=category,
                amount=amount,
                memo=memo,
                date=entry_date
            )
            db.create_record(container, record.model_dump(mode="json"))
            st.success("Record added successfully.")
            st.rerun()

def render_delete_form(db, container, pd_data):
    st.subheader("Delete a Record")
    with st.form("delete_form"):
        delete_id = st.selectbox("Delete ID", pd_data["id"])
        delete_submitted = st.form_submit_button("Delete")
        if delete_submitted:
            db.delete_record(container, delete_id)
            st.success("Record deleted successfully.")
            st.rerun()
