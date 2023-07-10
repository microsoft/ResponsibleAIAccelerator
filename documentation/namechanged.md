## Steps to change the name of the Compute Instance in the JupyterNotebook

- After uploading any of the notebooks to the Machine Learning workspace, please navigate to the cell under **User Configuration** section, as indicated in the screenshot. In that cell, you will find instructions to specify the compute name.

![UserConfiguration](/documentation/media/depsuccess/name_compute3.png)

- In the code snippet, it is evident that the `compute_name` variable has been assigned the value "ResponsibleAI". To ensure proper configuration, replace the "ResponsibleAI" string with the compute name that you obtained as an output from the deployment script.

![UserConfiguration1](/documentation/media/depsuccess/name_compute1.png)

- After replacing the variable name, the output should appear similar to the following (with the name of your compute instance being different). This modification ensures that the execution of your Notebook will proceed smoothly and without encountering any issues.

![UserConfiguration1](/documentation/media/depsuccess/name_compute2.png)

**Reminder:** Update the `compute_name` variable in each notebook to ensure smooth execution of each example. 