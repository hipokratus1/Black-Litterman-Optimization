# Выгружаем бибилиотеки
import math
from grabber import grab_coins_data


def cal_score():
    b = grab_coins_data()
    # Ранжируем показатели для скоринга по надежности
    b['platforms_rank'] = b['platforms'].rank(ascending=False, method='min')
    b['links_rank'] = b['links'].rank(ascending=False, method='min')
    b['coingecko_score_rank'] = b['coingecko_score'].rank(ascending=False, method='min')
    b['developer_score_rank'] = b['developer_score'].rank(ascending=False, method='min')
    b['community_score_rank'] = b['community_score'].rank(ascending=False, method='min')
    b['liquidity_score_rank'] = b['liquidity_score'].rank(ascending=False, method='min')
    b['community_data_rank'] = b['community_data'].rank(ascending=False, method='min')
    b['developer_data_rank'] = b['developer_data'].rank(ascending=False, method='min')
    b['volume_market_cap_rank'] = b['volume_market_cap'].rank(ascending=False, method='min')

    svetofor_platforms_rank = []
    green_border_right_platforms_rank = []
    green_border_left_platforms_rank = []
    red_border_left_platforms_rank = []
    red_border_right_platforms_rank = []
    for i in b['platforms_rank']:
        if i < b['platforms_rank'].quantile(q=0.3):
            svetofor_platforms_rank_1 = 'green'
        elif i > b['platforms_rank'].quantile(q=0.8):
            svetofor_platforms_rank_1 = 'red'
        else:
            svetofor_platforms_rank_1 = 'yellow'
        svetofor_platforms_rank.append(
            svetofor_platforms_rank_1)
        green_border_right_platforms_rank.append(b['platforms_rank'].quantile(q=0.3))
        green_border_left_platforms_rank.append(b['platforms_rank'].min())
        red_border_left_platforms_rank.append(b['platforms_rank'].quantile(q=0.8))
        red_border_right_platforms_rank.append(b['platforms_rank'].max())
    b['svetofor_platforms_rank'] = svetofor_platforms_rank
    b['green_border_right_platforms_rank'] = green_border_right_platforms_rank
    b['green_border_left_platforms_rank'] = green_border_left_platforms_rank
    b['red_border_left_platforms_rank'] = red_border_left_platforms_rank
    b['red_border_right_platforms_rank'] = red_border_right_platforms_rank

    svetofor_links_rank = []
    green_border_right_links_rank = []
    green_border_left_links_rank = []
    red_border_left_links_rank = []
    red_border_right_links_rank = []
    for i in b['links_rank']:
        if i < b['links_rank'].quantile(q=0.3):
            svetofor_links_rank_1 = 'green'
        elif i > b['links_rank'].quantile(q=0.8):
            svetofor_links_rank_1 = 'red'
        else:
            svetofor_links_rank_1 = 'yellow'
        svetofor_links_rank.append(
            svetofor_links_rank_1)
        green_border_right_links_rank.append(b['links_rank'].quantile(q=0.3))
        green_border_left_links_rank.append(b['links_rank'].min())
        red_border_left_links_rank.append(b['links_rank'].quantile(q=0.8))
        red_border_right_links_rank.append(b['links_rank'].max())
    b['svetofor_links_rank'] = svetofor_links_rank
    b['green_border_right_links_rank'] = green_border_right_links_rank
    b['green_border_left_links_rank'] = green_border_left_links_rank
    b['red_border_left_links_rank'] = red_border_left_links_rank
    b['red_border_right_links_rank'] = red_border_right_links_rank

    svetofor_coingecko_score_rank = []
    green_border_right_coingecko_score_rank = []
    green_border_left_coingecko_score_rank = []
    red_border_left_coingecko_score_rank = []
    red_border_right_coingecko_score_rank = []
    for i in b['coingecko_score_rank']:
        if i < b['coingecko_score_rank'].quantile(q=0.3):
            svetofor_coingecko_score_rank_1 = 'green'
        elif i > b['coingecko_score_rank'].quantile(q=0.8):
            svetofor_coingecko_score_rank_1 = 'red'
        else:
            svetofor_coingecko_score_rank_1 = 'yellow'
        svetofor_coingecko_score_rank.append(
            svetofor_coingecko_score_rank_1)
        green_border_right_coingecko_score_rank.append(b['coingecko_score_rank'].quantile(q=0.3))
        green_border_left_coingecko_score_rank.append(b['coingecko_score_rank'].min())
        red_border_left_coingecko_score_rank.append(b['coingecko_score_rank'].quantile(q=0.8))
        red_border_right_coingecko_score_rank.append(b['coingecko_score_rank'].max())
    b['svetofor_coingecko_score_rank'] = svetofor_coingecko_score_rank
    b['green_border_right_coingecko_score_rank'] = green_border_right_coingecko_score_rank
    b['green_border_left_coingecko_score_rank'] = green_border_left_coingecko_score_rank
    b['red_border_left_coingecko_score_rank'] = red_border_left_coingecko_score_rank
    b['red_border_right_coingecko_score_rank'] = red_border_right_coingecko_score_rank

    svetofor_developer_score_rank = []
    green_border_right_developer_score_rank = []
    green_border_left_developer_score_rank = []
    red_border_left_developer_score_rank = []
    red_border_right_developer_score_rank = []
    for i in b['developer_score_rank']:
        if i < b['developer_score_rank'].quantile(q=0.3):
            svetofor_developer_score_rank_1 = 'green'
        elif i > b['developer_score_rank'].quantile(q=0.8):
            svetofor_developer_score_rank_1 = 'red'
        else:
            svetofor_developer_score_rank_1 = 'yellow'
        svetofor_developer_score_rank.append(
            svetofor_developer_score_rank_1)
        green_border_right_developer_score_rank.append(b['developer_score_rank'].quantile(q=0.3))
        green_border_left_developer_score_rank.append(b['developer_score_rank'].min())
        red_border_left_developer_score_rank.append(b['developer_score_rank'].quantile(q=0.8))
        red_border_right_developer_score_rank.append(b['developer_score_rank'].max())
    b['svetofor_developer_score_rank'] = svetofor_developer_score_rank
    b['green_border_right_developer_score_rank'] = green_border_right_developer_score_rank
    b['green_border_left_developer_score_rank'] = green_border_left_developer_score_rank
    b['red_border_left_developer_score_rank'] = red_border_left_developer_score_rank
    b['red_border_right_developer_score_rank'] = red_border_right_developer_score_rank

    svetofor_community_score_rank = []
    green_border_right_community_score_rank = []
    green_border_left_community_score_rank = []
    red_border_left_community_score_rank = []
    red_border_right_community_score_rank = []
    for i in b['community_score_rank']:
        if i < b['community_score_rank'].quantile(q=0.3):
            svetofor_community_score_rank_1 = 'green'
        elif i > b['community_score_rank'].quantile(q=0.8):
            svetofor_community_score_rank_1 = 'red'
        else:
            svetofor_community_score_rank_1 = 'yellow'
        svetofor_community_score_rank.append(
            svetofor_community_score_rank_1)
        green_border_right_community_score_rank.append(b['community_score_rank'].quantile(q=0.3))
        green_border_left_community_score_rank.append(b['community_score_rank'].min())
        red_border_left_community_score_rank.append(b['community_score_rank'].quantile(q=0.8))
        red_border_right_community_score_rank.append(b['community_score_rank'].max())
    b['svetofor_community_score_rank'] = svetofor_community_score_rank
    b['green_border_right_community_score_rank'] = green_border_right_community_score_rank
    b['green_border_left_community_score_rank'] = green_border_left_community_score_rank
    b['red_border_left_community_score_rank'] = red_border_left_community_score_rank
    b['red_border_right_community_score_rank'] = red_border_right_community_score_rank

    svetofor_liquidity_score_rank = []
    green_border_right_liquidity_score_rank = []
    green_border_left_liquidity_score_rank = []
    red_border_left_liquidity_score_rank = []
    red_border_right_liquidity_score_rank = []
    for i in b['liquidity_score_rank']:
        if i < b['liquidity_score_rank'].quantile(q=0.3):
            svetofor_liquidity_score_rank_1 = 'green'
        elif i > b['liquidity_score_rank'].quantile(q=0.8):
            svetofor_liquidity_score_rank_1 = 'red'
        else:
            svetofor_liquidity_score_rank_1 = 'yellow'
        svetofor_liquidity_score_rank.append(
            svetofor_liquidity_score_rank_1)
        green_border_right_liquidity_score_rank.append(b['liquidity_score_rank'].quantile(q=0.3))
        green_border_left_liquidity_score_rank.append(b['liquidity_score_rank'].min())
        red_border_left_liquidity_score_rank.append(b['liquidity_score_rank'].quantile(q=0.8))
        red_border_right_liquidity_score_rank.append(b['liquidity_score_rank'].max())
    b['svetofor_liquidity_score_rank'] = svetofor_liquidity_score_rank
    b['green_border_right_liquidity_score_rank'] = green_border_right_liquidity_score_rank
    b['green_border_left_liquidity_score_rank'] = green_border_left_liquidity_score_rank
    b['red_border_left_liquidity_score_rank'] = red_border_left_liquidity_score_rank
    b['red_border_right_liquidity_score_rank'] = red_border_right_liquidity_score_rank

    svetofor_community_data_rank = []
    green_border_right_community_data_rank = []
    green_border_left_community_data_rank = []
    red_border_left_community_data_rank = []
    red_border_right_community_data_rank = []
    for i in b['community_data_rank']:
        if i < b['community_data_rank'].quantile(q=0.3):
            svetofor_community_data_rank_1 = 'green'
        elif i > b['community_data_rank'].quantile(q=0.8):
            svetofor_community_data_rank_1 = 'red'
        else:
            svetofor_community_data_rank_1 = 'yellow'
        svetofor_community_data_rank.append(
            svetofor_community_data_rank_1)
        green_border_right_community_data_rank.append(b['community_data_rank'].quantile(q=0.3))
        green_border_left_community_data_rank.append(b['community_data_rank'].min())
        red_border_left_community_data_rank.append(b['community_data_rank'].quantile(q=0.8))
        red_border_right_community_data_rank.append(b['community_data_rank'].max())
    b['svetofor_community_data_rank'] = svetofor_community_data_rank
    b['green_border_right_community_data_rank'] = green_border_right_community_data_rank
    b['green_border_left_community_data_rank'] = green_border_left_community_data_rank
    b['red_border_left_community_data_rank'] = red_border_left_community_data_rank
    b['red_border_right_community_data_rank'] = red_border_right_community_data_rank

    svetofor_developer_data_rank = []
    green_border_right_developer_data_rank = []
    green_border_left_developer_data_rank = []
    red_border_left_developer_data_rank = []
    red_border_right_developer_data_rank = []
    for i in b['developer_data_rank']:
        if i < b['developer_data_rank'].quantile(q=0.3):
            svetofor_developer_data_rank_1 = 'green'
        elif i > b['developer_data_rank'].quantile(q=0.8):
            svetofor_developer_data_rank_1 = 'red'
        else:
            svetofor_developer_data_rank_1 = 'yellow'
        svetofor_developer_data_rank.append(
            svetofor_developer_data_rank_1)
        green_border_right_developer_data_rank.append(b['developer_data_rank'].quantile(q=0.3))
        green_border_left_developer_data_rank.append(b['developer_data_rank'].min())
        red_border_left_developer_data_rank.append(b['developer_data_rank'].quantile(q=0.8))
        red_border_right_developer_data_rank.append(b['developer_data_rank'].max())
    b['svetofor_developer_data_rank'] = svetofor_developer_data_rank
    b['green_border_right_developer_data_rank'] = green_border_right_developer_data_rank
    b['green_border_left_developer_data_rank'] = green_border_left_developer_data_rank
    b['red_border_left_developer_data_rank'] = red_border_left_developer_data_rank
    b['red_border_right_developer_data_rank'] = red_border_right_developer_data_rank

    svetofor_volume_market_cap_rank = []
    green_border_right_volume_market_cap_rank = []
    green_border_left_volume_market_cap_rank = []
    red_border_left_volume_market_cap_rank = []
    red_border_right_volume_market_cap_rank = []
    for i in b['volume_market_cap_rank']:
        if i < b['volume_market_cap_rank'].quantile(q=0.3):
            svetofor_volume_market_cap_rank_1 = 'green'
        elif i > b['volume_market_cap_rank'].quantile(q=0.8):
            svetofor_volume_market_cap_rank_1 = 'red'
        else:
            svetofor_volume_market_cap_rank_1 = 'yellow'
        svetofor_volume_market_cap_rank.append(
            svetofor_volume_market_cap_rank_1)
        green_border_right_volume_market_cap_rank.append(b['volume_market_cap_rank'].quantile(q=0.3))
        green_border_left_volume_market_cap_rank.append(b['volume_market_cap_rank'].min())
        red_border_left_volume_market_cap_rank.append(b['volume_market_cap_rank'].quantile(q=0.8))
        red_border_right_volume_market_cap_rank.append(b['volume_market_cap_rank'].max())
    b['svetofor_volume_market_cap_rank'] = svetofor_volume_market_cap_rank
    b['green_border_right_volume_market_cap_rank'] = green_border_right_volume_market_cap_rank
    b['green_border_left_volume_market_cap_rank'] = green_border_left_volume_market_cap_rank
    b['red_border_left_volume_market_cap_rank'] = red_border_left_volume_market_cap_rank
    b['red_border_right_volume_market_cap_rank'] = red_border_right_volume_market_cap_rank

    # Рассчитываем скоринг надежности
    b['reliability_scoring'] = b[['platforms_rank', 'links_rank',
                                  'coingecko_score_rank', 'developer_score_rank', 'community_score_rank',
                                  'liquidity_score_rank', 'community_data_rank', 'developer_data_rank',
                                  'volume_market_cap_rank']].sum(axis=1)

    # Ранжируем показатели для скоринга по доходности
    b['market_cap_in_btc_rank'] = b['market_cap_in_btc'].rank(ascending=False, method='min')
    b['market_cap_change_percentage_24h_in_currency_rank'] = b['market_cap_change_percentage_24h_in_currency'].rank(
        ascending=False, method='min')
    b['price_change_percentage_30d_in_btc_rank'] = b['price_change_percentage_30d_in_btc'].rank(ascending=False,
                                                                                                method='min')
    b['price_change_percentage_7d_in_btc_rank'] = b['price_change_percentage_7d_in_btc'].rank(ascending=False,
                                                                                              method='min')
    b['price_change_percentage_24h_in_btc_rank'] = b['price_change_percentage_24h_in_btc'].rank(ascending=False,
                                                                                                method='min')

    svetofor_market_cap_in_btc_rank = []
    green_border_right_market_cap_in_btc_rank = []
    green_border_left_market_cap_in_btc_rank = []
    red_border_left_market_cap_in_btc_rank = []
    red_border_right_market_cap_in_btc_rank = []
    for i in b['market_cap_in_btc_rank']:
        if i < b['market_cap_in_btc_rank'].quantile(q=0.3):
            svetofor_market_cap_in_btc_rank_1 = 'green'
        elif i > b['market_cap_in_btc_rank'].quantile(q=0.8):
            svetofor_market_cap_in_btc_rank_1 = 'red'
        else:
            svetofor_market_cap_in_btc_rank_1 = 'yellow'
        svetofor_market_cap_in_btc_rank.append(
            svetofor_market_cap_in_btc_rank_1)
        green_border_right_market_cap_in_btc_rank.append(b['market_cap_in_btc_rank'].quantile(q=0.3))
        green_border_left_market_cap_in_btc_rank.append(b['market_cap_in_btc_rank'].min())
        red_border_left_market_cap_in_btc_rank.append(b['market_cap_in_btc_rank'].quantile(q=0.8))
        red_border_right_market_cap_in_btc_rank.append(b['market_cap_in_btc_rank'].max())
    b['svetofor_market_cap_in_btc_rank'] = svetofor_market_cap_in_btc_rank
    b['green_border_right_market_cap_in_btc_rank'] = green_border_right_market_cap_in_btc_rank
    b['green_border_left_market_cap_in_btc_rank'] = green_border_left_market_cap_in_btc_rank
    b['red_border_left_market_cap_in_btc_rank'] = red_border_left_market_cap_in_btc_rank
    b['red_border_right_market_cap_in_btc_rank'] = red_border_right_market_cap_in_btc_rank

    svetofor_market_cap_change_percentage_24h_in_currency_rank = []
    green_border_right_market_cap_change_percentage_24h_in_currency_rank = []
    green_border_left_market_cap_change_percentage_24h_in_currency_rank = []
    red_border_left_market_cap_change_percentage_24h_in_currency_rank = []
    red_border_right_market_cap_change_percentage_24h_in_currency_rank = []
    for i in b['market_cap_change_percentage_24h_in_currency_rank']:
        if i < b['market_cap_change_percentage_24h_in_currency_rank'].quantile(q=0.3):
            svetofor_market_cap_change_percentage_24h_in_currency_rank_1 = 'green'
        elif i > b['market_cap_change_percentage_24h_in_currency_rank'].quantile(q=0.8):
            svetofor_market_cap_change_percentage_24h_in_currency_rank_1 = 'red'
        else:
            svetofor_market_cap_change_percentage_24h_in_currency_rank_1 = 'yellow'
        svetofor_market_cap_change_percentage_24h_in_currency_rank.append(
            svetofor_market_cap_change_percentage_24h_in_currency_rank_1)
        green_border_right_market_cap_change_percentage_24h_in_currency_rank.append(
            b['market_cap_change_percentage_24h_in_currency_rank'].quantile(q=0.3))
        green_border_left_market_cap_change_percentage_24h_in_currency_rank.append(
            b['market_cap_change_percentage_24h_in_currency_rank'].min())
        red_border_left_market_cap_change_percentage_24h_in_currency_rank.append(
            b['market_cap_change_percentage_24h_in_currency_rank'].quantile(q=0.8))
        red_border_right_market_cap_change_percentage_24h_in_currency_rank.append(
            b['market_cap_change_percentage_24h_in_currency_rank'].max())
    b[
        'svetofor_market_cap_change_percentage_24h_in_currency_rank'] = svetofor_market_cap_change_percentage_24h_in_currency_rank
    b[
        'green_border_right_market_cap_change_percentage_24h_in_currency_rank'] = green_border_right_market_cap_change_percentage_24h_in_currency_rank
    b[
        'green_border_left_market_cap_change_percentage_24h_in_currency_rank'] = green_border_left_market_cap_change_percentage_24h_in_currency_rank
    b[
        'red_border_left_market_cap_change_percentage_24h_in_currency_rank'] = red_border_left_market_cap_change_percentage_24h_in_currency_rank
    b[
        'red_border_right_market_cap_change_percentage_24h_in_currency_rank'] = red_border_right_market_cap_change_percentage_24h_in_currency_rank

    svetofor_price_change_percentage_30d_in_btc_rank = []
    green_border_right_price_change_percentage_30d_in_btc_rank = []
    green_border_left_price_change_percentage_30d_in_btc_rank = []
    red_border_left_price_change_percentage_30d_in_btc_rank = []
    red_border_right_price_change_percentage_30d_in_btc_rank = []
    for i in b['price_change_percentage_30d_in_btc_rank']:
        if i < b['price_change_percentage_30d_in_btc_rank'].quantile(q=0.3):
            svetofor_price_change_percentage_30d_in_btc_rank_1 = 'green'
        elif i > b['price_change_percentage_30d_in_btc_rank'].quantile(q=0.8):
            svetofor_price_change_percentage_30d_in_btc_rank_1 = 'red'
        else:
            svetofor_price_change_percentage_30d_in_btc_rank_1 = 'yellow'
        svetofor_price_change_percentage_30d_in_btc_rank.append(
            svetofor_price_change_percentage_30d_in_btc_rank_1)
        green_border_right_price_change_percentage_30d_in_btc_rank.append(
            b['price_change_percentage_30d_in_btc_rank'].quantile(q=0.3))
        green_border_left_price_change_percentage_30d_in_btc_rank.append(
            b['price_change_percentage_30d_in_btc_rank'].min())
        red_border_left_price_change_percentage_30d_in_btc_rank.append(
            b['price_change_percentage_30d_in_btc_rank'].quantile(q=0.8))
        red_border_right_price_change_percentage_30d_in_btc_rank.append(
            b['price_change_percentage_30d_in_btc_rank'].max())
    b['svetofor_price_change_percentage_30d_in_btc_rank'] = svetofor_price_change_percentage_30d_in_btc_rank
    b[
        'green_border_right_price_change_percentage_30d_in_btc_rank'] = green_border_right_price_change_percentage_30d_in_btc_rank
    b[
        'green_border_left_price_change_percentage_30d_in_btc_rank'] = green_border_left_price_change_percentage_30d_in_btc_rank
    b[
        'red_border_left_price_change_percentage_30d_in_btc_rank'] = red_border_left_price_change_percentage_30d_in_btc_rank
    b[
        'red_border_right_price_change_percentage_30d_in_btc_rank'] = red_border_right_price_change_percentage_30d_in_btc_rank

    svetofor_price_change_percentage_7d_in_btc_rank = []
    green_border_right_price_change_percentage_7d_in_btc_rank = []
    green_border_left_price_change_percentage_7d_in_btc_rank = []
    red_border_left_price_change_percentage_7d_in_btc_rank = []
    red_border_right_price_change_percentage_7d_in_btc_rank = []
    for i in b['price_change_percentage_7d_in_btc_rank']:
        if i < b['price_change_percentage_7d_in_btc_rank'].quantile(q=0.3):
            svetofor_price_change_percentage_7d_in_btc_rank_1 = 'green'
        elif i > b['price_change_percentage_7d_in_btc_rank'].quantile(q=0.8):
            svetofor_price_change_percentage_7d_in_btc_rank_1 = 'red'
        else:
            svetofor_price_change_percentage_7d_in_btc_rank_1 = 'yellow'
        svetofor_price_change_percentage_7d_in_btc_rank.append(
            svetofor_price_change_percentage_7d_in_btc_rank_1)
        green_border_right_price_change_percentage_7d_in_btc_rank.append(
            b['price_change_percentage_7d_in_btc_rank'].quantile(q=0.3))
        green_border_left_price_change_percentage_7d_in_btc_rank.append(
            b['price_change_percentage_7d_in_btc_rank'].min())
        red_border_left_price_change_percentage_7d_in_btc_rank.append(
            b['price_change_percentage_7d_in_btc_rank'].quantile(q=0.8))
        red_border_right_price_change_percentage_7d_in_btc_rank.append(
            b['price_change_percentage_7d_in_btc_rank'].max())
    b['svetofor_price_change_percentage_7d_in_btc_rank'] = svetofor_price_change_percentage_7d_in_btc_rank
    b[
        'green_border_right_price_change_percentage_7d_in_btc_rank'] = green_border_right_price_change_percentage_7d_in_btc_rank
    b[
        'green_border_left_price_change_percentage_7d_in_btc_rank'] = green_border_left_price_change_percentage_7d_in_btc_rank
    b['red_border_left_price_change_percentage_7d_in_btc_rank'] = red_border_left_price_change_percentage_7d_in_btc_rank
    b[
        'red_border_right_price_change_percentage_7d_in_btc_rank'] = red_border_right_price_change_percentage_7d_in_btc_rank

    svetofor_price_change_percentage_24h_in_btc_rank = []
    green_border_right_price_change_percentage_24h_in_btc_rank = []
    green_border_left_price_change_percentage_24h_in_btc_rank = []
    red_border_left_price_change_percentage_24h_in_btc_rank = []
    red_border_right_price_change_percentage_24h_in_btc_rank = []
    for i in b['price_change_percentage_24h_in_btc_rank']:
        if i < b['price_change_percentage_24h_in_btc_rank'].quantile(q=0.3):
            svetofor_price_change_percentage_24h_in_btc_rank_1 = 'green'
        elif i > b['price_change_percentage_24h_in_btc_rank'].quantile(q=0.8):
            svetofor_price_change_percentage_24h_in_btc_rank_1 = 'red'
        else:
            svetofor_price_change_percentage_24h_in_btc_rank_1 = 'yellow'
        svetofor_price_change_percentage_24h_in_btc_rank.append(
            svetofor_price_change_percentage_24h_in_btc_rank_1)
        green_border_right_price_change_percentage_24h_in_btc_rank.append(
            b['price_change_percentage_24h_in_btc_rank'].quantile(q=0.3))
        green_border_left_price_change_percentage_24h_in_btc_rank.append(
            b['price_change_percentage_24h_in_btc_rank'].min())
        red_border_left_price_change_percentage_24h_in_btc_rank.append(
            b['price_change_percentage_24h_in_btc_rank'].quantile(q=0.8))
        red_border_right_price_change_percentage_24h_in_btc_rank.append(
            b['price_change_percentage_24h_in_btc_rank'].max())
    b['svetofor_price_change_percentage_24h_in_btc_rank'] = svetofor_price_change_percentage_24h_in_btc_rank
    b[
        'green_border_right_price_change_percentage_24h_in_btc_rank'] = green_border_right_price_change_percentage_24h_in_btc_rank
    b[
        'green_border_left_price_change_percentage_24h_in_btc_rank'] = green_border_left_price_change_percentage_24h_in_btc_rank
    b[
        'red_border_left_price_change_percentage_24h_in_btc_rank'] = red_border_left_price_change_percentage_24h_in_btc_rank
    b[
        'red_border_right_price_change_percentage_24h_in_btc_rank'] = red_border_right_price_change_percentage_24h_in_btc_rank

    # Рассчитываем скоринг доходности
    b['profitability_scoring'] = b[['market_cap_in_btc_rank', 'market_cap_change_percentage_24h_in_currency_rank',
                                    'price_change_percentage_30d_in_btc_rank', 'price_change_percentage_7d_in_btc_rank',
                                    'price_change_percentage_24h_in_btc_rank']].sum(axis=1)

    quan_p = []
    min = b['profitability_scoring'].min()
    max = b['profitability_scoring'].max()
    for i in b['profitability_scoring']:
        quan_p1 = (i - min) / (max - min)
        quan_p.append(quan_p1)
    b['quantile_profitability_scoring'] = quan_p

    # Ранжируем скоринг волатильности
    b['market_cap_change_percentage_24h_in_currency_volatility_rank'] = b[
        'market_cap_change_percentage_24h_in_currency'].abs().rank(
        ascending=True, method='min')
    b['price_change_percentage_30d_in_btc_volatility_rank'] = b['price_change_percentage_30d_in_btc'].abs().rank(
        ascending=True,
        method='min')
    b['price_change_percentage_7d_in_btc_volatility_rank'] = b['price_change_percentage_7d_in_btc'].abs().rank(
        ascending=True,
        method='min')
    b['price_change_percentage_24h_in_btc_volatility_rank'] = b['price_change_percentage_24h_in_btc'].abs().rank(
        ascending=True,
        method='min')

    quan_r = []
    min = b['reliability_scoring'].min()
    max = b['reliability_scoring'].max()
    for i in b['reliability_scoring']:
        quan_r1 = (i - min) / (max - min)
        quan_r.append(quan_r1)
    b['quantile_reliability_scoring'] = quan_r

    svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank = []
    green_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank = []
    green_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank = []
    red_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank = []
    red_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank = []
    for i in b['market_cap_change_percentage_24h_in_currency_volatility_rank']:
        if i < b['market_cap_change_percentage_24h_in_currency_volatility_rank'].quantile(q=0.3):
            svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank_1 = 'green'
        elif i > b['market_cap_change_percentage_24h_in_currency_volatility_rank'].quantile(q=0.8):
            svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank_1 = 'red'
        else:
            svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank_1 = 'yellow'
        svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank.append(
            svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank_1)
        green_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank.append(
            b['market_cap_change_percentage_24h_in_currency_volatility_rank'].quantile(q=0.3))
        green_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank.append(
            b['market_cap_change_percentage_24h_in_currency_volatility_rank'].min())
        red_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank.append(
            b['market_cap_change_percentage_24h_in_currency_volatility_rank'].quantile(q=0.8))
        red_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank.append(
            b['market_cap_change_percentage_24h_in_currency_volatility_rank'].max())
    b[
        'svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank'] = svetofor_market_cap_change_percentage_24h_in_currency_volatility_rank
    b[
        'green_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank'] = green_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank
    b[
        'green_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank'] = green_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank
    b[
        'red_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank'] = red_border_left_market_cap_change_percentage_24h_in_currency_volatility_rank
    b[
        'red_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank'] = red_border_right_market_cap_change_percentage_24h_in_currency_volatility_rank

    svetofor_price_change_percentage_30d_in_btc_volatility_rank = []
    green_border_right_price_change_percentage_30d_in_btc_volatility_rank = []
    green_border_left_price_change_percentage_30d_in_btc_volatility_rank = []
    red_border_left_price_change_percentage_30d_in_btc_volatility_rank = []
    red_border_right_price_change_percentage_30d_in_btc_volatility_rank = []
    for i in b['price_change_percentage_30d_in_btc_volatility_rank']:
        if i < b['price_change_percentage_30d_in_btc_volatility_rank'].quantile(q=0.3):
            svetofor_price_change_percentage_30d_in_btc_volatility_rank_1 = 'green'
        elif i > b['price_change_percentage_30d_in_btc_volatility_rank'].quantile(q=0.8):
            svetofor_price_change_percentage_30d_in_btc_volatility_rank_1 = 'red'
        else:
            svetofor_price_change_percentage_30d_in_btc_volatility_rank_1 = 'yellow'
        svetofor_price_change_percentage_30d_in_btc_volatility_rank.append(
            svetofor_price_change_percentage_30d_in_btc_volatility_rank_1)
        green_border_right_price_change_percentage_30d_in_btc_volatility_rank.append(
            b['price_change_percentage_30d_in_btc_volatility_rank'].quantile(q=0.3))
        green_border_left_price_change_percentage_30d_in_btc_volatility_rank.append(
            b['price_change_percentage_30d_in_btc_volatility_rank'].min())
        red_border_left_price_change_percentage_30d_in_btc_volatility_rank.append(
            b['price_change_percentage_30d_in_btc_volatility_rank'].quantile(q=0.8))
        red_border_right_price_change_percentage_30d_in_btc_volatility_rank.append(
            b['price_change_percentage_30d_in_btc_volatility_rank'].max())
    b[
        'svetofor_price_change_percentage_30d_in_btc_volatility_rank'] = svetofor_price_change_percentage_30d_in_btc_volatility_rank
    b[
        'green_border_right_price_change_percentage_30d_in_btc_volatility_rank'] = green_border_right_price_change_percentage_30d_in_btc_volatility_rank
    b[
        'green_border_left_price_change_percentage_30d_in_btc_volatility_rank'] = green_border_left_price_change_percentage_30d_in_btc_volatility_rank
    b[
        'red_border_left_price_change_percentage_30d_in_btc_volatility_rank'] = red_border_left_price_change_percentage_30d_in_btc_volatility_rank
    b[
        'red_border_right_price_change_percentage_30d_in_btc_volatility_rank'] = red_border_right_price_change_percentage_30d_in_btc_volatility_rank

    svetofor_price_change_percentage_7d_in_btc_volatility_rank = []
    green_border_right_price_change_percentage_7d_in_btc_volatility_rank = []
    green_border_left_price_change_percentage_7d_in_btc_volatility_rank = []
    red_border_left_price_change_percentage_7d_in_btc_volatility_rank = []
    red_border_right_price_change_percentage_7d_in_btc_volatility_rank = []
    for i in b['price_change_percentage_7d_in_btc_volatility_rank']:
        if i < b['price_change_percentage_7d_in_btc_volatility_rank'].quantile(q=0.3):
            svetofor_price_change_percentage_7d_in_btc_volatility_rank_1 = 'green'
        elif i > b['price_change_percentage_7d_in_btc_volatility_rank'].quantile(q=0.8):
            svetofor_price_change_percentage_7d_in_btc_volatility_rank_1 = 'red'
        else:
            svetofor_price_change_percentage_7d_in_btc_volatility_rank_1 = 'yellow'
        svetofor_price_change_percentage_7d_in_btc_volatility_rank.append(
            svetofor_price_change_percentage_7d_in_btc_volatility_rank_1)
        green_border_right_price_change_percentage_7d_in_btc_volatility_rank.append(
            b['price_change_percentage_7d_in_btc_volatility_rank'].quantile(q=0.3))
        green_border_left_price_change_percentage_7d_in_btc_volatility_rank.append(
            b['price_change_percentage_7d_in_btc_volatility_rank'].min())
        red_border_left_price_change_percentage_7d_in_btc_volatility_rank.append(
            b['price_change_percentage_7d_in_btc_volatility_rank'].quantile(q=0.8))
        red_border_right_price_change_percentage_7d_in_btc_volatility_rank.append(
            b['price_change_percentage_7d_in_btc_volatility_rank'].max())
    b[
        'svetofor_price_change_percentage_7d_in_btc_volatility_rank'] = svetofor_price_change_percentage_7d_in_btc_volatility_rank
    b[
        'green_border_right_price_change_percentage_7d_in_btc_volatility_rank'] = green_border_right_price_change_percentage_7d_in_btc_volatility_rank
    b[
        'green_border_left_price_change_percentage_7d_in_btc_volatility_rank'] = green_border_left_price_change_percentage_7d_in_btc_volatility_rank
    b[
        'red_border_left_price_change_percentage_7d_in_btc_volatility_rank'] = red_border_left_price_change_percentage_7d_in_btc_volatility_rank
    b[
        'red_border_right_price_change_percentage_7d_in_btc_volatility_rank'] = red_border_right_price_change_percentage_7d_in_btc_volatility_rank

    svetofor_price_change_percentage_24h_in_btc_volatility_rank = []
    green_border_right_price_change_percentage_24h_in_btc_volatility_rank = []
    green_border_left_price_change_percentage_24h_in_btc_volatility_rank = []
    red_border_left_price_change_percentage_24h_in_btc_volatility_rank = []
    red_border_right_price_change_percentage_24h_in_btc_volatility_rank = []
    for i in b['price_change_percentage_24h_in_btc_volatility_rank']:
        if i < b['price_change_percentage_24h_in_btc_volatility_rank'].quantile(q=0.3):
            svetofor_price_change_percentage_24h_in_btc_volatility_rank_1 = 'green'
        elif i > b['price_change_percentage_24h_in_btc_volatility_rank'].quantile(q=0.8):
            svetofor_price_change_percentage_24h_in_btc_volatility_rank_1 = 'red'
        else:
            svetofor_price_change_percentage_24h_in_btc_volatility_rank_1 = 'yellow'
        svetofor_price_change_percentage_24h_in_btc_volatility_rank.append(
            svetofor_price_change_percentage_24h_in_btc_volatility_rank_1)
        green_border_right_price_change_percentage_24h_in_btc_volatility_rank.append(
            b['price_change_percentage_24h_in_btc_volatility_rank'].quantile(q=0.3))
        green_border_left_price_change_percentage_24h_in_btc_volatility_rank.append(
            b['price_change_percentage_24h_in_btc_volatility_rank'].min())
        red_border_left_price_change_percentage_24h_in_btc_volatility_rank.append(
            b['price_change_percentage_24h_in_btc_volatility_rank'].quantile(q=0.8))
        red_border_right_price_change_percentage_24h_in_btc_volatility_rank.append(
            b['price_change_percentage_24h_in_btc_volatility_rank'].max())
    b[
        'svetofor_price_change_percentage_24h_in_btc_volatility_rank'] = svetofor_price_change_percentage_24h_in_btc_volatility_rank
    b[
        'green_border_right_price_change_percentage_24h_in_btc_volatility_rank'] = green_border_right_price_change_percentage_24h_in_btc_volatility_rank
    b[
        'green_border_left_price_change_percentage_24h_in_btc_volatility_rank'] = green_border_left_price_change_percentage_24h_in_btc_volatility_rank
    b[
        'red_border_left_price_change_percentage_24h_in_btc_volatility_rank'] = red_border_left_price_change_percentage_24h_in_btc_volatility_rank
    b[
        'red_border_right_price_change_percentage_24h_in_btc_volatility_rank'] = red_border_right_price_change_percentage_24h_in_btc_volatility_rank

    # Рассчитываем скоринг волатильности
    b['volatility_scoring'] = b[['market_cap_change_percentage_24h_in_currency_volatility_rank',
                                 'price_change_percentage_30d_in_btc_volatility_rank',
                                 'price_change_percentage_7d_in_btc_volatility_rank',
                                 'price_change_percentage_24h_in_btc_volatility_rank']].sum(axis=1)

    quan_v = []
    min = b['volatility_scoring'].min()
    max = b['volatility_scoring'].max()
    for i in b['volatility_scoring']:
        quan_v1 = (i - min) / (max - min)
        quan_v.append(quan_v1)
    b['quantile_volatility_scoring'] = quan_v

    # Удаляем использованный столбец
    final = b.drop(
        ['market_data'],
        axis=1)

    # Создаем итоговый скоринг из всех
    b = b.sort_values(by='reliability_scoring', ascending=True)
    svetofor_reliability = []
    green_border_right_reliability = []
    green_border_left_reliability = []
    red_border_left_reliability = []
    red_border_right_reliability = []
    for i in b['reliability_scoring']:
        if i < b['reliability_scoring'].quantile(q=0.3):
            svetofor_reliability_1 = 'green'
        elif i > b['reliability_scoring'].quantile(q=0.8):
            svetofor_reliability_1 = 'red'
        else:
            svetofor_reliability_1 = 'yellow'
        svetofor_reliability.append(
            svetofor_reliability_1)
        green_border_right_reliability.append(
            b['reliability_scoring'].quantile(q=0.3))
        green_border_left_reliability.append(
            b['reliability_scoring'].min())
        red_border_left_reliability.append(
            b['reliability_scoring'].quantile(q=0.8))
        red_border_right_reliability.append(
            b['reliability_scoring'].max())
    b[
        'svetofor_reliability'] = svetofor_reliability
    b[
        'green_border_right_reliability'] = green_border_right_reliability
    b[
        'green_border_left_reliability'] = green_border_left_reliability
    b[
        'red_border_left_reliability'] = red_border_left_reliability
    b[
        'red_border_right_reliability'] = red_border_right_reliability

    b = b.sort_values(by='profitability_scoring', ascending=True)
    svetofor_profitability = []
    green_border_right_profitability = []
    green_border_left_profitability = []
    red_border_left_profitability = []
    red_border_right_profitability = []
    for i in b['profitability_scoring']:
        if i < b['profitability_scoring'].quantile(q=0.3):
            svetofor_profitability_1 = 'green'
        elif i > b['profitability_scoring'].quantile(q=0.8):
            svetofor_profitability_1 = 'red'
        else:
            svetofor_profitability_1 = 'yellow'
        svetofor_profitability.append(
            svetofor_profitability_1)
        green_border_right_profitability.append(
            b['profitability_scoring'].quantile(q=0.3))
        green_border_left_profitability.append(
            b['profitability_scoring'].min())
        red_border_left_profitability.append(
            b['profitability_scoring'].quantile(q=0.8))
        red_border_right_profitability.append(
            b['profitability_scoring'].max())
    b[
        'svetofor_profitability'] = svetofor_profitability
    b[
        'green_border_right_profitability'] = green_border_right_profitability
    b[
        'green_border_left_profitability'] = green_border_left_profitability
    b[
        'red_border_left_profitability'] = red_border_left_profitability
    b[
        'red_border_right_profitability'] = red_border_right_profitability

    b = b.sort_values(by='volatility_scoring', ascending=True)
    svetofor_volatility = []
    green_border_right_volatility = []
    green_border_left_volatility = []
    red_border_left_volatility = []
    red_border_right_volatility = []
    for i in b['volatility_scoring']:
        if i < b['volatility_scoring'].quantile(q=0.3):
            svetofor_volatility_1 = 'green'
        elif i > b['volatility_scoring'].quantile(q=0.8):
            svetofor_volatility_1 = 'red'
        else:
            svetofor_volatility_1 = 'yellow'
        svetofor_volatility.append(
            svetofor_volatility_1)
        green_border_right_volatility.append(
            b['volatility_scoring'].quantile(q=0.3))
        green_border_left_volatility.append(
            b['volatility_scoring'].min())
        red_border_left_volatility.append(
            b['volatility_scoring'].quantile(q=0.8))
        red_border_right_volatility.append(
            b['volatility_scoring'].max())
    b[
        'svetofor_volatility'] = svetofor_volatility
    b[
        'green_border_right_volatility'] = green_border_right_volatility
    b[
        'green_border_left_volatility'] = green_border_left_volatility
    b[
        'red_border_left_volatility'] = red_border_left_volatility
    b[
        'red_border_right_volatility'] = red_border_right_volatility

    b['quantile_scoring'] = b[
        ['reliability_scoring', 'volatility_scoring', 'profitability_scoring']].sum(axis=1)

    # Сортируем столбцы по итоговому скорингу
    final = b.sort_values(by='quantile_scoring', ascending=True)

    svetofor = []
    green_border_right_svetofor = []
    green_border_left_svetofor = []
    red_border_left_svetofor = []
    red_border_right_svetofor = []
    for i in final['quantile_scoring']:
        if i < final['quantile_scoring'].quantile(q=0.3):
            svetofor_1 = 'green'
        elif i > final['quantile_scoring'].quantile(q=0.8):
            svetofor_1 = 'red'
        else:
            svetofor_1 = 'yellow'
        svetofor.append(
            svetofor_1)
        green_border_right_svetofor.append(
            final['quantile_scoring'].quantile(q=0.3))
        green_border_left_svetofor.append(
            final['quantile_scoring'].min())
        red_border_left_svetofor.append(
            final['quantile_scoring'].quantile(q=0.8))
        red_border_right_svetofor.append(
            final['quantile_scoring'].max())

    final['svetofor'] = svetofor
    final['green_border_right_svetofor'] = green_border_right_svetofor
    final['green_border_left_svetofor'] = green_border_left_svetofor
    final['red_border_left_svetofor'] = red_border_left_svetofor
    final['red_border_right_svetofor'] = red_border_right_svetofor

    final = final.drop(columns=['categories', 'market_data', 'tickers', 'contract_address'])
    return final