import web

db_host = 'localhost'
db_name = 'acme_store_mvc'
db_user = ''
db_pw = ''

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )