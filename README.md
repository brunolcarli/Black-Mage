<table align="center"><tr><td align="center" width="9999">
<img src="https://thumbs.gfycat.com/IdioticRepulsiveBorer-size_restricted.gif" align="center" width="80" height="80" alt="Project icon">

# Black Mage API

![Generic badge](https://img.shields.io/badge/version-0.0.1-silver.svg)

[![Generic badge](https://img.shields.io/badge/read_the_docs-Wiki-blue.svg)](https://github.com/brunolcarli/Black-Mage/wiki)

> "Although ill-suited for wielding weapons, Black Mages easily bend destructive black magic spells to their will." ~ Dawn of Souls instructions

API Server
</td></tr></table>

<hr />

## Black Mage (API Server)


[Black Mage](https://finalfantasy.fandom.com/wiki/Black_Mage_(Final_Fantasy)) is a [API](https://en.wikipedia.org/wiki/Application_programming_interface) server which handles data for a future social network.


## Installing and Running (Development)

Clone this repository to your local machine.

Make sure your in a activated virtual env, if not familiar with virtualenvs take a look
at [this article](https://docs.python-guide.org/dev/virtualenvs/).

## Install the system requirements with the command:

```
$ make install
```

## Migrate the database:

```
$ make migrate
```

#### Then finnaly, run the service with:

```
$ make run
```

The system will be disponible at `localhost:8000/graphql/`

# Docker



 <table align="center"><tr><td align="center" width="9999">

<img src="https://maraaverick.rbind.io/banners/nyan_docker_whale_gfycat.gif" align="center" width="140" height="80" alt="Project icon">


</td></tr></table>

Make sure you have `docker-compose` installed. If you dont just run:

## Install docker dependency

```
$ pip install docker-compose
```

or within a virtualenv run the requirements installation:

```
$ make install
```

## Build the container:

```
$ docker-compose build
```

Run the service:

```
$ docker-compose up
```


# Dev Demo

A demo version for development access is available [here](https://black-mage-devel--brunolcarli.repl.co/graphql/)!
