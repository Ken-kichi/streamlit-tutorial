

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
~/Desktop/streamlit_dev $ uv pip install streamlit pandas matplotlib azure-cosmos azure-identity
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

```bash
az acr create --name <ACR_NAME> --resource-group <RESOURCE_GROUP> --sku Basic
```

コンテナアプリの確認
```bash
az containerapp list --output table
```
環境変数の設定方法
```
az containerapp update \
  --name my-app \
  --resource-group my-group \
  --set-env-vars "AZURE_ENDPOINT=xxxxx" "AZURE_KEY=xxxxx"
```

✅ 【方法1】Azure Portalでの手順（GUI）
🔐 Key Vault 側の設定
1. Azure Key Vault を作成（していなければ）
2.AZURE_KEY という名前でシークレットを登録（値は Cosmos DB のキー）

🧾 Container App 側の設定
1.Azure Portal → コンテナアプリを開く
2.左メニューから 「シークレット」 を選択
3.「+ 追加」で以下を入力：
    - 名前：AZURE_KEY
4.Key Vault のシークレットを使用 にチェック
5.Key Vault を選択
6.シークレット名を選択（例：AZURE_KEY）
6.「保存」
7.次に、**「環境変数」**に移動
    - 名前：AZURE_KEY
    - 値の種類：シークレット
    - シークレット：AZURE_KEY（先ほどのシークレット）

保存・再起動すれば反映されます。
