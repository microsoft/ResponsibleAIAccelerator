## Steps to create a Runtime

- Please select the "**Runtime**" section, which is highlighted in the screenshot, from the various sections displayed.

![runtime1](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_1.png)

- Before creating a Runtime, please ensure that you have a compute instance available in your Machine Learning workspace. If you do not have a compute instance, you can create one in the Machine Learning workspace.

- Once you have a successfully running compute instance, please return to the "**Runtime**" section. You will notice a highlighted click button, so go ahead and click on it.

![runtime2](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_2.png)

- After clicking on the create button, you will be presented with two options. It is advisable to choose the "**Compute instance runtime**" option from the dropdown menu.

![runtime3](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_3.png)

- When you select the "**Compute instance Runtime**" option, a page will appear where you need to fill in the required details to add a compute instance runtime.

![runtime4](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_4.png)

- Here are the details that you need to take care of when adding a compute instance runtime:

1. "*Runtime name*": You can provide any name for the runtime that you prefer.
2. "*Description*": This detail is optional. You can add a description if desired, but it is not necessary.
3. "*Select Azure ML compute instance*": From the dropdown menu labeled "Select Azure ML compute instance," please select the compute instance that you have created and is currently running as depicted in the screenshot.
4. "*Custom Application*": Under the "*Custom application*" detail, you have the choice to select either "*New*" or "*Existing*". However, for the Financial News Classification workflow, the "*New*" option should work perfectly fine.
5. "*Environment*": Under the "*Environment*" detail, you have the option to choose either "*Use default environment*" or "*Use customized environment*". However, for the Financial News Classification workflow, selecting the "Use default environment" option should work perfectly fine.

![runtime5](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_5.png)

- Once you have filled out the required details, your screen should resemble the layout shown in the screenshot. At this point, all you need to do is click on the "Create" button to proceed.

![runtime6](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_6.png)

- Please note that it may take approximately 4-5 minutes for the runtime to become available and running. You can monitor the progress in the notification section, as it will provide updates on the status of the runtime.
Until your runtime is successfully created, the status of the runtime will be displayed as "*Not available*". Please wait for the runtime creation process to complete before it becomes available for use.

![runtime7](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_7.png)

- After a few minutes, you will observe that the runtime is up and running, as depicted in the screenshot. Please check the status to confirm when the runtime becomes available for use.

![runtime8](/news_article_classification/promptflow_classification/promptflow_documentation/promptflow_media/runtime_8.png)