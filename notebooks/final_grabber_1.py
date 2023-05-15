from pycoingecko import CoinGeckoAPI
import time
import pandas as pd
from pandas.core.common import flatten
# Включаем API на CoinGecko
cg = CoinGeckoAPI()

def grab_coins_data():
    sample = cg.get_coins_list()
    sam = []
    for i in sample:
        sam1 = i.get('id')
        sam.append(sam1)
    sample2 = sam

    # Создаем пустой DateFrame
    a = pd.DataFrame()

    # Выгружаем все данные по монетам и преобразуем их в DataFrame
    for item in sample2:
        try:
            moneta = cg.get_coin_by_id(id=item, localization=False, tickers=True,
                                       market_data=True,
                                       community_data=True,
                                       developer_data=True, Sparkline=True)
            time.sleep(1)
            new = pd.DataFrame.from_dict(data=moneta, orient='index')
            new1 = new.T
            a = pd.concat([a, new1], axis=0, sort=False)
        except ValueError:
            pass

    # Удаляем ненужные столбцы
    b = a.drop(
        ['block_time_in_minutes', 'description', 'public_notice', 'additional_notices', 'image', 'country_origin',
         'status_updates',
         'genesis_date', 'sentiment_votes_down_percentage', 'last_updated', 'public_interest_score',
         'hashing_algorithm', 'coingecko_rank', 'public_interest_stats',
         'asset_platform_id', 'sentiment_votes_up_percentage'],
        axis=1)

    # Ставим фильтр на наличие рыночной капитализации
    b = b[b['market_cap_rank'] > 1]

    # Подсчитываем количество платформ для каждой монеты
    plat = []
    for i in b['platforms']:
        plat1 = len(i)
        plat.append(plat1)
    b['platforms'] = plat

    # Подсчитываем количество подписчиков во всех каналах для связи
    com = []
    for i in b['community_data']:
        com1 = list(i.values())
        com2 = 0
        for j in com1:
            if j is not None:
                com2 += j
        com.append(com2)
    b['community_data'] = com

    # Подсчитываем уровень обновляемости кода и его доступности для инвесторов
    dev = []
    for i in b['developer_data']:
        del i['code_additions_deletions_4_weeks']
        del i['commit_count_4_weeks']
        del i['last_4_weeks_commit_activity_series']
        dev1 = list(i.values())
        dev2 = 0
        for j in dev1:
            dev2 += j
        dev.append(dev2)
    b['developer_data'] = dev

    # Выгружаем все криптобиржи, на которых торгуется монета
    tick = []
    for i in b['tickers']:
        tick1 = []
        for j in i:
            tick2 = j.get('market')
            tick1.append(tick2.get('name'))
        tick.append(tick1)
    b['tickers'] = tick
    tick3 = []
    for i in b['tickers']:
        tick4 = dict.fromkeys(i)
        tick5 = list(tick4)
        tick3.append(tick5)
    b['tickers'] = tick3

    # Подсчитываем количество информационных источников по каждой монете
    link = []
    for i in b['links']:
        del i['repos_url']
        link1 = list(i.values())
        link2 = list(flatten(link1))
        link3 = 0
        for j in link2:
            if j is not None and j != '':
                link3 += 1
            else:
                link3 += 0
        link.append(link3)
    b['links'] = link

    # Получаем курс каждой монеты в btc
    cur = []
    for i in b['market_data']:
        cur1 = []
        cur2 = i.get('current_price')
        cur1.append(cur2.get('btc'))
        cur += cur1
    b['current_price_in_btc'] = cur
    b = b[b['current_price_in_btc'] > 0]

    # Получаем капитализацию каждой монеты в btc
    cap = []
    for i in b['market_data']:
        cap1 = []
        cap2 = i.get('market_cap')
        cap1.append(cap2.get('btc'))
        cap += cap1
    b['market_cap_in_btc'] = cap

    # Получаем объем торгов каждой монеты в btc
    vol = []
    for i in b['market_data']:
        vol1 = []
        vol2 = i.get('total_volume')
        vol1.append(vol2.get('btc'))
        vol += vol1
    b['total_volume_in_btc'] = vol
    b = b[b['total_volume_in_btc'] > 0]

    # Получаем изменение капитализации каждой монеты в процентах за 24 часа
    cap24 = []
    for i in b['market_data']:
        cap24_1 = []
        cap24_2 = i.get('market_cap_change_percentage_24h_in_currency')
        cap24_1.append(cap24_2.get('btc'))
        cap24 += cap24_1
    b['market_cap_change_percentage_24h_in_currency'] = cap24
    b = b[abs(b['market_cap_change_percentage_24h_in_currency']) > 0]

    # Получаем изменение цены каждой монеты в процентах за 30 дней
    cur30 = []
    for i in b['market_data']:
        cur30_1 = []
        cur30_2 = i.get('price_change_percentage_30d_in_currency')
        cur30_1.append(cur30_2.get('btc'))
        cur30 += cur30_1
    b['price_change_percentage_30d_in_btc'] = cur30
    b = b[abs(b['price_change_percentage_30d_in_btc']) > 0]

    # Получаем изменение цены каждой монеты в процентах за 7 дней
    cur7 = []
    for i in b['market_data']:
        cur7_1 = []
        cur7_2 = i.get('price_change_percentage_7d_in_currency')
        cur7_1.append(cur7_2.get('btc'))
        cur7 += cur7_1
    b['price_change_percentage_7d_in_btc'] = cur7
    b = b[abs(b['price_change_percentage_7d_in_btc']) > 0]

    # Получаем изменение цены каждой монеты в процентах за 24 часа
    cur24 = []
    for i in b['market_data']:
        cur24_1 = []
        cur24_2 = i.get('price_change_percentage_24h_in_currency')
        cur24_1.append(cur24_2.get('btc'))
        cur24 += cur24_1
    b['price_change_percentage_24h_in_btc'] = cur24
    b = b[abs(b['price_change_percentage_24h_in_btc']) > 0]

    # Рассчитываем отношение объема продаж к рыночной капитализации
    b['volume_market_cap'] = b['total_volume_in_btc'] / b['market_cap_in_btc']
    b = b[b['volume_market_cap'] > 0]
    return b