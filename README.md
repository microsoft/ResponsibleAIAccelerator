## About this repository
This repo demonstrates how you can use the Azure Machine Learning [Responsible AI dashboard](https://github.com/microsoft/responsible-ai-toolbox#introducing-responsible-ai-dashboard) to evaluate and debug your machine learning models, 
to help reduce error and fairness issues in your model predictions and data driven decisions. 
It describes two different demonstration implementations of the dashboard, covering a financial services scenario and a health care scenario.


Understanding your model predictions, resolving errors to ensure trust, and checking for potential fairness issues must be important goals for all AI developers. 
We all are accountable and responsible to test whether machine learning models are inadvertently withholding access to certain resources, information, or opportunities based on sensitive attributes, 
such as gender or race, whether they have performance blind spots that could lead to trust and reliability issues, 
or whether they provide a different quality of service to different demographic groups.  

### Responsible AI dashboard
The Responsible AI dashboard is a one-stop shop for putting Responsible AI principles into practice. 
It is designed to achieve the following goals:  

- To guide model developers through a fluid and end-to-end model debugging experience, 

- To help business stakeholders explore causal relationships in the data and take informed decisions in the real world.


Part of the Azure ML studio, the dashboard provides an easy-to-use interface for identifying and diagnosing a variety of reliability and fairness issues in AI models. 
The dashboard includes the following components:


- **Error Analysis** helps to identify cohorts of data with higher error rate than the overall benchmark. 
These discrepancies might occur when the system or model underperforms for specific demographic groups or infrequently observed input conditions in the training data. 
This tool reveals the blind spots of your machine learning model.  

- **Performance and Fairness Assessment** evaluates the performance of your model and your model's group fairness issues by identifying which groups of people may be disproportionately impacted, 
often in a negative way, by the AI system. 
It enables you to observe both the overall performance of your model on the whole test data, 
as well as the disaggregated analysis of the model performance across different data cohorts 
(such as cohorts defined in terms of sensitive attributes). 


- **Data Analysis** helps you gain an overall understanding of your dataset's distributions and statistics. 

- **Model Interpretability** explains the outcomes of your opaquebox machine learning models, helping you understand how overall and individual predictions are made.

- **Counterfactual Analysis** and **What-if Analysis** provide two functionalities:

    - What-if: Enabling you to observe how feature perturbations would affect your model predictions

    - Counterfactual: Providing the closest data points with opposing or different model predictions. It shows feature-perturbed versions of the same datapoint who would have received a different prediction outcome, 
    e.g., a loan applicant has been rejected by the model, but they would have got the loan approval prediction if their income was $10,000 higher.

- **Causal Analysis** uses historical data to derive the causal effects of treatment features on real-world outcomes. 
It focuses on answering "what-if" style questions to apply data-driven decision-making. 
For example, how would revenue be affected if a corporation pursues a new pricing strategy? 
Would a new medication improve a patient’s condition, if all else is equal? 

- **Scorecard** in the form of a PDF report that allows you to easily share model assessment insights captured via the components above with stakeholders outside of your organization, 
especially those without access to Azure Machine Learning, for auditing or approval processes. 

More information, including details around the Responsible AI dashboard and scorecard can be found [here](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2).

### Demo scenarios
We will use two different business scenarios to illustrate how to use dashboard features for model debugging and responsible decision-making purposes:  

- **Financial Services** - A consumer applies for and is denied a home loan. The underwriter investigates details of why the applicant was rejected. 
With these valuable insights, the customer service representative can make concrete recommendations to the customer, to increase the likelihood of approval on the next application.  

- **Health Care** - Medical professionals are working to ensure there is enough hospital capacity Covid patients. They use a variety of data about infected patients to identify those likely to require hospitalization. The dashboard can also guide their treatments, to help reduce the number of hospitalizations. 

## Solution Overview 

**Architectural Diagram**  
The Responsible AI dashboard contains several tools that help you a) Identify and Diagnose issues in your model results, 
and b) Inform next steps to improve outcomes for your end users and customers.  

![RAI Architecture](./documentation/media/raiArchitecture.png)



## Getting Started

### Prerequisites
1. Active Azure Subscription 
1. Working knowledge of Azure Machine Learning


### Deploy demo environment
Use the "Deploy to Azure" button to deploy the simulation into your Azure Subscription. 
Please review this [step-by-step guide](./documentation/DetailsInAzurePortal.md) 
to preview the Azure Portal experience before proceeding.  

<br />

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fsaresponsibleai.blob.core.windows.net%2Fdataset%2FARMTemplate.json)

<br />

Here are two important reminders to help you successfully complete this accelerator. 
- **VM Sizing** -- The ARM template provided deploys a standard size VM. 
If you want to change the VM size, please refer to [this guidance](./documentation/ScalingtheVMsize.md).  

- **Select Azure ML kernel** -- Be sure to select the "Python 3.8 - AzureML" kernel, via the drop-down menu at the right end of the taskbar, as it includes several required packages.  

![Deploy-Environment-00](./documentation/media/deployEnvironment_selectKernel.png)

### Clone the repo

You can clone this repo directly to you newly created Azure ML workspace. 
For help with this task, please review [these instructions](./documentation/CloneRepo.md).

Alternatively, you can also download the files and then upload them to the Azure ML workspace. 
Refer to [this document](./documentation/uploadjupyternotebookandrun.md) 
if you need additional guidance with this task. 


### Review business scenarios

1. **Financial Services**
    This scenario highlights several features of the Responsible AI dashboard, including: Explainability, Fairness, Error analysis, and What-if counterfactual analysis. 
    This notebook takes about **20-25 minutes** to create the dashboard.  

    - Follow this link to the [Jupyter notebook](./finance_story/Finance_Dashboard.ipynb). 
        - If you choose not to clone this repo to Azure ML studio, 
        check [this link](./documentation/uploadjupyternotebookandrun.md) for guidance on uploading the notebook and data files.  
    - Once you have finished running the notebook,
    refer to this [Financial Services scenario guide](./documentation/financialServicesExample.md) 
    for suggestions on how to interpret and apply the Responsible AI dashboard.  
    <br />

1. **Health Care**
    In addition to several components that can help you improve model performance, 
    this scenario highlights a causal analysis tool that can guide real-world action. 
    This notebook takes about **25-30 minutes** to create the dashboard.  
    
    - Follow this link to the [Jupyter notebook](./healthcare_story/Covid_Healthcare_Dashboard.ipynb). 
        - If you choose not to clone this repo to Azure ML studio, 
        check [this link](./documentation/uploadjupyternotebookandrun.md) for guidance on uploading the notebook and data files.  
    - Once you have finished running the notebook,
    refer to this [Health Care scenario guide](./documentation/healthCareExample.md) 
    for suggestions on how to interpret and apply the Responsible AI dashboard.  
    <br />


## Folders 
- documentation
    - Contains additional documentation files, including scenario guides and data dictionaries 
- finance_story
    - Contains synthetic data and a Jupyter notebook to support the financial services demo
- healthcare_story
    - Contains synthetic data and a Jupyter notebook to support the financial services demo
- templates
    - Contains ARM templates for the deployment of Microsoft Azure resources



## Trademarks
This project may contain trademarks or logos for projects, products, or services. 
Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks). 
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. 
Any use of third-party trademarks or logos are subject to those third-party’s policies.