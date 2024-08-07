# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run this notebook, you need to use one of the following Databricks runtime(s): **12.2.x-cpu-ml-scala2.12**

# COMMAND ----------

# MAGIC %md
# MAGIC # Agenda
# MAGIC ## Deep Learning with Databricks

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Day 1 AM
# MAGIC | Time | Lesson &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 30m  | **Introductions & Setup**                               | *Registration, Courseware, and Q&As* |
# MAGIC | 25m  | **[Linear Regression]($./01 Keras Fundamentals/01.1 - Linear Regression)** | 1. Build a linear regression model using Scikit-learn (sklearn) and reimplement it in Keras </br> 2. Modify # of epochs </br> 3. Visualize loss </br> 4. Make predictions| 
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 30m  | **[Keras]($./01 Keras Fundamentals/01.2 - Keras)**  | 1. Modify the following parameters for increased model performance: <ul><li>Activation functions </li> <li> Loss functions</li> <li> Optimizer</li><li> Batch size </li></ul> 2. Save and load models |
# MAGIC | 25m    | **[Keras Lab]($./01 Keras Fundamentals/01.2L - Keras Lab)**    | Build and evaluate your first Keras model! |
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 25m  | **[Preprocessing]($./01 Keras Fundamentals/01.3 - Preprocessing)** | Learn how to use normalization/standardization procedures for better model convergence |
# MAGIC | 35m  | **[Callbacks]($./01 Keras Fundamentals/01.4 - Callbacks)** | 1. Perform data standardization for better model convergence </br> 2. Add validation data </br> 3. Generate model checkpointing/callbacks </br> 4. Use TensorBoard </br> 5. Apply dropout regularization |

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Day 1 PM
# MAGIC | Time | Lesson &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 10m  | **Review**                               | *Review of Day 1 AM* |
# MAGIC | 35m  | **[Callbacks Lab]($./01 Keras Fundamentals/01.4L - Callbacks Lab)**      | Practice using checkpoints and callbacks
# MAGIC | 35m  |**[MLflow]($./02 MLflow/02.1 - MLflow)** | 1. Introduction to MLflow </br> 2. Track ML Experiments </br> 3. Query the MLflow server </br> 4. User-defined Functions applied to a Spark DataFrame |
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 25m  | **[MLflow Lab]($./02 MLflow/02.1L - MLflow Lab)**| Log and explore ML experiments with MLflow |
# MAGIC | 30m  | **[Hyperopt]($./03 Hyperopt/03.1 - Hyperopt)** | Perform better parameter searching using Hyperopt with Keras |
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 30m  | **[Hyperopt Lab]($./03 Hyperopt/03.1L - Hyperopt Lab)** | Use Hyperopt with SparkTrials to perform distributed hyperparameter search |
# MAGIC | 25m  | **[Petastorm for Large Data]($./04 Petastorm and Horovod/04.1 - Petastorm for Large Data)** | 1. Perform data preparation using Petastorm </br> 2. Compare upstream & downstream vectorization |

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Day 2 AM
# MAGIC | Time | Lesson &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 20m  | **Review**                               | *Review of Day 1* |
# MAGIC | 45m  | **[Horovod for Distributed Training]($./04 Petastorm and Horovod/04.2 - Horovod for Distributed Training)** | 1. Use Horovod to train a distributed neural network </br> 2. Distributed Deep Learning best practices |
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 35m  | **[Horovod with Petastorm Lab]($./04 Petastorm and Horovod/04.2L - Horovod with Petastorm Lab)** | 1. Prepare your data for use with Horovod</br> 2. Distribute the training of our model using HorovodRunner</br> 3. Use Parquet files as input data for our distributed deep learning model with Petastorm + Horovod | 
# MAGIC | 25m  | **[Model Interpretability]($./05 Model Interpretability/05.1 - Model Interpretability)**  | Use SHAP to understand which features are most important in the model's prediction for that data point |
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 30m    | **[Distributed Inference with CNNs]($./06 Convolutional Neural Networks/06.1 - Distributed Inference with CNNs)**    | 1. Analyze popular CNN architectures </br> 2. Apply pre-trained CNNs to images using Pandas Scalar Iterator UDF and Pandas Function API |
# MAGIC | 30m  | **[SHAP for CNN Lab]($./06 Convolutional Neural Networks/06.1L - SHAP for CNNs Lab)**  | Use SHAP to generate explanations behind a CNN's predictions |

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Day 2 PM
# MAGIC | Time | Lesson &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 10m  | **Review**                               | *Review of Day 2 AM* |
# MAGIC | 20m  | **[Transfer Learning with Data Generators]($./07 Transfer Learning/07.1 - Transfer Learning with Data Generators)**                               | 1. Motivate why transfer learning is a promising frontier for deep learning<br> 2. Compare transfer learning approaches<br>3. Perform transfer learning to create an cat vs dog classifier |
# MAGIC | 20m  | **[Transfer Learning with TFRecord]($./07 Transfer Learning/07.2 - Transfer Learning with TFRecord)**                               | Learn to use the TFRecord format & how to use TFRecord for improved model training |
# MAGIC | 20m  | **[Transfer Learning for CNN Lab]($./07 Transfer Learning/07.2L - Transfer Learning for CNNs Lab)**         | Apply transfer learning to predict pneuomnia based on chest x-rays |
# MAGIC | 10m  | **Break** | ||
# MAGIC | 20m  | **[Distributed Training with TFRecord]($./08 TFRecords/08.1 - Distributed Training with TFRecord)**                               | Conduct distributed training with TFRecord using `spark-tensorflow-distributor` |
# MAGIC | 30m  | **[Model Serving]($./09 Model Serving/09.1 - Model Serving)**  | Real time deployment of a convolutional neural network using REST and Databricks MLflow (v 1.x) Model Serving |
# MAGIC | 10m  | **Break** | ||
# MAGIC | 50m  | **[Embeddings]($./10 Natural Language Processing/10.1 - Embeddings)**  | Understand what embeddings are and how to use them in Natural Language Processing (NLP)|
# MAGIC | 10m  | **Break** | ||
# MAGIC | 50m  | **[NER with SparkNLP]($./10 Natural Language Processing/10.2 - NER with SparkNLP)**  | Extract Named Entities with SparkNLP |
# MAGIC
# MAGIC Time permitting, additional [NLP Lab]($./10 Natural Language Processing/10.2L - Transfer Learning for Document Classification) for transfer learning on news article topic classification.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>