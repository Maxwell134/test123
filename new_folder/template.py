from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Product:
    def __init__(self, product_id, product_name, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity


    def update(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity


# Inventory list to store Product instances
inventory = []

@app.route("/")
def index():
    return render_template("index.html", inventory=inventory)

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        if any(product.product_id == product_id for product in inventory):
            return "Product ID already exists."
        product_name = request.form.get("product_name")
        quantity = int(request.form.get("quantity"))
        product = Product(product_id, product_name, quantity)
        inventory.append(product)
        return redirect(url_for("index"))
    return render_template("add_movie.html")


@app.route("/modify_product/<product_id>", methods=["GET", "POST"])
def modify_product(product_id):
    product = next((p for p in inventory if p.product_id == product_id), None)
    if product is None:
        return "Product not found."

    if request.method == "POST":
        product_name = request.form.get("product_name")
        quantity = int(request.form.get("quantity"))
        product.update(product_name, quantity)
        return redirect(url_for("index"))

    return render_template("display.html", product=product)


@app.route("/delete_product/<product_id>")
def delete_product(product_id):
    product = next((p for p in inventory if p.product_id == product_id), None)
    if product is None:
        return "Product not found."

    inventory.remove(product)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
