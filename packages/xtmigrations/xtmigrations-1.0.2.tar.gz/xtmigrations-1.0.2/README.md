# xtmigrations
Fast migration tool using python.  This supports Postgres-based Database Management Systems.

### Installation

Via pip (python 3+ supported)
> pip install xtmigrations

If you have virtualenv, make sure to run source ~/<virtualenv_folder/bin/activate to be able to have access to the "migrate" command

### To initialize a new migrations directory structure
Go to the desired folder (e.g. /Users/myuser/Projects/my_project/) where you want your "migrations" folder created
> migrate init

### Now go inside migrations/ folder
> cd migrations

###  Configure conf/db.cnf with your database settings (Note at this time we only support Postgres)
Once it is configure, try to run the following to check if the settings work
> migrate status

###  Apply the migration
> migrate up

###  Create a new migration (No need for quotes)
> migrate new my new migration
This will create a new migration SQL file under sql/ folder.

### Make sure to edit the migrations file.  There is a @Up and a @Down section

### To unapply a migration, run the following:
> migrate down


### Usage

> migrate <init | status | new <title> | up [number of migrations to apply] | down [number of migrations to unapply]
    
Note: [number of migrations to apply/unapply can be 0 which means "all"]
    
### We used to support MariaDB.  We are planning to bring back support to MariaDB.