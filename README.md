**Structure du projet :**

```
docker-compose-app/
├── .env
├── .gitignore
├── README.md
├── docker-compose.yml
│
├── fastapi_app/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── streamlit_app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── prometheus/
│   └── prometheus.yml
│
├── grafana/
│   ├── dashboards.py
│   │   ├── dashboards.json
│   │   └── dashboards.yml
└── └── datasources
        └── datasources.yml
```

**Fichier `.env` :**

```
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=admin
FASTAPI_PORT=8080
STREAMLIT_PORT=8501
PROMETHEUS_PORT=9090
GRAFANA_PORT=3000
```


**FastAPI (`fastapi_app/requirements.txt`) :**

```
fastapi
uvicorn
pydantic
prometheus-client
python-multipart
```

**Streamlit (`streamlit_app/requirements.txt`) :**

```
streamlit
requests
loguru
```
