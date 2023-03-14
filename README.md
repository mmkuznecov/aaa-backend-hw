# Проверка выполнения задания
```bash
docker build -t ds-backend .
./run.sh
curl -v http://localhost:8080/readNumberById?id=10022
curl -v "http://localhost:8080/readArray?id=10022&id=9965"
```

# Репозиторий к семинару "Основы backend-разработки"

## Что нужно сделать перед семинаром?
#### Собрать проект на виртуалке
1. зайти на виртуалку и склонировать на нее склонировать этот репозиторий
2. выполнить команду `docker build -t ds-backend .`
3. запустить сервис командой `./run.sh`
4. открыть в браузере страничку *http://<vm_ip>:8080* и проверить, что выводится слово *"Hello"* 

#### Настроить VS Code для удаленного редактирования
1. установить VS Code на свою машину
2. установить в VS Code расширение "Remote - SSH" - [инструкция](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) (раздел "Getting started")
3. открыть проект в VS Code через Remote SSH

### Проверка выполнения задания

```bash
docker build -t ds-backend .
./run.sh
curl -v "http://localhost:8080/NumberByImageId?id=10022"
curl -v "http://localhost:8080/NumberByImageId?id=9965"
curl -v "http://localhost:8080/NumbersByImageIds?id=10022&id=9965"
curl -v "http://localhost:8080/NumbersByImageIds?id=9965&id=10022"
```

