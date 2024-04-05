from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
categories = spark.createDataFrame([
  [1, 'Категория 1'],
  [2, "Категория 2"],
  [3, "Категория 3"],
], ["id", "category_name"])

products = spark.createDataFrame([
  [1, 'Товар 1'],
  [1, "Товар 2"],
  [2, "Товар 3"],
], ["category_id", "product_name"])

situation = products.category_id == categories.id
product_category = products.join(categories, situation, 'inner')
product_category = product_category.select('product_name', 'category_name')
product_category.show()

product_without_category = products.join(categories, situation, 'left_anti')
product_without_category = product_without_category.select('product_name')
product_without_category.show()

