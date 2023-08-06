# 1.导入方法

```cmd
pip install flask-markdown
```

```python
    from flask import Flask
    from flask-markdown import flask_markdown
    app=Flask(__name__)
    app.config["markdown_path"]="./markdown"
    md=flask_markdown(app)
```

# 2.函数使用

确保目录结构为以下结构

> app.py

> markdown **为config中的路径**

## 2.1 markdown_to_html

使用方法 

```html
    {{ md.markdown_to_html("markdown代码") }}
```
_确保你已经导入本库_

## 2.2 render_markdown

使用方法

```python
    @app.route("/")
    def index():
        return render_markdown("在markdown_path路径下的文件.md")
```
_确保你的markdown_path无误_