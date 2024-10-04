"""
    Beginning steps for a stock monitor app, using yfinance and Textual
    to fetch and display stock prices with a friendly UI, all from the terminal.
"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Button, Static
import yfinance as yf

def fetch_stock_price(symbol: str) -> str:
    try:
        stock = yf.Ticker(symbol)
        stock_info = stock.info
        current_price = stock_info.get("currentPrice")

        if current_price is not None:
            return f"Price of {symbol} is {current_price}"
        else:
            return f"Price data for {symbol} not available"
    except Exception as e:
        return f"Error fetching price: {e}"
    
class StockMonitorApp(App):

    CSS = """

    Screen {
        background: #18458c;
    }

    #title {
        margin: 2 2 2 2;
        border: solid black;
        text-align: center;
    }
    #stock-input {
        margin: 2;
    }
    #fetch-button {
        margin: 1;
    }

    #stock-price {
        border: solid black;
    }
    """

    def compose(self) -> ComposeResult:

        yield Vertical(
            Static("Yahoo Finance Price Finder", id="title"),
            Input(placeholder="Enter stock symbol", id="stock_input"),
            Button("Get Price", id="fetch-button"),
            Static("Stock price will appear here", id="stock-price"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        stock_input = self.query_one("#stock_input", Input).value
    
        if stock_input:

            stock_price = fetch_stock_price(stock_input.upper())
          
            self.query_one("#stock-price", Static).update(stock_price)

if __name__ == "__main__":
    app = StockMonitorApp()
    app.run()