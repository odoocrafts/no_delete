{
    'name': 'No Delete - Global Delete restriction',
    'version': '18.0.1.0.0',
    'category': 'System/Security',
    'summary': 'Disables record deletion globally for all models',
    'description': """
        This module removes the ability to delete records from any model in the system.
        Users should archive records instead of deleting them.
        
        Exceptions:
        - TransientModels (Wizards) are allowed to be deleted to ensure system stability.
    """,
    'author': 'Antigravity',
    'depends': ['base'],
    'data': [
        'views/ir_model_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
