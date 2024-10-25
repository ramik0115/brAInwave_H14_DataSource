# Drug Bioactivity Prediction with Machine Learning

## Project Overview
Our project is focused on enhancing the drug design process by utilizing machine learning (ML) techniques to predict the bioactivity of chemical compounds against target proteins. By accurately predicting the potential efficacy of compounds early in the design phase, we aim to significantly reduce both the time and financial costs associated with drug development. This approach allows researchers to identify and eliminate potential failure points, ultimately improving the overall success rates in drug discovery.


## Objectives

1. **Reduce drug discovery timelines** by automating the design process with machine learning.
2. **Minimize financial costs** involved in initial research.
3. **Identify and eliminate potential failure points** at early stages, improving the success rate of drug candidates.


## Workflow

Our workflow consists of several key phases that guide our project from data collection to deployment:

1. **Data Collection**: We begin by gathering comprehensive data on FDA-approved drugs. This data serves as the backbone of our analysis and model training, ensuring that we work with reliable and relevant information.

2. **Data Preprocessing**: Once we have collected the data, the next step involves cleaning and preparing it for analysis. This stage is crucial as it ensures the accuracy and quality of the dataset we will use in subsequent phases.

3. **Exploratory Data Analysis (EDA)**: We conduct a thorough analysis and visualization of the data to uncover patterns and identify key features that may influence drug bioactivity. This step helps us better understand the dataset and informs our model-building decisions.

4. **Molecular Descriptor Calculation**: To enrich our dataset, we compute molecular descriptors, which are numerical representations of molecular structure. These descriptors enhance our models' ability to predict bioactivity by providing critical chemical information.

5. **Dataset Preparation**: After calculating the molecular descriptors, we organize the dataset to facilitate efficient training and testing of our models. This preparation ensures that our data is structured in a way that optimizes model performance.

6. **Model Building**: With the prepared dataset, we train multiple machine learning models. We focus on optimizing hyperparameters to enhance the performance of each model, ensuring that we explore a variety of algorithms to find the best fit for our prediction task.

7. **Model Comparison**: After training, we compare the performance of the different models to identify the one that delivers the most accurate predictions. This comparison is essential for selecting the best model to move forward with.

8. **Deployment**: Once we have identified the best-performing model, we deploy it as a Streamlit web application. This user-friendly interface allows researchers, professors, academicians, and students in pharmaceuticals and medicine to access our predictions easily.

9. **Integration with LLM Chatbot**: To further enhance the research experience, we incorporate an AI-powered chatbot using [OnDemand.io](https://www.ondemand.io). This chatbot automates initial research steps for R&D professionals, providing real-time assistance and streamlining workflows.

[Google Colab Files for Evaluation](https://github.com/ramik0115/Colab_Notebooks_brAInwave_TeamH14)

## OnDemand AI Agent Overview
![OnDemand AI Agent Overview](AI_Agent Architecture for OnDemand.io.JPG)


## Getting Started

### Prerequisites
- Python 3.x
- [Streamlit](https://streamlit.io/)
- [OnDemand.io API Key](https://ondemand.io/)
- Other necessary libraries as listed in `requirements.txt`

### Installation
To set up the project locally, clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/drug-bioactivity-prediction.git
cd drug-bioactivity-prediction
pip install -r requirements.txt
