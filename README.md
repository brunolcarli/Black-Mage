# API Server

`Under development`

## Installing and Running (Development)

Step-by-Step

First clone this repository to your local machine.

Change your directory to the `core` folder inside the project.

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


