
{
    'name': 'Performance Appraisal',
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Manage employee performance appraisals',
    'description': 'Module to manage performance appraisals for employees including appraisers and scoring.',
    'author': 'Musleh Uddin Juned',
    'website': 'http://www.zachai-bachhai.com',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/report_performance_appraisal.xml',
        'views/performance_appraisal_views.xml',
    ],
    'installable': True,
    'application': False,
}
