# automatic-search-for-links-in-a-file
Automatic Search for Links in a File — утилита для автоматического поиска HTTP/HTTPS‑ссылок в файлах. Сканирует отдельные файлы и директории, извлекает ссылки с привязкой к пути и строке. Результаты выдаёт в виде списка, txt файле . Подходит для аудита, контроля актуальности ссылок и подготовки данных к анализу.

# README: Automatic Search for Links in a File / Автоматический поиск ссылок в файле

## 🇬🇧 English version

### Overview

Automatic Search for Links in a File is a lightweight command-line utility designed to scan files and directories for HTTP/HTTPS URLs. It extracts links along with contextual metadata (file path, line number) and exports the results in multiple formats.

The tool is suitable for auditing documentation, maintaining link inventories, validating external references, and preparing data for further analysis. Its modular design allows easy extension for new file formats, output types, or additional processing logic.

### Key Features

- **URL detection**: regex-based extraction with strict validation for `http://` and `https://` schemes.
- **Multi-format support**: works with `.txt`, `.md`, `.html`, `.json`, and `.yaml` files; parses string values in structured formats.
- **Directory scanning**: recursive traversal of folders to process entire project trees.
- **Flexible output**: results can be exported as a plain list, CSV, or JSON with metadata.
- **CLI interface**: simple, intuitive commands for quick integration into workflows and pipelines.
- **Contextual data**: each found link includes the source file path and line number for easy verification.

### Installation

To install the project dependencies, run:

```bash
pip install -r requirements.txt

🇷🇺 Русская версия
Обзор
«Автоматический поиск ссылок в файле» — лёгкая утилита командной строки для поиска HTTP/HTTPS‑ссылок в файлах и директориях. Она извлекает найденные ссылки вместе с контекстными метаданными (путь к файлу, номер строки) и экспортирует результаты в нескольких форматах.

Инструмент подходит для аудита документации, ведения реестров ссылок, проверки внешних ссылок и подготовки данных к анализу. Модульная архитектура позволяет легко добавлять поддержку новых форматов файлов, типов вывода или дополнительной логики обработки.

Основные возможности
Поиск URL: извлечение ссылок на основе регулярных выражений с проверкой схем http:// и https://.

Поддержка разных форматов: работает с файлами .txt, .md, .html, .json и .yaml; в структурированных форматах ищет ссылки внутри строковых значений.

Сканирование директорий: рекурсивный обход папок для обработки целых деревьев проектов.

Гибкий вывод: результаты можно экспортировать как простой список, CSV или JSON с метаданными.

Интерфейс командной строки: простые и понятные команды для быстрой интеграции в рабочие процессы и пайплайны.

Контекстные данные: для каждой найденной ссылки указывается путь к файлу и номер строки — это упрощает проверку и работу с результатами.
