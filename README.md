# django-visualiser

# Project Setup and Access Guide

This guide will walk you through setting up the project locally. Please follow these steps carefully for a smooth setup.

## Local Setup
1. Clone the project repository to your local machine.
bash command
```
git clone https://github.com/codegeasscode/django-visualizer.git
cd /data_visualizer

```
2. Build Docker Image
bash
```
sudo docker build -t django-visualizer .

```
3. Run the docker container
bash
```
sudo docker run -p 8000:8000 django-visualizer

```
4. access the url: http://127.0.0.1:8000/visualise/

5. Example Payload:
```
        [
            {
                "id": "1",
                "name": "Example Bar",
                "data": [[1, 2, 3], [10, 20, 30]],
                "type": "bar"
            },
            {
                "id": "2",
                "name": "Example Table",
                "data": [{"Name":"Alok", "Dept":"Backend"}, {"Name":"Binu", "Dept":"Manager"}, {"Name":"Rahul", "Dept":"Frontend"}],
                "type": "table"
            }
        ]

```

