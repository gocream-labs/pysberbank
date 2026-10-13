# Known Issues

Ограничения текущей реализации, которые необходимо учитывать до выпуска. План исправлений находится в [Roadmap](roadmap.md).


## Response Handling

- Код успеха сравнивается со строкой `"0"`; числовой `0` обрабатывается как ошибка.
- Проверяется только ключ `errorCode`, вариант `ErrorCode` не учитывается.
- HTTP-статус сам по себе не вызывает исключение: ответ HTTP 500 с пустым JSON-объектом может быть возвращён как результат.
- JSON-массив или ошибка без поля `errorMessage` могут приводить к `AttributeError` и `KeyError`.

Эти ограничения относятся к HTTP-обработке всех методов [клиента][gocream_pysberbank.http.SberbankClient].


## Compatibility

- [SberbankRequestException][gocream_pysberbank.errors.SberbankRequestException] наследует [BaseSberbankException][gocream_pysberbank.errors.BaseSberbankException], но не [SberbankException][gocream_pysberbank.errors.SberbankException]. Подробнее в [Exceptions](reference/exceptions.md).
- В [order_status_extended][gocream_pysberbank.http.SberbankClient.order_status_extended] сохранён неиспользуемый аргумент `anguage`; его удаление затронет позиционные вызовы.


## Development Checks

В существующем `test_register` HTTP-мок ожидает словарь вместо JSON-строки. Ручной `tests.suite()` ссылается на два имени тестов без префикса `test_`. Эти ошибки тестов и накопленные замечания Ruff исправляются отдельно от организации документации.
