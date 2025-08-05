{
    'name': 'Manufacturing & Purchase Orders from Sale Order',
    'version': '18.0',
    'summary': 'Adds buttons in Sale Order to view related Manufacturing and Purchase Orders.',
    'description': """
This module adds two buttons in the Sale Order form:
- View Manufacturing Orders linked to this sale order.
- View Purchase Orders linked to this sale order.

The orders are filtered by the Sale Order name (origin field).
    """,
    'category': 'Sales/Manufacturing/Purchase',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'contributors': 'Mohit Nare',
    'price': 7.99,
    'currency': 'USD',
    'license': 'OPL-1',
    'website': 'http://namahsoftech.com/',
    'support': 'support@namahsoftech.com',
    'depends': ['sale_management', 'mrp', 'purchase', ],
    'data': [
        'views/sale_order_view.xml'
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
