# How to use jQuery for changing images

## Description

### 下面這個jQuery程式用來更改html的內容

```html
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#id_backfile').change(function() {
                $('#show_back_image').html('<img src="'+'{{ base_url }}'+'/images/'+
                    $(this).find(':selected').val() + '" width="100%">');
            });
        });
    </script>
</head>
```

### 一開始會去監聽id叫做`id_backfile`的 **\<select>** 內容有沒有被修改。在網站裡 **\<select>** 長下面這樣

```html
<select name="backfile" id="id_backfile">
    <option value="1.jpg">1.jpg</option>

    <option value="2.jpg">2.jpg</option>

    <option value="3.jpg">3.jpg</option>

    <option value="4.jpg">4.jpg</option>

    <option value="5.jpg">5.jpg</option>

    <option value="6.jpg">6.jpg</option>

    <option value="7.jpg">7.jpg</option>

    <option value="8.jpg">8.jpg</option>

    <option value="9.jpg">9.jpg</option>

    <option value="10.jpg">10.jpg</option>
</select>
```

### 發現有變動(選取某個選項)，`$(this).find(':selected').val()`就會回傳選項的值(value)。</br></br>接著找到 **\<div>** 有id叫做`show_back_image`的tag，把這個 **\<div>** 的內容做修改，也就是把 **\<img>** 重寫，這樣就可以動態的改變網站上顯示的圖片

```HTML
<div class='card-body' id='show_back_image'>
    <!-- 更改成選擇的圖片名稱(value) -->
    <!-- 預設圖片名稱是1.jpg  -->
    <img src="{{ base_url }}/images/1.jpg" width="100%">
</div>

```

> [!IMPORTANT]
> jQuery腳本網址一定要放在`<head>`裡面。

## Reference

* [jQuery change() Method :](https://www.w3schools.com/jquery/event_change.asp)

    The change event occurs when the value of an element has been changed (only works on `<input>`, `<textarea>` and `<select>` elements).

    The change() method triggers the change event, or attaches a function to run when a change event occurs.

    > [!NOTE]
    > For select menus, the change event occurs when an option is selected. For text fields or text areas, the change event occurs when the field loses focus, after the content has been changed.

* [jQuery html() Method :](https://www.w3schools.com/jquery/html_html.asp)

    The html() method sets or returns the content (innerHTML) of the selected elements.

    When this method is used to return content, it returns the content of the FIRST matched element.

    When this method is used to set content, it overwrites the content of ALL matched elements.

    > [!IMPORTANT]
    > To set or return only the text content of the selected elements, use the text() method.

* [jQuery find() Method :](https://www.w3schools.com/jquery/traversing_find.asp)

    The find() method returns descendant elements of the selected element.

    A descendant is a child, grandchild, great-grandchild, and so on.

    The Document Object Model (DOM) tree: This method traverse downwards along descendants of DOM elements, all the way down to the last descendant. To only traverse a single level down the DOM tree (to return direct children), use the children() method.

    > [!NOTE]
    > The filter parameter is required for the find() method, unlike the rest of the tree traversal methods.

    > [!IMPORTANT]
    > To return all of the descendant elements, use the `*` selector.

* [jQuery val() Method :](https://www.w3schools.com/jquery/html_val.asp)

    The val() method returns or sets the value attribute of the selected elements.

  * When used to return value :

    This method returns the value of the value attribute of the FIRST matched element.

  * When used to set value :

    This method sets the value of the value attribute for ALL matched elements.

  > [!NOTE]
  > The val() method is mostly used with HTML form elements.
