# Playerok Universal
Современный бот-помощник для Playerok 🤖🟦

## 🧭 Навигация:
- [Функционал бота](#-функционал)
- [Установка бота](#%EF%B8%8F-установка)
- [Полезные ссылки](#-полезные-ссылки)
- [Для разработчиков](#-для-разработчиков)

## ⚡ Функционал
- Система модулей
- Удобный Telegram бот для настройки бота (используется aiogram 3.10.0)
- Базовый функционал:
  - Вечный онлайн на сайте
  - Автоматическое поднятия предметов после их покупки
  - Приветственное сообщение
  - Возможность добавления пользовательских команд
  - Возможность добавления пользовательской авто-выдачи на предметы
  - Команда `!продавец` для вызова продавца (уведомляет вас в Telegram боте, что покупателю требуется помощь)
- Прочий мелкий функционал:
  - Добавление/удаление/редактирование водяного знака под сообщениями ботов
  - Возможность читать/не читать чат перед отправкой сообщения
  
и др.

## ⬇️ Установка
1. Скачайте последнюю Release версию и распакуйте в любое удобное для вас место
2. Убедитесь, что у вас установлен **Python версии 3.x.x - 3.12**. Если не установлен, сделайте это, перейдя по ссылке https://www.python.org/downloads (при установке нажмите на пункт `Add to PATH`)
3. Откройте `install_requirements.bat` и дождитесь установки всех необходимых для работы библиотек, а после закройте окно
4. Чтобы запустить бота, откройте запускатор `start.bat`
5. После первого запуска вас попросят настроить бота для работы

## 📚 Для разработчиков

Модульная система помогает внедрять в бота дополнительный функционал, сделанный энтузиастами. По сути, это же, что и плагины, но в более удобном формате.

<details>
  <summary><strong>📌 Основные ивенты</strong></summary>

  ### Ивенты бота (BOT_EVENT_HANDLERS)

  Ивенты, которые выполняются при определённом действии бота.

  | Ивент | Когда вызывается | Передающиеся аргументы |
  |-------|------------------|------------------------|
  | `ON_MODULE_CONNECTED` | При подключении модуля | `Module` |
  | `ON_INIT` | При инициализации бота | `-` |
  | `ON_PLAYEROK_BOT_INIT` | При инициализации (запуске) Playerok бота | `PlayerokBot` |
  | `ON_TELEGRAM_BOT_INIT` | При инициализации (запуске) Telegram бота | `TelegramBot` |

  ### Ивенты Playerok (PLAYEROK_EVENT_HANDLERS)

  Ивенты, которые выполняются при получении ивента в слушателе событий в Playerok боте.

  | Ивент | Когда вызывается | Передающиеся аргументы |
  |-------|------------------|------------------------|
  | `EventTypes.CHAT_INITIALIZED` | Чат инициализирован | `PlayerokBot`, `ChatInitializedEvent` |
  | `EventTypes.NEW_MESSAGE` | Новое сообщение в чате | `PlayerokBot`, `NewMessageEvent` |
  | `EventTypes.NEW_DEAL` | Создана новая сделка (когда покупатель оплатил товар) | `PlayerokBot`, `NewDealEvent` |
  | `EventTypes.DEAL_CONFIRMED` | Сделка подтверждена | `PlayerokBot`, `DealConfirmedEvent` |
  | `EventTypes.DEAL_ROLLED_BACK` | Продавец оформил возврат сделки | `PlayerokBot`, `DealRolledBackEvent` |
  | `EventTypes.DEAL_HAS_PROBLEM` | Пользователь сообщил о проблеме в сделке | `PlayerokBot`, `DealHasProblemEvent` |
  | `EventTypes.DEAL_PROBLEM_RESOLVED` | Проблема в сделке решена | `PlayerokBot`, `DealProblemResolvedEvent` |
  | `EventTypes.DEAL_STATUS_CHANGED` | Статус сделки изменён | `PlayerokBot`, `DealStatusChangedEvent` |
  | `EventTypes.ITEM_PAID` | Пользователь оплатил предмет | `PlayerokBot`, `ItemPaidEvent` |
  | `EventTypes.ITEM_SENT` | Предмет отправлен (продавец подтвердил выполнение сделки) | `PlayerokBot`, `ItemSentEvent` |

</details>

<details>
  <summary><strong>📁 Строение модуля</strong></summary>  
  
  </br>Модуль - это папка, внутри которой находятся важные компоненты.

  Строение модуля может быть абсолютно любым на ваше усмотрение, но всё же в каждом модуля должен быть обязательный файл инициализации **`__init__.py`**, в котором задаются все основные параметры для корректной
  работы модуля.

  Обязательные константы хендлеров:
  | Константа | Тип | Описание |
  |-----------|-----|----------|
  | `BOT_EVENT_HANDLERS` | `dict[str, list[Any]]` | В этом словаре задаются хендлеры ивентов бота |
  | `PLAYEROK_EVENT_HANDLERS` | `dict[EventTypes, list[Any]` | В этом словаре задаются хендлеры ивентов Playerok |
  | `TELEGRAM_BOT_ROUTERS` | `list[Router]` | В этом массиве задаются роутеры модульного Telegram бота  |

  Обязательные константы метаданных:
  | Константа | Тип | Описание |
  |-----------|-----|----------|
  | `PREFIX` | `str` | Префикс |
  | `VERSION` | `str` | Версия |
  | `NAME` | `str` | Название |
  | `DESCRIPTION` | `str` | Описание |
  | `AUTHORS` | `str` | Авторы |
  | `LINKS` | `str` | Ссылки на авторов |

  Также, если модуль требует дополнительных зависимостей, в нём должен быть файл зависимостей **requirements.txt**, которые будут сами скачиваться при загрузке всех модулей бота.

  #### 🔧 Пример содержимого:
  Обратите внимание, что метаданные были вынесены в отдельный файл `meta.py`, но импортируются в `__init__.py`.
  Это сделано для избежания конфликтов импорта в дальнейшей части кода модуля.

  **`meta.py`**:
  ```python
  from colorama import Fore, Style

  PREFIX = f"{Fore.LIGHTCYAN_EX}[test module]{Fore.WHITE}"
  VERSION = "0.1"
  NAME = "test_module"
  DESCRIPTION = "Тестовый модуль. /test_module в Telegram боте для управления"
  AUTHORS = "@alleexxeeyy"
  LINKS = "https://t.me/alleexxeeyy, https://t.me/alexeyproduction"
  ```

  **`__init__.py`**:
  ```python
  from .plbot.playerokbot_handlers import PlayerokBotHandlers
  from .tgbot.telegrambot_handlers import TelegramBotHandlers
  from .tgbot import router
  from .meta import *
  from playerokapi.listener.events import EventTypes
  from core.modules_manager import disable_module, Module
  
  _module: Module = None
  def get_module(module: Module):
      global _module
      _module = module
  
  def handler_on_init():
      try:
          # ...
          print(f"{PREFIX} Модуль инициализирован")
      except:
          disable_module(_module.uuid)
  
  BOT_EVENT_HANDLERS = {
      "ON_MODULE_CONNECTED": [handle_on_module_connected],
      "ON_INIT": [handler_on_init],
      "ON_PLAYEROK_BOT_INIT": [PlayerokBotHandlers.handler_on_playerok_bot_init],
      "ON_TELEGRAM_BOT_INIT": [TelegramBotHandlers.handler_on_telegram_bot_init]
  }
  PLAYEROK_EVENT_HANDLERS = {
      EventTypes.NEW_MESSAGE: [PlayerokBotHandlers.handler_new_message],
      EventTypes.NEW_DEAL: [PlayerokBotHandlers.handler_new_deal],
      # ...
  }
  TELEGRAM_BOT_ROUTERS = [router]
  ```

</details>

<details>
  <summary><strong>❗ Примечания</strong></summary>

  </br>Функционал Telegram бота написан на библиотеке aiogram 3, система внедрения пользовательского функционала Telegram бота работает на основе роутеров, которые сливаются с основным, главным роутером бота.
  И так, как они сливаются воедино, могут возникнуть осложнения, если, например Callback данные имеют идентичное название. Поэтому, после написания функционала Telegram бота для модуля, лучше переименуйте
  эти данные уникальным образом, чтобы они не совпадали с названиями основного бота или дополнительных подключаемых модулей.

</details>


## 🔗 Полезные ссылки
- Разработчик: https://github.com/alleexxeeyy (в профиле есть актуальные ссылки на все контакты для связи)
- Telegram канал: https://t.me/alexeyproduction
- Telegram бот для покупки официальных модулей: https://t.me/alexey_production_bot
