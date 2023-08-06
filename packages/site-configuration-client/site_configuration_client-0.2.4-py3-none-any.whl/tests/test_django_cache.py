"""
Tests for Cache
"""
import pytest


@pytest.fixture
def django_cache_adapter(settings):
    # Local import to avoid test failures for non-openedx tests
    from site_config_client.django_cache import DjangoCache

    settings.CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }
    return DjangoCache(cache_name='default', cache_timeout=100)


@pytest.mark.django
def test_empty_get(django_cache_adapter):
    cache_key = 'client.040e0ec3-2578-4fcf-b5db-030dadf68f30.live'
    assert django_cache_adapter.get(key=cache_key) is None


@pytest.mark.django
@pytest.mark.parametrize('params,expected_timeout,message', [
    ({'cache_timeout': None}, 300, 'None defaults to 300'),
    ({'cache_timeout': ''}, 300, 'Empty string --> 300'),
    ({'cache_timeout': '600'}, 600, 'string is converted to int'),
    ({'cache_timeout': 800}, 800, 'int 800 is kept as-is'),
])
def test_timeout(params, expected_timeout, message):
    """
    Ensure `cache_timeout` is can be configured with both int and str with sane defaults.
    """
    from site_config_client.django_cache import DjangoCache
    cache = DjangoCache(cache_name='default', **params)
    assert cache.cache_timeout == expected_timeout, message


@pytest.mark.django
def test_set_get(django_cache_adapter):
    configs = {
     "site": {
            "uuid": "77d4ee4e-6888-4965-b246-b8629ac65bce",
            "domain_name": "croissant.edu",
            "tier": "trial",
            "always_active": False,
            "subscription_ends": "2021-10-31T16:44:45+0000",
            "is_active": True},
     "status": "live",
     "configuration": {
            "admin": [
                {
                    "name": "features",
                    "value": ["bi_connector", "google_tag_manageer"]
                }
            ],
            "css": [
                {
                    "name": "accent-font",
                    "value": "monospace"
                }
            ],
            "page": [],
            "setting": [
                {
                    "name": "PLATFORM_NAME",
                    "value": "Momofuku Academy"
                }
            ],
            "integration": [],
            "secret": [
                {
                    "name": "SEGMENT_KEY",
                    "value": "orc"
                },
                {
                    "name": "SECRET_KEY",
                    "value": "hobbit"
                }
            ]}
    }
    cache_key = 'client.040e0ec3-2578-4fcf-b5db-030dadf68f30.live'
    django_cache_adapter.set(key=cache_key, value=configs)
    assert django_cache_adapter.get(key=cache_key) == configs
