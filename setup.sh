sudo pip3 install virtualenv
virtualenv -p python3 envs
source envs/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
