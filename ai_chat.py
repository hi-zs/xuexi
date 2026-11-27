# 第一个 AI 程序：调用 DeepSeek 大模型对话
import requests

# 1. 从 .env 文件读取 API Key
def load_api_key():
    with open(".env", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1]
    return ""

api_key = load_api_key()

# 2. DeepSeek 的接口地址（固定）
url = "https://api.deepseek.com/chat/completions"

# 3. 请求头（固定不变，定义一次即可）
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
}

# 4. 循环对话，直到用户输入"退出"
while True:
    # 获取用户输入
    question = input("\n你：")
    if question == "退出":
        print("再见！")
        break

    # 打包请求
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": question}
        ],
    }

    # 发送请求
    response = requests.post(url, json=data, headers=headers)

    # 解析并打印回答
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    print("AI 回答：", answer)
