from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-nk$v9_^w+8lfb*6%))45h0ov8qs_82ib%4#dx2(o12)(op6+br'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'tinymce',
    'azbankgateways',

    'account.apps.AccountConfig',
    'post.apps.PostConfig',
    'course.apps.CourseConfig',
    'category.apps.CategoryConfig',
    'base.apps.BaseConfig',
]

TINYMCE_DEFAULT_CONFIG = {
    "height": "600px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code quickbars"
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "en_US",
}

TINYMCE_SPELLCHECKER = True

AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        'IDPAY': {
            'MERCHANT_CODE': 'c8bdf78e-5e36-404e-943a-6252efe969f2',
            'METHOD': 'POST',  # GET or POST
            'X_SANDBOX': 1,  # 0 disable, 1 active
        },
    },
    'IS_SAMPLE_FORM_ENABLE': False,  # اختیاری و پیش فرض غیر فعال است
    'DEFAULT': 'IDPAY',
    'CURRENCY': 'IRR',  # اختیاری
    'TRACKING_CODE_QUERY_PARAM': 'tc',  # اختیاری
    'TRACKING_CODE_LENGTH': 16,  # اختیاری
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader',  # اختیاری
    'BANK_PRIORITIES': [
        # and so on ...
    ],  # اختیاری
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/db.sqlite3/',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'account.User'

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
