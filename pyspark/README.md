Based on the provided notes on Spark DataFrames, PySpark, and Spark SQL, here is a comprehensive, structured explanation of the concepts covered in the document:

---

Markdown
# PySpark & Spark SQL Study Material & Cheat Sheet

This repository contains comprehensive notes, code snippets, and key concepts for working with **Apache Spark**, **PySpark DataFrames**, and **Spark SQL**.

---

## Table of Contents
- [1. Filtering Data](#1-filtering-data)
- [2. Spark SQL Views](#2-spark-sql-views)
- [3. Selecting & Renaming Columns](#3-selecting--renaming-columns)
- [4. Dropping Columns & Duplicates](#4-dropping-columns--duplicates)
- [5. Sorting Data & Null Handling](#5-sorting-data--null-handling)
- [6. Aggregations & GroupBy](#6-aggregations--groupby)
- [7. Joins in PySpark](#7-joins-in-pyspark)
- [8. Reading & Writing Data](#8-reading--writing-data)
- [9. Transformations, Actions & Performance Tuning](#9-transformations-actions--performance-tuning)

---

## 1. Filtering Data from DataFrames

You can filter DataFrames using either `.filter()` or `.where()`. Both functions perform the same operation and can be written using **NoSQL (Pythonic/Column object API)** syntax or **SQL string** syntax.

### Syntax Options:

* **NoSQL / Pythonic Way:** Uses DataFrame column objects like `df.age` or `col('age')`.


* **SQL Way:** Passes raw SQL condition strings like `'age > 3'`.



### Examples:

```python
# NoSQL / Pythonic Way
from pyspark.sql.functions import col

user_df.filter(col('id') == 1).show()[cite: 1]
user_df.where(df['id'] == 1).show()[cite: 1]
user_df.filter(df.age > 3).show()[cite: 1]

# SQL Way (passed as a string)
user_df.filter("id = 1").show()[cite: 1]
user_df.where('is_customer = "true"').show()[cite: 1]

```

### Filtering Operations & Operators:

| Operation | NoSQL (PySpark API) | SQL String |
| --- | --- | --- |
| **Equal** | `==`<br> | `=`<br> |
| **Not Equal** | `!=`<br> | `!=` or `<>` |
| **Comparison** | `>`, `<`, `>=`, `<=`<br> | `>`, `<`, `>=`, `<=`<br> |
| **In List** | `.isin('Delhi', 'Noida')`<br> | `IN ('Delhi', 'Noida')`<br> |
| **Between** | `col('amount').between(850, 900)`<br> | `amount BETWEEN 850 AND 900`<br> |
| **Null Checks** | `.isNull()`, `.isNotNull()`<br> | `IS NULL`, `IS NOT NULL`<br> |
| **Boolean AND** | `&` (Conditions must be in `()`)

 | `AND`<br> |
| **Boolean OR** | `|` (Conditions must be in `()`)

 | `OR`<br> |
| **Boolean NOT** | `~` | `NOT` |

> **Note on Boolean Values & Dates:**
> * Boolean string conversions (like passing `'true'` as a string) undergo implicit conversion.
> 
> 
> * Date conditions must be passed as strings (e.g., `'2022-01-21'`) in both NoSQL and SQL syntax.
> 
> 
> 
> 

---

## 2. Views in Spark SQL

Views allow you to execute SQL queries directly against DataFrames:

1. **Local Temporary View:**
* Created using `user_df.createOrReplaceTempView('users')`.


* Lifetime is **limited to the specific Spark Session**.




2. **Global Temporary View:**
* Created using `createOrReplaceGlobalTempView('user')`.


* Lifetime spans the entire **Spark Application** across multiple sessions.





```python
# Querying via SQL
user_df.createOrReplaceTempView('users')[cite: 1]
spark.sql("SELECT * FROM users WHERE id = 1").show()[cite: 1]

```

---

## 3. Selecting and Renaming Columns

### Selecting Columns:

* `df.select('id', 'name')` — Using strings


* `df.select(['id', 'name'])` — Using a Python list of strings


* `df.select(col('id'), col('name'))` — Using the `col()` function


* `df.select(df['id'])` or `df.select(df.id)` — Using DataFrame attribute reference



### Advanced Selection with `selectExpr`:

Allows you to write SQL-like expression strings and SQL functions inside the DataFrame API:

```python
df.selectExpr("id", "fname", "lname", "concat(fname, ' ', lname) AS full_name").show()[cite: 1]

```

### Renaming & Adding Columns:

* **`withColumnRenamed('old_name', 'new_name')`:** Best for renaming a single column at a time.


* **`withColumn('new_col', expression)`:** Used to add a new derived column, apply transformations, or change data types.


* **`toDF(*cols)`:** Renames all columns in a DataFrame at once by passing a new list of column names.



---

## 4. Dropping Columns & Duplicate Records

### Dropping Columns:

* **Single Column:** `df.drop('id')`, `df.drop(df['id'])`, or `df.drop(col('id'))`

* **Multiple Columns:** Must be passed as individual string arguments (e.g., `df.drop('id', 'name')`) or unpacked from a list `df.drop(*list)`. (Passing column objects like `col()` for multiple drops will fail).



### Dropping Duplicates:

* **`df.distinct()`:** Removes duplicates based on **all** columns.


* **`df.dropDuplicates(['col1', 'col2'])`:** Removes duplicates based on a specific subset of columns.



### Handling Null Values (`dropna`):

* `df.dropna()` or `df.na.drop()`

* `how='any'` (drops row if any column is null) or `how='all'` (drops row only if all columns are null).


* `thresh=2`: Drops rows having fewer than 2 non-null values.


* `subset=['col1']`: Restricts null checks to specified columns.



---

## 5. Sorting Data & Null Handling

Sorting can be done via `df.sort()` or `df.orderBy()`:

### Ascending / Descending Order:

* `df.sort(col('id').asc())` or `df.sort(col('id').desc())`

* `df.sort(['c1', 'c2'], ascending=[True, False])`


### Controlling Null Positions During Sorting:

* `.asc_nulls_first()` / `.asc_nulls_last()`

* `.desc_nulls_first()` / `.desc_nulls_last()`


```python
df.sort(df['id'].asc_nulls_last())[cite: 1]

```

---

## 6. Aggregations and GroupBy

Aggregations compute metrics like `count()`, `sum()`, `min()`, `max()`, `avg()`, and `stddev()`.

### Direct / Standalone Aggregations:

```python
df.select(count("*")).show()[cite: 1]
df.count()  # Action: Triggers immediate execution[cite: 1]

```

### GroupBy Aggregations:

```python
# Grouping followed by direct aggregate function
df.groupBy("status").avg().show()[cite: 1]

# Grouping using the .agg() method (supports aliasing and multiple functions)
from pyspark.sql.functions import sum, round, min

df.groupBy("status").agg(
    round(sum("amount"), 2).alias("total_amount"),
    min("age")
).show()[cite: 1]

```

---

## 7. Joins in PySpark

### Join Types:

Supported types include `'inner'`, `'left'`, `'right'`, `'full'` / `'outer'`, and `'cross'`.

### Syntax Examples:

```python
# Single join key with same name
df1.join(df2, 'name', 'inner')[cite: 1]

# Multiple join keys
df1.join(df2, ['name', 'age'], 'left')[cite: 1]

# Conditional join keys with explicit column matching
df1.join(df2, (df1.id == df2.user_id) & (df1.age == df2.user_age), 'right')[cite: 1]

```

### Broadcast Join:

* Broadcasts smaller datasets (< 10MB by default) to all worker nodes to avoid expensive data shuffling across the network.


* Controlled by `spark.sql.autoBroadcastJoinThreshold`.



---

## 8. Reading and Writing Data

### Reading Files:

```python
# CSV with Schema & Options
df = spark.read.option("header", True).option("inferSchema", True).csv("path")[cite: 1]

# JSON & Parquet
df = spark.read.json("path")[cite: 1]
df = spark.read.parquet("path")[cite: 1]

```

### Save / Write Modes:

* `append`: Adds contents to the destination.


* `overwrite`: Overwrites existing data.


* `error` / `errorifexists`: Throws an exception if data already exists.


* `ignore`: Silently ignores write if files exist.



### Coalesce vs Repartition:

* **`coalesce(n)`:** Reduces the number of partitions **without shuffling data** (combines local partitions). Cannot increase partition count.


* **`repartition(n)`:** Reshuffles data across the network to increase or decrease the number of partitions evenly.



### Partitioning Output:

```python
df.write.partitionBy("city").parquet("output_path")[cite: 1]

```

---

## 9. Transformations vs Actions & Performance Optimization

### Transformations (Lazy Evaluation):

Transformations build a Directed Acyclic Graph (DAG) and do not execute immediately.

* **Narrow Transformations:** Work on individual partitions independently without data shuffling (e.g., `select`, `filter`, `withColumn`, `drop`).


* **Wide Transformations:** Require shuffling data across multiple partitions/nodes (e.g., `groupBy`, `join`, `distinct`, `repartition`).



### Actions:

Actions trigger computation and return results to the driver or write output to storage (e.g., `count()`, `collect()`, `take()`, `write`).

### Adaptive Query Execution (AQE):

Introduced in Spark 3.0 (`spark.sql.adaptive.enabled = true`), AQE optimizes queries dynamically at runtime based on intermediate stage statistics:

1. **Dynamic Coalescing:** Combines small shuffle partitions automatically.


2. **Dynamic Join Switching:** Switches Sort-Merge Join to Broadcast Hash Join if runtime dataset size is small enough.


3. **Dynamic Skew Join Optimization:** Handles data skew by splitting large skewed partitions automatically.



### Caching and Persistence:

* **`cache()`:** Stores the DataFrame in memory using default storage level (`MEMORY_AND_DISK`).


* **`persist(StorageLevel)`:** Offers granular control over storage level (e.g., `MEMORY_ONLY`, `MEMORY_ONLY_SER`, `DISK_ONLY`).


* **`unpersist()`:** Clears cached data from memory/disk.