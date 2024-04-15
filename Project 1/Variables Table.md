|**Variables Table**||||||
|---|---|---|---|---|---|
|**Variable Name**|**Role**|**Type**|**Description**|**Units**|**Missing Values**|
|holiday|Feature|Categorical|US National holidays plus regional holiday Minnesota State Fair| ||no|
|temp|Feature|Continuous|Average temp in kelvin|Kelvin|no|
|rain_1h|Feature|Continuous|Amount in mm of rain that occurred in the hour|mm|no|
|snow_1h|Feature|Continuous|Amount in mm of snow that occurred in the hour|mm|no|
|clouds_all|Feature|Integer|Percentage of cloud cover|%|no|
|weather_main|Feature|Categorical|Short textual description of the current weather||no|
|weather_description|Feature|Categorical|Longer textual description of the current weather||no|
|date_time|Feature|Date|Hour of the data collected in local CST time||no|
|traffic_volume|Target|Integer|Hourly I-94 ATR 301 reported westbound traffic volume||no|

**Variable Types :**

- **Categorial Variable** : Categorical Variables represent categories or groups. It can take fixed number of possible values to represent qualtative characteristics.

- **Continuous Variable** : Continous Variables are numeric vaiables. These values can be fractional or decimal.

- **Integer Variables** : Integer Variables are numeric. These values can be only integers.

- **Date Variable** : Date vaiable in this context repsents date and time.

**Dataset Characteristics :**
    Multivariate, Sequential, Time-Series

- **Multivarate** : A Multivariate dataset contains mutliple variables(features or attributes) for each data points. Each variable (feature or attribute) representing different aspect or characteristics of data.

- **Sequential** : A equential dataset consists of data points that are arranged in a specific sequence or time series. Each data point respresents an observation(data point) capatured at time intervals

- **Time-Series** : A Time Series dataset represents obseravation (data point) collected at equally spaced time intervals.

Other types of dataset that exists are Sptial Dataset (features observed across various regions, locations), Image dataset (digial or visual data stored in matrix format), Text Dataset (textual data or document, such as cutsomer reivews).

**Role of a variable**

- **Feaute** is indepdent variable (input varible or predictor).These are used to make predictions or model relationships

- **Target** is dedependent variable(response variabel or output variable ) that machine learning model seeks to predict or explain.