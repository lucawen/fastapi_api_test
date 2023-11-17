# Rate Api

## Overview
Rate API is a RESTful web service that provides a endpoint to convert monetary values.
It is built using FastAPI, dependency-injector and Docker.


## Requirements
Before running it, you need to already have the `Docker` and `Docker Compose` installed in your machine.

## Running
To run the API, follow these steps:

1. Clone the repository
    ```$ git clone https://github.com/lucawen/fastapi_api_test```
2. Configure the API environment.
    This is the `.env` file content:
    ```
    COIN_API_TOKEN=111230409c1f8f739be901cfasfa16916a
    ```
    As mandatory, we just have the `COIN_API_TOKEN` environment. (This is a dummy env, as we are not using a api that uses api keys).
    You can check the `.env.example` to see all available environment variables.
3. Run the containers:
    ```$ make run```

After running all the requirements, you can access the application over `http://localhost:8000/`

## Usage
The API provides the following endpoints:

- `GET /api/v1/conversion/request`: request a rate conversion between two currencies. 
Example:
`http://127.0.0.1:8000/api/v1/conversion/request?value_from=BTC&value_to=USD&amount=10`

If you are running the application, you can access `http://localhost:8000/redoc/` to access a interactive documentation with more detailed information.

# Development
This api is ready to accept debug from VSCODE. You just need to run these steps:

1. Create a file `launch.json` inside the `.vscode` folder (if the folder does not exist, create it) with the content:
   ```
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: FastAPI",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "localhost",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/service"
                    }
                ]
            }
        ]
    }
    ```

2. Instead of running the api over `make run`, run it using this command:
    ```$ make debug```

3. At the `Run and Debug` page on VSCODE, start the debug option.