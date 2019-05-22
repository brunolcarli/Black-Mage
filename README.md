| [![Generic badge](https://img.shields.io/badge/level-backend-black.svg)](https://shields.io/) | [![Generic badge](https://img.shields.io/badge/status-under_development-yellow.svg)](https://shields.io/) | [![Generic badge](https://img.shields.io/badge/progress-25%-blue.svg)](https://shields.io/) | 

# Black Mage (API Server)

> "Although ill-suited for wielding weapons, Black Mages easily bend destructive black magic spells to their will."

> ~ Dawn of Souls instructions

[Black Mage](https://finalfantasy.fandom.com/wiki/Black_Mage_(Final_Fantasy)) é o servidor [API](https://en.wikipedia.org/wiki/Application_programming_interface) que disponibilizará acesso aos dados para a plataforma do sistema Civil-Cultural.


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

# Docker



 <table align="center"><tr><td align="center" width="9999">
 
```
                    ##        .            
              ## ## ##       ==            
           ## ## ## ##      ===            
       /""""""""""""""""\___/ ===        
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
       \______ o          __/            
         \    \        __/             
          \____\______/                
```

# Sorry

The docker option is currently under development.
</td></tr></table>