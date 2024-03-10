
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

Añadiremos data y un xml para que se muestre en la interfaz de Odoo:

```xml
<odoo>
    <data>

        <record model="usuarios" id="openacademy.usuarios">

            <field name="name">Jay</field>
            <field name="description">Senior Full Stack Developer</field>

        </record>

    </data>
</odoo>
```

Referenciamos este nuevo xml en el manifest:

```python
    'data': [
        # 'security/ir.model.access.csv',
        'data/materiales.xml',
        'views/views.xml',
        'views/templates.xml',
    ]
```

Luego, como ultimi paso para que se muestre en la interfaz de Odoo, modificaremos views/views.xml:

```xml
<odoo>
  <data>
    <!-- explicit list view definition -->

    <record model="ir.ui.view" id="openacademy.lista_materiales">
      <field name="name">openacademy list</field>
      <field name="model">materiales</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="description"/>
          <field name="precio"/>
        </tree>
      </field>
    </record>


    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="openacademy.action_window_materiales">
      <field name="name">materiales</field>
      <field name="res_model">materiales</field>
      <field name="view_mode">tree,form</field>
    </record>


    <!-- server action to the one above -->
<!--
    <record model="ir.actions.server" id="openacademy.action_server">
      <field name="name">openacademy server</field>
      <field name="model_id" ref="model_openacademy_openacademy"/>
      <field name="state">code</field>
      <field name="code">
        action = {
          "type": "ir.actions.act_window",
          "view_mode": "tree,form",
          "res_model": model._name,
        }
      </field>
    </record>
-->

    <!-- Top menu item -->

    <menuitem name="openacademy" id="openacademy.menu_root"/>

    <!-- menu categories -->

    <menuitem name="Ejemplo" id="openacademy.menu_materiales" parent="openacademy.menu_root"/>
<!--
    <menuitem name="Menu 2" id="openacademy.menu_2" parent="openacademy.menu_root"/>
-->
    <!-- actions -->

    <menuitem name="Lista de materiales" id="openacademy.listaMateriales" parent="openacademy.menu_materiales"
              action="openacademy.action_window_materiales"/>
<!--
    <menuitem name="Server to list" id="openacademy" parent="openacademy.menu_2"
              action="openacademy.action_server"/>
-->
  </data>
</odoo>
```

Luego modificaremos ir.model.access.csv:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_openacademy_materiales,openacademy.openacademy,model_materiales,base.group_user,1,1,1,1
```

Y lo referenciaremos en el views.xml:

```xml
    'data': [
        'security/ir.model.access.csv',
        'data/materiales.xml',
        'views/views.xml',
        'views/templates.xml',
    ]
```

Esta sería la vista final en Odoo:

![App en Odoo](https://github.com/RubenDanielCastelao/SXE-Odoo_Modulo/blob/master/images/odoo-tabla.png)