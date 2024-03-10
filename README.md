
```markdown
# Creación de Odoo

Para crear el contenedor de Odoo, hemos utilizado la imagen `odoo:16.0` de Docker. El comando utilizado para crear el contenedor es el siguiente:

```bash
docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo --name db postgres:13
docker run -p 8069:8069 --name odoo --link db:db -t odoo
```

# Añadir el nuevo addon de openacademy

Para crear el addon `openacademy`, hemos utilizado el comando `scaffold` de Odoo. El comando exacto es el siguiente:

```bash
docker exec -it odoo-mydb-1 odoo scaffold openacademy /mnt/extra-addons
```

Este es el resultado de la carpeta addon:

![Carpeta addon](https://github.com/RubenDanielCastelao/SXE-Odoo_Modulo/blob/master/images/addon-file.png)

Después de crear el addon, lo hemos añadido al contenedor de Odoo montando un volumen para los addons. El comando utilizado es el siguiente:

```bash
docker run -v /path/to/addons:/mnt/extra-addons -d -p 8069:8069 --name odoo --link db:db -t odoo
```

Finalmente, hemos reiniciado el contenedor para que Odoo reconozca el nuevo addon.
```

Recuerda reemplazar `/path/to/addons` con la ruta real a tu directorio de addons.
```

Despues modificaremos eml manifest.py para que quese muestre la información que queremos en el modulo:

Este sería nuestro ejemplo:

```python
# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Modulo Ruben para SXE""",

    'description': """
        Un modulo de prueba para SXE
    """,

    'author': "RubenNG",
    'website': "https://github.com/RubenDanielCastelao",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Modulo de ejemplo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

```

Y asi se vería en Odoo:

![App en Odoo](https://github.com/RubenDanielCastelao/SXE-Odoo_Modulo/blob/master/images/odoo-addon.png)

> [!AVISO]
> Para poder añadir el addon, se debera activar el modo desarrollador en Odoo. Para ello, se deberá ir a `Ajustes` -> `Activar el modo desarrollador` y luego ir a `Aplicaciones` -> `Actualizar lista de aplicaciones` y buscar el modulo `openacademy` y instalarlo.

Luego para crear una tabla modificaremos models/models.py:

```python

from odoo import fields, models

class materiales(models.Model):
    _name = 'materiales'
    _description = 'tabla de materiales y sus datos'

    name = fields.Char(String = 'Nombre')
    description = fields.Char(String = 'Descripcion')
    precio = fields.Float(String = 'Precio')

```

Reiniciaremos el docker, y luego haremos un Upgrade en Odoo, para que se cree la tabla en la base de datos.

Asi se vería en la BD:

![App en Odoo](https://github.com/RubenDanielCastelao/SXE-Odoo_Modulo/blob/master/images/db.png)


Luego, para que se muestre en la interfaz de Odoo, modificaremos views/views.xml:

```xml