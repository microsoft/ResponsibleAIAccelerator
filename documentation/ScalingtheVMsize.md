## Steps to change the Compute instance size as created in the Azure Machine Learning Workspace

- From the Machine Learning Workspace click on the **_Studio web URL_** as highlighted in the screensnap. After clicking on the link a new tab will open up and that would be Machine Learning Studio.  

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/machine_learningstudio.png)

- The Machine Learning Studio home page would open-up and it would like as shown in the screenshot.

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/compute_1.PNG)

- From the screensnap click on the **Compute** option as marked. As you click on the **Compute** button you will be migrated to a new page which shows - lists of compute that are already running for the machine learning workspace. As a compute instance is already created by default using the **Deploy to Azure** button. So you can see it in the tab.

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/compute_2.PNG)

- An option of scaling is not available after the compute instance is once created hence we can follow a method. Where you delete the existing compute instance and create a new compute instance according to your convenience.

    - To delete an existing compute instance you can select the compute and choose an option to **Delete** as shown in the screensnap.

    - The whole process to delete the compute instance will take approximately 2-3 minutes. 

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/compute_3.PNG)

- After successful deletion of the compute instance, a new page will open-up as shown in the screenshot. In the new page you need to click on the **New** button.

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/compute_4.PNG)

- Once you click on the **New** button you will be prompted to a list of questions. As you can see that this list consist of information about the compute instance that you want to create. The first information that you need to fill up is the name of the compute instance. You can fill that up in the **Compute name** gap.

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/compute_5.PNG)

- The next detail that you have to fill-up is **Virtual machine type**. For this detail you need to select whether you want to choose the CPU option or the GPU option. Anyone of the options can be selected according to your requirement.

- The third detail that you have to fill-up is to choose the **Virtual machine size**. Of the two options from **Select from recommended option** and **Select from all options** you can choose anyone of them. The only difference between the two options is the list of the Compute instance sizes will be larger for the latter one.

    - As can be seen in the screensnap, I have selected **Select from recommended option**, and after getting the list of compute instance sizes I have choosen the compute instance according to my requirement.

    - After this click on the **Create** button as highlighted using a red box.

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/compute_6.PNG)

- Once you click on the **Create** button, you have to wait for couple of minutes before your compute instance gets created and comes up running as can be seen in the screensnap. Just verify the size and name of the compute instance that you created.

![Open Up Machine Learning Studio](/documentation/media/resource_deployment/compute_7.PNG)
    