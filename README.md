
## Feature:
- users registration can be done by:
  - google account
  - email and confirmd by email link
  - user namd and password
- profile for each user
- blog > can be published by own/users
- event > can be published by own/users
- shop > display only now
- users can RSVP/cancel the attending to the event

## further dev:

- [ ] build CICD pipeline for ease of future development
  - find a better way to pass env variables rather than manually
  - write test for all units.
- [ ] taking paymeng function for shop
- [ ] upgrade css/looking
- [ ] let user to comment below the blog
- [ ] periodiclly auto backup database.

## answers need to find:
- switch DEBUG to false 
- best practise to load staitc/media file form s3 bucket


---
#### bcbc v1 was deployed by aws EC2 manually previously
#### bcbc v2 current version is deployed by aws EC2 elatstic beanstalk, independent RDS of postgres database and s3 bucket storing static/media file.
#### For v2, initial deploement as below for record, in case for rebuild in the future:
- bring the repo
- eb init
- eb create
- eb deploy
  it will auto create superuser: (default: admin@admin.com + 123)
- configure env variables in console configuration:
  - AWS_ACCESS_KEY_ID
  - AWS_S3_REGION_NAME
  - AWS_SECRET_ACCESS_KEY
  - AWS_STORAGE_BUCKET_NAME
  - DS_DB_NAME
  - RDS_USERNAME
  - RDS_PASSWORD
  - RDS_HOSTNAME
  - RDS_PORT
  - EMAIL_HOST
  - EMAIL_HOST_USER
  - EMAIL_HOST_PASSWORD
  - RECIPIENT_ADDRESS
  - GIT_TOKEN
  - USE_S3='True'
  - SE_RDS='True'

- add ssl: 
  - create license aws ACM for the domain
  - create aws route53 let it namage the DNS instead of godaddy. changing there nameservers to aws.   
    https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-beanstalk-environment.html#routing-to-beanstalk-environment-create-alias-procedure
    - NS record for aws 4 value 
    - A record to connect EB url
    - CNMA record to connect ACM license

- add listner/loadbalancer:
  https://testdriven.io/blog/django-elastic-beanstalk/#modify-the-load-balancer-to-serve-https
  - config listener in code 
    - change ALLOWED_HOSTS (add webwites also managed ec2 ip)
    - add listener in aws config
      - 443 port.
      - https
      - attach license
    - config apache ssl_rewrite.conf

- after deploy: may need to add ALLOED_HOST for the eb-EC2 IP 

- for google oauth:
  setup google oauth -> GCP console -> APIs and services -> set credential
  go admin page.
  - sites -> delete exaple -> add site ++http://127.0.0.1:8000++http://127.0.0.1:8000
  - social application-> add: provider

## Takeaways:
divide static/media/DB
- static: less change image/css/js files.
- media: user upload ones.

- STATIC_URL/MEDIA_URL: the paths the django gonne scan for collection
- STATICFILES_DIRS: after scanning everywhere, looking this path for the extra static files
- STATIC_ROOT/MEDIA_ROOT: destination path where to put the collections for serving the web.

- to backup the database: 
```python manage.py dumpdata > backup.json```
- to load the data:
```python manage.py loaddata backup.json```
- even for a empty db without superuser. it can all be moved to.but need to remember to migrate before moving.
- to reset db: 
```python manage.py dbshell> ```: ```DROP SCHEMA public CASCADE;CREATE SCHEMA public;```
- django_site table: site_id is created whenever creating a new site
- socialaccount_socialapp_sites is the cross table connect the django_site. site_id to the social_site_id
- for init db without any data input. table would not created for the render. 
  so we need to run following command after the init migrate. to avoid the bug:
  ```python migrate --run-syncdb```

## For further management of eb:

- always work with use_s3 off. rds off for dev stage

- before deploy
  - dumpdata to backup prod database
  - check static file, delete waste ones
  - pip freeze

- be careful social application credential is shared when dump/load the data, can apply the partial dump/load to avoid it

