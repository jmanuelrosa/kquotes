#!/bin/bash

# For postgresql
echo "-> Remove kquotes DB"
dropdb kquotes
echo "-> Create kquotes DB"
createdb kquotes
echo "-> Create DB tables"
python manage.py migrate

#echo "-> Generate sample data"
#python manage.py sampledata --traceback

