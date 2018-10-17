import app.application.controllers.products.config as config


class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_product):
        result = config.model.get_products(int(id_product))
        return config.render.delete(result)

    def POST(self, id_product):
        form = config.web.input()
        config.model.delete_products(form['id_product'])
        raise config.web.seeother('/')
