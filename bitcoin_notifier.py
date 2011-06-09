#!/usr/bin/env python

import urllib
from decimal import Decimal

from BeautifulSoup import BeautifulSoup


URL_UOL_COTACOES = 'http://economia.uol.com.br/cotacoes/'
URL_BITCOINCHARTS_MTGOX = 'http://bitcoincharts.com/markets/mtgoxUSD_trades.html'


def uol_usdbrl():
  html = urllib.urlopen(URL_UOL_COTACOES).read()
  soup = BeautifulSoup(html)

  data = soup.find('span', 'cotacao-dolar').text
  usdbrl = data.split()[1].replace(',', '.')
  usdbrl = Decimal(usdbrl)

  return usdbrl

def mtgox_15min_usdbtc():
  html = urllib.urlopen(URL_BITCOINCHARTS_MTGOX).read()
  soup = BeautifulSoup(html)

  recent_trades = soup.find('table', 'data')
  top_row = recent_trades.find('tr', 'odd')
  
  assert top_row.first().text == u'15min'
  cell = top_row.findAll()[-1]
  usdbtc = Decimal(cell.text)

  return usdbtc

