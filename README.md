
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
