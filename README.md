<h1 align="center" style="font-size:42px;font-weight:700;vertical-align:middle;">
	<img src="https://raw.githubusercontent.com/gocream-labs/.github/master/branding/logo.png" alt="GoCream Labs" width="auto" height="42px" style="height:42px;vertical-align:middle;" />
	×
	<img src="https://raw.githubusercontent.com/gocream-labs/pysberbank/master/logo.svg" alt="sber" width="auto" height="42px" style="height:42px;vertical-align:middle;" />
</h1>

<p align="center">
	<a href="https://pypi.org/project/gocream-pysberbank">
		<img src="https://img.shields.io/pypi/status/gocream-pysberbank.svg" alt="PyPI - Status" />
	</a>
	<a href="https://pypi.org/project/gocream-pysberbank">
		<img src="https://img.shields.io/pypi/v/gocream-pysberbank.svg" alt="PyPI - Version" />
	</a>
	<a href="https://pypi.org/project/gocream-pysberbank">
		<img src="https://img.shields.io/pypi/dm/gocream-pysberbank.svg" alt="PyPI - Downloads" />
	</a>
	<a href="https://pypi.org/project/gocream-pysberbank">
		<img src="https://img.shields.io/pypi/pyversions/gocream-pysberbank.svg" alt="PyPI - Python Version" />
	</a>
</p>
<p align="center">
	<a href="https://github.com/gocream-labs/pysberbank/actions/workflows/ci.yml" >
		<img src="https://img.shields.io/github/actions/workflow/status/gocream-labs/pysberbank/ci.yml?branch=master&logo=github&label=tests" alt="Tests - Running" />
	</a>
	<a href="https://codecov.io/gh/gocream-labs/pysberbank" >
		<img src="https://img.shields.io/codecov/c/github/gocream-labs/pysberbank?logo=codecov&logoColor=white&label=coverage" alt="Coverage" />
	</a>
</p>
<p align="center">
	<a href="https://github.com/pypa/hatch" target="_blank">
		<img src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg" alt="Hatch project" />
	</a>
	<a href="https://gitmoji.dev" target="_blank">
		<img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg" alt="Gitmoji" />
	</a>
	<a href="https://squidfunk.github.io/mkdocs-material/" target="_blank">
		<img src="https://img.shields.io/badge/-Material_for_MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white&labelColor=gray" alt="Built with Material for MkDocs" />
	</a>
	<a href="https://github.com/astral-sh/ruff" target="_blank">
		<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="linting - Ruff" />
	</a>
	<a href="https://raw.githubusercontent.com/gocream-labs/pysberbank/master/LICENSE" target="_blank">
		<img src="https://img.shields.io/pypi/l/gocream-pysberbank" alt="License - Mozilla Public License Version 2.0" />
	</a>
</p>

<p align="center">
	<b>Documentation: <a href="https://gocream-labs.github.io/pysberbank/">gocream-labs.github.io/pysberbank</a></b>
</p>

Python-клиент для [унаследованного API СберБанка][api_url], который ЮKassa сохраняет для компаний, перешедших из Сбера. Это не клиент для современного API ЮKassa.

Описание протокола - [инструкция ЮKassa][protocol_spec].

Архивные материалы СберБанка - [документация API][sberbank_api_url] и [тестовые карты][sberbank_test_cards].


## Installation

Требуется Python 3.10 или новее.

```sh
pip install gocream-pysberbank
```

Для предварительных версий используйте `pip install --pre gocream-pysberbank`.

```python
from gocream_pysberbank import SberbankClient
from gocream_pysberbank.constants import DESCRIPTION_BY_ACTION_CODE
```

Для совместимости с прежним API сохранены имена `Sberbank` и
`SberbankPaymentApi`.


## Quick Start

```python
from gocream_pysberbank import SberbankClient

client = SberbankClient(
    username="merchant-api",
    password="password-from-secret-storage",
    url="https://gateway.example/payment/{api_type}/{method}",
)
```

Замените URL адресом шлюза из настроек вашего подключения. Если `url` не передан, используется исторический адрес `https://3dsec.sberbank.ru/payment/{api_type}/{method}`. Вместо пары `username`/`password` можно передать `token`.

Клиент предоставляет методы `register`, `reverse`, `refund`, `order_status` и `order_status_extended`. Параметры `**kwargs` передаются в Requests; это не произвольные параметры платёжного API. По умолчанию timeout равен `(3, 27)` секундам на соединение и чтение.

При переходе со старого пакета замените импорты `pysberbank` на `gocream_pysberbank`, включая пути моков и имя логгера.


## Documentation

- **API Reference**: [Client](https://gocream-labs.github.io/pysberbank/next/reference/), [Payments](https://gocream-labs.github.io/pysberbank/next/reference/payments/), [Order Status](https://gocream-labs.github.io/pysberbank/next/reference/status/), [Exceptions](https://gocream-labs.github.io/pysberbank/next/reference/exceptions/), [Constants](https://gocream-labs.github.io/pysberbank/next/reference/constants/).
- **Project**: [Known Issues](https://gocream-labs.github.io/pysberbank/next/known-issues/), [Roadmap](https://gocream-labs.github.io/pysberbank/next/roadmap/), [Changelog](https://gocream-labs.github.io/pysberbank/next/changelog/).
- **Development**: [Contributing](https://gocream-labs.github.io/pysberbank/next/contributing/), [Releasing](https://gocream-labs.github.io/pysberbank/next/releasing/).


[api_url]: https://yookassa.ru/docs/support/payments/onboarding/integration-sber
[protocol_spec]: https://yoomoney.ru/i/forms/yc-program-interface-api-sberbank.pdf
[sberbank_api_url]: https://securepayments.sberbank.ru/wiki/doku.php/integration:api:start
[sberbank_test_cards]: https://securepayments.sberbank.ru/wiki/doku.php/test_cards
