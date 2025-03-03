DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWD = "password"
DB_NAME = "news"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWD,
        'HOST': DB_HOST,
        'PORT': DB_PORT
    }
}

ALLOW_TAGS = ["国内", "国际", "社会", "体育", "娱乐", "军事", "科技", "财经", "股市", "美股"]

