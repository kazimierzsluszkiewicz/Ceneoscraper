from requests import get

# product_code = input('please enter the product code')
product_code = '36991221'
url = f'https://www.ceneo.pl/{product_code}#tab-reviews'
response = get(url)
print(response.status_code)