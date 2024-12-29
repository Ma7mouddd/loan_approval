FROM python:3.12  

# Install Python packages
RUN pip install --no-cache-dir pandas numpy seaborn matplotlib scikit-learn scipy

# Set up working directory
WORKDIR /project
COPY . /project

CMD ["/bin/bash"]  # Default shell for the container
