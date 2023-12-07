- Spark is a Bigdata tool used for Data processing
- Like Hadoop, we can't store data, we can only process data
- **Definition** : Lightweight cluster designed for fast bigdata processing

---

- HDFS
  - is a heavyweight cluster it needs the following components
    - Map reducing
      - Job Tracker
      - Task Tracker
    - components
      - Name node: Store metadata
      - Data Node: Store actual data
      - Secondary Name node : backup data
---
- There are many components in spark, but unlike Hadoop, we don't need all components at a time
- Spark 100 times faster than Hadoop (Because `In-memory computation`)
- Features of Sparks:
  1. Light weigh cluster
  2. Speed (in-memory computation)
  3. Re-usability: can work on batch-produced data and real time data
  4. Advanced Analysis: Visualization, machine learning
  5. Lazy evaluation
  6. Fault Tolerance: Recover data when loss
  7. Polyglot: can work on multiple programming languages (scala, python, java, R)

---
- ***Lazy Evaluation***
  - Data structure (convert given data to spark data structure)
    1. RDD : Resilient Distributed Dataset  
       - RDD has two types of operations
         1. Action 
         2. Transformation
    2. Data frame
---
- ***Spark Components***
  1. Spark core
     - Engine of spark
     - convert incoming data to RDD or dataframe
  2. Spark SQL
     - For processing Structured(to dataframe) or semi-structure data
  3. Spark streaming
     - Used for Real time data
  4. Spark mlib
     - For perform machine learning
  5. Spark graphx
     - For visualization
- Spark libraries
  1. Spark SQL
  2. Spark streaming
  3. Spark mlib
  4. spark graphx