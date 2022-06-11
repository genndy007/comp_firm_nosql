# Computer Firm NoSQL

## What is it?       

This application uses MongoDB and PyMongo engine to interact with collections. Collections are Customers 
and Suppliers. Application has a wrapper for a collection type and gives comfortable API to interact with Mongo.

## Installation for developer
```shell
pip install poetry   # package manager
poetry install       # install dependencies
poetry shell         # shell with deps
githooks             # activate hooks and lint-check
cp app/.env.example app/.env  # fill env file with mongodb credentials
```
