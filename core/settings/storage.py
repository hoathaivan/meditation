# import os
# from pathlib import Path
# import environ
# 
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# 
# # URL that handles the media served from MEDIA_ROOT, use for get images
# MEDIA_URL = '/images/'
# 
# # Local
# # URL to use when referring to static files located in STATIC_ROOT.refer to static folder
# # đường dẫn khi sử dụng static file .../static/...
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# 
# 
# # STATICFILES_DIRS = [
# #     os.path.join(BASE_DIR, 'static')
# # ]
# 
# # user upload file to
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/')
# # absolute path to the directory where collectstatic will collect static
# # file for deployment
# 
# # comment for deployment
# env = environ.Env()
# environ.Env.read_env()
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
# 
# # AWS
# AWS_LOCATION = 'static'
# 
# # AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# # AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# # AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# 
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# 
# # Boto 3
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
# # STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
