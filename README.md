

```bash
~/Desktop $ mkdir streamlit_dev
~/Desktop $ cd streamlit_dev
~/Desktop/streamlit_dev $ uv init
~/Desktop/streamlit_dev $ code .
```

```bash
~/Desktop/streamlit_dev $ uv venv
~/Desktop/streamlit_dev $ source .venv/bin/activate
```


## コンテナ作成

```bash
~/Desktop/streamlit_dev $ uv pip install streamlit pandas matplotlib
```

```bash
~/Desktop/streamlit_dev $ uv pip freeze > requirements.txt
```

```bash
~/Desktop/streamlit_dev $ docker build household_budget_app .
```

```bash
 ~/Desktop/streamlit_dev $ docker run -p 8501:8501 household_budget_app
```

## コンテナをAzureにプッシュ
```bash
 ~/Desktop/streamlit_dev $ docker tag household:latest container0603.azurecr.io/household:latest
```

```bash
 ~/Desktop/streamlit_dev $ docker push container0603.azurecr.io/household:latest
```

## App Serviceの作成


az acr create --name <ACR_NAME> --resource-group <RESOURCE_GROUP> --sku Basic
# streamlit-tutorial
