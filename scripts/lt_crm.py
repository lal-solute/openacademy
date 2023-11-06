from OdooLocust import OdooLocustUser, crm


class OdooCalm(OdooLocustUser.OdooLocustUser):
    host = "localhost"
    database = "odoo-exp"
    login = "admin"
    password = "admin"
    port = 8069
    protocol = "jsonrpc"

    tasks = {crm.partner.ResPartner: 1, crm.lead: 2}
