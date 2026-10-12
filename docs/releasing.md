# Releasing

Релизы выполняются через GitHub Actions и Python Semantic Release 10.7.0, по образцу pycdek. Версия, changelog, Git-тег, GitHub Release и публикация пакета формируются автоматически.


## Release Flow

| Channel | Source | Trigger |
|---|---|---|
| Beta | Рабочая ветка, кроме `master` и `next` | Ручной запуск Prerelease |
| RC | `next` | Push или merge |
| Stable | `master` | Push или merge |

В pull request запускается CI. Changelog обновляется при выпуске, а не отдельным коммитом в PR. Stable создаёт release-коммит с версией и changelog; beta и RC меняют эти файлы только в рабочем каталоге сборки, тег остаётся на исходном коммите. Поэтому для prerelease используйте wheel и sdist из PyPI или приложений GitHub Release: автоматически созданный архив Source code содержит исходную версию.

Для RC обязательна успешная матрица тестов и проверка совместимости. Ручная beta, как в pycdek, пропускает CI: сначала выполните проверки самостоятельно. Stable полагается на обязательные проверки PR перед merge; запущенный после него CI для `master` не блокирует публикацию.


## Initial Setup

До первого выпуска необходимо:

1. Отправить в GitHub конфигурацию, исходники и существующие теги `v0.1.x`, сохранив их исходные коммиты.
2. Создать ветку `next` от согласованного состояния разработки. Ручные workflows доступны после добавления файлов в default branch.
3. Включить обязательные проверки PR в ruleset `master`: Test (3.10-3.14), Compatibility (Python 3.10 / Requests 2.28.2), Build package, Lint и Documentation. До их успешного завершения релиз не готов.
4. Создать GitHub environment `pypi` и настроить PyPI Trusted Publishing для проекта `gocream-pysberbank`, owner `gocream-labs`, repository `pysberbank`, environment `pypi`. Нужны publishers для `release.yml` и `prerelease.yml`. Если проекта ещё нет, сначала создайте pending publisher для первого выпуска, затем добавьте второй.
5. Установить GitHub App с `Contents: Read and write`, разрешить ему bypass ruleset `master` для release-коммитов. Сохранить Client ID в Actions variable `RELEASE_APP_CLIENT_ID`, private key - в Actions secret `RELEASE_APP_PRIVATE_KEY`.
6. Выбрать GitHub Pages source: Deploy from a branch, `gh-pages`, `/ (root)`. Ветку создаёт первый deploy Mike. При необходимости добавить `CODECOV_TOKEN` для загрузки покрытия.

Локальные файлы не создают эти настройки внешних сервисов. Ключи и токены не хранятся в репозитории.


## Versioning

Сохраняется исторический формат тегов `v{version}`: `v0.1.9`, `v1.0.0-b.1`, `v1.0.0-rc.1`, `v1.0.0`. Python нормализует prerelease-версию в метаданных, например `1.0.0b1`.

PSR рассчитывает версию по Git-тегам и сообщениям коммитов, а не по текущему значению `__version__`. При добавлении автоматизации в исходниках стоит `2.0.0-b.1`, но последний локальный тег - `v0.1.9`. Само это значение не задаёт старт новой серии 2.x. Перед первым выпуском необходимо согласовать целевой номер и проверить preview; нельзя создавать фиктивный тег уже опубликованного релиза только ради нужного номера. Старые теги не переименовываются.

Уровни gitmoji описаны в [Commits](contributing.md#commits). При добавлении маркера обновляйте его уровень, `allowed_tags` и `SECTION_TITLES` в шаблоне. Здесь дополнительно поддерживается существующий маркер `🔇` для исправления небезопасного логирования.

```sh
hatch run release:preview
hatch run release:beta-preview
```

Эти команды не изменяют файлы и не публикуют версии. Перед реальным выпуском синхронизируйте историю и теги с origin. При нескольких beta-ветках учитывайте общие уже опубликованные номера.


## Changelog

Файл обновляется в режиме `update` по шаблонам из `templates/`. Сохраняйте маркер `<!-- version list -->`: новые версии вставляются под ним, а прежняя история остаётся ниже. Раздел `0.1.7` сохранён из старого changelog.

Вручную новые записи и разделы Unreleased не добавляются. Содержательное описание исправления должно находиться в коммите. Команда `hatch run release:changelog` записывает changelog локально для проверки шаблонов; результат предварительной генерации не нужно коммитить как историю выпущенной версии.


## Publishing

Для beta отправьте рабочую ветку на GitHub и выберите её в Actions → Prerelease → Run workflow. Push в `next` выпускает RC после тестов. Для stable создайте PR в `master`, дождитесь обязательных проверок и выполните merge. Затем синхронизируйте `master` обратно в `next`.

Публикация PyPI и GitHub Release использует один комплект артефактов и выполняется независимыми jobs. При ошибке публикации повторяйте соответствующие упавшие jobs; создание нового тега не исправляет незавершённую публикацию прежней версии.


## Documentation

MkDocs Material собирает страницы и API-справочник; Mike сохраняет версии сайта. Успешные тесты в `next` разрешают deploy версии `next`, а stable публикует `major.minor` с алиасом `latest`. Beta документацию не публикует. До первого stable корень сайта может возвращать 404: версия `next` доступна по своему пути.

```sh
hatch run docs:build
hatch run docs:links
hatch run docs:serve
hatch run docs:versions
hatch run docs:serve-versions
hatch run docs:links-external
```

CI выполняет строгую сборку и проверку внутренних ссылок. Проверка внешних ссылок запускается отдельно вручную.


## Verification

После выпуска проверьте успешные publication jobs, версию в PyPI, GitHub Release и тег, соответствие wheel/sdist выбранной версии и доступность документации. Первый запуск требует отдельно проверить настройки GitHub App, branch rules, Trusted Publishers и Pages.
