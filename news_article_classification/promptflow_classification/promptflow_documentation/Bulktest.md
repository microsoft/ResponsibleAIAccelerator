## Calculating the accuracy for the entire dataset

- To calculate the overall accuracy for the dataset, let's return to the original Financial News Classification flow that you created.

- Let's begin with the bulk test by clicking on the "**Bulk Test**" option, as depicted in the screenshot.

![accuracy7](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy7.png)

- Upon clicking on the "**Bulk Test**" option, a page will open up with fields to fill in important details. You can provide any desired "*Name*" for the bulk test, write a few lines in the "*Description*" field, and ensure that the "*Runtime*" is set correctly.

![accuracy8](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy8.png)

- You have two options: You can either click on the "Upload a new data*" link to upload the dataset, or you can use an existing dataset. After uploading the dataset, your page should resemble the layout shown in the screenshot. Click on the **Next** button.

![accuracy9](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy9.png)

- Once you click on the "**Next**" button, you will be prompted to "**Select evaluation method**". At this stage, you can choose the recently created Evaluation method. Once you have selected the Evaluation method, the next set of details will appear on the screen, as shown in the screenshot.

![accuracy10](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy10.png)

- After selecting the Accuracy flow, you will need to choose the type of data that should be provided in the ground truth field. Since you already have a "**Category**" field in your dataset, you can select that as your ground truth data.

![accuracy11](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy11.png)

- The next step is to select the value that should be filled in the "**prediction**" field. For this, you will use the output obtained from this flow. Therefore, the value to be entered in the "prediction" field will be {output.output_prompt}. Click on the "**Next**" button as shown in the screenshot.

![accuracy12](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy12.png)

- The final step is to review all the information you have filled in and then submit it. Please click on the "Submit" button, as shown in the screenshot, to proceed with the submission.

![accuracy13](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy13.png)

- To view the details of the job you have submitted, you can either click on the "Go to run details page" link, as shown in the screenshot, or click on the icon to access the "Runs" page. Both options will provide you with the details of the submitted job.

![accuracy14](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy14.png)

- Upon clicking the link or button, you will be directed to the "Runs" page, as depicted in the screenshot. To access the latest run, click on the Run name, as indicated in the screenshot.

![accuracy15](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy15.png)

- Upon clicking the link, you will be directed to the next page, which will display all the outputs and evaluations. The page will resemble the layout shown in the screenshot.

![accuracy16](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy16.png)

- You can obtain the overall accuracy by clicking on the metrics section.

![accuracy17](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/accuracy17.png)