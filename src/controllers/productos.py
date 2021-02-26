from flask import render_template
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    productosModel = ProductosModel()

    productos = productosModel.traerTodos()

    print(productos)

    return render_template('productos/index.html')