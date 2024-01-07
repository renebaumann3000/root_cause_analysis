# Root Cause Predictor - Proof of Concept

## Attention:
- This repo uses Git LFS (please see fork section).
- About the commits: 
- Initially I always committed all files, including the Jupyter checkpoints. These are either no longer available or they are larger files.
- The commits to the requirements refer to the deploy, as I had tried 5 different hosters. Since all hosters have different requirements, only try and error worked for me.
In the end I chose Streamlit Share because the Heroku slug size didn't matter and Streamlit Share is also suitable for larger ML models!
- A flowchart predictor has also been developed and committed, it works great, but has not yet been deployed. The file has therefore been removed from the repo.
- The app is deployed here: https://rootcauseanalysis-4ldogxgtc692sptsqpzfrw.streamlit.app/

# Introduction to Contact Drivers and Root Cause Analysis in Customer Service

Understanding customer service interactions and efficiently addressing them is critical for any business. This introduction delves into the concepts of 'Contact Drivers' and 'Root Causes', their traditional analysis methods, and the significance of detecting and eliminating root causes.

## What is a Contact Driver?

A 'Contact Driver' refers to any event, question, issue, or need that prompts a customer to reach out to a company's customer service department. Contact drivers are pivotal in understanding customer needs and expectations. They encompass a wide range of interactions, from product inquiries and service requests to complaints and feedback.

### Impact on a Company
- **Technology**: Contact drivers influence the development and implementation of customer service technologies, such as chatbots or CRM systems, to handle inquiries efficiently.
- **Staffing**: They affect staffing decisions, determining the need for customer service personnel, their training, and specialization areas.
- **Costs**: High volumes of contact drivers can lead to increased operational costs, including staffing, technology, and resources dedicated to customer service.
- **Customer Experience**: Effective handling of contact drivers is crucial for maintaining a high standard of customer experience and satisfaction.

## What is a Root Cause?

A 'Root Cause' is the fundamental underlying reason for a contact driver. It is not just a superficial issue or an immediate problem, but the primary cause that, if resolved, prevents the recurrence of a similar issue.

### Traditional Root Cause Analysis
Traditional root cause analysis typically follows a step-by-step approach:
1. **Identify the Problem**: Clearly define the problem or issue that has emerged.
2. **Collect Data**: Gather data relevant to the problem, including frequency, impact, and patterns.
3. **Identify Possible Causes**: Brainstorm potential causes for the issue.
4. **Analyze Causes**: Use tools like the 5 Whys or Cause-and-Effect Diagrams to drill down to the underlying causes.
5. **Implement Solutions**: Develop and implement strategies to address the root cause.
6. **Monitor and Adjust**: Continuously monitor the effectiveness of the solution and make adjustments as necessary.

## The Importance of Detecting and Eliminating Root Causes

Detecting and eliminating root causes is vital for several reasons:
- **Prevent Recurrence**: Addressing the root cause of an issue prevents its recurrence, thereby reducing the future workload on customer service.
- **Improve Customer Satisfaction**: Resolving issues at their source enhances overall customer satisfaction, as customers experience fewer problems.
- **Cost Efficiency**: By eliminating root causes, companies can reduce the costs associated with repeated customer service interactions and temporary fixes.
- **Long-term Improvement**: Understanding and addressing root causes leads to long-term improvements in products, services, and processes, enhancing the company's reputation and reliability.

# Business Case for ML Solution in Root Cause Prediction

## 1. Business Objective
The primary business objective is to enhance customer service efficiency and effectiveness by accurately predicting root causes of customer inquiries and issues. Implementing a machine learning solution for root cause prediction can significantly streamline customer service processes, enabling quicker and more accurate responses, and preemptively addressing potential issues.

## 2. Creation of Synthetic Data
Due to the highly specific and variable nature of root causes across different companies, I propose the creation of synthetic data. The synthetic data was created based on help centers (please see credits). The root causes are based on my 14 years of experience in customer service. This approach will allow to develop and test the model in a controlled environment, ensuring adaptability and scalability to real-world scenarios.

## 3. Proof of Concept Approach
For the initial proof of concept, complex integrations like APIs or specialized dashboards are not required. The focus is on demonstrating the core functionality and potential of the ML model in making accurate predictions.

## 4. Success Criteria
Success for the proof of concept is defined as obtaining at least one potential prediction that is correct and provides insightful results. This achievement would validate the model’s utility and open avenues for future enhancements and iterations of the pre-alpha version.

## 5. Ethical and Privacy Concerns
Ensuring compliance with GDPR and best practices in data privacy and ethics is paramount. Company data used for training and predictions must be handled securely, with appropriate measures to protect sensitive information.

## 6. Prediction Performance Level
A prediction accuracy of 96% is considered a fair and realistic target for the proof of concept. Achieving this level of accuracy would demonstrate the model's effectiveness and reliability.

## 7. Project Inputs and Intended Outputs
- **Inputs**: The primary input is the ‘Contact Driver’ data, which represents triggers or reasons for customer service interactions.
- **Outputs**: The intended output is the predicted root cause for each contact driver. Identifying these root causes accurately can lead to reduced costs, improved customer satisfaction, enhanced product quality, and increased sales.

## 8. Model Selection
Based on the data characteristics, a model like DistilBERT, which is efficient in processing natural language data, is suggested. Its ability to understand context and nuances in text makes it well-suited for this application.

## 9. Company Benefits
Implementing this ML solution offers multiple benefits:
- **Enhanced Customer Service**: Quick and accurate root cause identification improves response times and customer satisfaction.
- **Increased Efficiency**: Streamlining the process of handling customer inquiries reduces operational costs.
- **Data-Driven Insights**: The model can uncover patterns and trends in customer issues, guiding product and service improvements.
- **Competitive Advantage**: Improved customer service and efficiency can enhance the company's market position and reputation.

# Features of the Root Cause Analysis App

The Root Cause Analysis App is designed to streamline and enhance the process of identifying and addressing the underlying causes of customer service issues. Here are its key features:

## 1. Automated Root Cause Prediction
   - Utilizes a machine learning model, specifically DistilBERT for Natural Language Processing (NLP), to analyze customer inquiries and predict root causes.
   - Offers instant predictions, helping customer service department leads, product leads and the management to quickly understand and address the underlying issues in customer queries.

## 2. User-Friendly Interface
   - Simple and intuitive interface for users to input the description of customer service interactions (Contact Drivers).
   - Clear presentation of predicted root causes, allowing for easy interpretation and action.

## 3. Customizable Data Input
   - Flexible input fields for various types of customer service data, including Contact Driver Category, Product Category, and more.
   - Ability to handle diverse and complex customer inquiries.

## 4. High Prediction Accuracy
   - Aims for a high level of prediction accuracy (targeted at 96% for the proof of concept), ensuring reliable and useful root cause identifications.

## 5. Synthetic Data Adaptation
   - Capable of being trained on synthetic data to cater to the specific needs and contexts of different companies.
   - Adapts to various industries and service scenarios through tailored training.

## 6. Real-Time Analysis and Reporting
   - Provides real-time analysis of customer inquiries, offering immediate insights.

## 7. Deployment on Streamlit Share (for the proof of concept)
   - Deployed as an interactive web application on Streamlit Share, making it easily accessible for testing and demonstration.

   # Features left to implement

   - Self-Learning ML Model
   - Enhanced Product Categorization
   - Product Lifecycle Tracking
   - Enhanced image prediction (for defect products)

# How to use:

Basically, the initial scenario of building a root cause analysis for different industries is almost impossible. The diversity is too enormous. With my limited experience, what do I even think I'm doing trying to do that? Also, the data used here (900 root causes) is actually far too sparse for an ml model. However, despite all the decisions I made when training the model, the results are surprisingly good.
When making predictions, it is important to stay within the industries and product categories that can be displayed. Overly specific features or fancy English words will not (yet) work. When testing, it is worth trying a high level contact driver category as well as going into more detail. Currently, software root causes are included in the prediction. This is because all business types are always available online. Theoretically, software bugs must therefore be taken into consideration.
From a statistical point of view, the crux of a root cause is that it can be both the root cause with the highest and the lowest statistical relevance. For this reason, I do not give any percentages in the prediction, but leave it at an interpretation. The steps that can be assumed after the prediction are based on the Ishikawa diagram.

## Example Retail:
Lets say, you are a Retail - Supermarket and your customers complain about the milk quality aka the milk is sour.

![milk](/assets/documentation/retail.png "milk")

## Example E-Commerce:
Lets say you are an fashion online store and your customers complain about the button quality from that nice designer shirt.

![fashion](/assets/documentation/fashion.png "fashion")

## Example Marketing:
Lets say you are a marketeer and want to start your newsletter campaign but some of your contacts got bounced.

![marketing](/assets/documentation/marketing.png "marketing")

## Example Telecommunication:
Lets say your company offers telecommunication services and the customers complain about the poor 5G connection.

![telecommunication](/assets/documentation/telecommunication.png "telecommunication")

## Example Cars:
Last but not least, we try to test if underrepresented classes could be predicted.
Lets say your company selling cars and your customer have a problem with the airbag.

![underrepresented](/assets/documentation/underrepresented.png "underrepresented")

# User Stories

1. **Inspect Summary Page**
   - **Story**: As a user, I want to inspect a summary page so that I can get an overview of the app’s functionalities and understand how to navigate through different features effectively.

2. **Inspect Prediction Page**
   - **Story**: As a user, I want to be able to inspect the prediction page so that I can understand where and how to input my queries for root cause analysis.

3. **Choose Between Dropdown Menus**
   - **Story**: As a user, I want to choose options from dropdown menus for Business Type, Specialisation, and Product Category, so that I can tailor my query input to be more specific and relevant to my needs.

4. **Utilize Prediction Function**
   - **Story**: As a user, I want to use the prediction function by entering a detailed description of a customer service interaction so that I can receive a prediction of the likely root causes.

5. **View Bar Chart After Prediction**
   - **Story**: As a user, after receiving predictions, I want to see a bar chart visualizing the probabilities of different root causes so that I can better understand and interpret the prediction results.

6. **See Follow-ups After Prediction**
   - **Story**: As a user, I want to see suggested follow-up actions or detailed insights after a prediction is made so that I can take appropriate and informed actions based on the root cause analysis.

7. **Receive Error for Empty Prediction Text**
   - **Story**: As a user, if I accidentally leave the text input for prediction empty and attempt to get a prediction, I want to receive an error message so that I can be prompted to provide the necessary information for a valid query.

# Testing User Stories:

Tested every user story with Function > Expected result  > Action taken > Result

![testing](/assets/documentation/testing.PNG "testing")

# Forking LFS GitHub Repo and Deploying via Streamlit

## Forking a LFS GitHub Repository

### Step 1: Set Up Git LFS
- **Install Git LFS**: Download and install Git Large File Storage (LFS) from [git-lfs.github.com](https://git-lfs.github.com/).
- After installation, set up Git LFS by running `git lfs install` in your terminal.

### Step 2: Fork the Repository
- **Fork the Repository**: Click the "Fork" button in the upper right corner of the GitHub interface. This creates a copy of the repository in your GitHub account.

### Step 3: Clone the Forked Repository
- **Clone Locally**: Open your terminal, and use `git clone https://github.com/renebaumann3000/root_cause_analysis` to clone the repository to your local machine.
- **Initialize LFS**: Navigate to the cloned repository directory in your terminal and run `git lfs pull` to download the large files.

## Deploying via Streamlit

### Step 1: Set Up Streamlit
- **Install Streamlit**: Install Streamlit by running `pip install streamlit` in your terminal.

### Step 2: Prepare for Deployment
- **Test Locally**: Run `streamlit run main_app.py` in your terminal to test the app locally.

### Step 3: Sign Up for Streamlit Sharing
- **Create Streamlit Account**: Sign up at [Streamlit Sharing](https://streamlit.io/sharing).
- **Log In**: Log into your Streamlit account.

### Step 4: Deploy the App
- **Deploy**: In the Streamlit dashboard, choose the option to deploy a new app.
- **Link Repository**: Link your GitHub repository with the forked app to Streamlit.
- **Configure Deployment**: Enter any necessary configuration details like branch to deploy from and file paths.
- **Launch**: Deploy the app. Streamlit will provide you with a URL where your app is hosted.

# Credits:
Since there is no real world data on relevant root causes, I decided to create my own dataset (synthetic data), which is also part of the practice in data science. I created the data based on my 14 years of experience in customer service. I chose real help centers for inspiration. I have either worked in these industries myself or have them close to me in my network.

Help Centers I used for inspiration to create the dataset:

- https://en.zalando.de/faq?_rfl=de
- https://en.aboutyou.de/h?force-language=1
- https://www.hellofresh.com/about/faq
- https://www.amazon.com/gp/help/customer/display.html?nodeId=202040870
- https://www.kaufland.de/help/marketplace/
- https://www.rewe.de/service/fragen-und-antworten/
- https://www.walmart.com/help
- https://help.salesforce.com/s/products/service?language=en_US
- https://knowledge.hubspot.com/
- https://support.zendesk.com/hc/en-us
- https://support.pipedrive.com/en
- https://help.surveymonkey.com/en/
- https://support.stripe.com/
- https://support.checkout.com/hc/en-us
- https://help.revolut.com/de-DE/business/help/
- https://help.sap.com/docs/
- https://www.sw.siemens.com/en-US/support-services/
- https://www.bosch.com/contact/
- https://www.tesla.com/support
- https://geschaeftskunden.telekom.de/hilfe-und-service
- https://support.n26.com/en-eu
- https://www.comdirect.de/cms/fragen-und-antworten.html

Additional tutorials I used for self-learning:
- https://towardsdatascience.com/bert-roberta-distilbert-xlnet-which-one-to-use-3d5ab82ba5f8
- https://towardsdatascience.com/from-raw-text-to-model-prediction-in-under-30-lines-of-python-32133d853407
