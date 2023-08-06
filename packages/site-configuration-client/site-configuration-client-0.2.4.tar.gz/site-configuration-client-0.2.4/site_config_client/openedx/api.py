"""
External Open edX Python API helpers goes here.

### API Contract:
 * Those APIs should be stable and abstract internal changes.

 * Non-stable and internal APIs should be placed in other modules.

 * The parameters of existing functions should change in a backward compatible way:
   - No parameters should be removed from the function
   - New parameters should have safe defaults
 * For breaking changes, new functions should be created
"""

try:
    from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
except ImportError:
    # Silence the initial import error, but runtime errors will occur in tests and non-Open edX environments.
    # In tests, `configuration_helpers` should be mocked via `override_site_config()`
    pass


def get_current_configuration(site_configuration=None, site=None):
    """
    Gets current site configuration with possibility to override.

    This function can be used in both Studio and test contexts.
    """
    if site_configuration:
        return site_configuration
    elif site:
        return site.configuration
    else:
        return configuration_helpers.get_current_site_configuration()


def get_admin_value(name, default=None, site_configuration=None, site=None):
    """
    Get `admin` setting from the site configuration service.

    Proxy for `site_configuration.get_admin_setting` until site_configuration is deprecated.
    """
    site_configuration = get_current_configuration(site_configuration=site_configuration, site=site)

    if site_configuration:
        return site_configuration.get_admin_setting(name, default)
    return default


def get_secret_value(name, default=None, site_configuration=None, site=None):
    """
    Get `secret` setting from the site configuration service.

    Proxy for `site_configuration.get_secret_value` until site_configuration is deprecated.
    """
    site_configuration = get_current_configuration(site_configuration=site_configuration, site=site)
    if site_configuration:
        return site_configuration.get_secret_value(name, default)
    return default


def get_setting_value(name, default=None, site_configuration=None, site=None):
    """
    Get `setting` setting from the site configuration service.

    Proxy for `site_configuration.get_value` until site_configuration is deprecated.
    """
    site_configuration = get_current_configuration(site_configuration=site_configuration, site=site)
    if site_configuration:
        return site_configuration.get_value(name, default)
    return default


def get_page_value(name, default=None, site_configuration=None, site=None):
    """
    Get `page` setting from the site configuration service.

    Proxy for `site_configuration.get_page_content` until site_configuration is deprecated.
    """
    site_configuration = get_current_configuration(site_configuration=site_configuration, site=site)
    if site_configuration:
        return site_configuration.get_page_content(name, default)
    return default
