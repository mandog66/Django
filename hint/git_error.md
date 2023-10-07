# Git Error

## Description

```git push```後，如果github資料夾有箭頭圖案無法開啟，那是因為資料夾(folder)內有其他的.git檔案，所以被認為是子模塊，只要刪掉並重新上傳就可以解決。如下圖

![網路隨便找的](images/image.png)

## Solution

* step 1.

    ```bash
    cd folder
    ```

* step 2.

    ```bash
    rm -rf .git
    ```

  > -f &emsp;&emsp; deletes read-only files immediately, without asking for confirmation. When you specify this option and a file does not exist, rm does not display a warning message and does not modify the exit status. If you specify both -f and -i, rm uses the option that appears last on the command line.
  >
  > -R &emsp;&emsp; recursively removes the entire directory structure if file is a directory

* step 3.

    ```git
    cd ..

    git rm --cached folder

    git add folder

    git commit -m "Message"

    git push
    ```

  > --cached &emsp;&emsp; only remove from the index
