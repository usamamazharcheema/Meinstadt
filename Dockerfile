FROM public.ecr.aws/lambda/python:3.9
COPY . ${LAMBDA_TASK_ROOT}

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "handler.handler" ]
