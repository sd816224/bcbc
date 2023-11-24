bcbc was deployed by aws EC2 previously
this repo is for deployments of aws elatstic beanstalk, independent RDS of postgres database and s3 bucket storing static file.

step as follow:

- eb init

- as we use custom user admin,
  comment out admin.site.urls and django.contrib.admin. run the migrations to setup init db

- eb create
- eb deploy
- configure 14 env variables:
  AWS_ACCESS_KEY_ID
  AWS_S3_REGION_NAME
  AWS_SECRET_ACCESS_KEY
  AWS_STORAGE_BUCKET_NAME
  DS_DB_NAME
  RDS_USERNAME
  RDS_PASSWORD
  RDS_HOSTNAME
  RDS_PORT
  EMAIL_HOST
  EMAIL_HOST_USER
  EMAIL_HOST_PASSWORD
  RECIPIENT_ADDRESS
  GIT_TOKEN

- uncomment and eb deploy
  auto create superuser: ++admin@admin.com ++123
  change the password in the eb url

create aws route53: change godaddy nameservers to aws.  
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-beanstalk-environment.html#routing-to-beanstalk-environment-create-alias-procedure

create license aws ACM: create records in route 53

set load balancer in eb console for 443 port https attached with license

config listener.
https://testdriven.io/blog/django-elastic-beanstalk/#modify-the-load-balancer-to-serve-https
1: change ALLOWED_HOSTS (add webwites also managed ec2 ip)
2: config apache in aws config
3: config apache ssl_rewrite.conf
