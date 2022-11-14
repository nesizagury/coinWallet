FROM nickgryg/alpine-pandas

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["view.py" ]