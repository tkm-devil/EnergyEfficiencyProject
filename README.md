# Energy Efficiency Project

The Energy Efficiency Prediction project is a machine learning application designed to estimate the heating load and cooling load of buildings based on various architectural and environmental factors. It leverages Flask, a web framework in Python, to provide a user-friendly interface for inputting building characteristics and receiving predicted load values.

The project is built with a modular and organized code structure, allowing for easy maintenance and scalability. It consists of several key components, including data preprocessing, model training, and prediction generation. The data preprocessing module applies necessary transformations and feature engineering techniques to prepare the input data for the prediction model. The model training module utilizes machine learning algorithms to train models on historical data, enabling accurate load predictions.

With the Flask integration, users can access the Energy Efficiency Prediction application through a web browser. The application presents a form where users can input the relevant architectural parameters of a building, such as relative compactness, surface area, wall area, roof area, overall height, orientation, glazing area, and glazing area distribution. Upon form submission, the backend processes the input, applies the pre-trained prediction model, and generates the estimated heating load and cooling load values.

The project includes Jupyter notebooks for data exploration, model training, and evaluation, providing transparency and reproducibility. The README file offers detailed instructions on setting up the application environment and deploying the Flask web server.

In summary, the Energy Efficiency Prediction project combines machine learning techniques, Flask web integration, and a well-structured codebase to deliver a practical solution for estimating the heating load and cooling load of buildings. It offers an intuitive user interface and facilitates accurate predictions to assist in energy-efficient building design and optimization.

## Workflow

The project follows a typical workflow consisting of the following steps:

1. Data Collection - The data was collected from UCI Machine Learning Repository. For more information please visit https://archive.ics.uci.edu/dataset/242/energy+efficiency.

2. Data Preprocessing - Use the provided Jupyter notebooks to preprocess the data. This step includes cleaning the data, handling missing values, feature engineering, and scaling the features.

3. Model Training - Train the prediction models using the preprocessed data. The project includes pre-trained models, but you can also retrain the models using your own datasets if desired. Refer to the provided Jupyter notebooks for details on model training.

4. Web Application Setup: Install the required dependencies and set up the Flask web application. The project includes the necessary files and folder structure for running the web application locally.

5. Run the Web Application: Start the Flask server and access the application through a web browser. The application will present a form where users can input the building characteristics. Upon form submission, the backend will process the input, apply the prediction model, and display the estimated heating load and cooling load values.

6. Deployment: Once you're satisfied with the local testing, you can deploy the web application to a production server. Refer to the Flask documentation for instructions on deploying Flask applications.

## Getting Started

These instructions will give you a copy of the project on your local machine for testing and development purposes.

### Prerequisites

Before running the project, ensure you have the following software installed:

Python 3.x: Download and install Python

### Installing

Follow the steps below to setup the development environment in your local machine.
Run the following command in command prompt or terminal

1. Clone the repository:

```
git clone https://github.com/tkm-devil/EnergyEfficiencyProject.git
cd EnergyEfficiencyProject
```

2. Create a virtual environment and activate it:

```
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Start the Flask application:

```
python application.py 
```

5. Access the application in your web browser at http://127.0.0.1:5000

## Usage

1. Open your web browser and navigate to http://127.0.0.1:5000
2. Click the "Go to form" button
3. Fill in the form with the relevant architectural parameters of the building.
4. Click the "Submit" button.
5. The application will process the input and display the predicted heating load and cooling load values.

## Deployment 

The Energy Efficiency Prediction application has been successfully deployed to AWS App Runner, but before that, it went through a CI/CD pipeline, which involved the following steps:

1. Containerization with Docker: The application was containerized using Docker, which allowed us to package the application and its dependencies into a single container image.

2. CI/CD Setup: We set up a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions. The CI/CD pipeline automatically triggered a build process whenever changes were pushed to the main branch of the GitHub repository.

3. GitHub Actions Workflow: The CI/CD pipeline used a GitHub Actions workflow with different stages and jobs. The workflow included steps to build the Docker image, push the image to Amazon Elastic Container Registry (ECR), and deploy the application to AWS App Runner.

4. Amazon Elastic Container Registry (ECR): We used ECR as a secure and scalable container registry service provided by AWS. The CI/CD pipeline pushed the Docker container image to ECR, making it available for deployment.

5. AWS App Runner Setup: The AWS App Runner service was set up in the AWS Management Console. We specified the ECR container image as the source and provided the necessary configurations.

6. Deployment Configuration: During the setup, we defined the deployment configuration, including the number of instances, CPU, and memory allocation.

7. Start AWS App Runner: Once the configuration was completed, we started the AWS App Runner service, and the application was automatically deployed to the specified number of instances.

8. Continuous Deployment: The CI/CD pipeline was configured to automatically update the application in AWS App Runner whenever a new image was pushed to the specified ECR repository. This enabled continuous deployment of the application.

9. Monitoring and Scaling: AWS App Runner automatically handled the scaling of instances based on demand, ensuring that the application could handle varying levels of traffic.

10. Accessibility: The deployed application is accessible via the public URL provided by AWS App Runner. Users can access the Energy Efficiency Prediction application through their web browsers.

The CI/CD pipeline provided an automated and efficient way to deploy changes to the application while maintaining consistency and reliability. It eliminated manual deployment processes, reduced the risk of errors, and allowed for faster and more frequent updates.

Currently I have Paused the application due to charges of aws app runner.

## Built with

* [Flask](https://flask.palletsprojects.com/en/2.3.x/) - The web framework used
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) - Simple integration of Flask and WTForms
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/) - Form validation and rendering library
* [Numpy](https://numpy.org/) - Data Manipulation library
* [Pandas](https://pandas.pydata.org/) - Data Manipulation library
* [Matplotlib](https://matplotlib.org/) - Data Visualization library
* [Seaborn](https://seaborn.pydata.org/) - Data Visualization library
* [Scikit-learn](https://scikit-learn.org/stable/) - Machine learning library

## Contributing

Contributions are welcome! If you have any ideas or improvements, please open an issue or submit a pull request.

## Authors

* **Tilak Kishor Mishra** - *Initial work* - [tkm-devil](https://github.com/tkm-devil)

## License

This Project is licensed under MIT license - see the [license](https://opensource.org/license/mit/) for more details.

## Acknowledgements

* The UCI Machine Learning Repository for providing the dataset.