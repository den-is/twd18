#### To run "local" env
1. `cd project`
2. `docker build -t somename .`
3. `docker run -it --rm -P somename bash`
4. if needed:
  1. `./manage.py migrate`
  2. `./manage.py createsuperuser`
5. `./manage.py runserver 0.0.0.0:8000`

If you are using included rangodb.sqlite3, there are two included users. user/pass: `admin/admin` and `test/test`

#### To run "prod" env
Complete following steps in repository root, where location of docker-compose.yml is:
1. `docker-compose build                # to build project only`
2. or `docker-compose up --build        # to start project and build it`
3. or `docker-compose up                # to start already built project or will build and start it`
4. or `docker-compose up -d             # same as above, but will start in detached mode`
5. `docker-compose run app bash`
  1. `./manage.py migrate`
  2. `./manage.py collectstatic -v0 --noinput`
  3. `./manage.py createsuperuser`
6. `docker-compose logs -f              # view containers output, logs`
7. `docker-compose down --rmi all -v    # delete project, created images, volumes, networks`
