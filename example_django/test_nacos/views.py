import logging

from django.conf import settings
from django.http import JsonResponse
from django.views.generic.list import BaseListView

logger = logging.getLogger(__name__)


class NacosView(BaseListView):
    def get(self, request, *args, **kwargs):
        logger.error(settings.__dict__)

        logger.error(settings.OPENAI)

        return JsonResponse({
            "message": "fastapi",
            "settings": settings.OPENAI,
        })
