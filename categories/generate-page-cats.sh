#!/bin/bash

echo "Generate categories for all pages"
./category_mapper.py skos_categories_en.nt categories.sql | sort | ./category_reducer.py > page_cats

