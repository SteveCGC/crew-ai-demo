# crew-ai-demo

学习 [CrewAI](https://docs.crewai.com/) 的项目。

## 目录结构

- [demos/](demos/)：学习各个知识点用的小 demo（单 Agent、多 Agent、Tools、Flow 等）
- [projects/](projects/)：更完整的项目实战

## 环境准备

项目使用 Python 3.13 虚拟环境（CrewAI 目前对 3.14 支持还不完善）。

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 配置百炼 API Key

1. 复制 `.env.example` 为 `.env`
2. 到[阿里百炼控制台](https://bailian.console.aliyun.com/)获取 API Key，填入 `DASHSCOPE_API_KEY`

```bash
cp .env.example .env
```

> 如果你用的是国际站(International)账号，把 `.env` 里的 `DASHSCOPE_BASE_URL` 换成
> `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`。

## 运行 demo

```bash
source .venv/bin/activate
python demos/bailian_basic.py
```

`demos/bailian_basic.py` 创建了一个"科普作家"角色的 Agent，执行一个任务（用 3 句话解释 CrewAI），
并打印最终结果。默认使用 `qwen-plus` 模型，可以在 `.env` 里改 `DASHSCOPE_MODEL`
换成 `dashscope/qwen-turbo` / `dashscope/qwen-max` 等，无需改代码。
