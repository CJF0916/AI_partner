# 🤖 AI 智能伴侣对话平台
> 一款支持多会话记忆与角色自定义的 AI 对话应用，模拟真实伴侣的聊天体验。

---

## ✨ 项目亮点
- 🎭 **角色自定义**：可自由设置伴侣昵称与性格，AI 会根据设定生成专属对话风格
- 📚 **多会话管理**：支持新建、加载、删除会话，对话记录自动持久化保存
- ⚡ **流式对话输出**：AI 回复逐字生成，模拟真实聊天的打字感
- 💾 **JSON 持久化**：所有会话数据本地存储，重启应用后可无缝恢复
- 🎨 **极简交互界面**：基于 Streamlit 构建，侧边栏可直接管理会话与角色信息

---

## 🛠️ 技术栈
| 技术/工具 | 用途 |
| :--- | :--- |
| Python | 核心业务逻辑实现 |
| Streamlit | 前端页面构建与交互管理 |
| DeepSeek API | 大模型对话生成 |
| JSON | 会话数据持久化存储 |
| os / datetime | 文件操作与时间戳生成 |

---

## 🚀 快速开始

### 1. 环境准备
```bash
git clone https://github.com/CJF0916/AI_partner.git
cd AI_partner
pip install streamlit openai python-dotenv

ai-intelligent-companion/
├── AI应用/
│   ├── sessions/          # 会话JSON文件存储目录（自动创建）
│   ├── resources/         # 静态资源（如logo图片）
│   └── ai_partner03.py    # 项目主程序
├── .env                   # API密钥配置文件
└── README.md              # 项目说明文档
