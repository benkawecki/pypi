from pyramid.view import view_config
from pyramid.request import Request
import pyramid.httpexceptions as x


@view_config(
    route_name="package_details", renderer="pypi:templates/packages/details.pt"
)
@view_config(
    route_name="package_details/", renderer="pypi:templates/packages/details.pt"
)
def package_details(request: Request):

    package_name = request.matchdict.get("package_name")
    if not package_name:
        raise x.HTTPNotFound()

    return {"package_name": package_name}


@view_config(route_name="releases", renderer="pypi:templates/packages/releases.pt")
@view_config(route_name="releases/", renderer="pypi:templates/packages/releases.pt")
def releases(request: Request):

    package_name = request.matchdict.get("package_name")
    if not package_name:
        raise x.HTTPNotFound()

    return {"package_name": package_name, "releases": []}


@view_config(
    route_name="release_version", renderer="pypi:templates/packages/release_details.pt"
)
def home_index(request: Request):

    package_name = request.matchdict.get("package_name")
    release_version = request.matchdict.get("release_version")

    if not package_name:
        raise x.HTTPNotFound()

    return {
        "package_name": package_name,
        "release_version": release_version,
        "releases": [],
    }
