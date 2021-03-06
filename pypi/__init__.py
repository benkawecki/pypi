from pyramid.config import Configurator
from pypi.data.db_session import DbSession
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include(init_db)
        config.include(init_routing)
        config.include("pyramid_chameleon")

    return config.make_wsgi_app()


def init_includes(config):
    config.include("pyramid_chameleon")


def init_routing(config):
    config.add_static_view("static", "static", cache_max_age=3600)

    # ################### HOME ###################
    config.add_route("home", "/")
    config.add_route("about", "/about")

    # ################## PACKAGES ################
    config.add_route(
        "popular",
        "{num}",
        custom_predicates=[lambda info, _: info["match"].get("num", "").isdigit()],
    )
    config.add_route("package_details", "project/{package_name}")
    config.add_route("package_details/", "project/{package_name}/")

    config.add_route("releases", "/project/{package_name}/releases")
    config.add_route("releases/", "/project/{package_name}/releases/")

    config.add_route(
        "release_version", "/project/{package_name}/releases/{release_version}"
    )

    # ################ ACCOUNT ###################
    config.add_route("account_home", "/account")
    config.add_route("login", "/account/login")
    config.add_route("register", "/account/register")
    config.add_route("logout", "/account/logout")

    # ################ CMS #######################
    config.add_route("cms_page", "*subpath")
    config.scan()



def init_db(_):
    db_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'db',
            'pypi.sqlite'
        )
    )

    DbSession.global_init(db_file)
