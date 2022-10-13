# Check-Out Rasa Assistant

Requirements:
In order to set up the project locally, you need to first satisfy the following requirements:

1. Docker installed on your computer
    Here is the installation guide for docker [Install Docker Engine | Docker Documentation](https://docs.docker.com/engine/install/)
2. Docker-compose install on your computer
    Here is the installation guide for docker-compose [Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)

## Run

1. Run all three modules
   For Linux or Mac users, you can simply run the deploy.sh script to run the system. The deploy.sh script is for the Jenkins pipeline to automatically deploy the latest system. In this case, you can use it to run the system as well.
   Open your terminal and enter:

   ```shell
   cd path-to-the-repository/
   chmod +x deploy.sh
   sudo ./deploy.sh
   ```

   For Windows users, you need to manually execute the commands:

    ```shell 
    cd path-to-the-repository/
    sudo docker-compose build
    sudo docker-compose up -d
    ```

After running these commands for every repository,  you can use:
`docker ps`
to see all the running containers, there should have the following container running:

- checkout-rasa_chatbot-rasa_1
- checkout-rasa_chatbot-rasa-action_1

Note: it takes about 1 minute to load the model, you can use: 
`docker logs [id of the checkout-rasa container]`
to check if it is correctly loaded

After the Assistant correctly loaded, you should be able to get a hi message from rasa at
http://localhost:5005/

