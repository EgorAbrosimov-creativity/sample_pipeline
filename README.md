# sample_pipeline

This is my test assignment for position of Data Scientist at Perfsol. 

To see details on data prep and model development pipeline you should consider looking into Jupyter notebooks enumerated 01, 02 and so on.

To make a prediction you should

1) Clone this repo

2) Open command line and run 

conda env create -f environment.yml

3) Upload into the local directory the file you want to make prediction on

4) In command line run

conda activate perfsol

python predict.py <PATH TO YOUR DATA?>

5) go to results/ folder and find prediction.csv file

HOORAY!

Note: this pipeline is not ideal. In my opinion, it could have been organized as a web service or and API, but due to the lack of time I figured it would suffice