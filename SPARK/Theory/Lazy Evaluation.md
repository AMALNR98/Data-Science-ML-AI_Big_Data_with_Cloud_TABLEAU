Lazy evaluation in Spark (with PySpark, the Python API for Spark) follows the same principles as in other Spark APIs. In Spark, transformations on RDDs or DataFrames are not immediately executed. Instead, they are recorded and only executed when an action is called. This allows Spark to optimize the execution plan and perform computations more efficiently.

Here's a brief overview of how lazy evaluation works in PySpark:

1. **Transformations:** When you perform a transformation on an RDD or DataFrame in PySpark, such as `map`, `filter`, or `groupBy`, Spark does not immediately execute the operation. Instead, it builds up a logical execution plan, recording the transformations applied to the data.

    ```python
    from pyspark.sql import SparkSession

    # Create a Theory session
    spark = SparkSession.builder.appName("LazyEvaluationExample").getOrCreate()

    # Read a CSV file into a DataFrame (transformation)
    df = spark.read.csv("example.csv", header=True, inferSchema=True)

    # Apply transformations (lazy evaluation)
    filtered_df = df.filter(df["age"] > 21)
    mapped_df = filtered_df.select("name", "age")

    # No computation has happened yet
    ```

2. **Actions:** Actions are operations that trigger the execution of the transformations and produce a result. Common actions include `count`, `collect`, and `show`. When an action is called, Spark optimizes the execution plan and computes the result.

    ```python
    # Perform actions (lazy evaluation is triggered)
    result_count = mapped_df.count()
    result_collect = mapped_df.collect()

    # Now the transformations are executed
    ```

3. **Optimizations:** Spark leverages the logical execution plan and performs optimizations, such as pipelining transformations and pruning unnecessary computations. This helps in minimizing the amount of data shuffled between nodes in the cluster.

    ```python
    # Further transformations and actions
    final_result = mapped_df.groupBy("age").agg({"name": "count"}).collect()

    # Lazy evaluation is still in effect until an action is called
    ```

Lazy evaluation is a key feature in Spark that contributes to its performance and efficiency. It allows Spark to optimize the computation plan and execute only the necessary operations, reducing unnecessary computations and improving overall performance. Keep in mind that while lazy evaluation can lead to performance benefits, it's essential to be aware of when actions are triggered to manage the execution flow effectively.