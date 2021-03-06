import web

urls = (
    '/', 'application.controllers.index.Index',
    '/clientes','application.controllers.clientes.index.Index',
    '/clientes/insert', 'application.controllers.clientes.insert.Insert',
    '/clientes/update/(.*)','application.controllers.clientes.update.Update',
    '/clientes/delete/(.*)','application.controllers.clientes.delete.Delete',
    '/clientes/view/(.*)','application.controllers.clientes.view.View',
    '/productos','application.controllers.productos.index.Index',
    '/productos/insert','application.controllers.productos.insert.Insert',
    '/productos/update/(.*)','application.controllers.productos.update.Update',
    '/productos/delete/(.*)','application.controllers.productos.delete.Delete',
    '/productos/view/(.*)','application.controllers.productos.view.View',
)

render = web.template.render('application/views/',base='master')
if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
