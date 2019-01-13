from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/home_index.pt')
def home_index(request):
    return {'project': 'Python Package Index'}
