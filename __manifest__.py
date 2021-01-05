{
    'name': 'Hospital Management',
    'version': '1.0',
    'sequence':'0',
    'description': 'manage hospital',
    'summary': '',
    'author': 'cupangserit',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base',
        'mail',
        'sale',
        'contacts',
    ],
    'data': [
        'views/patients_view.xml',
        'views/appointment_view.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
    ],
    'application': True,
}

#test commit