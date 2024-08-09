<img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/Odoo_Official_Logo.png" width="35%" alt="Odoo lindo">

## odoo modules practice

This is a practice to learn the essential aspects of Odoo.

### Observations

#1 Module information must be added to the __init__.py file for Odoo to detect modules correctly. If this information is not added, Odoo will not create the tables for the models.

#2 The data files within module directories are employed to populate the database with initial records. To ensure correct data loading, file names must align with their corresponding model names.

#3 For some strange reason, in the ir.module.access.csv file, all values must be without spaces. This way, Odoo will not generate errors when importing security files.

#4 Odoo provides the flexibility to customize views through XML files. These XML files enable us to incorporate search functionalities, such as search bars, into the user interface.

#5 When creating a one2many field, a many2one field must be created in the related model to ensure a correct relationship.
