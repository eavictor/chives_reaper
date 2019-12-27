純靠北工程師．韭菜收割器
========================

預設指令
--------

#. **!公告 公告內容**
    BOT 會自動tag所有人然後重複公告內容，接著把原來的訊息砍掉

#. **!割韭菜 message_id**
    BOT 會搜尋給的message_id，留下有身份組的人、BOT、有回應的人以後把所有沒活動的韭菜都踢掉

#. 要其他指令的自己寫啊，作者是懶癌末期患者！

需要的權限
----------

總之權限是 **142338** 就是下面這些

#. Kick Members

#. View Channels

#. Send Messages

#. Manage Messages

#. Mention Everyone

建立BOT
-------

#. 到 `Discord Developer Page <https://discordapp.com/developers/applications/>`_ 點右上角建立一個新的Application

#. 點左邊的 **Bot** 建立一個新的Discord BOT

#. 複製 **Client ID**

#. 建立邀請URL

    格式

    .. code-block::

        https://discordapp.com/api/oauth2/authorize?client_id={Client ID填這}&scope=bot&permissions=142338

    就像這樣

    .. code-block::

        https://discordapp.com/api/oauth2/authorize?client_id=1234567890987654321&scope=bot&permissions=142338

#. 複製 **TOKEN**

#. 把複製來的 **TOKEN** 貼到 ``/src/settings.json`` 裡面 ``{"token": null}`` 的 **null** 的位置。記得要有雙引號！

#. 把第4步的 **URL** 貼上瀏覽器，將大膽的想法化為大膽的行動，催下去選伺服器加入

#. 用下面的其中一種方法叫 **BOT** 起床

使用方法(千年傳統，沒有新感受)
------------------------------

#. 安裝 **python 3.7.x** 或更新的版本，要把 **python interpreter** 加到 **path** 裡，沒加的是智障！

#. 複製或下載這個專案

#. 安裝套件

    Linux/MacOS

    .. code-block::

        sudo pip3 install -Ur ./src/requirements.txt

    Windows

    .. code-block::

        pip install -Ur ./src/requirements.txt

4. 執行 bot.py

    Linux/MacOS

    .. code-block::

         python3 -m ./src/bot.py

    Windows

    .. code-block::

        python -m .\src\bot.py

使用方法(Docker)
----------------

#. 安裝 **Docker-CE**

#. 建立 **Docker Image**
    .. code-block::

        docker build . --tag yourname/image_name:version

#. 照著預設的 **/src/settings.json** 範例修改內容。記得不要貪圖方便把 TOKEN 一起傳上 Docker Hub，這樣太危險！

#. 啟動 **Docker Container**

    --volume=Host上的檔案位置:Container內的檔案位置:ro(唯獨)或rw(讀寫，預設)

    .. code-block::

        docker run -d --volume=./settings.json:/src/settings.json:ro --restart always yourname/image_name:version
