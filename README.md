<div align="center">

# 自强 Studio Django 后端工程模板

_✨ 武汉大学自强网络综合技术社团 · 后端标准模板 ✨_

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" alt="python">
  <img src="https://img.shields.io/badge/Django-4.2%2B-blue" alt="django">
  <img src="https://img.shields.io/badge/Linter-Ruff-blue" alt="ruff">
  <img src="https://img.shields.io/badge/Package%20Manager-uv-blue" alt="uv">
  <br />
  <a href="https://github.com/ZiqiangStudio/zq_django_template/actions/workflows/cicd.yml">
    <img src="https://github.com/ZiqiangStudio/zq_django_template/actions/workflows/cicd.yml/badge.svg?branch=main" alt="CI/CD">
  </a>
</p>
</div>

## 🚀 快速建项

本项目为 **GitHub Template 仓库**：
1. 点击 GitHub 页面右上角的 **[Use this template]** -> **[Create a new repository]**。
2. 输入您的新项目仓库名（如 `zq_score_backend`），完成创建。
3. 克隆新仓库到本地即可开始开发。

---

## 🛠️ 本地开发上手

### 1. 初始化环境（使用 uv）

```bash
# 1. 创建 Python 3.12 虚拟环境并激活
uv venv --python 3.12
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2. 安装所有依赖
uv pip install -r pyproject.toml -e ".[dev,test]"
```

### 2. 启动服务（零配置开箱即用）

本地未配置外部环境变量时，项目默认自动使用 SQLite 与内存缓存，直接启动即可：

```bash
python manage.py migrate
python manage.py runserver
```

若需定制本地环境变量（如连接本地 MySQL / Redis / Sentry）：

```bash
cp config/.env.example config/.env
```

### 3. 代码检查与测试

```bash
# 代码规范检查 (Ruff)
ruff check server

# 运行单元测试
pytest
```

---

## 📦 自动化部署 (zq-deploy)

项目内置 `.github/workflows/cicd.yml`，推送至 `main` 分支时将自动调用组织中央部署流水线 (`zq-deploy`) 完成 Docker 构建与发布。
- **端口契约**：容器内部标准监听 `8000` 端口。
- **域名绑定**：由项目负责人在 `.github/workflows/cicd.yml` 中的 `domain:` 字段直接填入，直观透明。
- **生产配置**：生产环境的 RDS 数据库、Redis 连接串与密钥由部署平台统一挂载注入，代码仓库零敏感信息。
