import odoolib

connection = odoolib.get_connection(
    hostname="localhost",
    database="odoo-exp",
    login="admin",
    password="admin",
)
partner_model = connection.get_model("res.partner")
ids = partner_model.search([])
partner_info = partner_model.read(ids[0], ["name"])

print(partner_info["name"])
