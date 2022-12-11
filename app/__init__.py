from flask import Flask, redirect, render_template
from flask_migrate import Migrate

from app.config import Configuration
from app.models import db, Package
from app.shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)


@app.route("/new_package", methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        print("VALIDATED")
        package = Package(sender=form.data["sender"],
                          recipient=form.data["recipient"],
                          origin=form.data["origin"],
                          destination=form.data["destination"],
                          location=form.data["origin"])
        print(package)
        db.session.add(package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect("/")

    print("ERRORS", form.errors)
    return render_template('shipping_request.html', form=form)
