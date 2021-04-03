# fb

###django commands used
*django-admin startproject fb*

*python manage.py runserver*

*python manage.py migrate*

*python manage.py makemigrations*

*python manage.py startapp blog*

*python manage.py createsuperuser*

*python manage.py sqlmigrate blog 0001*

<mark>author = models.ForeignKey(User, on_delete=models.CASCADE)</mark>
post.author.email

user.post_set

user.post_set.all()

user.post_set.create(title='Blog 3', content='Third Post Content!')