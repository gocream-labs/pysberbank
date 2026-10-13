# Exceptions

Общий базовый класс исключений библиотеки - [BaseSberbankException][gocream_pysberbank.errors.BaseSberbankException]. Транспортное исключение [SberbankRequestException][gocream_pysberbank.errors.SberbankRequestException] не наследует [SberbankException][gocream_pysberbank.errors.SberbankException]; для общего обработчика используйте базовый класс.

Ограничения обработки ответов описаны в [Known Issues](../known-issues.md#response-handling).

::: gocream_pysberbank.errors
    options:
      show_if_no_docstring: true
