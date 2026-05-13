
<img width="1302" height="753" alt="image" src="https://github.com/user-attachments/assets/c3c08491-094d-4464-8271-486e58dcc904" />


# 🤖 AI 智能伴侣对话平台
> 一款支持角色自定义 + 多会话管理 + 持久化存储的 AI 聊天应用

## 项目介绍
基于 Python + Streamlit + DeepSeek 大模型开发，实现可自由定制角色的沉浸式对话体验。
用户可自定义伴侣昵称与性格，系统自动生成对应风格的回复；所有会话自动保存，支持历史记录加载、新建与删除，搭配流式输出效果，接近真实聊天体验。

## 工具
- **前端交互**：Streamlit（页面构建、会话状态管理、流式输出）
- **AI 模型**：DeepSeek API（对话生成）
- **数据存储**：JSON 文件本地持久化
- **工具模块**：os、datetime（文件管理、时间戳生成）
- **开发语言**：Python

## 项目亮点
- 🎭 **角色自定义**：自由设置昵称与性格，AI 自动匹配对话风格
- 📚 **多会话管理**：支持新建、加载、删除历史会话
- ⚡ **流式输出**：AI 回复逐字显示，交互更自然
- 💾 **本地持久化**：所有对话自动保存为 JSON 文件
- 🎨 **简洁 UI**：基于 Streamlit 快速构建美观易用界面

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



