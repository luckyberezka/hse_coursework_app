FROM python:3.10

WORKDIR /usr/src/app

COPY conf conf
COPY dev dev
COPY odoo odoo

RUN apt update && apt install -y libldap2-dev libpq-dev libsasl2-dev
RUN pip install -r odoo/requirements.txt


ENTRYPOINT ["python", "odoo/odoo-bin",\
            "--db_host", "db",\
            "-d", "postgres",\
            "-r", "odoo",\
            "-w", "odoo",\
            "--addons-path", "odoo/addons,dev",\
            "-u", "om_hse"]
