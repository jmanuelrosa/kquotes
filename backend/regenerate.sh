#!/bin/bash

# For postgresql
echo "-> Remove kquotes DB"
dropdb kquotes
echo "-> Create kquotes DB"
createdb kquotes

echo "-> Run syncdb"
python manage.py migrate
#echo "-> Generate sample data"
#python manage.py sample_data --traceback
