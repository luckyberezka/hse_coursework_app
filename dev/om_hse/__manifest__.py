{
    'name': 'HSE Coursework Management System',
    'author': 'nardzhiev',
    'category': 'HSE Coursework/Users',
    'depends': ['mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/reject_project_view.xml',
        'views/menu.xml',
        'views/coursework.xml',
    ],
    'application': True,
    'installable': True,
}
