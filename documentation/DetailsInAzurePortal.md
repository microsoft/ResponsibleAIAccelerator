## Steps to deployment in Azure Portal:

- As soon as you click on the **Deploy to Azure Button** you will be naviagted to the sign-in Page of the Azure Portal. After entering the username and password, you will be navigated to **Custom Deployment** page as shown in the screenshot.

- To create a Machine Learning Workspace there are four underlying resources that must be created first. Here are the list of resources:

    1. **Azure Storage Account**: It is used as the default datastore for the workspace.

    2. **Azure Container Registry**: Registers the docker container that is used for Azure Machine Learning environments, AutoML, Data profiling.

    3. **Azure Application Insights**: Stores monitoring and diagonstics information.

    4. **Azure Key Vault**: Stores secrets that are used by compute targets and other sensitive information that's needed by the workspace.

- Here is the list of paramaters and the description of the details that can be entered for the parameters:

    1. **Subscription** - Enter the name of your subscription to which these resources need to be deployed.It is a required parameter.

    2. **Resource Group** - Enter the name of the resource group which these resources need to be part of. Either you can create a new Resource Group by clicking on **_Create new_** link or you can use an existing Resource Group.

    3. **Region** - It will be automatically taken from the Resource Group that you have choosen or created. So there is no need to fill this parameter.

    4. **Work Space Name Prefix** - This is a prefix name that will be prefixed for all the 4 underlying resources and Machine Learning Workspace. You need to choose any name which is between 3 to 5 character long.

-   The details mentioned about the parameters should be kept in mind while creating the resources. Here are the steps that can be followed to create the resources:

    1. As soon as the "Deploy to Azure" button is clicked a Azure portal window will open. As can be seen in the screenshot.
    
    ![Open Up Machine Learning Studio](/documentation/media/resource_deployment/basictemplate.png)

    2. Fill in the details. The user can select the subscription in which the resources can be deployed. From the drop-down user can select the **ResourceGroup** in which they want to deploy the resources. As can be seen in the screenshot.

    ![Open Up Machine Learning Studio](/documentation/media/resource_deployment/custom_deployment_param.png)

    3. After selecting the ResourceGroup it can be seen that the **Region** parameter is automatically set. Fill-up the **WorkSpaceName Prefix** parameter but take care that it is between 3-5 characters long. As shown in the screenshot.

    ![Open Up Machine Learning Studio](/documentation/media/resource_deployment/deploymentparameters2.png)

    4. After filling up the parameters in this section the user is supposed to click on the **Review + create** button as highlighted in the screenshot. This button will take user to the next section to provide the next set of parameters.

    ![Open Up Machine Learning Studio](/documentation/media/resource_deployment/deploymentparameters2_1.png)

- Validation tests will run in the background and after passing these tests your page in Azure portal will look as shown in the screenshot. 
    * Note that the validation tests are cleared. After this you can click on the **Create** option.
![Validation](/documentation/media/resource_deployment/Validation_param.png)

- As soon as you click to **Create** option you will be moved to deployment page. The deployment in progress screenshot is as shown.
![Deployment In progress](/documentation/media/resource_deployment/deployment_in_progress.png)

- After successful deployment your page will look as shown in the screenshot. You can simply go to the Resource Group and check if the resources were created according to your choices. 
    * You will see that the name to the workspace and resoures were assigned automaticall. The name to all the resources are unique and are a combination of **_Work Space Name Prefix_** and other options.
![Deployment succeed](/documentation/media/resource_deployment/deployment_succeed.png)

- As we can see that everything is set by default and the size of all the resources have been pre-defined. But there are further steps to increase/decrease the size of various resources. To change the size of the VM you can refer to this [link](/documentation/ScalingtheVMsize.md)