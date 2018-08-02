==============================
homebot
==============================

自宅のRaspiで動くBot達
==============================

googlehomenotifier
------------------------------

Google Homeにしゃべってもらう

rain_fall
------------------------------

雨雲レーダを表示する

add_task
------------------------------

todoistにタスクを追加する

nanaco
------------------------------

nanacoの残高照会、チャージを行う

.. code-block:: sh

  @bot nanaco charge 1000
  @bot nanaco now

使い方
==============================

.. code-block:: sh

  $ python -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  $ python run.sh
