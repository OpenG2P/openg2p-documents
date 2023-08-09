# Part of OpenG2P Documents. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Documents Store",
    "category": "G2P",
    "version": "15.0.1.2.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "storage_backend_s3",
        "storage_file",
    ],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/main_view.xml",
        "views/g2p_document_store.xml",
        "views/g2p_document_files.xml",
        "views/g2p_document_tags.xml",
        "data/storage_backend.xml",
    ],
    "external_dependencies": {"python": ["boto3<=1.15.18", "python_slugify"]},
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
