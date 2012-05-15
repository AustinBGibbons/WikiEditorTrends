#!/bin/bash

echo "Generate categories for all pages"
./build-category-hierarchy.py skos_categories_en.nt categories.sql > page_cats.map

