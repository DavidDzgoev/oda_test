from fastapi import FastAPI
import yfinance as yf
import plotly.express as px
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World! We are ODA!"


@app.get("/{ticker}")
async def get_data(ticker):
    return yf.download(tickers=ticker, period='max', interval='1d').to_json()


@app.get("/{ticker}/dash/{column}", response_class=HTMLResponse)
async def get_dash(ticker, column):
    df = yf.download(tickers=ticker, period='max', interval='1d')
    fig = px.line(df, x=df.index, y=column, title=column)
    return fig.to_html()