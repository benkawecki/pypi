from pyramid.view import view_config
from pyramid.request import Request
import pyramid.httpexceptions as x

fake_db = {"history": {"page_title": "History", "page_details": "blah blah blah"}}


@view_config(route_name="cms_page", renderer="pypi:templates/cms/page.pt")
def package_details(request: Request):

    subpath = request.matchdict.get("subpath")
    suburl = "/".join(subpath)

    page = fake_db.get(suburl)

    if not page:
        raise x.HTTPNotFound()

    return page
