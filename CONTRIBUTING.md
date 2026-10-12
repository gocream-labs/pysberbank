# Contributing

Раздел описывает работу над библиотекой: настройку окружения, проверки, документацию, ветки и оформление pull request. Выпуск и публикация версий описаны отдельно в [Releasing](https://gocream-labs.github.io/pysberbank/next/releasing/).

Общий порядок работы:

1. Создайте рабочую ветку от актуальной `next`.
2. Внесите небольшое, законченное изменение и добавьте тесты для изменённого поведения.
3. Запустите подходящие локальные проверки.
4. Оформите коммиты в формате gitmoji со скоупом.
5. Отправьте pull request в `next` и дождитесь CI и review.


## Local Setup

Окружениями управляет [Hatch](https://hatch.pypa.io/). Зависимости из `pyproject.toml` устанавливаются при первом запуске команды.

Тесты и dev-окружение используют Python 3.10, линтер, документация и релизные инструменты - Python 3.14.

Из корня репозитория выполните:

```sh
hatch run init
```

Команда настраивает `git blame` через `.git-blame-ignore-revs` и устанавливает хуки: pre-commit запускает Ruff для файлов библиотеки и `pyproject.toml`, commit-msg проверяет заголовки через gitlint. Форматирование и тесты проверяйте отдельно. `hatch run remove` отменяет настройку.


## Checks

| Command | Purpose |
|---|---|
| `hatch run test:check` | Тесты с покрытием на Python 3.10 |
| `hatch run mtest:check` | Матрица Python × Requests с отчётом `coverage.xml` для каждого прогона |
| `hatch run lint:check` | Статический анализ Ruff |
| `hatch run lint:fmt-check` | Проверка форматирования без изменения файлов |
| `hatch run lint:format` | Автоисправление Ruff и форматирование |
| `hatch build --clean` | Чистая сборка sdist и wheel |
| `hatch run package:check` | Строгая проверка метаданных готовых дистрибутивов через Twine |

Матрица проверяет Requests 2.34.2 на Python 3.10-3.14 и Requests 2.28.2 на Python 3.10-3.11. Для одного сочетания используйте `hatch run mtest.py3.10-2.28.2:check`. Локальные прогоны перезаписывают `coverage.xml`, в CI каждый отчёт отдельно отправляется в Codecov.

Начинайте с тестов изменённого компонента, затем запускайте затронутый набор. Например, для подготовки параметров запроса:

```sh
hatch run test:check tests/request_data.py -q
```

Сетевые обращения в тестах блокирует `pytest-socket`. Подменяйте HTTP-ответы моками. Регрессионные тесты должны воспроизводить ошибку и проверять результат, а тесты сериализации - фактически переданные HTTP-параметры.

Для небольшого изменения ограничивайте автоформатирование конкретными файлами:

```sh
hatch run lint:format tests/request_data.py
```

Перед `package:check` выполните `hatch build --clean`: проверка читает готовые дистрибутивы из `dist/`.


## Documentation

Документация собирается через MkDocs Material. Навигация описана в `docs/SUMMARY.md`, справочник API генерируется из docstring с помощью mkdocstrings.

| Command | Purpose |
|---|---|
| `hatch run docs:build` | Строгая сборка сайта в `site/` |
| `hatch run docs:links` | Проверка внутренних ссылок уже собранного сайта |
| `hatch run docs:serve` | Локальный сервер с обновлением при изменении исходников |
| `hatch run docs:versions` | Список опубликованных версий документации |
| `hatch run docs:links-external` | Отдельная сетевая проверка опубликованного сайта и внешних ссылок |

После изменения навигации, ссылок или API-справочника запускайте `docs:build`, затем `docs:links`. Публикация сайта описана в [Releasing](https://gocream-labs.github.io/pysberbank/next/releasing/#documentation).

Главная страница включает `README.md`. Roadmap, Changelog и Contributing связаны символическими ссылками с корневыми файлами. Редактируйте `ROADMAP.md`, `CHANGELOG.md` и `CONTRIBUTING.md`, сохраняя ссылки: дата изменения на сайте берётся из Git-истории исходника.

Заголовки и меню пишите на английском, основной текст - на русском. Описание API храните в docstring на русском в [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings). Для перекрёстных ссылок используйте полные пути mkdocstrings, например `[SberbankClient][gocream_pysberbank.http.SberbankClient]`.


## Branches

Основные ветки:

- `next` - разработка, RC-релизы и документация `next`;
- `master` - стабильные релизы.

После создания `next` в удалённом репозитории рабочую ветку можно подготовить так:

```sh
git fetch origin
git switch next
git pull --ff-only
git switch -c codex/request-parameters
```

Имя рабочей ветки должно кратко описывать изменение. Из неё можно вручную выпустить beta. Для stable-релиза создайте PR в `master`. Предварительные beta и RC необязательны.

После stable-релиза синхронизируйте `master` обратно в `next`, включая release-коммит и тег.


## Commits

Заголовок состоит из emoji-маркера [gitmoji](https://gitmoji.dev/), скоупа и краткого описания на английском:

```text
🐛 (client): Preserve zero request parameters
🔇 (client): Remove sensitive request logging
✨ (client): Add API method
🎨 (style): Format code
```

Скоуп обозначает затронутую область, например `client`, `tests`, `docs` или `project`. При необходимости в теле коммита поясните причину изменения и последствия для совместимости.

`💥` повышает major, `✨` - minor. Поддерживаемые исправления и конфигурационные изменения повышают patch. `🎨`, `🧪` и `📄` попадают в changelog без повышения версии. Полные списки находятся в `[tool.semantic_release.commit_parser_options]` в `pyproject.toml`.

Python Semantic Release определяет повышение версии по маркеру. При squash merge итоговое сообщение должно сохранять этот формат. Добавление маркера описано в [Releasing](https://gocream-labs.github.io/pysberbank/next/releasing/#versioning).

Версию и `CHANGELOG.md` обновляет релизный workflow по коммитам. В обычном PR их менять не нужно. Для локальной проверки:

| Command | Purpose |
|---|---|
| `hatch run release:preview` | Показать следующую версию для текущей ветки без изменения файлов |
| `hatch run release:beta-preview` | Показать следующую beta-версию без изменения файлов |
| `hatch run release:changelog` | Сгенерировать и записать `CHANGELOG.md` локально для проверки содержимого и шаблонов |

Команды ничего не публикуют и не создают коммитов или тегов. Расчёт учитывает закоммиченные изменения и локальные теги `v{version}`. Перед проверкой загрузите историю и теги командой `git fetch origin --tags`.

`release:changelog` записывает файл. Просмотрите результат через `git diff -- CHANGELOG.md` и не коммитьте предварительный Unreleased как историю выпущенной версии.


## Pull Requests

Перед отправкой PR:

1. Добавьте или обновите тесты изменённого поведения.
2. Запустите подходящие проверки из [Checks](#checks), а при изменении структуры документации и ссылок - из [Documentation](#documentation).
3. Уберите посторонние изменения из diff и выполните `git diff --check`.
4. Опишите проблему, итоговое поведение и выполненные проверки.
5. Отдельно отметьте изменения публичных сигнатур, исключений, формата ответов или совместимости с потребителями.

Дождитесь успешного CI и review. Существующие ошибки вне задачи отмечайте отдельно, не ослабляя тесты и проверки.

Один PR должен решать одну задачу. Для релизного PR в `master` дополнительно следуйте [Releasing](https://gocream-labs.github.io/pysberbank/next/releasing/).
