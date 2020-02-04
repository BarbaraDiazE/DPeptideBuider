FROM continuumio/anaconda3:5.0.1

RUN conda create -c rdkit -n rdkit-env rdkit -y

WORKDIR /src

RUN /opt/conda/envs/rdkit-env/bin/pip install --upgrade pip
ADD config/requirements.txt .
RUN /opt/conda/envs/rdkit-env/bin/pip install -r requirements.txt

ADD ./src/ .

RUN /opt/conda/envs/rdkit-env/bin/python3 manage.py migrate; \
    /opt/conda/envs/rdkit-env/bin/python3 manage.py collectstatic --noinput; \
    /opt/conda/envs/rdkit-env/bin/python3 population.py

CMD [ "/src/docker-entrypoint.sh" ]
