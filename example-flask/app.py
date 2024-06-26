import logging

from flask import Flask, jsonify

from settings import get_settings
from .nacos import init_nacos

logger = logging.getLogger(__name__)

app = Flask(__name__)
init_nacos()


@app.route('/')
def root():
    # 这里需要 依赖注入
    settings = get_settings()
    logger.error(settings)

    return jsonify({
        "message": "flask",
        "settings": settings.model_dump(),
    })


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
