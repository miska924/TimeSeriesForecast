from typing import Optional, Tuple
from retry import retry

import apimoex
import requests


class MoexAPI:
    @staticmethod
    @retry(tries=3, delay=2, backoff=2)
    def get_ticker_info(session, ticker):
        url = f'https://iss.moex.com/iss/securities/{ticker}.json'
        table = 'boards'
        query = apimoex.requests._make_query(table=table, columns=None)
        data = apimoex.requests._get_short_data(session, url, table, query)
        for info in data:
            if info['secid'] == ticker:
                return info

        raise Exception("No such ticker on MOEX!")

    @staticmethod
    @retry(tries=3, delay=2, backoff=2)
    def get_board_history(
            session: requests.Session,
            security: str,
            start: Optional[str] = None,
            end: Optional[str] = None,
            columns: Optional[Tuple[str, ...]] = (
                "BOARDID",
                "TRADEDATE",
                "CLOSE",
                "VOLUME",
                "VALUE",
            ),
            board: str = "TQBR",
            market: str = "shares",
            engine: str = "stock",
    ):
        return apimoex.get_board_history(session, security, start, end, columns, board, market, engine)
