<table align="center"><tr><td align="center" width="9999">
<img src="https://thumbs.gfycat.com/IdioticRepulsiveBorer-size_restricted.gif" align="center" width="80" height="80" alt="Project icon">

# Black Mage API

[![Generic badge](https://img.shields.io/badge/docs-yellow.svg)](https://gitlab.com/civil-cultural/black-mage/wikis/home)

> "Although ill-suited for wielding weapons, Black Mages easily bend destructive black magic spells to their will."

> ~ Dawn of Souls instructions

API Server
</td></tr></table>

<hr />

## Black Mage (API Server)


[Black Mage](https://finalfantasy.fandom.com/wiki/Black_Mage_(Final_Fantasy)) é o servidor [API](https://en.wikipedia.org/wiki/Application_programming_interface) que disponibilizará acesso aos dados para a plataforma do sistema Civil-Cultural. Inicilamente englibando o serviços básicos e posteriormente desacoplando-se para atuar como gateway de acesso aos serviços. 



## Installing and Running (Development)

Clone this repository to your local machine.

Make sure your in a activated virtual env, if not familiar with virtualenvs take a look
at [this article](https://docs.python-guide.org/dev/virtualenvs/).

#### Install the system requirements with the command:

```
make install
```

#### Migrate the database:

```
make migrate
```

#### Then finnaly, run the service with:

```
make run
```

The system will be disponible at `localhost:8000/graphql/`


# Dev Demo

A demo version for development access is available [here](https://black-mage-devel--brunolcarli.repl.co/graphql/)!