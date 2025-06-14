import streamlit as st
import matplotlib.pyplot as plt

def show_summary_metrics(pd_data):
    income_sum = pd_data[pd_data['entry_type'] == 'Income']['amount'].sum()
    expense_sum = pd_data[pd_data['entry_type'] == 'Expense']['amount'].sum()
    balance = income_sum - expense_sum
    st.metric("💰 Balance", f"{balance:,.0f} JPY")

def render_pie_chart(pd_data):
    fig, ax = plt.subplots()
    summary = pd_data.groupby('entry_type')['amount'].sum()
    ax.pie(summary, labels=summary.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

def render_daily_bar_chart(pd_data):
    st.subheader("📈 Daily Net Income/Expense")
    pd_data["signed_amount"] = pd_data.apply(
        lambda row: row["amount"] if row["entry_type"] == "Income" else -row["amount"], axis=1
    )
    daily_balance = pd_data.groupby("date")["signed_amount"].sum()

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(daily_balance.index, daily_balance.values, color=["green" if x >= 0 else "red" for x in daily_balance.values])

    ax.set_xlabel("Date")
    ax.set_ylabel("Net Amount (JPY)")
    ax.set_title("Daily Net Income/Expense")
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height if height >= 0 else 0, f"{height:,.0f}", ha='center', va='bottom' if height >= 0 else 'top', fontsize=10)

    st.pyplot(fig)
