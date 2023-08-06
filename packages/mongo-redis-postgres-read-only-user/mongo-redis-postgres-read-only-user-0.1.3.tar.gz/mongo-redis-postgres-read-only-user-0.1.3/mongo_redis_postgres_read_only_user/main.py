import pymongo
import psycopg2
import redis
import typer

DATABASE_URI = ''
connection_status = False



# PostgreSQL


class PgReadAccessUser:
    def __init__(self, database_name):
        global connection_status
        try:
            connection_string = f'{DATABASE_URI}/{database_name}'
            self.conn = psycopg2.connect(connection_string)
            connection_status = True
        except Exception as e:
            typer.echo("Connection failed, " + str(e))

    def check_user_available(self, username):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"""SELECT rolname FROM pg_roles where rolname='{username}'""")
            username = cursor.fetchone()
            if username:
                return True
            return False
        except Exception as e:
            typer.echo("Error Occurred in check read user available, " + str(e))

    def grant_read_permission(self, username, database_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"""GRANT CONNECT ON DATABASE {database_name} TO """ + username)
            cursor.execute("""GRANT USAGE ON SCHEMA public TO """ + username)
            cursor.execute("""GRANT SELECT ON ALL TABLES IN SCHEMA public TO """ + username)
            cursor.execute("""GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO """ + username)
            cursor.execute("""ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO """ + username)
            self.conn.commit()
        except Exception as e:
            typer.echo("Exception occurred in grant read permission, " + str(e))

    def create_user(self, username, user_password):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """CREATE ROLE """ + username + f""" WITH LOGIN PASSWORD '{user_password}' NOSUPERUSER 
                INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION VALID UNTIL 'infinity';""")
            self.conn.commit()
        except Exception as e:
            typer.echo("User Creation failed,Error occurred in create read user, " + str(e))

    def get_all_databases(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT datname FROM pg_database WHERE datistemplate = false""")
            databases = []
            data = cursor.fetchall()
            for i in data:
                databases.append(str(i)[2:-3])
            return databases
        except Exception as e:
            typer.echo("Fetching all databases is failed, " + str(e))


# Redis


def create_read_only_user(database_uri, username, password):
    client = redis.from_url(database_uri)
    client.acl_setuser(username=username, passwords=[f"+{password}"], keys="*", commands=["+get", "-SADD"],
                         enabled=True)


# MongoDB


class MongoReadAccessUser:
    def __init__(self, database_uri):
        try:
            self.client = pymongo.MongoClient(database_uri)
        except Exception as e:
            typer.echo("Exception mongodb connection", str(e))

    def is_user_available(self, user):
        try:
            print("ok")
            for i in range(len(self.client.admin.command('usersInfo')['users'])):
                if self.client.admin.command('usersInfo')['users'][i]['user'] == user:
                    return True
            return False
        except Exception as e:
            typer.echo("Exception in is_user_available", str(e))

    def create_read_only_user(self, username, password):
        try:
            roles = []
            for i in self.client.list_database_names():
                roles.append({'role': 'read', 'db': i})
            self.client.admin.command("createUser", username, pwd=password, roles=roles)
        except Exception as e:
            typer.echo("Exception in create_read_only_user", str(e))

def detail():
    """
Script to create read user for Mongodb,PostgreSQL,Redis
    """

app = typer.Typer(callback=detail)
# Different commands of the scripts
@app.command()
def postgres(database_uri: str = typer.Option(..., "--uri",
                                              help="Database Connection URI for PostgreSQL"),
             username=typer.Option(..., "--username", "-u", help="User Name of the read user is to be created"),
             user_password=typer.Option(..., "--password", "-p", prompt="Password",confirmation_prompt=True, hide_input=True,
                                        help="Password of the read user is to be created")):
    """
    Command to create PostgreSQL read user\n
    python script.py postgres --uri postgres://USERNAME:PASSWORD@HOST:PORT -u USERNAME -p PASSWORD
    """
    try:
        global DATABASE_URI
        DATABASE_URI = database_uri
        read_access_user = PgReadAccessUser('postgres')
        if connection_status:
            if not read_access_user.check_user_available(username):
                read_access_user.create_user(username, user_password)
                databases = read_access_user.get_all_databases()
                for database_name in databases:
                    read_access_user = PgReadAccessUser(database_name)
                    read_access_user.grant_read_permission(username, database_name)
                typer.echo("Read User Created Successfully")
            else:
                typer.echo("User is already available")
    except Exception as e:
        typer.echo("Exception in create_read_user, " + str(e))


@app.command("redis")
def redisdb(database_uri=typer.Option(..., "--uri", help="Database Connection URI for Redis"),
          username=typer.Option(..., "--username", "-u", help="User Name of the read user is to be created"),
          password=typer.Option(..., "--password", "-p", prompt="Password",confirmation_prompt=True, hide_input=True,
                                help="Password of the read user is to be created")):
    """
    Command to create Redis read user \n
    python script.py redis --uri redis://USERNAME:PASSWORD@HOST:PORT -u USERNAME -p PASSWORD
    """
    try:
        create_read_only_user(database_uri, username, password)
    except Exception as e:
        typer.echo("Exception in redis, " + str(e))


@app.command()
def mongodb(database_uri=typer.Option(..., "--uri", help="Database Connection URI for Mongodb"),
            username=typer.Option(..., "--username", "-u", help="User Name of the read user is to be created"),
            password=typer.Option(..., "--password", "-p",prompt="Password",confirmation_prompt=True, hide_input=True, help="Password of the read user is to be created")):
    """
    Command to create MongoDB read user\n
    python script.py mongo --uri mongodb://USERNAME:PASSWORD@HOST:PORT -u USERNAME -p PASSWORD
    """
    try:
        mongo_read_access_user = MongoReadAccessUser(database_uri)
        if not mongo_read_access_user.is_user_available(username):
            mongo_read_access_user.create_read_only_user(username, password)
        else:
            typer.echo("User is already available")
    except Exception as e:
        typer.echo("Exception in Mongo, " + str(e))


app = typer.main.get_command(app)
app.params = [
    param
    for param in app.params
    if param.name != "show_completion" and param.name != "install_completion"
]

if __name__ == "__main__":
    app()
