from datetime import timedelta
from functools import partial
from typing import Callable, Dict

from django.conf import settings
from django.db.models import QuerySet
from django.contrib.auth import get_user_model

from drf_temptoken import models

User = get_user_model()

TMP_TOKEN_AUTH_HEADER: str = 'Authorization'

TMP_TOKEN_HEADR_PREFIX: str = 'TMP'

TMP_TOKEN_TIME_DELTA_KWARGS: Dict[str, int] = {
    'days': 7
}

get_header_prefix: Callable[[], str] = lambda: getattr(settings, 'TMP_TOKEN_HEADR_PREFIX', TMP_TOKEN_HEADR_PREFIX) + ' '

get_query_param: Callable[[], str] = partial(getattr, settings, 'TMP_TOKEN_QUERY_PARAM', None)

get_time_delta: Callable[[], Dict[str, int]] = partial(timedelta, **getattr(settings, 'TMP_TOKEN_TIME_DELTA_KWARGS', TMP_TOKEN_TIME_DELTA_KWARGS))

get_user_tokens: Callable[[User], QuerySet] = lambda user: models.TempToken.objects.filter(user=user)

create_token: Callable[[User], models.TempToken] = lambda user, **kwargs: models.TempToken.objects.create(user=user, **kwargs)
