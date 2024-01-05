`SparkContext` is the entry point to any Spark functionality in Apache Spark. It serves as a connection to the Spark cluster and can be used to create RDDs (Resilient Distributed Datasets) and perform various operations on them. In the context of PySpark (Spark's Python API), `SparkContext` is often abbreviated as `sc`.

Here's a basic overview of using `SparkContext` in a PySpark application:

### Initializing SparkContext:

```python
from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "MyApp")
```

In the above example:

- `"local"` specifies that Spark will run in local mode, using a single machine.
- `"MyApp"` is the name of your Spark application.

### Performing Operations:

Once you have created a `SparkContext`, you can use it to perform various operations. For example:

```python
# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Perform operations on the RDD
result = rdd.map(lambda x: x * 2).collect()

# Print the result
print(result)
```

### Stopping SparkContext:

After you finish using Spark, it's essential to stop the `SparkContext` to release resources:

```python
# Stop the SparkContext
sc.stop()
```

**Note:** In modern versions of Spark, it's common to use the `SparkSession` instead of directly creating a `SparkContext`. The `SparkSession` provides a higher-level interface that includes DataFrame and SQL operations. If you're working with PySpark in a notebook or interactive environment, the `SparkSession` is usually created for you, and you can access it using `spark` (lowercase).

```python
from pyspark.sql import SparkSession

# Create a SparkSession (if not created already)
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Perform operations using SparkSession
# ...
```

Using `SparkSession` is often more convenient, especially when working with structured data using DataFrames and Spark SQL.