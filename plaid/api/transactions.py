from plaid.api.api import API


class Transactions(API):
    '''Transactions endpoints.'''

    def get(self,
            access_token,
            start_date,
            end_date,
            _options=None,
            account_ids=None,
            count=None,
            offset=None,
            session=None):
        '''
        Return accounts and transactions for an item.
        (`HTTP docs <https://plaid.com/docs/api/#transactions>`__)

        The transactions in the response are paginated -- compare the number of
        transactions received so far against response['total_transactions'] to
        determine whether to fetch another page.

        :param  str     access_token:
        :param  str     start_date:     The earliest date for transactions.
        :param  str     end_date:       The latest date for transactions.
        :param  [str]   account_ids:    A list of account_ids to retrieve for
                                        the item. Optional.
        :param  int     count:          The number of transactions to fetch.
                                        Optional.
        :param  int     offset:         The number of transactions to skip from
                                        the beginning of the fetch. Optional.
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.

        All date should be formatted as ``YYYY-MM-DD``.
        '''
        options = _options or {}

        if account_ids is not None:
            options['account_ids'] = account_ids
        if count is not None:
            options['count'] = count
        if offset is not None:
            options['offset'] = offset

        return self.client.post('/transactions/get', {
            'access_token': access_token,
            'start_date': start_date,
            'end_date': end_date,
            'options': options,
        }, session=session)

    def refresh(self,
                access_token,
                session=None,
                ):
        '''
        Request on-demand refresh of transactions and balances for an Item
        (`HTTP docs <https://plaid.com/docs/api/#transactions-refresh>`__)

        Calls to /transactions/refresh will initiate an on-demand check for new
        transactions since last scheduled update. If there are fresh
        transactions, Plaid will fire a webhook. To fetch these transactions,
        call /transactions/get.

        :param  str     access_token:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        return self.client.post('/transactions/refresh', {
            'access_token': access_token,
        }, session=session)
