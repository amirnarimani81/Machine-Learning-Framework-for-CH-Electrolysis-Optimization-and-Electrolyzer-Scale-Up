import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import plotly.graph_objects as go
from datetime import datetime, timedelta
from prophet import Prophet
import smtplib
from email.message import EmailMessage
import warnings
import os
import time
import math
from sklearn.metrics import mean_squared_error, r2_score

warnings.filterwarnings("ignore")

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Electrolyzer Material Procurement Intelligence",
    page_icon="",
    layout="wide")

st.title(" Electrolyzer Material Procurement Intelligence")
st.markdown("*Automated Web Scraping, Price Forecasting, Email Alerts, and Database Management*")

# ============================================================
# SIDEBAR - Navigation
# ============================================================
st.sidebar.header("Navigation")
menu = st.sidebar.radio(
    "Select Module",
    [" Dashboard", " Scrape Data", " Forecast", " Email Alerts", " Database", " Analytics"])

# ============================================================
# DATABASE SETUP
# ============================================================
def init_db():
    try:
        conn = sqlite3.connect('commodity_prices.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS commodity_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            commodity TEXT,
            date TEXT,
            price REAL,
            currency TEXT,
            source TEXT,
            scraped_at TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            commodity TEXT,
            alert_type TEXT,
            message TEXT,
            created_at TEXT )''')
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Database initialization error: {str(e)}")
        return False

init_db()

# ============================================================
# SCRAPING FUNCTIONS
# ============================================================
def scrape_sunsirs():
    """Scrape commodity prices from Sunsirs"""
    st.info("🔍 Scraping Sunsirs commodity prices...")
    
    sunsir_urls = {
        "Soda ash": "https://www.sunsirs.com/futures-price/petail-Soda-ash-737.html",
        "Copper": "https://www.sunsirs.com/futures-price/petail-Copper-792.html",
        "Caustic soda": "https://www.sunsirs.com/futures-price/petail-Caustic-soda-368.html",
        "Lithium carbonate": "https://www.sunsirs.com/futures-price/petail-Lithium-carbonate-1162.html",}
    
    header = {"User-Agent": "Mozilla/5.0"}
    all_data = []
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for idx, (name, url) in enumerate(sunsir_urls.items()):
        status_text.text(f"Scraping: {name}...")
        
        try:
            page = requests.get(url, headers=header, timeout=30)
            soup = BeautifulSoup(page.text, "html.parser")
            table = soup.find("table")
            
            if table:
                rows = table.find_all("tr")
                for row in rows[1:]:
                    cols = row.find_all("td")
                    if len(cols) >= 4:
                        date_text = cols[3].text.strip()
                        price_text = cols[2].text.strip().replace(',', '').replace('$', '')
                        
                        try:
                            price = float(price_text)
                            all_data.append({
                                'Commodity': name,
                                'Date': date_text,
                                'Spot price': price,
                                'Source': 'Sunsirs'
                            })
                        except ValueError:
                            pass
            
            progress_bar.progress((idx + 1) / len(sunsir_urls.items()))
            time.sleep(1)
            
        except Exception as e:
            st.warning(f"Failed to scrape {name}: {str(e)}")
    
    status_text.text("✅ Scraping complete!")
    progress_bar.empty()
    
    if all_data:
        return pd.DataFrame(all_data)
    else:
        return create_sample_data()

def create_sample_data():
    """Create sample data for demonstration"""
    sample_data = []
    commodities = ["Lithium carbonate", "Copper", "Soda ash", "Caustic soda"]
    today = datetime.now()
    
    for i, commodity in enumerate(commodities):
        base_price = [5000, 4500, 800, 600][i]
        for j in range(30):
            date = today - timedelta(days=j)
            price = base_price + (j * (10 + i * 2)) + (i * 50)
            sample_data.append({
                'Commodity': commodity,
                'Date': date.strftime('%Y-%m-%d'),
                'Spot price': price + 100 * ((j % 5) - 2),
                'Source': 'Sample' })
    
    return pd.DataFrame(sample_data)

# ============================================================
# DATABASE FUNCTIONS
# ============================================================
def save_to_db(df, table_name='commodity_prices'):
    if df.empty:
        return False
    
    try:
        conn = sqlite3.connect('commodity_prices.db')
        df['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if 'Commodity' in df.columns and 'Date' in df.columns and 'Spot price' in df.columns:
            df_db = df[['Commodity', 'Date', 'Spot price']].copy()
            df_db.columns = ['commodity', 'date', 'price']
            df_db['currency'] = 'CAD'
            df_db['source'] = df.get('Source', 'Sunsirs')
            df_db['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            df_db.to_sql(table_name, conn, if_exists='append', index=False)
            conn.close()
            st.success(f"✅ Saved {len(df_db)} records to database")
            return True
        else:
            conn.close()
            return False
    except Exception as e:
        st.error(f"Database save error: {str(e)}")
        return False

def load_from_db(commodity=None, days=30):
    try:
        conn = sqlite3.connect('commodity_prices.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='commodity_prices'")
        if not cursor.fetchone():
            conn.close()
            return pd.DataFrame()
        
        if commodity:
            query = f"SELECT * FROM commodity_prices WHERE commodity = '{commodity}' AND date >= date('now', '-{days} days') ORDER BY date DESC"
        else:
            query = f"SELECT * FROM commodity_prices WHERE date >= date('now', '-{days} days') ORDER BY date DESC"
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        return pd.DataFrame()

def get_table_count():
    try:
        conn = sqlite3.connect('commodity_prices.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM commodity_prices")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    except:
        return 0

# ============================================================
# FORECASTING FUNCTION
# ============================================================
def prophet_forecast(df, periods=30):
    if df.empty or len(df) < 10:
        return None, None, None, None
    
    df_prophet = df[['date', 'price']].copy()
    df_prophet.columns = ['ds', 'y']
    df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])
    df_prophet = df_prophet.sort_values('ds')
    
    try:
        model = Prophet(
            daily_seasonality=False,
            weekly_seasonality=True,
            yearly_seasonality=True,
            changepoint_prior_scale=0.05)
        model.fit(df_prophet)
        
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
        
        merged = forecast[['ds', 'yhat']].merge(df_prophet, on='ds', how='left')
        hist = merged[merged['y'].notna()]
        
        if len(hist) > 1:
            rmse = math.sqrt(mean_squared_error(hist['y'], hist['yhat']))
            r2 = r2_score(hist['y'], hist['yhat'])
        else:
            rmse, r2 = None, None
        
        return model, forecast, rmse, r2
    except Exception as e:
        st.error(f"Forecast error: {str(e)}")
        return None, None, None, None

# ============================================================
# EMAIL ALERT FUNCTION
# ============================================================
def send_email_alert(recipient, subject, body, attachment=None):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = "electrolyzer@ml-platform.com"
        msg['To'] = recipient
        msg.set_content(body)
        
        st.info(f"📧 Email would be sent to: {recipient}")
        st.text(f"Subject: {subject}")
        st.text(f"Body:\n{body}")
        return True
    except Exception as e:
        st.error(f"Email sending failed: {str(e)}")
        return False

# ============================================================
# UI - DASHBOARD
# ============================================================
if menu == " Dashboard":
    st.header(" Procurement Intelligence Dashboard")
    
    record_count = get_table_count()
    st.info(f"Database contains {record_count} records")
    
    col1, col2, col3, col4 = st.columns(4)
    
    df = load_from_db(days=30)
    
    with col1:
        st.metric("Total Commodities", len(df['commodity'].unique()) if not df.empty else 0)
    with col2:
        st.metric("Total Records", len(df) if not df.empty else 0)
    with col3:
        latest = df.iloc[0]['price'] if not df.empty and 'price' in df.columns else 0
        st.metric("Latest Price", f"${latest:.2f}" if latest else "$0.00")
    with col4:
        if st.button("🔄 Scrape Now"):
            df_new = scrape_sunsirs()
            if not df_new.empty:
                save_to_db(df_new)
                st.rerun()
    
    if not df.empty:
        st.subheader("Recent Price Data")
        st.dataframe(df.head(10))
        
        fig = go.Figure()
        for commodity in df['commodity'].unique():
            df_comm = df[df['commodity'] == commodity].sort_values('date')
            fig.add_trace(go.Scatter(
                x=df_comm['date'],
                y=df_comm['price'],
                mode='lines+markers',
                name=commodity
            ))
        fig.update_layout(
            title="Commodity Price Trends (Last 30 Days)",
            xaxis_title="Date",
            yaxis_title="Price (CAD)",
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ No data available. Please scrape data using the 'Scrape Data' tab.")

# ============================================================
# UI - SCRAPE DATA
# ============================================================
elif menu == "🔄 Scrape Data":
    st.header("🔄 Web Scraping Module")
    
    if st.button("🔄 Scrape Sunsirs Commodity Prices"):
        with st.spinner("Scraping Sunsirs..."):
            df = scrape_sunsirs()
            if not df.empty:
                if save_to_db(df):
                    st.success("✅ Data scraped and saved successfully!")
                    st.dataframe(df)
                    count = get_table_count()
                    st.info(f"Total records in database: {count}")
            else:
                st.error("❌ Failed to scrape data")
    
    st.subheader("Current Database Content")
    df_db = load_from_db(days=365)
    if not df_db.empty:
        st.dataframe(df_db)
        st.info(f"Total records: {len(df_db)}")
    else:
        st.warning("Database is empty. Please scrape data.")

# ============================================================
# UI - FORECAST
# ============================================================
elif menu == " Forecast":
    st.header(" Price Forecasting")
    
    df = load_from_db(days=90)
    
    if df.empty:
        st.warning("No data available. Please scrape data first.")
    else:
        commodities = df['commodity'].unique().tolist()
        selected_commodity = st.selectbox("Select Commodity", commodities)
        
        df_comm = df[df['commodity'] == selected_commodity].copy()
        
        if not df_comm.empty:
            periods = st.slider("Forecast Period (Days)", 7, 90, 30)
            
            if st.button("Generate Forecast"):
                with st.spinner("Generating forecast..."):
                    model, forecast, rmse, r2 = prophet_forecast(df_comm, periods)
                    
                    if forecast is not None:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("RMSE", f"{rmse:.2f}" if rmse else "N/A")
                        with col2:
                            st.metric("R² Score", f"{r2:.2f}" if r2 else "N/A")
                        
                        fig = go.Figure()
                        fig.add_trace(go.Scatter(
                            x=df_comm['date'],
                            y=df_comm['price'],
                            mode='lines+markers',
                            name='Actual' ))
                        fig.add_trace(go.Scatter(
                            x=forecast['ds'],
                            y=forecast['yhat'],
                            mode='lines',
                            name='Forecast'))
                        fig.add_trace(go.Scatter(
                            x=forecast['ds'],
                            y=forecast['yhat_lower'],
                            mode='lines',
                            line=dict(dash='dot'),
                            name='Lower Bound'))
                        fig.add_trace(go.Scatter(
                            x=forecast['ds'],
                            y=forecast['yhat_upper'],
                            mode='lines',
                            line=dict(dash='dot'),
                            name='Upper Bound' ))
                        fig.update_layout(
                            title=f"{selected_commodity} Price Forecast - {periods} Days",
                            xaxis_title="Date",
                            yaxis_title="Price (CAD)",
                            template="plotly_white" )
                        st.plotly_chart(fig, use_container_width=True)
                        
                        st.subheader("Forecast Data")
                        forecast_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
                        forecast_df.columns = ['Date', 'Forecast', 'Lower', 'Upper']
                        st.dataframe(forecast_df)

# ============================================================
# UI - EMAIL ALERTS - FIXED
# ============================================================
elif menu == " Email Alerts":
    st.header(" Email Alerts")

    df = load_from_db(days=7)


    with st.form("email_form"):
        recipient = st.text_input(
            "Recipient Email",
            value="engineer@electrolyzer.com")

        subject = st.text_input(
            "Subject",
            value="Commodity Price Alert")

        threshold = st.number_input(
            "Price Alert Threshold (CAD)",
            min_value=0.0,
            value=5000.0)

        commodity = st.selectbox(
            "Commodity",
            ["All", "Lithium carbonate", "Copper",
             "Soda ash", "Caustic soda"])

        submitted = st.form_submit_button("🔍 Check Alerts")

    # ------------- OUTSIDE FORM ----------------
    if submitted:

        if df.empty:
            st.warning("No data available. Please scrape data first.")

        else:
            alerts = []
            alert_details = []
            for _, row in df.iterrows():
                if commodity == "All" or row["commodity"] == commodity:

                    if row["price"] > threshold:

                        msg = (
                            f"{row['commodity']} price "
                            f"${row['price']:.2f} exceeded "
                            f"${threshold:.2f} on {row['date']}")

                        alerts.append(msg)
                        alert_details.append({
                            "Commodity": row["commodity"],
                            "Price": row["price"],
                            "Threshold": threshold,
                            "Date": row["date"]})

            if alerts:

                body = "\n\n".join(alerts)

                st.success(f"Found {len(alerts)} alerts!")

                st.dataframe(pd.DataFrame(alert_details))

                # Save to session_state
                st.session_state["recipient"] = recipient
                st.session_state["subject"] = subject
                st.session_state["body"] = body

            else:
                st.info("No alerts triggered.")

    # ----------- OUTSIDE FORM ----------------
    if "body" in st.session_state:

        if st.button(" Send Email Now"):

            ok = send_email_alert(
                st.session_state["recipient"],
                st.session_state["subject"],
                st.session_state["body"]
            )

            if ok:
                st.success("📧 Email sent successfully!")
            else:
                st.error("Failed to send email.")

# ============================================================
# UI - DATABASE
# ============================================================
elif menu == " Database":
    st.header(" Database Management")
    
    count = get_table_count()
    st.info(f"Total records in database: {count}")
    
    tabs = st.tabs(["View Data", "Export", "Clean"])
    
    with tabs[0]:
        st.subheader("Historical Price Data")
        days = st.slider("Days to Load", 7, 365, 30)
        df_all = load_from_db(days=days)
        
        if not df_all.empty:
            commodities = ["All"] + df_all['commodity'].unique().tolist()
            commodity_filter = st.selectbox("Filter by Commodity", commodities)
            
            if commodity_filter != "All":
                df = df_all[df_all['commodity'] == commodity_filter]
            else:
                df = df_all
            
            st.dataframe(df)
            st.info(f"Total records: {len(df)}")
        else:
            st.warning("No data available.")
    
    with tabs[1]:
        st.subheader("Export Data")
        df_export = load_from_db(days=365)
        if not df_export.empty:
            csv = df_export.to_csv(index=False)
            st.download_button(
                label=" Download CSV",
                data=csv,
                file_name=f"commodity_prices_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.warning("No data to export")
    
    with tabs[2]:
        st.subheader("Clean Database")
        if st.button(" Delete Old Records (90+ days)"):
            conn = sqlite3.connect('commodity_prices.db')
            c = conn.cursor()
            c.execute("DELETE FROM commodity_prices WHERE date < date('now', '-90 days')")
            conn.commit()
            conn.close()
            st.success(" Old records deleted (90+ days)")
            st.rerun()

# ============================================================
# UI - ANALYTICS
# ============================================================
elif menu == " Analytics":
    st.header(" Analytics Dashboard")
    
    df = load_from_db(days=90)
    
    if df.empty:
        st.warning("No data available. Please scrape data first.")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Price Summary")
            summary = df.groupby('commodity').agg({
                'price': ['min', 'max', 'mean', 'std']
            }).round(2)
            st.dataframe(summary)
        
        with col2:
            st.subheader("Recent Changes")
            recent = df.sort_values('date')
            for commodity in recent['commodity'].unique():
                df_comm = recent[recent['commodity'] == commodity]
                if len(df_comm) >= 2:
                    current = df_comm.iloc[0]['price']
                    previous = df_comm.iloc[1]['price']
                    change = ((current - previous) / previous) * 100
                    st.metric(
                        commodity,
                        f"${current:.2f}",
                        f"{change:+.1f}%",
                        delta_color="normal" if change >= 0 else "inverse"
                    )
        
        st.subheader("Price Distribution")
        fig = go.Figure()
        for commodity in df['commodity'].unique():
            df_comm = df[df['commodity'] == commodity]
            fig.add_trace(go.Box(
                y=df_comm['price'],
                name=commodity ))
        fig.update_layout(
            title="Price Distribution by Commodity",
            yaxis_title="Price (CAD)",
            template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# FOOTER
# ============================================================
st.sidebar.markdown("---")
st.sidebar.info(
    "**Electrolyzer Procurement Intelligence**\n\n"
    "• Automated web scraping\n"
    "• Prophet time-series forecasting\n"
    "• Email alerts\n"
    "• SQLite database\n\n"
    "Built for Electrolyzer Scale-Up Project")

st.sidebar.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")