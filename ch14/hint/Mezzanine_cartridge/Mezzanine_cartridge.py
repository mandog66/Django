# Cartridge 是 Mezzanine 的購物車套件

# 安裝步驟
# 1.確認版本
#     1.1.python==3.10-slim or python==3.10(python==3.10-alpine測試過，會安裝失敗，可以看Dockerfile)
#     1.2.django==4.1.3
#     1.3.pip
#     1.4.mezzanine
#     1.4.cartridge
# 2.docker compose --build --rm web mezzanian-project -a cartridge ${PROJECT_NAME}
# 這裡要先啟動容器(經過測試，執行 docker compose run --rm 也可以)
# 3.docker compose up -d
# 4.在 Terminal 輸入 locale -a 查看可以使用的地區，這裡使用 en_US.utf8
# 5.在local_settings.py 加上 SHOP_CURRENCY_LOCALE = "en_US.utf8"
# 6.docker compose --rm web python ${PROJECT_NAME}/manage.py createdb

# Dockerfile 測試能用
# 這裡在除錯，安裝 Cartridge 有地區的問題，error 會要我們輸入 SHOP_CURRENCY_LOCALE 這個變數，
# 當我們輸入之後卻有地區問題，讓我們無法建立資料庫。
# Error Message : 
# 2023-09-22 20:00:26 ERRORS:
# 2023-09-22 20:00:26 shop.CartItem.total_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.CartItem.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Category.price_max: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Category.price_min: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.DiscountCode.discount_deduct: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.DiscountCode.discount_exact: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.DiscountCode.min_purchase: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Order.discount_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Order.item_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Order.shipping_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Order.tax_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Order.total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.OrderItem.total_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.OrderItem.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Product.sale_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Product.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.ProductVariation.sale_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.ProductVariation.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Sale.discount_deduct: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 2023-09-22 20:00:26 shop.Sale.discount_exact: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
# 所以要額外安裝套件(locales-all)，這個套件可以幫忙下載正確地區的資料，在 alpine 即使安裝套件後也無法建立資料庫，只有在 slim or 完整版本可以
# 安裝成功。

##################################################################
# FROM python:3.10-slim AS builder

# EXPOSE 8000

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /usr/src/app

# COPY requirements.txt ./

# RUN apt-get update && apt-get -y install locales-all
# RUN pip install --no-cache-dir -r requirements.txt
##################################################################
# FROM python:3.10 AS builder

# EXPOSE 8000

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /usr/src/app

# COPY requirements.txt ./

# RUN apt-get update && apt-get -y install locales-all
# RUN pip install --no-cache-dir -r requirements.txt
##################################################################
