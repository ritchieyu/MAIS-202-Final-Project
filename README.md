# MAIS202
### Final project files for MAIS 202 Fall 2020 cohort. This project sought to predict whether next generation amino acid mutations would occurr in the spike glycoprotein of SARS-CoV-2. Two approaches were taken, and dual stacked LSTM neural network architecture was employed.
### 1) Multilabel binary classification
#### Input a list of protein embedded representations of amino acid sequences tracing the estimated evolutionary path of SARS-CoV-2 in the past 10 months and return a binary vector labelling whether each site would mutate (1 = mutation, 0 = no mutation).
### 2) Single site binary classification
#### Input a list of single site embedded representatios, also tracing the estimated evolutionary path, and return a binary value indicating whether the specific site is predicted to occur. This process can also be iterated across all amino acid sites to determine whether mutations are predicted to occur at each site. 
### Despite my best efforts, these two approaches cannot confidently predict mutations in the SARS-CoV-2 spike glycoprotein amino acid sequence. This can be illustrated with an example. Site 222 on the glycoprotein amino acid sequence was selected for single site mutation prediction because it was found to be the most abundant mutation. While the model classified whether it would mutate to an accuracy of ~56%, this value is inconclusive, because it is nearly identical to the data distribution. That is, it may as well have returned the exact same binary value each time, and would have still obtained a similar accuracy. Similarly, multilable binary classification was inconclusive as well. Further details on the possible reasons for these results are included in the final project poster. 
### mais_final_project.pdf contains the final project poster 
### main.pynb contains all the code needed to run this project. It contains preprocessing steps, model assembling, and model training. All models were implemented using the Keras framework.

