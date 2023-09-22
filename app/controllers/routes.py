from datetime import datetime


import app
from app.controllers.services.helper import Helper
from app.forms.contact_form import ContactForm
from app.forms.login_form import LoginForm
from flask import redirect, render_template, request, send_from_directory
from flask_sitemap import Sitemap


def init_app(app):
    # Sitemap
    ext = Sitemap(app=app)
    now = datetime.now().isoformat()

    # 404
    @app.errorhandler(404)
    def pagina_nao_encotrada():
        return render_template("404.html")

    # Robots
    @app.route("/robots.txt")
    def static_from_root():
        return send_from_directory(app.static_folder, request.path[1:])

    # Rota da página de login
    @app.route("/login", methods=["GET", "POST"])
    def login():

        form = LoginForm()

        if form.validate_on_submit():

            return render_template("login.html", form=form)

        return render_template("login.html", form=form)

    @app.route("/logout")
    def logout():
        # logout_user()
        # session.pop('username', None)
        return redirect(url_for("login"))

    # Rotas das páginas Admin
    @app.route("/admin")
    def dashboard():
        try:

            # if 'username' in session:
            #   return render_template("admin/index.html")
            # return redirect(url_for("login"))

            return render_template("admin/index.html")
        except:
            return render_template("admin/index.html")
            # retun redirect(url_for("login"))

    @app.route("/adminlayoutstatic")
    def adminlayoutstatic():
        return render_template("admin/layout-static.html")

    @app.route("/adminlayoutsidenav")
    def adminlayoutsidenav():
        return render_template("admin/layout-sidenav-light.html")

    @app.route("/adminlogin")
    def adminlogin():
        return render_template("admin/login.html")

    @app.route("/adminregister")
    def adminregister():
        return render_template("admin/register.html")

    @app.route("/adminpassword")
    def adminpassword():
        return render_template("admin/password.html")

    @app.route("/admin401")
    def admin401():
        return render_template("admin/401.html")

    @app.route("/admin404")
    def admin404():
        return render_template("admin/404.html")

    @app.route("/admin500")
    def admin500():
        return render_template("admin/500.html")

    @app.route("/admincharts")
    def admincharts():
        return render_template("admin/charts.html")

    @app.route("/admintables")
    def admintables():
        return render_template("admin/tables.html")

    # Rota das páginas principais
    @app.route("/")
    def index():
        return render_template("index.html")

    @ext.register_generator
    def index():
        yield "index", {}, now, "never", 1.0
        yield "sobre", {}, now, "never", 0.8
        yield "alugar", {}, now, "never", 0.8
        yield "comprar", {}, now, "never", 0.8
        yield "contato", {}, now, "never", 0.8
        yield "sucesso", {}, now, "never", 0.8
        yield "apartamento1", {}, now, "never", 0.8
        yield "apartamento2", {}, now, "never", 0.8
        yield "apartamento3", {}, now, "never", 0.8
        yield "casa1", {}, now, "never", 0.8
        yield "casa2", {}, now, "never", 0.8
        yield "casa3", {}, now, "never", 0.8
        yield "casa4", {}, now, "never", 0.8
        yield "casa5", {}, now, "never", 0.8
        yield "casa6", {}, now, "never", 0.8
        yield "casa7", {}, now, "never", 0.8
        yield "casa8", {}, now, "never", 0.8
        yield "flat1", {}, now, "never", 0.8
        yield "suite1", {}, now, "never", 0.8
        yield "terreno1", {}, now, "never", 0.8

    @app.route("/cristina-santos")
    def sobre():
        return render_template("cristina-santos.html")

    @app.route("/alugar")
    def alugar():
        return render_template("alugar.html")

    @app.route("/comprar")
    def comprar():
        return render_template("comprar.html")

    @app.route("/contato", methods=["POST", "GET"])
    def contato():
        form = ContactForm()
        if form.validate_on_submit():
            Helper.enviar_email(
                request.form["subject"],
                ["oi@gmail.com"],
                "contact",
                email=request.form["email"],
            )
            return redirect("/sucesso")

        return render_template("contato.html", form=form)

    @app.route("/sucesso")
    def sucesso():
        return render_template("sucesso.html")

    # Rota dos imóveis
    # Apartamentos
    @app.route("/comprar/apartamento-arraial-dajuda-proximo-ao-centro")
    def apartamento1():
        return render_template("ap1.html")

    @app.route("/alugar/apartamento-arraial-dajuda-centro")
    def apartamento2():
        return render_template("ap2.html")

    @app.route("/alugar/apartamento-arraial-santiago")
    def apartamento3():
        return render_template("ap3.html")

    # Casas
    @app.route("/comprar/casa-arraial-dajuda-villas-do-arraial")
    def casa1():
        return render_template("ca1.html")

    @app.route("/comprar/casa-arraial-dajuda-alto-da-pitinga")
    def casa2():
        return render_template("ca2.html")

    @app.route("/comprar/casa-arraial-dajuda-mangabeira")
    def casa3():
        return render_template("ca3.html")

    @app.route("/comprar/casa-arraial-dajuda-corais")
    def casa4():
        return render_template("ca4.html")

    @app.route("/alugar/casa-arraial-dajuda-temporada")
    def casa5():
        return render_template("ca5.html")

    @app.route("/alugar/casa-arraial-dajuda-mucuge")
    def casa6():
        return render_template("ca6.html")

    @app.route("/comprar/casa-arraial-dajuda-duplex")
    def casa7():
        return render_template("ca7.html")

    @app.route("/comprar/casa-arraial-dajuda-centro-duplex")
    def casa8():
        return render_template("ca8.html")

    # Flats
    @app.route("/alugar/flats-arraial-dajuda-praia-pescador")
    def flat1():
        return render_template("fl1.html")

    # Suítes
    @app.route("/alugar/suites-arraial-dajuda")
    def suite1():
        return render_template("su1.html")

    # Terrenos
    @app.route("/comprar/terreno-caraiva")
    def terreno1():
        return render_template("te1.html")
