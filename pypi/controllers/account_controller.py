from pyramid.view import view_config
#
#
# def get_test_packages():
#     return [
#         {"name": "requests", "version": "1.2.3"},
#         {"name": "sqlalchemy", "version": "2.0.0"},
#         {"name": "pyramid", "version": "1.9.1"},
#     ]
#
#
# @view_config(route_name="home", renderer="pypi:templates/home/index.pt")
# def home_index(request):
#     return {"packages": get_test_packages()}
#
#
# @view_config(route_name="about", renderer="pypi:templates/home/about.pt")
# def about(request):
#     return {"packages": None}
