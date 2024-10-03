# build_files.sh
pip install -r requirements.txt  # Install dependencies
python3.9 manage.py collectstatic --noinput  # Collect static files
