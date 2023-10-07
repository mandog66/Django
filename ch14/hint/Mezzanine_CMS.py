# https://www.nss.com.tw/what-is-cms
# CMS系統是什麼？
# CMS（Content Management System）意思是內容管理系統，掌管網站後台的編輯、新增、儲存和組織功能，
# 讓網站的視覺化能井然有序地呈現，例如多媒體功能、購物車功能、會員管理、留言互動和社群連結等，都能讓不曾接觸過程式語言的人以直覺來操作。
# CMS系統就像擁有一個全天候運作的網站工程師，只需要給予明確的資料，就可以自行編輯排版將文章或商品上架，
# 擁有半自主性且簡單好操作，而良好的CMS系統還會定期維護更新功能，保障網站的安全性，主要提供給想要建立個人部落格的人使用。
# 最常見的CMS內容管理系統有：WordPress、Joomla和Drupal等等，開放原始碼的特性也讓這些CMS系統能夠依據自身需求，
# 修改或是新增外掛程式，讓網站本身有更多可能性，並加強網站在搜尋引擎中的排名。

# 安裝步驟
# 1.確認版本
#     1.1.python==3.10-alpine
#     1.2.django==4.1.3
#     1.3.pip==23.0.1
#     1.4.mezzanine==6.0.0
# 2.docker compose --build --rm web mezzanian-project ${PROJECT_NAME}
# 3.docker compose --rm web python ${PROJECT_NAME}/manage.py createdb
# 4.docker compose up -d