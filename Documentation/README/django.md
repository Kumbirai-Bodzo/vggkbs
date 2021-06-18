python3 manage.py collectstatic

python3 manage.py createsuperuser

python3 manage.py collectstatic

manage.py dumpdata --output dump.json
manage.py loaddata dump.json

manage.py runserver 192.168.43.9:8000

# Squash migrations

manage.py squashmigrations Accommodation <squashfrom> <squashto>
manage.py squashmigrations Adventure
manage.py squashmigrations app
manage.py squashmigrations app

# backend data backup

    python3 manage.py dumpdata --output dump.json
    python3 manage.py loaddata dump.json

echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@gmail.com', 'root')" | python manage.py shell
