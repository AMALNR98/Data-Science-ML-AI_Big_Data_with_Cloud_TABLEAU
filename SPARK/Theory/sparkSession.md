`SparkSession` is the entry point for reading data, working with Spark SQL, and managing DataFrame and SQL functionality in Apache Spark. It provides a unified interface for working with Spark, incorporating the functionality previously provided by `SparkContext`, `SQLContext`, and `HiveContext`.

Here's how you typically create a `SparkSession` in PySpark:

```python
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()
```

You can set various configuration options using the `config` method on the `SparkSession.builder`. The `appName` method is used to set a name for your Spark application.

### Example Usage:

Once you have a `SparkSession`, you can use it for various operations, such as reading data, creating DataFrames, and executing SQL queries. Here's a simple example:

```python
# Create a DataFrame from a list of tuples
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Perform a simple transformation
df_transformed = df.withColumn("AgeAfter5Years", df["Age"] + 5)

# Show the transformed DataFrame
df_transformed.show()

# Execute a SQL query
df.createOrReplaceTempView("people")
result = spark.sql("SELECT * FROM people WHERE Age > 30")
result.show()
```

### Stopping SparkSession:

After you finish your Spark tasks, it's good practice to stop the `SparkSession` to release resources:

```python
# Stop the SparkSession
spark.stop()
```

Using `SparkSession` provides a more user-friendly and powerful interface compared to the older `SparkContext` and `SQLContext`. It integrates SQL, DataFrames, and Datasets seamlessly and is the recommended way of interacting with Spark, especially in applications involving structured data.