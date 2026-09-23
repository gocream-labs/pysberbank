# gocream-pysberbank

Python-клиент для [унаследованного API СберБанка][api_url], который ЮKassa
сохраняет для компаний, перешедших из Сбера. Это не клиент для современного
API ЮKassa.

Описание протокола - [инструкция ЮKassa][protocol_spec].
Архивные материалы СберБанка - [документация API][sberbank_api_url] и
[тестовые карты][sberbank_test_cards].


## Installation

```sh
python -m pip install gocream-pysberbank
```

```python
from gocream_pysberbank import SberbankClient
from gocream_pysberbank.constants import DESCRIPTION_BY_ACTION_CODE
```

Для совместимости с прежним API сохранены имена `Sberbank` и
`SberbankPaymentApi`.


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


[api_url]: https://yookassa.ru/docs/support/payments/onboarding/integration-sber
[protocol_spec]: https://yoomoney.ru/i/forms/yc-program-interface-api-sberbank.pdf
[sberbank_api_url]: https://securepayments.sberbank.ru/wiki/doku.php/integration:api:start
[sberbank_test_cards]: https://securepayments.sberbank.ru/wiki/doku.php/test_cards
