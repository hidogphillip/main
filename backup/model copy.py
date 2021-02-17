from flaskapp import db, ma


# Customer Class/Model
class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer)
    contact_id = db.Column(db.Integer)
    email = db.Column(db.String(50))
    salutation = db.Column(db.String(5))
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(60))
    phone = db.Column(db.String(20))
    fax = db.Column(db.String(20))
    country = db.Column(db.String(30))
    state = db.Column(db.String(30))
    city = db.Column(db.String(25))
    street_address_2 = db.Column(db.String(40))
    street_address_3 = db.Column(db.String(40))
    address = db.Column(db.String(40))
    postal_code = db.Column(db.String(10))
    tax_vat_number = db.Column(db.String(20))
    currency = db.Column(db.String(3))
    company_name = db.Column(db.String(40))
    registration_no = db.Column(db.String(20))
    jobtitle = db.Column(db.String(30))
    jobfunction = db.Column(db.String(30))
    industry_name = db.Column(db.String(10))
    sub_industry = db.Column(db.String(10))
    business_category = db.Column(db.String(60))
    type_of_company = db.Column(db.String(60))
    date_incorporated = db.Column(db.DateTime)
    place_incorporated = db.Column(db.String(30))
    credit_limit_required = db.Column(db.Integer)
    credit_term_required = db.Column(db.String(3))
    name_of_purchaser = db.Column(db.String(30))
    name_of_person_in_charge_of_payment = db.Column(db.String(30))
    person_in_charge_email = db.Column(db.String(50))
    invoice_consolidation_required = db.Column(db.String(1))
    customer_po_required = db.Column(db.String(1))
    monthly_statement_required = db.Column(db.String(1))
    email_address_1 = db.Column(db.String(60))
    email_address_2 = db.Column(db.String(60))
    approval_status = db.Column(db.String(20))

    def __init__(self, company_id, contact_id, email, salutation, firstname, lastname, phone, fax, country, state, city, 
    street_address_2, street_address_3, address, postal_code, tax_vat_number, currency, company_name, registration_no, 
    jobtitle, jobfunction, industry_name, sub_industry, business_category, type_of_company, 
    date_incorporated, place_incorporated, credit_limit_required, credit_term_required, 
    name_of_purchaser, name_of_person_in_charge_of_payment, person_in_charge_email, 
    invoice_consolidation_required, customer_po_required, monthly_statement_required, 
    email_address_1, email_address_2, approval_status):
        self.company_id = company_id
        self.contact_id = contact_id
        self.email = email
        self.salutation = salutation
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.fax = fax
        self.country = country
        self.state = state
        self.city = city
        self.street_address_2 = street_address_2
        self.street_address_3 = street_address_3
        self.address = address
        self.postal_code = postal_code
        self.tax_vat_number = tax_vat_number
        self.currency = currency
        self.company_name = company_name
        self.registration_no = registration_no
        self.jobtitle = jobtitle
        self.jobfunction = jobfunction
        self.industry_name = industry_name
        self.sub_industry = sub_industry
        self.business_category = business_category
        self.type_of_company = type_of_company
        self.date_incorporated = date_incorporated
        self.place_incorporated = place_incorporated
        self.credit_limit_required = credit_limit_required
        self.credit_term_required = credit_term_required
        self.name_of_purchaser = name_of_purchaser
        self.name_of_person_in_charge_of_payment = name_of_person_in_charge_of_payment
        self.person_in_charge_email = person_in_charge_email
        self.invoice_consolidation_required = invoice_consolidation_required
        self.customer_po_required = customer_po_required
        self.monthly_statement_required = monthly_statement_required
        self.email_address_1 = email_address_1
        self.email_address_2 = email_address_2
        self.approval_status = approval_status


# OrderHeader Class/Model
class OrderHeader(db.Model):
    __tablename__ = 'order_header'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.String(25))
    hubspot_id = db.Column(db.BigInteger)
    state = db.Column(db.String(32))
    status = db.Column(db.String(32))
    shipping_description = db.Column(db.String(255))
    is_virtual = db.Column(db.SmallInteger)
    discount_invoiced = db.Column(db.Numeric(15,2))
    grand_total = db.Column(db.Numeric(15,2))
    shipping_amount = db.Column(db.Numeric(15,2))
    shipping_invoiced = db.Column(db.Numeric(15,2))
    subtotal = db.Column(db.Numeric(15,2))
    subtotal_invoiced = db.Column(db.Numeric(15,2))
    total_invoiced = db.Column(db.Numeric(15,2))
    total_paid = db.Column(db.Numeric(15,2))
    total_qty_ordered = db.Column(db.Integer)
    subtotal_incl_tax = db.Column(db.Numeric(15,2))
    total_due = db.Column(db.Numeric(15,2))
    weight = db.Column(db.Numeric(12,4))
    applied_rule_ids = db.Column(db.String(128))
    customer_email = db.Column(db.String(128))
    order_currency_code = db.Column(db.String(3))
    shipping_method = db.Column(db.String(110))
    total_item_count = db.Column(db.SmallInteger)
    shipping_incl_tax = db.Column(db.Numeric(15,2))
    status_label = db.Column(db.String(128))
    company_id = db.Column(db.Integer, db.ForeignKey("customer.company_id"))
    customer = db.relationship("Customer", backref="orderheaders")

    def __init__(self, order_id, hubspot_id, state, status, shipping_description, 
    is_virtual, discount_invoiced, grand_total, shipping_amount, shipping_invoiced, 
	subtotal, subtotal_invoiced, total_invoiced, total_paid, total_qty_ordered, 
	subtotal_incl_tax, total_due, weight, applied_rule_ids, customer_email, 
	order_currency_code, shipping_method, total_item_count, shipping_incl_tax, 
	status_label):
        self.order_id = order_id
        self.hubspot_id = hubspot_id
        self.state = state
        self.status = status
        self.shipping_description = shipping_description
        self.is_virtual = is_virtual
        self.discount_invoiced = discount_invoiced
        self.grand_total = grand_total
        self.shipping_amount = shipping_amount
        self.shipping_invoiced = shipping_invoiced
        self.subtotal = subtotal
        self.subtotal_invoiced = subtotal_invoiced
        self.total_invoiced = total_invoiced
        self.total_paid = total_paid
        self.total_qty_ordered = total_qty_ordered
        self.subtotal_incl_tax = subtotal_incl_tax
        self.total_due = total_due
        self.weight = weight
        self.applied_rule_ids = applied_rule_ids
        self.customer_email = customer_email
        self.order_currency_code = order_currency_code
        self.shipping_method = shipping_method
        self.total_item_count = total_item_count
        self.shipping_incl_tax = shipping_incl_tax
        self.status_label = status_label 


# Customer Schema
class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
        fields = ('company_id', 'contact_id', 'email', 'salutation', 'firstname', 'lastname', 'phone', 'fax', 'country', 'state', 'city',  
        'street_address_2', 'street_address_3', 'address', 'postal_code', 'tax_vat_number', 'currency', 'company_name', 'registration_no',  
        'jobtitle', 'jobfunction', 'industry_name', 'sub_industry', 'business_category', 'type_of_company',  
        'date_incorporated', 'place_incorporated', 'credit_limit_required', 'credit_term_required',  
        'name_of_purchaser', 'name_of_person_in_charge_of_payment', 'person_in_charge_email',  
        'invoice_consolidation_required', 'customer_po_required', 'monthly_statement_required',  
        'email_address_1', 'email_address_2', 'approval_status')
        company_id = ma.auto_field()
        orderheaders = ma.auto_field()

# Init schema
customer_schema = CustomerSchema(strict=True)
customers_schema = CustomerSchema(many=True, strict=True)


# OrderHeader Schema
class OrderHeaderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = OrderHeader
        fields = ('order_id', 'hubspot_id', 'state', 'status', 'shipping_description', 
        'is_virtual', 'discount_invoiced', 'grand_total', 'shipping_amount', 'shipping_invoiced', 
        'subtotal', 'subtotal_invoiced', 'total_invoiced', 'total_paid', 'total_qty_ordered', 
        'subtotal_incl_tax', 'total_due', 'weight', 'applied_rule_ids', 'customer_email', 
        'order_currency_code', 'shipping_method', 'total_item_count', 'shipping_incl_tax', 'status_label')
        include_fk = True

# Init schema
orderheader_schema = OrderHeaderSchema(strict=True)
orderheader_schema = OrderHeaderSchema(many=True, strict=True)
