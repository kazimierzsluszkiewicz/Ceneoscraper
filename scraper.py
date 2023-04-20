from requests import get, codes
from bs4 import BeautifulSoup
import json

def get_element(ancestor, selector = None, attribute = None,  return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in opinion.select(selector)]
    try:
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()source
        return ancestor.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

# product_code = input('please enter the product code')
product_code = '36991221'
url = f'https://www.ceneo.pl/{product_code}#tab-reviews'
all_opinions = []
while url:
    response = get(url)
    if response.status_code == codes['ok']:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        opinions = page_dom.select('div.js_product-review')
        for opinion in opinions:
            for key, value in selectors.items():
                single_opinion[key] = get_element(opinion, *value)
            all_opinions.append(single_opinion)
    try:
        url = 'https://www.ceneo.pl' + get_element(page_dom, 'a.pagination__next', 'href')
    except:
        TypeError








            # for opinion in opinions:
            #     id = opinion['data-entry-id'].strip()
            #     author = opinion.select_one('span.user-post__author-name').text.strip()
            #     try:
            #         recommendation = opinion.select_one('span.user-post__author-recommendation > em').text.strip()
            #     except AttributeError:
            #         recommendation = None
            #     stars = opinion.select_one('span.user-post__score-count').text.strip()
            #     content = opinion.select_one('div.user-post__text').text.strip()
            #     pros = opinion.select('div.review_feature__title--positives ~ div.review-feature__item')
            #     pros = [p.text.strip() for p in pros]    
            #     cons = opinion.select('div.review_feature__title--negatives ~ div.review-feature__item')
            #     cons = [c.text.strip() for c in cons]    
            #     upvote = opinion.select_one('button.vote-yes')['data-total-vote'].strip()
            #     downvote = opinion.select_one('button.vote-no')['data-total-vote'].strip()
            #     posted = opinion.select_one('span.user-post__published > time:nth-child(1)')['datetime'].strip()
            #     try:
            #         purchased = opinion.select_one('span.user-post__published > time:nth-child(2)')['datetime'].strip()
            #     except TypeError:
            #         purchased = None
            #     single_opinion = {
            #         'id': id,
            #         'author': author,
            #         'recommendation':recommendation,
            #         'stars':stars,
            #         'content':content,
            #         'pros':pros,
            #         'cons':cons,
            #         'upvote':upvote,
            #         'downvote':downvote,
            #         'posted':posted,
            #         'purchased':purchased
            #     }
                # all_opinions.append(single_opinion)
with open(f'./opinions/{product_code}.json','u', encoding='UTF-8') as jf:
    json.dump(all_opinions, indent = 4,  ensure_ascii=False)


    