import apimoex


class MoexAPI:
    @staticmethod
    def get_ticker_info(session, ticker):
        url = f'https://iss.moex.com/iss/securities/{ticker}.json'
        table = 'boards'
        query = apimoex.requests._make_query(table=table, columns=None)
        data = apimoex.requests._get_short_data(session, url, table, query)
        for info in data:
            if info['secid'] == ticker:
                return info

        raise Exception("No such ticker on MOEX!")
