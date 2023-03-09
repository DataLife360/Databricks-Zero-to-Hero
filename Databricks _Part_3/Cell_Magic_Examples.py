# Databricks notebook source
# MAGIC %md
# MAGIC # Cell Magic 
# MAGIC 
# MAGIC This is the example notebook used in Part 3 of Databricks Zero to Hero.

# COMMAND ----------

# MAGIC %md
# MAGIC # 1. Cell Magic Examples
# MAGIC 
# MAGIC This notebook gives examples of using code magic. 
# MAGIC 
# MAGIC Important: Don't include other code or comments in a cell magic cell, unless its switching a language. It will error.

# COMMAND ----------

# MAGIC %md 
# MAGIC # 2. Readme (%md)
# MAGIC 
# MAGIC Readmes follow the normal readme formatting rules. Below is a common way to do readmes. 
# MAGIC <br>
# MAGIC For a great readme formatting tool check out: https://readme.so/

# COMMAND ----------

# DBTITLE 0,Readme: Format Example
# MAGIC %md
# MAGIC ## Example Readme
# MAGIC 
# MAGIC 
# MAGIC ![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)
# MAGIC 
# MAGIC 
# MAGIC ## Heading 2
# MAGIC 
# MAGIC 
# MAGIC ### Heading 3
# MAGIC     
# MAGIC ### Links Example
# MAGIC 
# MAGIC [MIT](https://choosealicense.com/licenses/mit/)
# MAGIC  - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
# MAGIC  - [Awesome README](https://github.com/matiassingers/awesome-readme)
# MAGIC  - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

# COMMAND ----------

# DBTITLE 1,Readme:  KaTeX Math Formulas
# MAGIC %md 
# MAGIC 
# MAGIC 
# MAGIC \\(c = \\pm\\sqrt{a^2 + b^2} \\)
# MAGIC 
# MAGIC \\(A{_i}{_j}=B{_i}{_j}\\)
# MAGIC 
# MAGIC $$c = \\pm\\sqrt{a^2 + b^2}$$
# MAGIC 
# MAGIC \\[A{_i}{_j}=B{_i}{_j}\\]

# COMMAND ----------

# MAGIC %md 
# MAGIC # 3. Switching Languages
# MAGIC 
# MAGIC The following are examples of cell magic. The CSVs and tables do not exist with this repository.

# COMMAND ----------

# DBTITLE 1,Python Example
# MAGIC %python
# MAGIC df = spark.read.csv("/path/to/data.csv", header=True, inferSchema=True)
# MAGIC df = spark.read.json("/path/to/data.json")

# COMMAND ----------

# DBTITLE 1,SQL Example
# MAGIC %sql
# MAGIC SELECT
# MAGIC   id,
# MAGIC   name,
# MAGIC   age
# MAGIC FROM
# MAGIC   my_table;

# COMMAND ----------

# DBTITLE 1,Scala Example
# MAGIC %scala
# MAGIC val diamonds_with_wrong_schema = spark.read.format("csv")
# MAGIC   .option("header", "true")
# MAGIC   .schema(schema)
# MAGIC   .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

# COMMAND ----------

# DBTITLE 1,R Example
# MAGIC %r
# MAGIC # Install the readr package if it is not already installed
# MAGIC install.packages("readr")
# MAGIC 
# MAGIC # Load the readr package
# MAGIC library(readr)
# MAGIC 
# MAGIC # Read the CSV file into a data frame
# MAGIC df <- read.csv("/path/to/data.csv")

# COMMAND ----------

# MAGIC %md 
# MAGIC # 4. Pip Install (%pip)

# COMMAND ----------

# DBTITLE 1,Pip Install (%pip)
# MAGIC %pip install missingno

# COMMAND ----------

# PIP installs locally on the notebook environment. This does not install it to the cluster. The library will disappear once the cluster is turned off.

# COMMAND ----------

# DBTITLE 1,Shell Commands - One Line (%sh)
# MAGIC %md 
# MAGIC 
# MAGIC # 5. Shell Commands (%sh)
# MAGIC 
# MAGIC Lets you run: 
# MAGIC * One line Shell Commands 
# MAGIC * Two Line Shell Commands
# MAGIC 
# MAGIC *CMD12:*
# MAGIC * Returns a directory 
# MAGIC 
# MAGIC *CMD13:*
# MAGIC * This will create a new directory called my_directory, change into the directory, and create a new file called my_file.txt.

# COMMAND ----------

# DBTITLE 1,Shell Commands - One Line (%sh)
# MAGIC %sh
# MAGIC ls -l

# COMMAND ----------

# DBTITLE 1,Shell Commands - Two Lines (%sh)
# MAGIC %sh
# MAGIC mkdir my_directory; cd my_directory; touch my_file.txt
# MAGIC 
# MAGIC #This will create a new directory called my_directory, change into the directory, and create a new file called my_file.txt.

# COMMAND ----------

# MAGIC %md 
# MAGIC #6. DBFS Command

# COMMAND ----------

# DBTITLE 1,Databricks File Storage - DBFS Command (%fs)
# MAGIC %fs
# MAGIC ls /path/to/directory

# COMMAND ----------

# MAGIC %md 
# MAGIC # 6. Run Program %run
# MAGIC 
# MAGIC Lets you run: 
# MAGIC * Python, SQL, Scala, and R files 
# MAGIC * Databricks Notebook 
# MAGIC 
# MAGIC The cell will return the outputs of a databricks notebook - dataframes, variables, readme, excetra. Even if its a different written in a different language like Scala or Spark SQL. 
# MAGIC When you import, you'll need to change the file path for both run programs. 
# MAGIC 
# MAGIC ## Warning: 
# MAGIC - Don't put comments before or after the %run. This may cause the cell not to find the notebook

# COMMAND ----------

# MAGIC %md
# MAGIC /Shared/print
# MAGIC 
# MAGIC place the "run" notebook into the shared folder in databricks to run it. Notebook will output "Notebook worked" if it is correct. 

# COMMAND ----------

# DBTITLE 1,Run a Scala Program  (%run)
# comment here
%run /Shared/Cell-Magic/display_output


# COMMAND ----------

# DBTITLE 1,Run a Databricks Notebook (%run)
# MAGIC %run /Shared/Cell-Magic/run

# COMMAND ----------


