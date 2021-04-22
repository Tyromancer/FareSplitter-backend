## Project Proposal: FareSplitter - Backend

The default access address is 127.0.0.1. To switch to a domain name, you need to set the app.config['SERVER_NAME'] in blueprint.py (blueprint) and the subdomain='www' parameter of app.register_blueprint

The database used by the project is mysql. Please modify the database address in config.py, write your database, and release the seal of db.create_all() under DB_module.py to create a database table immediately

The default registration amount of each account is 0. You need to set the default registration amount under the Account category in DB_account.py. Modify init(self, accounts=None, money=0 (modify to the default user amount you want)):


TODO:

1. If a password is required, please add the password field under the Account class in DB_account.py and add the function of password verification in the login.

2. Add calculate the average cash of all the money