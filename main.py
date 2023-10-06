from markets.tg_wallet import TGWallet as TgWalletMarket
from markets.tg_crypto_bot import CryptoBot as CryptoBotMarket
from markets.binance import Binance as BinanceMarket
from markets.commex import CommEx as CommExMarket
from markets.bybit import ByBit as ByBitMarket



if __name__ == "__main__":
    # Init markets
    markets = [TgWalletMarket()]
