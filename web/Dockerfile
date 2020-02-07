FROM continuumio/anaconda3:5.0.1

RUN conda create -c rdkit -n rdkit-env rdkit -y

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN /opt/conda/envs/rdkit-env/bin/pip install --upgrade pip
ADD config/requirements.txt .
RUN /opt/conda/envs/rdkit-env/bin/pip install -r requirements.txt

ADD ./src/ .

ENTRYPOINT [ "/src/docker-entrypoint.sh" ]
