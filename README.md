# Installation

Görev -> README.md dosyasında containerize edilmiş uygulamanın nasıl build alınacağı ve
nasıl çalıştırılacağı belirtilmelidir.

## Installation
```bash
git clone https://github.com/mcanozkulekci/Bestcloudforme.git
```

Building Image
```bash
$ sudo docker build -t <IMAGE NAME> .
```

Running Container
```bash
$ sudo docker run --name <CONTAINER NAME> --env URL_WHOOK=<DUMMY WHOOK> -p <DESIRED PORT>:5000 -d <IMAGE NAME>
```


## For POST Request into Webhook.site

```
curl --header "Content-Type: application/json" --request POST --data '{"firstname":"mehmetcan","lastname":"ozkulekci"}' http://localhost:<DESIRED PORT>/alert
```
