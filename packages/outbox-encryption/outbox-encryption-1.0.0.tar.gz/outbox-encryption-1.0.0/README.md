# DJANGO OUTBOX ENCRYPTION
--------------------------

Use For Encrypt Environment Variable and Other Encryption Purpose.


#####

Install to your environment :
    > pip install outbox-encryption

How to use :
------------
    This code for create .env.client file

    Test using python shell :
    > python manage.py shell

    Encryption Process :
    > from encryption import OutboxEncryption
    > lib = OutboxEncryption()
    > mplaint_text = {
            'DB_PASSWORD': '',
            'SECRET_KEY': 'xxg_7me8rl2m#a_h2oresgt2#ni=3_4*!ai*=rtsq)yi!g7_5-51xx'
        }
    > lib.encrypt_environ('.env.local', mplaint_text)
    > print('Show Hidden File to Show .env.local')  # file .env.local is created


    Decryption Process :
    Run inside settings.py (django project settings)            
    > lib.set_keyword_local('env_outbox_encrypt')   # this is use for local environment, env_outbox_encrypt only exists in local, not in server
    > mplaint_key = list(mplaint_text.keys())   # List of key variable that must be encrypt decrypt before set or get data
    > mplaint_list = ['ALLOWED_HOSTS']    # variable that must be cast as list from environmnet to settings.py
    > mplaint_tuple = ['SECURE_PROXY_SSL_HEADER']   # variable that must be casr 
    as tuple from environment to settings.py

    # mplaint_list and mplaint_tuple is optional
    > lib.decrypt_environ(mplaint_key, mplaint_list, mplaint_tuple)

    
    # Inside settings.py
    > from encryption import OutboxEncryption
    > mplaint_key = ['DB_PASSWORD', 'SECRET_KEY']
    > mplaint_list = ['ALLOWED_HOSTS']
    > mplaint_tuple = ['SECURE_PROXY_SSL_HEADER']

    > dict1 = lib.decrypt_environ(mplaint_key, mplaint_list, mplaint_tuple)
    > DEBUG = dict1['DEBUG']
    > UNDER_CONSTRUCTION = dict1['UNDER_CONSTRUCTION']
    > DEBUG = dict1['DEBUG']
    > SECRET_KEY = dict1['SECRET_KEY']
    > ALLOWED_HOSTS = dict1['ALLOWED_HOSTS']
    > DATABASES = {
        'default': {
            'ENGINE'    : dict1['DB_ENGINE'],
            'NAME'      : dict1['DB_NAME'],
            'USER'      : dict1['DB_USER'],
            'PASSWORD'  : dict1['DB_PASSWORD'],
            'HOST'      : dict1['DB_HOSTS'],
            'PORT'      : dict1['DB_POST'],
        }
    > SECURE_PROXY_SSL_HEADER = dict1['SECURE_PROXY_SSL_HEADER']
}