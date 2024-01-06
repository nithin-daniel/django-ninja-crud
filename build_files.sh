echo "BUILD START"
python3.9 -m pip install -r requirements.txt
# Apply database migrations
echo "Applying database migrations"
python3.9 manage.py migrate
echo "Done all database migrations"
echo "BUILD END"