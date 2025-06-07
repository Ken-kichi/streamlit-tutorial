import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# Title
st.title("📊 Household Budget App")

# Store record data in session state
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount', 'Note'])

# Input form
with st.form("entry_form"):
    st.subheader("Add a Record")

    col1, col2 = st.columns(2)
    with col1:
        entry_type = st.selectbox("Type", ["Income", "Expense"])
    with col2:
        category = st.selectbox("Category", ["Salary", "Food", "Transport", "Entertainment", "Other"])

    amount = st.number_input("Amount", min_value=0, step=100)
    memo = st.text_input("Note (optional)")
    entry_date = st.date_input("Date", value=date.today())

    submitted = st.form_submit_button("Add")

    if submitted:
        new_entry = pd.DataFrame([[entry_date, entry_type, category, amount, memo]],
                                 columns=['Date', 'Type', 'Category', 'Amount', 'Note'])
        st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)
        st.success("Record added successfully.")

# Show data table
st.subheader("📜 Record List")
st.dataframe(st.session_state.data)

# Show charts
st.subheader("📈 Visualization")

if not st.session_state.data.empty:
    # Calculate totals
    income_sum = st.session_state.data[st.session_state.data['Type'] == 'Income']['Amount'].sum()
    expense_sum = st.session_state.data[st.session_state.data['Type'] == 'Expense']['Amount'].sum()
    balance = income_sum - expense_sum

    st.metric("💰 Balance", f"{balance:,.0f} JPY")

    # Pie chart by type
    fig1, ax1 = plt.subplots()
    summary = st.session_state.data.groupby('Type')['Amount'].sum()
    ax1.pie(summary, labels=summary.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    # Bar chart by category (only for expenses)
    expense_data = st.session_state.data[st.session_state.data['Type'] == 'Expense']
    if not expense_data.empty:
        fig2, ax2 = plt.subplots()
        expense_summary = expense_data.groupby('Category')['Amount'].sum()
        expense_summary.plot(kind='bar', ax=ax2, color='tomato')
        ax2.set_ylabel("Amount")
        ax2.set_title("Expenses by Category")
        st.pyplot(fig2)
else:
    st.info("No records found. Please add some entries.")
