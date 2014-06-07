__version__ = (1, 0, 0, "final", 0)


ADMIN_PIPELINE_CSS = {

    'admin': {
        'source_filenames': (
            'admintools_bootstrap/chosen/chosen.css',
            'admintools_bootstrap/lib/bootstrap-datetimepicker.css',
            'admintools_bootstrap/lib/bootstrap-fileupload.scss',
            'admintools_bootstrap/sass/admin.scss',
            'admintools_bootstrap/css/mmenu.css',
        ),
        'output_filename': 'css/admin_bs3.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'admin_dashboard': {
        'source_filenames': (
            'admin_dashboard.css',
            'admintools_bootstrap/sass/dashboard.scss',
        ),
        'output_filename': 'css/admin_bs3_dashboard.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

ADMIN_PIPELINE_JS = {
    'admin': {
        'source_filenames': (
            'admintools_bootstrap/js/lazyload.js',
            'admintools_bootstrap/js/jquery-1.9.1.js',
            'admintools_bootstrap/js/jquery-ui-1.10.3.custom.js',
            'admintools_bootstrap/js/json2.js',
            'admin_tools/js/jquery/jquery.cookie.min.js',
            'admin_tools/js/jquery/jquery.dashboard.js',
            'admin_tools/js/menu.js',
            'admintools_bootstrap/chosen/chosen.jquery.js',
            'admintools_bootstrap/js/bootstrap/dropdown.js',
            'admintools_bootstrap/js/bootstrap/alert.js',
            'admintools_bootstrap/js/bootstrap-datetimepicker.js',
            'admintools_bootstrap/js/bootstrap-fileupload.js',
            'admintools_bootstrap/js/dismissAddAnotherPopup.js',
            'admintools_bootstrap/js/admin.js',
        ),
        'output_filename': 'js/admin_bs3_dashboard.js',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}
