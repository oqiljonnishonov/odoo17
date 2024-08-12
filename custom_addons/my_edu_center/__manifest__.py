{
    'name': 'Education Center Management',
    'version': '1.0',
    'summary': 'Manage courses, teachers, students, groups, and payments in an educational center.',
    'author': 'Author name',
    'category': 'Education',
    'depends': ['base', 'mail','web'],  # Include other necessary modules
    'data': [
        'security/ir.model.access.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/payment_dashboard_views.xml',
        # 'report/payment_check_report.xml',
        'report/report.xml', 
        'views/payment_views.xml',
        'views/report_payment_check.xml',
        'views/course_views.xml',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/group_views.xml',
        'views/teacher_payment.xml'
        
        
    ],
    

    'installable': True,
    'application': True,
}
