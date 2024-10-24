import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo9-addons-oca-web",
    description="Meta package for oca-web Odoo addons",
    version=version,
    install_requires=[
        'odoo9-addon-help_online',
        'odoo9-addon-support_branding',
        'odoo9-addon-web_access_rule_buttons',
        'odoo9-addon-web_action_conditionable',
        'odoo9-addon-web_advanced_search_x2x',
        'odoo9-addon-web_dashboard_tile',
        'odoo9-addon-web_decimal_numpad_dot',
        'odoo9-addon-web_dialog_size',
        'odoo9-addon-web_duplicate_visibility',
        'odoo9-addon-web_easy_switch_company',
        'odoo9-addon-web_editor_background_color',
        'odoo9-addon-web_environment_ribbon',
        'odoo9-addon-web_export_view',
        'odoo9-addon-web_favicon',
        'odoo9-addon-web_hide_db_manager_link',
        'odoo9-addon-web_ir_actions_act_window_message',
        'odoo9-addon-web_listview_custom_element_number',
        'odoo9-addon-web_m2x_options',
        'odoo9-addon-web_menu_collapsible',
        'odoo9-addon-web_notify',
        'odoo9-addon-web_readonly_bypass',
        'odoo9-addon-web_responsive',
        'odoo9-addon-web_searchbar_full_width',
        'odoo9-addon-web_send_message_popup',
        'odoo9-addon-web_sheet_full_width',
        'odoo9-addon-web_shortcut',
        'odoo9-addon-web_timeline',
        'odoo9-addon-web_translate_dialog',
        'odoo9-addon-web_tree_dynamic_colored_field',
        'odoo9-addon-web_tree_image',
        'odoo9-addon-web_tree_many2one_clickable',
        'odoo9-addon-web_widget_bokeh_chart',
        'odoo9-addon-web_widget_color',
        'odoo9-addon-web_widget_darkroom',
        'odoo9-addon-web_widget_datepicker_options',
        'odoo9-addon-web_widget_digitized_signature',
        'odoo9-addon-web_widget_float_formula',
        'odoo9-addon-web_widget_image_download',
        'odoo9-addon-web_widget_image_webcam',
        'odoo9-addon-web_widget_many2many_tags_multi_selection',
        'odoo9-addon-web_widget_timepicker',
        'odoo9-addon-web_widget_x2many_2d_matrix',
        'odoo9-addon-web_x2many_delete_all',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 9.0',
    ]
)
