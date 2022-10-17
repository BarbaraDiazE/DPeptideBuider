FROM continuumio/anaconda3:5.0.1

RUN conda create -c rdkit -n rdkit-env rdkit -y

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN /opt/conda/envs/rdkit-env/bin/python -m pip install --upgrade pip
ADD config/requirements.txt .
RUN /opt/conda/envs/rdkit-env/bin/pip install -r requirements.txt

COPY src/ .
RUN tar -xvzf trained_models.tar.gz

ENTRYPOINT [ "./docker-entrypoint.sh" ]
