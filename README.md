## URL Shortener Application with Docker and Kubernetes
This project demonstrates the development of a URL shortener application, Dockerizing the application, and deploying it on Kubernetes. The URL shortener allows users to shorten long URLs and provides a redirect service when the shortened URL is accessed.


### Task 1: URL Shortener Application
#### Development Environment Setup
1. Choose the programming language and framework of your choice. In this project, we used Python with Django.
2. Set up a virtual environment for your project.
   ```bash
   python -m venv venv
   source venv/bin/activate  # Activate the virtual environment
   ```
3. Install Django
   ```bash
   pip install django
   ```
#### URL Shortener Application
1. Design the application to accept a URL as input and store it in a database.
2. Implement a function that generates a unique short code for each URL, accounting for potential collisions.
3. Store the original URL and its corresponding short code in the database.
4. Implement a function that retrieves the original URL when provided the unique short code and redirects the user.
5. Create a simple UI for inputting URLs and displaying the shortened URLs.

#### Run the Application Locally
1. Run the Django development server to test the application locally.
   ```bash
   python manage.py runserver
   ```
#### Access the URL Shortener
* Open your web browser and navigate to http://127.0.0.1:8000/ to access the URL shortener application.
* You should see the input form where you can enter a URL and get a shortened URL.

### Task 2: Dockerize the Application
#### Docker Configuration
1. Create a Dockerfile for your application.
   ```path
   "urlshortener_project\Dockerfile"
   ```
#### Build and Run the Docker Image
1. Build the Docker image from the Dockerfile.
   ```bash
   docker build -t urlshortener-app .
   ```
2. Run the Docker Container.
   ```bash
   docker run -d -p 8000:8000 --name urlshortener-container urlshortener-app
   ```
* Your Django application should now be running inside a Docker container. You can access it by visiting **http://localhost:8000** in your web browser.
* This setup allows you to package and run your Django application consistently using Docker, making it easier to deploy and manage in various environments.

### Task 3: Kubernetes Deployment
1. Create Kubernetes Deployment and Service configurations for your application.
   - deployment.yaml
   - service.yaml
   ```path
   "urlshortener_project\kubernetes"
   ```
#### Set Up Kubernetes Environment
1. Install Minikube and start a local Kubernetes cluster.
   - If you haven't already, install Minikube on your local machine. You can follow the official Minikube documentation for installation instructions: https://minikube.sigs.k8s.io/docs/start/

2. Once Minikube is installed, start a local Kubernetes cluster by running:
   ```bash
   minikube start
   ```
3. Apply the Kubernetes configurations.
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```
4. Retrieve the NodePort assigned to the service.
   ```bash
   kubectl get svc urlshortener-service
   ```
5. Access your application using the Minikube IP address and the NodePort number. Find the Minikube IP using.
   ```bash
   minikube ip
   ```
* Then, in your web browser, navigate to "http://minikube-ip:nodeport" Replace "minikube-ip" with your Minikube IP and "nodeport" with the NodePort number.

### Conclusion
This project demonstrates the complete process of creating a URL shortener, Dockerizing the application, and deploying it on Kubernetes. Security considerations were not explicitly mentioned but can be addressed by using HTTPS for data transmission and ensuring proper access controls. 
