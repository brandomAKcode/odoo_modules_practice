<img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/Odoo_Official_Logo.png" width="35%" alt="Odoo lindo">

## odoo modules practice

This repository was created to have a reference for the creation of modules in Odoo. The views and modules were created even in a single file to have a quick reference.

### Observations

#1 Module information must be added to the __init__.py file for Odoo to detect modules correctly. If this information is not added, Odoo will not create the tables for the models.

#2 The data files within module directories are employed to populate the database with initial records. To ensure correct data loading, file names must align with their corresponding model names.

#3 For some strange reason, in the ir.module.access.csv file, all values must be without spaces. This way, Odoo will not generate errors when importing security files.

#4 Odoo provides the flexibility to customize views through XML files. These XML files enable us to incorporate search functionalities, such as search bars, into the user interface.

#5 When creating a one2many field, a many2one field must be created in the related model to ensure a correct relationship.

#6 The compute and onchange decorators are powerful tools for manipulating data in the view.

#7 SQL constraints are much faster than Python constraints.
