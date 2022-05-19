import imp
from tracemalloc import start
import webbrowser

from matplotlib import ticker
from matplotlib.ft2font import HORIZONTAL
import streamlit as st
import pandas as pd
#from stock import Stock
import datetime
from streamlit_option_menu import option_menu
from plotly import graph_objs as go
from st_aggrid import AgGrid


import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
from plotly import graph_objs as go

# st.write("Hello Streamlit")
st.set_page_config(
        page_title="Search and Predict",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )


# side bar menus
with st.sidebar:
    selected = option_menu(
        menu_title="Dashboard",
        options=["Home", "Nifty 50", "BankNifty","Sensex","Price Prediction","Favourites Predictions", "Profile", "Contact","Logout"],
        icons=['house', 'bank', 'kanban', 'book', 'currency-bitcoin','heart','emoji-sunglasses','person-rolodex','box-arrow-right'],
    )
START = "2015-1-1"
TODAY = datetime.date.today().strftime("%Y-%m-%d")

# for Home page
if selected == "Home":
    selected2 = option_menu(
        menu_title='',
        options=['Recent','Buzz News'],
        icons=['rss-fill','newspaper'],
        orientation="horizontal",
                )


# for Nifty 50
if selected == "Nifty 50":

    st.title("Know Your Stock")
    #st.write("Query Parameters")


    stock_list = pd.read_csv('https://raw.githubusercontent.com/Ritishshelke007/Ritishshelke007/main/Nifty50.txt')
    st.subheader("Select Stock")
    stocks_symbol = st.selectbox("", stock_list)
    if stocks_symbol=="Select Your Stock":
        st.header("PLease Select stock before Proceeding further")

    tickerData = yf.Ticker(stocks_symbol)
    n_years = st.slider("Years of Prediction : ", 1, 4)
    period = n_years * 365


    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data


    data_load_state = st.text("Load data...")
    data = load_data(stocks_symbol)
    data_load_state.text("Loading Data... Please wait for a while!")

    st.subheader("About Company")
    string_logo = '<img src=%s>' % tickerData.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)

    string_name = tickerData.info['longName']
    st.header('**%s**' % string_name)

    string_summary = tickerData.info['longBusinessSummary']
    st.info(string_summary)

    today = datetime.date.today()

    st.header('Price History')
    start_date = st.date_input(
        "From",
        today
    )

    end_date = st.date_input(
        "To",
        today
    )

    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
    st.write(tickerDf)

    st.subheader("Share Price since 2015")
    def plot_chart_for_range():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True)
        fig.update_layout(xaxis=dict(showgrid=False),
                          yaxis=dict(showgrid=False))
        st.plotly_chart(fig)

    plot_chart_for_range()


# for crypto
# if selected=="Cryptocurrency":
#     st.header("Know more about Cryptocurrency")
#     #st.button('Check Current Prices')
#     url = 'https://www.coinbase.com/price'

#     if st.button('Check Current Prices'):
#         webbrowser.open_new_tab(url)


#     crypto_list = pd.read_csv('https://raw.githubusercontent.com/Ritishshelke007/Ritishshelke007/main/crypto.txt')
#     st.subheader("Select Crypto")
#     crypto_symbol = st.selectbox("", crypto_list)

#     tickerData2 = yf.Ticker(crypto_symbol)
#     n_years = st.slider("Years of Prediction : ", 1, 4)
#     period = n_years * 365


#     @st.cache
#     def load_crypto_data(ticker2):
#         data2 = yf.download(ticker2, START, TODAY)
#         data2.reset_index(inplace=True)
#         return data2


#     data2_load_state = st.text("Load data...")
#     data2 = load_crypto_data(crypto_symbol)
#     data2_load_state.text("Loading Data... Please wait for a while!")

#     st.subheader("About Coin")
#     string_logo = '<img src=%s>' % tickerData2.info['logo_url']
#     st.markdown(string_logo, unsafe_allow_html=True)

#     # string_name = tickerData2.info['longName']
#     # st.header('**%s**' % string_name)

#     # string_summary = tickerData2.info['longBusinessSummary']
#     # st.info(string_summary)

#     today = date.today()

#     st.header('Price History')
#     start_date = st.date_input(
#         "From",
#         today
#     )

#     end_date = st.date_input(
#         "To",
#         today
#     )

#     tickerDf2 = tickerData2.history(period='1d', start=start_date, end=end_date)
#     st.write(tickerDf2)

#     st.subheader("Coin Price since 2015")


#     def plot_chart_for_crypto():
#         fig2 = go.Figure()
#         fig2.add_trace(go.Scatter(x=data2['Date'], y=data2['Open'], name='stock_open'))
#         fig2.add_trace(go.Scatter(x=data2['Date'], y=data2['Close'], name='stock_close'))
#         fig2.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
#         fig2.update_layout(xaxis=dict(showgrid=False),
#                           yaxis=dict(showgrid=False))
#         st.plotly_chart(fig2)


#     plot_chart_for_crypto()

# if selected=="Price Prediction":
#     # ------ layout setting---------------------------
#     window_selection_c = st.sidebar.container() # create an empty container in the sidebar
#     window_selection_c.markdown("## Insights") # add a title to the sidebar container
#     sub_columns = window_selection_c.columns(2) #Split the container into two columns for start and end date
#     # ----------Time window selection-----------------
#     YESTERDAY=datetime.date.today()-datetime.timedelta(days=1)

#     DEFAULT_START=YESTERDAY - datetime.timedelta(days=700)

#     # START_DATE_ = st.date_input("From", today)
#     # END_DATE_ = st.date_input("To", today)

 

