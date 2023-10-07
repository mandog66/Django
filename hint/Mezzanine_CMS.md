# CMS and Mezzanine

## CMS

### - Description

* CMS系統是什麼? `CMS(Content Management System)`意思是內容管理系統，掌管網站後台的編輯、新增、儲存和組織功能，讓網站的視覺化能井然有序地呈現，例如多媒體功能、購物車功能、會員管理、留言互動和社群連結等，都能讓不曾接觸過程式語言的人以直覺來操作。CMS系統就像擁有一個全天候運作的網站工程師，只需要給予明確的資料，就可以自行編輯排版將文章或商品上架，擁有半自主性且簡單好操作，而良好的CMS系統還會定期維護更新功能，保障網站的安全性，主要提供給想要建立個人部落格的人使用。最常見的CMS內容管理系統有：`WordPress`、Joomla和Drupal等等，開放原始碼的特性也讓這些CMS系統能夠依據自身需求，修改或是新增外掛程式，讓網站本身有更多可能性，並加強網站在搜尋引擎中的排名。[參考網站](https://www.nss.com.tw/what-is-cms)

## Mezzanine

### - Description

* Mezzanine是一個建立在Django框架的Django APP，也可以說是一個`內容管理平台`，包含許多CMS功能，可以做部落格、商品上架、`購物車功能(Cartridge)`，還有很多好處在[官網](https://github.com/stephenmcd/mezzanine)。

### - Install Mezzanine

1. 確認版本(2023/10/01)

   * 版本有相依

    ```text
    python==3.10-alpine

    django==4.1.3

    pip==23.0.1

    mezzanine==6.0.0
    ```

2. 建立專案

    ```docker
    docker compose run --build --rm web mezzanian-project ${PROJECT_NAME}
    ```

3. 連接資料庫

    ```docker
    docker compose run --rm web python ${PROJECT_NAME}/manage.py createdb
    ```

4. 啟動伺服器

    ```docker
    docker compose up -d
    ```

### - Install Mezzanine Cartridge

* Description
  * Cartridge 是 Mezzanine 的購物車套件。
  * 詳細資訊可以參考[官方網站](https://github.com/stephenmcd/cartridge)。

* Install
  1. 使用Docker的話，要確認Python安裝的是哪種版本，經過測試`slim`和`完整版(後面什麼都不加)`可以使用，`alpine`會有錯誤。
  2. 透過Mezzanine建立購物車專案。

     ```DOCKER
     docker compose run --build --rm web mezzanine-project -a cartridge ${PROJECT_NAME}
     ```

  3. 在測試時會有地區錯誤，要先確認地區資訊。
     啟動容器並在容器內輸入查詢地區指令。

     ```DOCKER
     docker compose up -d
     ```

     ```BASH
     locale -a
     ```

     > [!NOTE]
     > 這裡使用```docker compose run --rm web locale -a```也可以。
  4. 順利的話，可以看到所有地區，這裡使用`en_US.utf8`。
  5. 在local\_settings.py加上`SHOP_CURRENCY_LOCALE = "en_US.utf8"`。
  6. 建立資料庫

     ```DOCKER
     docker compose run --rm web python ${PROJECT_NAME}/manage.py createdb
     ````

> [!NOTE]
> 地區錯誤的原因，我們才會需要配置。
> 安裝是沒有問題，但建立資料庫會產生下面的錯誤。
>
> ```TEXT
> 2023-09-22 20:00:26 ERRORS:
> 2023-09-22 20:00:26 shop.CartItem.total_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.CartItem.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Category.price_max: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Category.price_min: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.DiscountCode.discount_deduct: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.DiscountCode.discount_exact: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.DiscountCode.min_purchase: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Order.discount_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Order.item_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Order.shipping_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Order.tax_total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Order.total: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.OrderItem.total_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.OrderItem.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Product.sale_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Product.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.ProductVariation.sale_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.ProductVariation.unit_price: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Sale.discount_deduct: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> 2023-09-22 20:00:26 shop.Sale.discount_exact: (fields.E134) 'max_digits' must be greater or equal to 'decimal_places'.
> ```

## Dockerfile

* [slim](doc/Dockerfile-slim)

```DOCKERFILE
FROM python:3.10-slim AS builder

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get -y install locales-all
RUN pip install --no-cache-dir -r requirements.txt

```

* [complete](doc/Dockerfile-complete)

```DOCKERFILE
FROM python:3.10 AS builder

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get -y install locales-all
RUN pip install --no-cache-dir -r requirements.txt
```
