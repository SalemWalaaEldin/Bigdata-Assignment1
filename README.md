# Big Data Assignment 1

## Team Members
salem attia 221000348
omar roshdy 221001265
amr sayed 202001219
## Docker build / run commands used

```bash
docker build -t myappcontainer .
docker rm myappcontainer
docker run -it --name myappcontainer docker_app
python ingest.py 
python preprocess.py 
python analytics.py 
python visualize.py 
python cluster.py 
bash summary.sh
 
 ## EXECUTION FLOW
ingest.py:
Reads the dirty dataset
Saves data_raw.csv

preprocess.py:
Cleans missing or invalid values
Removes duplicates
Encodes categorical columns
Drops unnecessary columns
Saves data_preprocessed.csv
Calls analytics.py

analytics.py:
Generates three textual insights:
Most sold item (insight1.txt)
Most common payment method (insight2.txt)
Average total spent per transaction (insight3.txt)
Calls visualize.py

visualize.py:
Generates correlation heatmap (summary_plot.png)
Calls cluster.py

cluster.py:
Applies K-Means clustering on selected features
Saves cluster results (clusters.txt and data_clustered.csv)

summary.sh:
Copies all outputs to folder results/
Stops and removes the Docker container

###Docker hub 
https://hub.docker.com/repository/docker/salalimos/bigdata1/general

### GITHUB
https://github.com/SalemWalaaEldin/Bigdata-Assignment1.git
