# learning_systemctl

## Зависимости

Проект требует ноды (url-адресс сервера, через который провайдер будет брать последние блоки).
Указать в .env (В КОРНЕ ПРОЕКТА)
Переменная должна называться NODE_URL

## Запуск проекта
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requerments.txt
python main.py
```
## Суть проекта
Проект, показывающий последний блок в Etherium
