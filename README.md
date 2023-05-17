# Portfolio optimization using the Black-Litterman model

### Установка
Для работы проекта необходим docker, инструкция по установке: https://docs.docker.com/desktop/
```shell
git clone git@github.com:hipokratus1/Kursach.git
```
### Использование
#### Создание docker образа
```shell
docker build -t portfolio_optimize .
```
#### Запуск контейнера 
```shell 
docker run -it --rm --name portfolio_optimize_container portfolio_optimize
```
#### Рекомендации по использованию
Вся работа с оптимизацией происходит в рамках запущенного контейнера

Пожалуйста, задавайте названия криптовалют заглавными буквами, как это делается на бирже [messari](https://messari.io), например: BTC, ETH

