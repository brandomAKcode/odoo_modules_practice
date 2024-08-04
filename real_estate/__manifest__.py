# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': """
        This is the Real Estate Module
    """,

    'description': """
        Real Estate
    """,

    'version': '0.1',
    'application': True,
    'category': 'Modules Practice/Real Estate',
    'installable': True,
    'license': 'AGPL-3',
    # import data to module (csv, xml....)
    'data': [
        'data/real_estate.property.csv',
        # security
        'security/ir.model.access.csv',
        # views
        'views/real_estate_property_views.xml',
    ]
}
