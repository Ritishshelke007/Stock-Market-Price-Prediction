import json
from turtle import heading
from urllib import response
import webbrowser

from matplotlib import ticker
from matplotlib.ft2font import HORIZONTAL
from nbformat import write
from simplejson import load
import streamlit as st
import pandas as pd
import spacy
#from stock import Stock
import datetime
from streamlit_option_menu import option_menu
from plotly import graph_objs as go
from st_aggrid import AgGrid
import requests
import bs4
from bs4 import BeautifulSoup
import feedparser
from streamlit_lottie import st_lottie

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
st.markdown("""
<style>
.big-font {
    font-size:18px !important;
}
</style>
""", unsafe_allow_html=True)



#hide side navigation
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


# side bar menus
with st.sidebar:
    selected = option_menu(
        menu_title="Dashboard",
        options=["Home", "Nifty 50", "BankNifty","Sensex","Price Prediction","Favourites Predictions", "Profile", "Contact","Logout"],
        icons=['house', 'bank', 'kanban', 'book', 'currency-bitcoin','heart','emoji-sunglasses','person-rolodex','box-arrow-right'],
    )
START = "2015-1-1"
TODAY = datetime.date.today().strftime("%Y-%m-%d")

#initialize session state
if "load_state" not in st.session_state:
    st.session_state.load_state = False

    

# for Home page
if selected == "Home":
    selected2 = option_menu(
        menu_title='',
        options=['Recent','Buzzing News⚡'],
        icons=['rss-fill','newspaper'],
        orientation="horizontal",
                )

    if selected2 == "Buzzing News⚡":
            st.header("Today's Trending Market News 📢")
            # resp = requests.get("https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms")
            # #st.write(resp)
            # soup = BeautifulSoup(resp.content, features='xml')
            # headlines = soup.findAll('title')
            # #st.header(headlines)
            nlp = spacy.load("en_core_web_sm")


                # stocks_df = pd.read_csv("ind_nifty50list.csv")
                # for title in headings:
                #     doc = nlp(title.text)
                #     for ent in doc.ents:
                #         try:
                #             if stocks_df['Company Name'].str.contains(ent.text).sum():
                #                 symbol = stocks_df[stocks_df['Company Name'].str.contains(ent.text)]['Symbol'].values[0]
                #                 org_name = stocks_df[stocks_df['Company Name'].str.contains(ent.text)]['Company Name'].values[0]

                #                 #sending yfinance symbol
                #                 stock_info = yf.Ticker(symbol+".NS").info



                #                 stock_info_dict['Org'].append(org_name)
                #                 stock_info_dict['Symbol'].append(symbol)
                #                 stock_info_dict['currentPrice'].append(stock_info['currentPrice'])
                #                 stock_info_dict['dayHigh'].append(stock_info['dayHigh'])
                #                 stock_info_dict['dayLow'].append(stock_info['dayLow'])
                #                 stock_info_dict['forwardPE'].append(stock_info['forwardPE'])
                #                 stock_info_dict['dividendYield'].append(stock_info['dividendYield'])
                #             else:
                #                 pass
                #         except:
                #             pass

                # output_df = pd.DataFrame(stock_info_dict)
                # return output_df
            #user_input = st.text_input("Add your RSS link here : ","https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms")
            #get finance headlines


            # def extract_text_from_rss():
            #     headings = []
            #     r = requests.get("https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms")
            #     soup = BeautifulSoup(r.content, features='lxml')
            #     headings = soup.findAll('title')
            #     description = soup.findAll('description')
            #     return headings

            
            def generate_stock_info(headings):
                stock_info_dict = {
                    'Org': [],
                    'Symbol': [],
                    'currentPrice': [],
                    'dayHigh': [],
                    'dayLow': [],
                    'forwardPE': [],
                    'dividendYield': []
                }


            #if feedparser does not work then will do this 

            # r = requests.get("https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms")
            # soup = BeautifulSoup(r.content, features='lxml')
            # headings = soup.findAll('title')
            # links = soup.findAll('link')
            # for heading in headings:
            #     st.markdown("* "+heading.text)

            #idea of using feedparser
            url = "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"
            f = feedparser.parse(url)
            
           
            with st.expander('Expand for financial stock news'):
                for entry in f.entries:
                    # st.write("* ",entry.title)
                    st.write("* ",entry.title)
                    #st.caption(entry.description)
                        #st.markdown('<p class="big-font">*  !!</p>', unsafe_allow_html=True)
                    st.write(entry.link)



            #fin_headings = extract_text_from_rss()

            #output 
            # output_df = generate_stock_info(fin_headings)
            # output_df.drop_duplicates(inplace=True)
            # st.dataframe(output_df)

            ##display headlines
            # with st.expander("Expand for financial stock news "):
            #     for heading in fin_headings:
            #         st.markdown("* "+heading.text)
            #         for desc in fin_headings:
            #             st.markdown()
                    




                            


        






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
    #n_years = st.slider("Years of Prediction : ", 1, 4)
    #period = n_years * 365


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


if selected == 'Profile':
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    def load_lottieurl(url : str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_3vbOcw.json")

    st.markdown("<h1 style='text-align: center; color: white;'>Your Profile</h1>", unsafe_allow_html=True)
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
            loop=True,
            quality="low",
        height=400,
        width=500,

    )

    #st_lottie(lottie_hello, key="Hello")

 

