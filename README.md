# gocream-pysberbank

API - [link][api_url]

Тестовые карты - [link][test_cards]


## Installation

```sh
python -m pip install gocream-pysberbank
```

```python
from gocream_pysberbank import Sberbank
from gocream_pysberbank.constants import DESCRIPTION_BY_ACTION_CODE
from gocream_pysberbank.http import SberbankPaymentApi
```


## Development

Окружения и сборка управляются через Hatch. Минимальная версия Python - 3.10.

```sh
hatch run test:check
hatch run mtest:check
hatch run lint:check
hatch run lint:fmt-check
hatch build --clean
```

`test` проверяет библиотеку на Python 3.10, `mtest` запускает матрицу Python 3.10-3.14. Тестам запрещены сетевые обращения. Окружение `lint` использует Python 3.14.

Для подключения git-хуков и настройки `git blame` выполните `hatch run init`. Команда `hatch run remove` отменяет эти локальные настройки.


## TO DO:

* all errors inheritance SberbankException and raise them
* add all params from api to class methods arguments
* unittests
* test flask app


[api_url]: https://securepayments.sberbank.ru/wiki/doku.php/integration:api:start
[test_cards]: https://securepayments.sberbank.ru/wiki/doku.php/test_cards
