# Bottle Storage Server

This is a minimal _HTTP API_ (_work in progress_) that allows you
to make use of _Google Cloud Storage_.

So far it only stores `json` and `files`.

To make use of this in your local environment you should have a
`gcloud_key.json` which you can generate from the Cloud Console.

Also you need to set the appreciate environment variables specified at
`example.env`.

_Suggestion:_ Copy `example.env` to `.env`, and then overwrite the values
in that file.

This project can be deployed as a _Google Cloud Run_ service.

## Development Instructions

First you should clone the repository with the `git clone <project-url>` command.

Make sure you have `python39` and `pipenv` installed on your system.

> to install `pipenv` execute `pip install pipenv`

Before running any python programs you should make sure you have the appropriate 
environment variables set in your `.env` file.

You can get started by copying `example.env` to `.env`, and then you should
overwrite the values at the `.env`.

 - `APP_SECRET`, the application secret used for encrypting data.
 - `STORAGE_METHOD` values should be `LOCAL` or `GCLOUD` depending what kind of
 file storage method you want to use. `LOCAL` for local file system and `GCLOUD` for
 google cloud storage.
 - `STORAGE_DIR` the directory where to store the files generated by the `api` in case you use `LOCAL` in `STORAGE_METHOD`.
 - `GCLOUD_BUCKET` the bucket where to store the files generated by the `api` in case you use `GCLOUD` in `STORAGE_METHOD`.
 - `CORS_DOMAINS`, is a list of comma separated valued needed to know which origins you should accept when you are required to enforce `CORS`.
 - `DATABASE_TYPE`, this value accepts `sqlite` or `postgresql`.
 - `DATABASE_NAME`, if you input `DATABASE_TYPE=sqlite`, then this variable is the path to the database file, if it's `postgresql`, then it's the actual name for the database to be used.
 - `DATABASE_USER`, this is required if you are using any database that is not `sqlite`.
 - `DATABASE_PASSWORD`, this is required if you are using any database that is not `sqlite`.
 - `DATABASE_HOST`, this is required if you are using any database that is not `sqlite`.
 - `DATABASE_PORT`, this is required if you are using any database that is not `sqlite`.

To enable the database for development we should first create a _migration_.

> Migrations are a collections of _pending_ alterations that we need to perform on the database
> in order to make it _compatible_ with the required database model used by our applications.

To perform a migration one can run `pipenv run migrate`, and this will create a new migration for the database targeted in the `.env` file.

> Migrations required that all your code can be _imported_ with no errors, so make your you don't have bad code at the moment of migration.

Once configure you should execute `pipenv install`, and if this was successful you can
go ahead an run `pipenv run start` which should run a `http` server powered by
`bottle.py` at `http://0.0.0.0:8080`.


# Contribute to the project

If you want to write a module that uses this project, please
name space every file in modules, routes, and docs.

Try and keep it to one file per directory.

If you are using storage, name pace your directories, and name space
your database tables manually and keep the database interface 
friendly.
