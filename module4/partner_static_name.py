class PartnerStaticName:
    name = None

    @staticmethod
    def get_partner_name():
        return PartnerStaticName.name

    @staticmethod
    def set_partner_name(new_name):
        PartnerStaticName.name = new_name