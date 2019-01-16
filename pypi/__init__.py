from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:

        config.include(init_routing)
        print("hello")
        config.include("pyramid_chameleon")

    return config.make_wsgi_app()


def init_includes(config):
    config.include("pyramid_chameleon")


def init_routing(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("about", "/about")
    config.scan()
