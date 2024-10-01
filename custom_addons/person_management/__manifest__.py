{
    "name": "Person Management",
    "version": "1.0",
    "category": "Website",
    "summary": "Manage persons with website integration",
    "description": """
        A module to manage persons with integration to the Odoo website.
    """,
    "author": "Bohdan Zinchenko",
    "depends": ["base", "website"],
    "data": [
        "views/person_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
