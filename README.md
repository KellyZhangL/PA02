# PA02: tracker.py and the Transaction class
## CS103a Spring 22

This git repository is for team 31's finance tracker, which includes a Python class Category to store financial transactions inside a SQL table, features to navigate and interact with the financial transactions in tracker.py, pytest tests for testing the features in test_category.py.

## Running Pylint
```bash
echo "pylint category.py
    pylint tracker.py"
````

## How to Run 
```python3 tracker.py```

This will pull up the Transaction Menu: <br>

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu


## How to Test with PyTest
```
pytest -v -m simple
pytest -v -m add
pytest -v -m delete
pytest -v -m update
```

## How to Lint with PyLint
```
pylint category.py
pylint tracker.py
pylint test_category.py
```
