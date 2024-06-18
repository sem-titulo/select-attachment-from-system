{
    "name": "Select Attachment From System",
    "version": "15.0.0.1",
    "description": "Select Attachment from ir attachment table",
    "summary": "Selecione arquivos do prõprio sistema para evitar carregamento repetido",
    "author": "Dev Fazer",
    "website": "https://devfazer.com.br/",
    "license": "AGPL-3",
    "category": "technical",
    "depends": ["base", "mail", "web"],
    "data": ["security/ir.model.access.csv", "views/attachment_views.xml"],
    "auto_install": False,
    "application": True,
    "price": 100.00,
    "currency": "EUR",
    "images": ["images/main_1.png", "images/main_2.png", "images/main_screenshot.png"],
    "assets": {
        "mail.assets_discuss_public": [
            "select_attachment_from_system/static/src/components/*/*",
            "select_attachment_from_system/static/src/components/*/*.js",
        ],
        "web.assets_qweb": [
            "select_attachment_from_system/static/src/components/attachment_box/*.xml",
        ],
        "web.assets_backend": [
            "select_attachment_from_system/static/src/components/attachment_box/*.js",
        ],
    },
}
