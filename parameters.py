db_name = 'apache_jira_data'
connection_link = 'mongodb://localhost:27017/'
collection_issues = 'issues'
collection_users = 'users'
collection_projects = 'projects'
data_out_folder = r"C:\Users\hp\Desktop\Module-3-Task-assigning\data\data_output"
trainable_data_folder = r"C:\Users\hp\Desktop\Module-3-Task-assigning\data\data_output\step3_2_processed_data"
embeddings_folder = r"C:\Users\hp\Desktop\Module-3-Task-assigning\data\embeddings"
min_assignees = 5
result_folder = r"results"
min_issues_per_assignee = 80
# Parameters for running the pipeline
num_assignees = 5
all_assignees = [5, 10, 15, 20]
num_topics = [4, 6, 8, 10, 12, 14, 16, 18, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]
projects = ["AMBARI", "ARROW", "CASSANDRA", "CB", "DATALAB", "FLINK", "GEODE", "HDDS", "IGNITE", "IMPALA", "MESOS", "OAK"]