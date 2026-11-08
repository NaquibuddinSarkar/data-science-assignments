# Assignment 3 — Distributed Transaction Analytics with PySpark

**Level:** Intermediate. **Course alignment:** Big Data, Spark and distributed data processing.

## Scenario
A multi-region online retailer collects millions of transaction records. The analytics team needs reliable monthly and regional summaries without collecting the entire dataset into local Pandas memory.

Use an openly licensed transaction dataset or a synthetic dataset generated with a fixed random seed.

## Tasks
1. Create a SparkSession and document runtime and master.
2. Define a transaction schema and explain why explicit schemas may be preferable to inference.
3. Load records into a Spark DataFrame; check row counts, nulls, duplicates and invalid values.
4. Filter invalid transactions and derive date/month columns.
5. Aggregate revenue, order count and average order value by region, category and month.
6. Join a customer dimension to segment transactions; explain when broadcast joins may help.
7. Use a window function for cumulative customer spend or rolling monthly sales.
8. Write Parquet and read it back.
9. Use explain() to inspect an execution plan.
10. Identify transformations versus actions and explain lazy evaluation.

## Performance discussion
Explain driver, executor and cluster-manager roles; why joins and groupBy can create shuffles; repartition versus coalesce; small-file overhead; and how an orchestrator can sequence ingestion, validation, processing and reporting.

## Deliverables
- pyspark_transaction_analytics.ipynb
- Synthetic data generator or source citation
- Parquet output schema and sample summary
- Two visualisations
- 400–600 word performance and architecture note

## Assessment rubric (100 points)
| Area | Points |
|---|---:|
| Schema, ingestion and quality controls | 20 |
| Correct DataFrame transformations and joins | 25 |
| Window functions and Parquet output | 15 |
| Execution-plan and Spark architecture explanation | 20 |
| Reproducibility and interpretation | 20 |

A local Spark run demonstrates the API and concepts, not performance at cluster scale.
