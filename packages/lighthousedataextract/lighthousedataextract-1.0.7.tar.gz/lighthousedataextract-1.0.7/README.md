# LightHouse Data Extract

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

This tool  parses the google lighthouse json data, accepts a csv file for categories of the URLs and returns 4  pandas DataFrames for metrics, opportunities, diagnostics and resources.

## Install

```python
pip install lighthousedataextract 
```

## Import 

```python
from lighthousedataextract import LightHouseDataExtract
```

## Create a report variable

If json files are in directory ./repprt/lighthouse/ and you don't want to give an input file for categories of URLs

```python
report = LightHouseDataExtract() 
```

If your json files are in another directory

```python
report = LightHouseDataExtract(
    path_to_json="./data/lighthouse/report/lighthouse/"
)
```

If you want to seperate URLs in categories

Your CSV of URLs should have two columns, without headers. Below you can see  an example:

|                                 |                  |
|---------------------------------|------------------|
| https://www.example.com/             | Home Page        |
| https://www.example.com/categories/category-1    | Middle Tail |
| https://www.example.com/products/product-1234 | Long Tail     |

```python
report = LightHouseDataExtract(url_category_file="./data/lighthouse/category.csv")
```

## Create a lighthouse metrics DataFrame


```python
from lighthousedataextract import LightHouseDataExtract

report = LightHouseDataExtract(
    path_to_json="./data/lighthouse/report/lighthouse/",
    url_category_file="./data/lighthouse/category.csv",
)
df_lh_perf_metrics = report.df_lh_perf_metrics()
df_lh_perf_metrics.set_index("url").T
```


## Create other DataFrames
```python
df_opportunities = report.df_opportunities()
display(df_opportunities)
df_diagnostics = report.df_diagnostics()
display(df_diagnostics)
df_resources = report.df_resources()
display(df_resources)
```
## If json files are obtained by gooogle pagespeed insights api then

```python
api_report = LightHouseDataExtract(from_api=True)
``` 
