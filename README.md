# Aplaybox 每日检查器

该项目自动化完成 Aplaybox 网站的每日登录和检查，目标页面为 [Aplaybox 模型详情](https://www.aplaybox.com/details/model/xfyv7yIWHaxH)。

## 功能
- 使用存储的 Cookie 每日登录+浏览作品获取10积分 半年过去能直升lv3.
- 通过 GitHub Actions 自动运行。

## 设置

### 前置条件
- 已安装 Python 3.x。
- Aplaybox 网站的有效 Cookie。

### 本地设置
1. 克隆此仓库：
   ```bash
   git clone https://github.com/Moeary/Aplaybox_Checker
   cd Aplaybox_Checker
   ```
2. 安装依赖：
   ```bash
   python -m pip install --upgrade pip
   pip install undetected-chromedriver selenium
   ```
3. 设置 `APLAYBOX_COOKIE` 环境变量：
   ```bash
   set APLAYBOX_COOKIE=你的_cookie_字符串
   ```
4. 运行脚本：
   ```bash
   python aplaybox_checker.py
   ```

### GitHub Actions 设置
1. Fork 此仓库。
2. 前往 GitHub 仓库的 `Settings > Secrets and variables > Actions`。
3. 添加一个名为 `APLAYBOX_COOKIE` 的新密钥，并粘贴你的 Cookie 字符串。
4. 工作流将每天在 UTC 时间午夜运行。

## 文件
- `aplaybox_checker.py`：用于登录和检查页面的主脚本。
- `.github/workflows/daily_check.yml`：用于自动化的 GitHub Actions 工作流。

## 注意事项
- 确保你的 Cookie 有效并定期更新。
- 脚本使用 Selenium 和 undetected-chromedriver 绕过机器人检测。