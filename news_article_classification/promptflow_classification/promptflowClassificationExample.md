##  Text classification with Azure OpenAI services
In this example we will use an LLM model to perform text classification, 
using the same data that we used for the NLP example. 
This will also to understand differences in the developer experience, 
and also compare performance metrics. 

## RAI dashboard availability for LLM model outputs
Unfortunately the RAI dashboard is not yet compatible with LLM models. 
We plan to add support for this class of models in the future. 

## Synthetic dataset and model 
**WARNING: Use of synthetic data**  
This accelerator was developed using synthetic data to emphasize the importance of data privacy. 
For this reason, you my find some anomalies in certain metrics or dashboard components. 
These should not distract from the demonstration. 
The tools and techniques described here remain valid, despite any data shortcomings that may be present. 

Data dictionary 

|Type           | Feature Name          |   Feature Description|
|---------------|-----------------------|----------------------|
Feature         |Article ID             |Unique identifier for each article
Feature         |Article Heading        |The title or headline of the article
Feature	        |Article Description    |Text from the main body of the article 
Feature	        |Category           	|The category or class to which the article belongs


Here are descriptions of the different article categories: 
- Banking and finance - Debt Market: News and updates related to the debt market within the banking and finance industry
- Stock Market Updates: News and updates about the stock market, including stock prices, market indices, and company earnings
- Business: News and articles about general business topics, such as corporate strategies, management, and industry trends
- Real Estate: News and updates related to the real estate industry, including property market trends and housing prices
- Cryptocurrency: News and information about cryptocurrencies, blockchain technology, and related developments
- Personal Finance: News and tips related to personal finance management, including budgeting, saving, and investing
- Financial Regulations: News and updates about financial regulations, compliance requirements, and legal developments

## Prerequisites
- **Azure OpenAI endpoint** -- This endpoint configured in the "Connections" section
- **Compute runtime** -- This can be a compute instance you have already configured, or one you can create as part of the building the flow
    - Please review this [guidance](/news_article_classification/promptflow_classification/promptflow_documentation/creatingRuntime.md) for creating a compute runtime



## Creating the LLM based classifier using Prompt flow

## Steps to create a Financial News Classification Promptflow 


1. In the Azure ML Studio gallery, at the upper-right of the screen, 
click on the "View prompt flow" button. 

![view-promptflow](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/llmSetup_viewPromptflow.png)


- Please click on the "**Create**" button on the PromptFlow page. 

![param2](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt2.png)

- After clicking on the "**Create**" button, a new page will appear, displaying information about creating new flows. From that page, please click on the "**Create**" button for the Standard flow, as indicated in the screenshot.

![param3](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt3.png)

- Once you select the "**Create**" option for the "**Standard flow**", the interface will appear as illustrated in the screenshot.

![param4](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt4.png)

- Once the Standard flow is created, you can proceed with the first step, which involves adding input data. For the Financial News Classification task, we will utilize the provided dataset. The dataset consists of two key columns that are crucial for prediction: *Article Heading* and *Article Description*.

- Before filling in the values from the data, it is important to add the column names. Please ensure that the column names match the names used in your dataset. In this example, we need to add two column names: "*Article Heading*" and "*Article Description*". Please ensure that you add the column names in the "*Name*" field while keeping the "Value" field empty for now. Also, make sure to set the type of the value as "*string*".

![param5](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt5.png)

- To add the data points manually, you can use the following strings as examples:

    -   For "Article Heading" field: 
        "Corporate Defaults Shake Debt Market Confidence"

    -   For "Article Description" field: 
        "Discover how recent corporate defaults have affected investor confidence in the debt market and the measures being taken to restore stability."
        
    After adding the input data, your input section should resemble the depiction in the screenshot.

![param11](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt11.png)

- To create the Financial News Classification flow, you will need two main components: Prompt and LLM. The Prompt serves as a system prompt, instructing the LLM (Language Model) about the task it needs to perform.

- If you already have an existing prompt, you can edit it. Alternatively, if you want to add a new prompt, you can click on the "**Prompt**" button, as highlighted in the screenshot. It is advisable to give your prompt a meaningful name for clarity.

![param12](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt12.png)

- Before proceeding to the next step, please ensure that you have a Runtime with a functioning compute environment.

![param14](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt14.png)

- Please copy the contents of the system prompt from the provided [file](/news_article_classification/promptflow_classification/promptflow_scripts/variants/variant_0.md) and paste it into the prompt section, as demonstrated in the screenshot. After pasting the content, please click on the "**Validate and parse input**" button. This button will be enabled due to the changes made in the prompt's content. 

![param13](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt13.png)

- After clicking on the "**Validate and parse input**" button, you will observe that there are two inputs considered, which will be populated by your datapoint in each iteration. For the "Article Headline," you can select the ${inputs.ArticleHeading}.

![param15](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt15.png)

- Once you have correctly filled both data points, your inputs section for the prompt will resemble the following screenshot. Please ensure that both data points are populated accurately within the inputs section.

![param16](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt16.png)

- After updating the system prompt section, you should proceed to add an LLM (Language Model) component. If you have an Python code component, you can delete it as it won't be necessary for the current task.

- Please click on the "**LLM**" button, as indicated in the screenshot.

![param17](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt17.png)

- The LLM model should always have a connection, which can be created as mentioned earlier in the code. The content of the LLM should be set as "{{prompt_text}}", as depicted in the screenshot. You will notice that the "**Validate and parse input**" button is now enabled. Please click on that button to validate and parse the input.

![param18](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt18.png)

- After clicking on the "**Validate and parse input**" button, you will be prompted to provide the necessary input.

![param19](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt19.png)

- The input that you will be providing to the LLM will be the output of the prompt. As depicted in the screenshot, please ensure that you connect the output of the prompt to the input of the LLM. Please select {system_prompt.output} from the provided dropdown menu and connect it as the input for the LLM component.

![param20](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt20.png)

- Scroll up on the page to locate the output section, just after the input section. From there, select the output of the LLM. In this case, the LLM is named "System_classification", so the output should be {System_classification.output}.

![param21](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt21.png)

- Once you have completed the entire setup, your page will resemble the layout shown in the screenshot.

![param22](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt22.png)

- Please click on the "Run" button as shown in the screenshot. This will initiate a basic test run using the selected data point from the input section.

![param23](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt23.png)

- As shown in the screenshot, the run has been successfully completed without any errors.

![param24](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt24.png)

- In the "outputs" section of your LLM, you will find the predicted output generated by your flow, as shown in the screenshot.

![param25](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/prompt25.png)