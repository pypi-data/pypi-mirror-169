# fin_crawler
## Finalcial Data Crawler


## Features
- Fetch Finalcial data like stock price or future price etc.

## Current Support List
- Taiwan stock price (daily stock price for all stocks)
- Taiwan stock price (monthly stock price for specific stock)

## Example

### Supported List
```
>>> from fin_crawler import FinCrawler
>>> FinCrawler.crawler_list
['tw_stock_price_all', 'tw_stock_price']
```

### Get Crawler Params Example
```
>>> params_example = FinCrawler.params_example('tw_stock_price_all')
爬取其中一天全部股票的價格
ex:{'date': '20220920'}
>>> params_example
{'date': '20220920'}
```

### Get Data
```
>>> stock_price = FinCrawler.get('tw_stock_price_all',{'date':'20220920'})
>>> stock_price.keys()
dict_keys(['stock_id', 'stock_name', 'vol', 'trade_num', 'trade_amount', 'open', 'close', 'high', 'low', 'spread', 'date'])
>>> stock_price['stock_id'][0]
'0050'
>>> stock_price['stock_name'][0]
'元大台灣50'
>>> stock_price['open'][0]
112.55
>>> stock_price['close'][0]
113.05
```