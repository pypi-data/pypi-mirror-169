<!--Copyright 2022 Tellius, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.-->
# Tellius Data Manager

[![Build Status](https://drone.app.tellius.com/api/badges/Tellius/tellius-data-manager/status.svg)](https://drone.app.tellius.com/Tellius/tellius-data-manager)

## About
Tellius Data Manager - tdm - takes the approach that a data pipeline is a flow of information from ingest, transform, write, and possible additional transformation. That is, it is impossble to really do ETL or ELT in the modern data stack. Instead, it is ETLTLTLT... etc....

A common mathematical reduction of data pipelines is to represent and even discuss data pipelines using the Abstract Algebraic concept of a Directed Acyclic Graph or DAG. This comes from engineers having at least basic understandings of mathematics and a greater number of data engineers having advanced CS or mathematics degrees (they may have been data scientists at one time). The reason this is so commonly used is it provides a clear explanation representation of how data MOVES through a system. Data in most any situation should not move recursively through a pipeline. In the event that you have created a sequence of steps that is looping - either you have done things incorrectly or you have moved to a grain that is TOO small, and that loop logically belongs embedded within a single step.

This being said, the logic behind how tdm has been developed is to represent all pipelines as DAGs - although we use a less mathematical language to make using the library more approachable. We currently support two different approaches to defining a pipeline: Declarative through a YAML file and pragmatic through direct coding. Each of these approaches will be described below.

### What is tdm
tdm, or Tellius Data Manager, is a framework for building ETL, ELT, etc. data pipelines. It is written in python, it is configurable, customizable and built with component reuse in mind. It abstracts away the concept of a secret so that code itself should never contain a secret directly. The  

### What is a data pipeline
In essence a pipeline is a sequence of dependent steps, each of which is executed in order and not executed (possibly conditionally) when a predecessor fails.

A data pipeline is a pipeline where each step in the processing pipeline has to do with
1. Ingestion of data
2. Transformation of data
3. Writing of data
4. Logical operations controlling the processing of the data.

A pipeline is created when each step is implicitly or explicitly linked to a parent process. Each pipeline will require at least one initial pipe and at least one terminal pipe.

### tdm architectural philosophy

There are many concepts espoused in tdm. And many more that could be added, but are not yet at this time - only when needed would they be.

* Pipelines
* Logging
* State Tracking
* Alerting

#### Pipeline
tdm - at its core - is based upon the philosophy that each step of a pipeline is an independently executable component. While in this space some would desire that a pipeline can be polyglottic tdm - does not directly espouse this approach - but since it is truly extensible, it is not in any way prevented. *If there is a desire to espouse polyglottism it is on the implementer to build out parallel implementations that operate with the same qualities that tdm does.*_

This means that the core processing unit of tdm is a Pipe. In implementation a Pipe will have one of 4 basic types
1. ReaderPipe
2. TransformerPipe
3. WriterPipe
4. LogicsPipe (More on this one later - WIP)

![Basic Pipeline](images/pipe_scenario_1.png)

Above is a very basic pipeline. This is still useful in many cases. It constitutes the simple act of reading data from one source and writing it to another.

![Transform Pipeline](images/pipe_scenario_2.png)

This is the next step up in complexity. Here there is an intermediate step of applying a transformation to the data.

![Multi Transform Pipeline](images/pipe_scenario_3.png)

In some situations transformations have to happen in parallel - or for better execution time they are performed in parallel.

![Complex Pipeline](images/pipe_scenario_4.png)

Pipelines can become very complex. In this situation there are multiple data sources, an intermediate write stage. A late stage read and finally a write to ultimately terminate the pipeline.

![Example Pipeline](images/pipe_scenario_5.png)

This is examplar of what may happen in a pipeline. In this case data is read from a RESTful endpoint. A data column is added to the data and a column represent a State (as in a State in the USA) is modified to a standard format. These two datasets are then joined and then written out to S3.

In tdm it is standard to define the configuration of your entire pipeline through either a YAML file or in code as a python dict.

#### Logging
Logging is built into the framework. There is a standardized logging format called TelliusLogger. This should be used where ever you write code. It should replace any tendency to print to stdio and used when capturing and handling exceptions. It extends the standard python logger and uses the same interface. It also captures some additional fields around the runtime.

The fields captured are open to change as the framework is extended.

#### State Tracking
The idea of state for tdm is not meant as a restorable state. It is instead intended to be used primarily for creating an audit trail. This will be used to capture metadata/statistics about the data as well.

#### Alerting
Alerting is important for production pipelines. An alert, at this time, in tdm nomenclature, corresponds to sending an email when a pipeline error occurs.

## Installing tdm

### System Requirements
1. Linux Operating System
2. Python 3.9 or higher

### Gaining Access to Private Repo
tdm is stored on pypi

```bash
https://pypi.org
```

and the repo is called

```bash
tellius-data-manager
```

It can be installed as
```bash
pip install tellius-data-manager
```

There is also a prebuilt Docker image at

https://hub.docker.com/r/telliusopensource/tellius-data-manager

## Creating a tdm project

At this time there is no magic button (CLI) for creating a tdm project, so some manual steps will be needed. First, in your user root location you will need to create a hidden directory called .tdm (*only linux systems are supported at this time.*). In this directory create two files, secrets.yml (for storing secret configurations) and config.yml (for storing pipeline configuration - still a WIP)

Once this is done you need to either us an existing project (repo) and add a sub project for the new group of pipelines. Regardless of the choice, you need to treat it as a standalone project. This means you will have a pyproject.toml, requirements.txt and other python project artifacts local to this pipelines as its dependencies may be different than those of other pipelines.

### Repository Structure

When installing tdm there is no CLI at this time, so you have to initialize the project by yourself. tdm operates under an opinionated file structure.
```bash
project_root
  pipeline_drivers
  pipelines
  tests
```

If you are planning to deploy with Argo CronWorkflows, then you need an argo directory.

Similarly, if using Kubernetes CronJobs, then create a manifests directory.

### Drivers vs Pipes

There will be two different kinds of code written for a pipeline (most often). These are Drivers and Pipes. A driver is a script where a pipeline is configured and orchestrated. Later versions will have the ability to abstract this away completely to a configuration file. Pipes are custom extensions to the various kinds of Pipe described above.

#### Drivers

The pipeline_drivers directory will have a file called entrypoint.py. This will serve as the main entrypoint to code execution. It will be a CLI that will group all the different pipelines together so that the orchestration engine will have a templatizable execution command.

The pipeline_drivers directory will also have one or more files defining the various data pipelines. These files will have the following general structure

```python

logging.setLogger(TelliusLogger)
_logger = logging.getLogger(__name__)


def some_function(table, state_file, data_file, pipeline_id):
  # Create a job_id - this uniquely identifies the execution run
  job_id = uuid.uuid4().hex

  # This will be used to track and log/persist the state (audit) of the piepline
  state_manager = StateManager(**configuration_dictionary)

  # Errors can happen!
  try:
    # Some pipelines may have configuration parameters we have not yet extracted to configuration - put them here.
    some_parameters...

    # This is where we are going to create a dict to define the configuration. Alternatively you could use the YAMLConfigReader that comes in tdm to read it from a configuration file that is local or stored at the USER_ROOT/.tdm/config.yml (more on this later)
    flow_model = {
      configuration of each step here
    }

    # Define the various pipeline steps
    read_pipe = QuerySomething(**flow_model['read'])
    transform_pipe = TransformSomething(**flow_model['transform'])
    write_pipe = WriteSomething(**flow_model['write'])

    # Sometimes the pipeline here can have control and looping logic. Hopefully this can all be handled through pipe definitions later - but it is not yet there. And for this reason some additional logic may be needed and possibly other parameters. However, we will not do so here.

    start_time = datetime.datetime.now().timestamp()
    # Build the execution flow
    read = read_pipe.run()
    transform = transform_pipe.run(parent=read)
    write = write_pipe.run(parent=transform)
  except:
    stop_time = datetime.datetime.now().timestamp()
    state_manager.update(
        stop_time=stop_time,
        start_time=start_time,
        flow_model=flow_model,
        status=status,
        meta_state={},
        pull_stats=read_stats,
        push_stats={},
        job_id=job_id,
    )
```

#### Pipes
The pipes directory contains custom Pipe definitions. We find it best to organize the custom pieces in folders with each folder containing all the pipe for a specific pipeline. There should also be a folder called reusable that will contain all pipe that are common across two or more pipelines - this will help promote DRY coding.

### Writing your Entrypoint CLI
The entrypoint.py is a CLI code. You can think of it as a driver of drivers. This file will be used by orchestration layers or can be used to create your own customer orchestration layer. It is used to wrap all the various pipelines that you have written into a single templatizable call and makes it friendly to call code from the command line in Dockerized situations.

The recommendation is to use click. Click is one of the better CLI libraries written for python and simplifies a lot of the argument parsing logic. Using click we would write the CLI something along these lines.

```python
@click.command()
@click.option('--pipeline', '-p', type=str, required=True, help='This is the name of the pipe')
@click.option('--pipeline_id', '-id', type=str, required=True, help='This is a required id to uniquely identify the pipeline')
@click.option('--state_file', '-s', type=str, required=True, help='This is the file where state will be stored')
@click.option('--data_file', '-d', type=str, required=True, help='This is the file bucket where data will be stored')
def tdm(pipeline, pipeline_id, state_file, data_file):
  if pipeline == "pipe-1":
    do_something(pipeline_id, state_file, data_file)
  elif pipeline == "pipe-2":
    do_something_else(pipeline_id, state_file, data_file)
  elif pipeline == "pipe-3":
    do_something_again(pipeline_id, state_file, data_file)
  else:
    raise ValueError(f'Pipeline {pipeline} does not exist.')
```

### Argo CronWorkflows vs Kubernets CronJobs
If you have an orchestration layer ofr your pipelines that needs additional code, then that code should be stored in another directory. For Argo and Kuberentes, two popular orchestration tools, we recommend placing them in a 
argo_workflows and cronjobs directory, respectively, at the same level as pipeline_drivers and pipes folders. 

### Using Secrets in Code
One thing, don't use secrets in code in any hard coded fashion. The Pipe construct has the ability to read a secrets.yml file - this file will be stored in the users root directory in a .tdm subdirectory

Example secrets.yml below

```bash
version: 1

Read Example Secrets:
  code: SECRET_CODE
  key: SECRET_KEY
  
S3:
  access_key_id: ADFASDF78789ASD897F
  secret_access_key_id: AHDH890SDAF897987A890SDF
```

## Building a Pipeline

The basics of building a pipeline...

We start with how you will structure your project. A project repository should have the following structure (Subject to change with tool maturity)

```text
argo_workflows
pipelines
  pipeline_drivers
  pipes
Dockerfile
```

This structure is conventional and should always be followed. At current there is no override for directories or directory structure.

The argo_jobs folder should contain ALL Argo CronWorkflow manifests.

The pipelines section is where all code lives.

The pipeline_drivers subdirectory must contain either
1. Python scripts - one per pragmatic pipeline
2. A master_driver script (main.py) that reads in the /root/.tdm/config.yml
3. A combination of the two

E.g.
```text
main.py
service_now_mdm.py
airwatch_mdm.py
```

The pipes subdirectory contains all the custom pipelines. This section can be organized however one sees fit. However, it is recommended to define a logical structure that will provide meaning to anyone who is working with the code and for yourself in the future. One such way is
```text
pipelines
  pipes
    service_now
    airwatch_mdm
    cloudwatch
    common
```

## Pipelines: From Script to Production

Many pipelines start as a script. And there is no issue or incorrectness in this when you are prototyping or working out some unknowns. Sometimes they are put together by amateur or junior developers. Regardless of how they originate, there is a need to move to a production pipelines. And that generally requires a large amount of custom coding, hardening, security awareness and much more. tdm provides both a framework for building custom steps with many of these concerns abstracted away or made easy to use - while also providing out of the box functionality to keep from creating the same code over and over.

What's covered here, that is different from the technical documentation above the goes into greater detail on how to do very specific extensions to or understanding of functionality of the various components is a step-by-step walk through of moving a script into a tdm production pipeline.

For simplicity we will assume that the script is written in python. If it is not written in python, then the engineer should add steps to translate to python. We will refer to it as **script.py**

### Original script

We will be working with the code in the below section.

```python
import various_libraries_here

some_df = pd.DataFrame()
another_df = pd.DataFrame()

payload = {}

headers = {
  'aw-tenant-code': 'SECRET_CODE',
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic SECRET_KEY'}

url="DYNAMIC_ACCESS_URL"
response = requests.request("GET", url, headers=headers, data = payload)

data=json.loads(response.text)
print(data)
data1=data["Devices"]
data1=pd.DataFrame(data1, columns=['SerialNumber','Uuid','Id_Value'])



for index, row in data1.iterrows():
    try:
        info=row['info']
        id = row['Uuid']
        payload = {}
        url = "URL_%s"%id
        response = requests.request("GET", url, headers=headers, data = payload)
        data=json.loads(response.text)
        data=data["some_items"]
        some_df = pd.DataFrame.from_dict(data)
        some_df["info"]=row['info']
        some_df["id"]=row['id']
        another_df=security_df.append(some_df,sort=False)
        print('Information','info')
    except Exception as error:
        print("Error fetching data %s",id,error)


another_df.rename(columns=COLUMN_MAPPING_DEFINITION)

bucket = 'bucket_name'
csv_buffer = StringIO()
another_df.to_csv(csv_buffer,sep =',',index=False)

session = boto3.Session(
aws_access_key_id='AWS_KEY',
aws_secret_access_key='AWS_SECRET_KEY'
)

# Creating S3 Resource From the Session.
s3_resource = session.resource('s3')
s3_resource.Object(bucket, 'FILENAME_AND_PATH.csv').put(Body=csv_buffer.getvalue())
```

#### Step 1
A trained engineer will many issues with the code, and they shouldn't worry about most of them as the goal is to rewrite it in a tdm fashion. However, one step will help - and it will help with the eyes. Make sure that you install the pyhton library black

```bash
pip install black
```

Then execute black against the script

```bash
black script.py
```

and to remove extra non-standard newlines. The result of which would be something like below.

```python
import various_libraries_here


some_df = pd.DataFrame()
security_df = pd.DataFrame()

payload = {}

headers = {
    "aw-tenant-code": "SECRET_CODE",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic SECRET_KEY",
}

url = "DYNAMIC_ACCESS_URL"
response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)
print(data)
data1 = data["Devices"]
data1 = pd.DataFrame(data1, columns=["info", "id", "value"])

for index, row in data1.iterrows():
    try:
        info = row["info"]
        id = row["Uuid"]
        payload = {}
        url = "URL_%s" % id
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        data = data["some_items"]
        some_df = pd.DataFrame.from_dict(data)
        some_df["info"] = row["info"]
        some_df["id"] = row["id"]
        another_df = security_df.append(some_df, sort=False)
        print("Information", "info")
    except Exception as error:
        print("Error fetching data %s", id, error)

another_df.rename(columns=COLUMN_MAPPING_DEFINITION)

bucket = "bucket_name"
csv_buffer = StringIO()
another_df.to_csv(csv_buffer, sep=",", index=False)

session = boto3.Session(
    aws_access_key_id="AWS_KEY", aws_secret_access_key="AWS_SECRET_KEY"
)

# Creating S3 Resource From the Session.
s3_resource = session.resource("s3")
s3_resource.Object(bucket, "FILENAME_AND_PATH.csv").put(Body=csv_buffer.getvalue())
```

#### Step 2 - Breaking Down the Processing Steps

This step can really happen after Step 3 (below), but that should be up to the engineers preference. The importance of the breakdown process is to different steps of the pipeline. Each of which would constitute a different Pipe.

As we go through the code there will be three general chunks we should look for

1. Reading Data
2. Transforming Data
3. Writing Data

In the above code, which is pretty friendly as it avoids writing to storage locations we will not be using (e.g. local instead of cloud object storage (S3)), we have these as the basic chunks

**Reading Data**
Reading is a two step process in this example. The output of the first read is used as input to the second read.

*Read Step 1*
```python
some_df = pd.DataFrame()
security_df = pd.DataFrame()

payload = {}

headers = {
    "aw-tenant-code": "SECRET_CODE",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic SECRET_KEY",
}

url = "DYNAMIC_ACCESS_URL"
response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)
print(data)
data1 = data["Devices"]
data1 = pd.DataFrame(data1, columns=["info", "id", "value"])
```

*Read 2*
```python
for index, row in data1.iterrows():
    try:
        info = row["info"]
        id = row["id"]
        payload = {}
        url = "URL_%s" % id
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        data = data["some_items"]
        some_df = pd.DataFrame.from_dict(data)
        some_df["info"] = row["info"]
        some_df["id"] = row["id"]
        another_df = security_df.append(some_df, sort=False)
        print("Information", "info")
    except Exception as error:
        print("Error fetching data %s", id, error)
```

**Transforming Data**

*Transform*

The next transformation is just a line of code. It is simple, but also very common. tdm has support for this.
```python
another_df.rename(columns=COLUMN_MAPPING_DEFINITION)
```



**Writing Data**

This final step will usually not require a custom implementation. Here we are dealing with writing a pandas DataFrame out to S3 as a csv file. tdm supports this write operation.
```python
bucket = "bucket_name"
csv_buffer = StringIO()
another_df.to_csv(csv_buffer, sep=",", index=False)

session = boto3.Session(
    aws_access_key_id="AWS_KEY", aws_secret_access_key="AWS_SECRET_KEY"
)

# Creating S3 Resource From the Session.
s3_resource = session.resource("s3")
s3_resource.Object(bucket, "FILENAME_AND_PATH.csv").put(Body=csv_buffer.getvalue())
```

Note that when tdm does not support the needed functionality it is always possible to add support for it.


#### Step 3 - Creating Pipes

Now, given chunks of code we need to create Pipe for each of them.

##### Creating the Read Pipe
Let's start with a Pipe to read the data. If you recall from above on how we structure our code, let's call this pipeline "Example Pipeline" so that in the pipes directory we create a subdirectory call 'example_pipeline' and in there a file called 'read.py'
```bash
some_project
  pipeline_drivers
  pipelines
    example_pipeline
      read_example_data.py
```

The contents of read.py should start as a ReaderPipe type that have the reading part of the script from abnove.
```python
class ReadExampleData(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, **kwargs) -> ReaderPipe:
    some_df = pd.DataFrame()
    another_df = pd.DataFrame()

    payload = {}

    headers = {
        "aw-tenant-code": "SECRET_CODE",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic SECRET_KEY",
    }

    url = "DYNAMIC_ACCESS_URL"
    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)
    print(data)
    data1 = data["Devices"]
    data1 = pd.DataFrame(data1, columns=["info", "id", "value"])

```

This is not yet executable and is still rather messy
* remove some_df - it is never used. Also, another_df is not used here either -> remove it.
* set data={} in requests GET call - and remove payload variable
* move url to key word argument

```python
class ReadExampleData(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, url: str, **kwargs) -> ReaderPipe:
    headers = {
        "aw-tenant-code": "SECRET_CODE",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic SECRET_KEY",
    }

    response = requests.request("GET", url, headers=headers, data={}})

    data = json.loads(response.text)
    print(data)
    data1 = data["Devices"]
    data1 = pd.DataFrame(data1, columns=["info", "id", "value"])

```

Remove the print command. We should never print the data out. Not only can this cause logs (as print commands should rightly be in production) to blow up, but this can result in sensitive information being logged out to less secure systems and/or violate compliance controls. In general, unless you are locally hacking at something - never use print as a 'logger'.

Also, you should see that 'Devices' is all that is needed from the read text - so simplify things further by combining lines of code.

Also, there is no reason to have data and data1. Make it all one line.

```python
class ReadExampleData(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, url: str, **kwargs) -> ReaderPipe:
    headers = {
        "aw-tenant-code": "SECRET_CODE",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Basic SECRET_KEY",
    }

    response = requests.request("GET", url, headers=headers, data={}})

    data = pd.DataFrame(json.loads(response.text)["Devices"], columns=["info", "id", "value"])
```

The next step is to move secrets to secrets.yml. This should be

```bash
Read Example Secrets:
  code: SECRET_CODE
  key: SECRET_KEY
```

And then to use the self._secrets property in the code directly.

```python
class ReadExampleData(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, url: str, **kwargs) -> ReaderPipe:
    headers = {
        "aw-tenant-code": self._secrets.code,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {self._secrets.key}",
    }

    response = requests.request("GET", url, headers=headers, data={}})

    data = pd.DataFrame(json.loads(response.text)["Devices"], columns=["info", "id", "value"])
```

We are almost there, we still need to adjust the metadata and return self.

Also, change data to df, that is the conventional approach when working with dataframes.

```python
class ReadExampleData(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, url: str, **kwargs) -> ReaderPipe:
    headers = {
        "aw-tenant-code": self._secrets.code,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {self._secrets.key}",
    }

    response = requests.request("GET", url, headers=headers, data={}})

    df = pd.DataFrame(json.loads(response.text)["Devices"], columns=["info", "id", "value"])

    self._state.update_metadata(key="data", value=df)

    return self
```

Now, two final things to have a minimally production version of this code. We need to add logging and handle any exceptional situations.
1. requests call can have a return that has a Status Code that is not 200 - indicating some kind of error.
2. Other errors can occur - 'Devices' not present in dataframe, secrets are missing, etc... But such errors will bubble up with clarity. The requests error would end up looking like a data error - which it is not.

```python
class ReadExampleData(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, url: str, **kwargs) -> ReaderPipe:
    headers = {
        "aw-tenant-code": self._secrets.code,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {self._secrets.key}",
    }
    response = requests.request("GET", url, headers=headers, data={}})

    if response.status_code != 200:
      raise ValueError(
        {
          "content": response.text,
          "code": response.status_code,
          "reason": response.reason,
        }
      )
    else:
      self._logger.debug('Successfully read data from restful endpoint.')


    df = pd.DataFrame(json.loads(response.text)["Devices"], columns=["info", "id", "value"])

    self._state.update_metadata(key="data", value=df)

    return self
```

Well, we are almost done, I lied. We need to add some docstrings.

```python
class ReadExampleData(ReaderPipe):
  """Example Pipe for reading data from a RESTful endpoint."""
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, url: str, **kwargs) -> ReaderPipe:
    """Execution of the ReadExampleData data ingestion pipe. Will pull data from a RESTful endpoint and pass the resulting pandas.DataFrame to the metadata layer.

    Args:
      url: URL endpoint from which data will be retrieved.

    Raises:
      ValueError: When the API call returns a status code other than 200.
    """
    headers = {
        "aw-tenant-code": self._secrets.code,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {self._secrets.key}",
    }
    response = requests.request("GET", url, headers=headers, data={}})

    if response.status_code != 200:
      raise ValueError(
        {
          "content": response.text,
          "code": response.status_code,
          "reason": response.reason,
        }
      )
    else:
      self._logger.debug('Successfully read data from restful endpoint.')


    df = pd.DataFrame(json.loads(response.text)["Devices"], columns=["info", "id", "value"])

    self._state.update_metadata(key="data", value=df)

    return self
```

*Note:* it could be argued that we should either pass the filter columns in as parameters or create a new step that filters the data. There are good arguments in both ways,

*Read 2*
If you recall, the read process was two steps. Each of these will be a separate ReaderPipe. Yes, one read can be input to another - why not. For reference, we will start with adding the data read to a ReaderPipe

```python
class ReadExampleDataIteratively(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, **kwargs) -> ReaderPipe:
    for index, row in data1.iterrows():
    try:
        info = row["info"]
        id = row["id"]
        payload = {}
        url = "URL_%s" % id
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        data = data["some_items"]
        some_df = pd.DataFrame.from_dict(data)
        some_df["info"] = row["info"]
        some_df["id"] = row["id"]
        another_df = security_df.append(some_df, sort=False)
        print("Information", "info")
    except Exception as error:
        print("Error fetching data %s", id, error)
```

This is just the start, we need to be able to get the data from the previous step. This will - under an assumption - come from a parent Pipe - the first parent Pipe. The way to get the data is then to create a reference to it in the code. Now, since this is done often it is useful to have a pattern to use for this

```python
class ReadExampleDataIteratively(ReaderPipe):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, url: str, **kwargs) -> ReaderPipe:    
    if len(self._parents) == 1:
            df: pd.DataFrame = self._parents[0].info["data"]
        else:
            raise ValueError("No parent Pipe was provided.")

        if data is None:
            raise ValueError("'data' not found in parent Pipe's metadata.")

    for _, row in df.iterrows():
    try:
        info = row["info"]
        id = row["id"]
        payload = {}
        url = "URL_%s" % id
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        data = data["some_items"]
        some_df = pd.DataFrame.from_dict(data)
        some_df["info"] = row["info"]
        some_df["id"] = row["id"]
        another_df = security_df.append(some_df, sort=False)
        print("Information", "info")
    except Exception as error:
        print("Error fetching data %s", id, error)
```

Now, without spending the same time breaking things down as before, we should end up with something like this.

```python
class ReadExampleDataIteratively(ReaderPipe):
  """Example Pipe for reading data from a RESTful endpoint iteratively given an input parent with information to iterate over."""
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def _run(self, **kwargs) -> ReaderPipe:
    """Execution of the ReadExampleData data ingestion pipe. Will pull data from a RESTful endpoint and pass the resulting pandas.DataFrame to the metadata layer.

    Raises:
      ValueError: When the API call returns a status code other than 200.
    """
    if len(self._parents) == 1:
            df: pd.DataFrame = self._parents[0].info["data"]
        else:
            raise ValueError("No parent Pipe was provided.")

        if data is None:
            raise ValueError("'data' not found in parent Pipe's metadata.")

    headers = {
      "aw-tenant-code": self._secrets.code,
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": f"Basic {self._secrets.key}",
    }

    iteratively_constructed_df = pd.DataFrame()
    for index, row in df.iterrows():
      try:
        url = f"URL_{id}"
        response = requests.request("GET", url, headers=headers, data={})
        if response.status_code != 200:
          raise ValueError(
            {
              "content": response.text,
              "code": response.status_code,
              "reason": response.reason,
            }
          )

        local_df = pd.DataFrame.from_dict(
          json.loads(response.text)['some_items']
        )
        local_df["info"] = row["info"]
        local_df["id"] = row["id"]
        iteratively_constructed_df = another_df.append(local_df, sort=False)
        self._logger.info({"Information": "info"})
      except:
        raise ValueError(
          {
            "Summary": f"Error fetching data for id={id}",
            'stack_trace': trackback.format_exc(),
          }
        )

      self._state.update_metadata(key="data", value=iteratively_constructed_df)

      return self
```

This last read step we will create in a file called read_example_data_iteratively.py. The file tree should now look like

```bash
some_project
  pipeline_drivers
  pipelines
    example_pipeline
      read_example_data.py
      read_example_data_iteratively.py
```


##### Creating the Transform Pipe

The sole transformation is just a line of code. It is simple, but also very common. tdm has support for this.
```python
another_df.rename(columns=COLUMN_MAPPING_DEFINITION)
```

You will just use the RenameColumns TransformerPipe.

```python
# some_config has a parameter for column_map
remap_columns = RenameColumns(**some_config)  

remapped_columns = remap_columns.run(parent=some_parent)
```

##### Creating the Write Pipe

If you recall, we also have methods for reading data. The first pass of this framework had a WriterPipe for each destination. However, the internal writing configuration makes this unnecessary. So you would use a FileWriter

```python
writer = FileWriter(**some_config)

data_wrote = writer.run(parent=remapped_columns)
```

In most cases you will not need to worry about creating custom write methods - unless there is a new destination. In this situation (and not covered here) you will need to create a new DataframeWriter (or similar) Writing method that will be constructed within the FileWriter.

#### Building Pipeline Driver

Now that we have created some custom Pipes and decomposed the pipeline, we need to create the orchestration layer to execute the pipeline. This is referred to as a pipeline_driver in the application layer. Each pipeline driver will take the name of the pipeline - this is the convention. Once creating this file, the file tree will be

```bash
some_project
  pipeline_drivers
    example_pipeline.py
  pipelines
    example_pipeline
      read_example_data.py
      read_example_data_iteratively
```

Let's walk through creating the pipeline_driver for example_pipeline.

##### Step 1 - Create a skeleton for the drivers

Create a base driver that has a method call and a set of pipeline instnaces.

```python
def example_pipeline(): <- we don't know what goes here yet

  workflow_config = {}

  # Create skeleton instances of all the pipes
  reader = ReadExampleData(**workflow_config['read'])
  iterative_reader = ReadExampleDataIteratively(**workflow_config['read'])
  column_renamer = RenameColumns(**workflow_config['read'])
  writer = FileWriter(**workflow_config['read'])

```

##### Step 2 - create basic orchestration flow

Write the pipeline orchestration flow

```python
def example_pipeline(): <- we don't know what goes here yet

  workflow_config = {}

  # Create skeleton instances of all the pipes
  reader = ReadExampleData(**workflow_config['read'])
  iterative_reader = ReadExampleDataIteratively(**workflow_config['read_iteratively'])
  column_renamer = RenameColumns(**workflow_config['rename'])
  writer = FileWriter(**workflow_config['write'])

  # pipeline orchestration
  read_data = reader.run()
  iteratively_read = reader.run(parent=iteratively_read)
  renamed_columns = column_renamer.run(parent=iteratively_read)
  written_data = writer.run(parent=renamed_columns)
```

##### Step 3 - Create Configuration

The configuration is how we are stating the inputs to the pipeline. You can opt for key word arguments in the constructors, but that would be a user decision - and when declarative pipelines are ready would require additional work.

```python
def example_pipeline(
  pipeline_id: str,
  job_id: str,
):

  workflow_config = {
      {
      "read": {
        "name": "Read Data",
        "secrets": {
          "type": "yamlconfigreader",
          "name": "Read RESTful Secrets",
        },
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "read": {
        "name": "Read Data",
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "read": {
        "name": "Read Data Iteratively",
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "write": {
        "name": "Write Data",
        "writer": {
          "name": "S3 Writer",
          "type": "FileWriter",
          "config": {
            "bucket": "name of bucket",
            "secrets": {
              "type": "yamlconfigreader",
              "name": "S3 Secrets",
            },
          },
        }
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },
    }

  # Create skeleton instances of all the pipes
  reader = ReadExampleData(**workflow_config['read'])
  iterative_reader = ReadExampleDataIteratively(**workflow_config['read'])
  column_renamer = RenameColumns(**workflow_config['read'])
  writer = FileWriter(**workflow_config['read'])

  # pipeline orchestration
  read_data = reader.run()
  iteratively_read = reader.run(parent=iteratively_read)
  renamed_columns = column_renamer.run(parent=iteratively_read)
  written_data = writer.run(parent=renamed_columns)
```

##### Step 4 - Adding a State Manager

The StateManager allows you to track the history of a data pipeline. Make sure to use a StateManager that is right for your needs.

```python
def example_pipeline(
  pipeline_id: str,
  job_id: str,
  asset: str,
  state_bucket: str,
  data_bucket: str
):


  state_manager = S3StateManager(
    **{
      "name": f"State Manager for SNOW Data - {asset}",
      "state_object_name": f"SNOW Data Pull - {asset}",
      "pipeline_id": pipeline_id,
      "job_id": job_id,
      "version": 1,
      "writer": {
        "type": "S3CSVWriter",
        "config": {
          "container": state_bucket,
          "secrets": {"name": "S3", "type": "yamlconfigreader"},
        },
        "name": "S3 State Writer",
      },
      "reader": {
        "type": "S3CSVReader",
        "config": {
          "bucket": state_bucket,
          "secrets": {"name": "S3", "type": "yamlconfigreader"},
        },
        "name": "S3 State Reader",
      },
    }
  )

  workflow_config = {
      {
      "read": {
        "name": "Read Data",
        "secrets": {
          "type": "yamlconfigreader",
          "name": "Read RESTful Secrets",
        },
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "read": {
        "name": "Read Data",
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "read": {
        "name": "Read Data Iteratively",
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "write": {
        "name": "Write Data",
        "writer": {
          "name": "S3 Writer",
          "type": "FileWriter",
          "config": {
            "bucket": data_bucket,
            "secrets": {
              "type": "yamlconfigreader",
              "name": "S3 Secrets",
            },
          },
        }
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },
    }

  # Create skeleton instances of all the pipes
  reader = ReadExampleData(**workflow_config['read'])
  iterative_reader = ReadExampleDataIteratively(**workflow_config['read'])
  column_renamer = RenameColumns(**workflow_config['read'])
  writer = FileWriter(**workflow_config['read'])

  # pipeline orchestration
  read_data = reader.run()
  iteratively_read = reader.run(parent=iteratively_read)
  renamed_columns = column_renamer.run(parent=iteratively_read)
  written_data = writer.run(parent=renamed_columns)
```

##### Step 5: Using the StateManager

To really use the state manager, you need to make sure that you are able to capture data from your pipeline, even if it fails. So we add some exception handling and create an entry(ies) to the StateManager
```python
The StateManager allows you to track the history of a data pipeline. Make sure to use a StateManager that is right for your needs.

```python
def example_pipeline(
  pipeline_id: str,
  job_id: str,
  state_container: str,
  asset: str,
  state_bucket: str,
  data_bucket: str,
):


  state_manager = S3StateManager(
    **{
      "name": f"State Manager for SNOW Data - {asset}",
      "state_object_name": f"SNOW Data Pull - {asset}",
      "pipeline_id": pipeline_id,
      "job_id": job_id,
      "version": 1,
      "writer": {
        "type": "S3CSVWriter",
        "config": {
          "container": state_bucket,
          "secrets": {"name": "S3", "type": "yamlconfigreader"},
        },
        "name": "S3 State Writer",
      },
      "reader": {
        "type": "S3CSVReader",
        "config": {
          "bucket": state_bucket,
          "secrets": {"name": "S3", "type": "yamlconfigreader"},
        },
        "name": "S3 State Reader",
      },
    }
  )

  workflow_config = {
      {
      "read": {
        "name": "Read Data",
        "secrets": {
          "type": "yamlconfigreader",
          "name": "Read RESTful Secrets",
        },
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "read": {
        "name": "Read Data",
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "read": {
        "name": "Read Data Iteratively",
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },

      "write": {
        "name": "Write Data",
        "writer": {
          "name": "S3 Writer",
          "type": "FileWriter",
          "config": {
            "bucket": "name of bucket",
            "secrets": {
              "type": "yamlconfigreader",
              "name": "S3 Secrets",
            },
          },
        }
        "pipe_id": uuid.uuid4().hex,
        "job_id": job_id,
        "pipeline_id": pipeline_id,
      },
    }

  start_time = datetime.now().timestamp()
  try:
    status = PipeStatus.QUEUED

    # Instances of all pipes
    reader = ReadExampleData(**workflow_config['read'])
    iterative_reader = ReadExampleDataIteratively(**workflow_config['read'])
    column_renamer = RenameColumns(**workflow_config['read'])
    writer = FileWriter(**workflow_config['read'])

    # pipeline orchestration
    executed_pipes = []
    read_data = reader.run()
    executed_pipes.append(read_data)

    iteratively_read = reader.run(parent=iteratively_read)
    executed_pipes.append(iteratively_read)

    renamed_columns = column_renamer.run(parent=iteratively_read)
    executed_pipes.append(renamed_columns)

    written_data = writer.run(parent=renamed_columns)
    executed_pipes.append(written_data)

    status = PipeStatus.FAILURE if any(
      [True for result in executed_pipes if result.status == PipeStatus.FAILURE]
    ) else PipeStatus.SUCCESS

  except:
    _logger.error(msg=traceback.format_exc())
    status = PipeStatus.FAILURE
    raise

  finally:
    stop_time = datetime.now().timestamp()
    state_manager.update(
        stop_time=stop_time,
        start_time=start_time,
        flow_model=workflow_config,
        status=status,
        meta_state={},
        pull_stats=read_stats,
        push_stats={},
        job_id=job_id,
    )
```

##### Step 6: Writing an entrypoint
An entrypoint is a CLI that can be used to execute the pipeline in orchestration platform like Argo Workflows, Kubernetes with CronJobs, etc...

The entrypoint should be something like:

```python
@click.command()
@click.option(
    "--pipeline", "-p", type=str, required=True, help="This is the name of the pipe"
)
@click.option(
    "--pipeline_id",
    "-id",
    type=str,
    required=True,
    help="This is a required id to uniquely identify the pipeline",
)
@click.option(
    "--asset",
    "-f",
    type=str,
    required=True,
    help="This is the name of the asset",
)
@click.option(
    "--state_bucket",
    "-s",
    type=str,
    required=True,
    help="This is the S3 bucket where state will be stored",
)
@click.option(
    "--data_bucket",
    "-d",
    type=str,
    required=True,
    help="This is the S3 bucket where data will be stored",
)
def tdm(
    pipeline: str,
    pipeline_id: str,
    state_bucket: str,
    data_bucket: str,
) -> None:
    if pipeline == "example_pipeline":
        example_pipeline(
            pipeline_id=pipeline_id,
            job_id=uuid.uuid4().hex,
            asset=asset,
            state_bucket=state_bucket,
            data_bucket=data_bucket,
        )
     else:
        raise ValueError(f'Pipeline {pipeline} does not exist.')
```

The first part of the code

##### Step 7: Orchestration - Creating the Argo Workflow
Here we are assuming that you are using an Argo Workflow. This should be similar for each.

Make sure to change the schedule - avoid too many pipelines scheduled at the same time.

Each pipeline needs a unique pipeline_id.

Set the other CLI variables accordingly.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: CronWorkflow
metadata:
  name: example_pipeline
spec:
  schedule: "20 * * * *"
  concurrencyPolicy: "Replace"
  startingDeadlineSeconds: 0
  workflowSpec:
    imagePullSecrets:
      - name: gcr
    entrypoint: example_pipeline
    templates:
    - name: Example Pipeline
      container:
        image: your_image
        imagePullPolicy: Always
        command: [ python,
                   -m,
                   pipelines.pipeline_drivers.entrypoint,
                   --pipeline,
                   example_pipeline,
                   --pipeline_id,
                   897289734789123894,
                   --asset,
                   some_asset,
                   --state_bucket,
                   state_bucket,
                   --data_bucket,
                   example_data ]
```

##### Step 8: Secrets & Configurations
While it is not straightforward at this time to always use a configuration for your pipelines - simple cases you can - it is best to store the alerting configuration in the config.yml in the .tdm directory. When starting development you may not have a configuration for your alerting. Use the one below.

```bash
version: 1

alert_managers:
  - name: Alert Manager
    type: nullalertmanager
    config:
      name: Not Real
      secrets:
        type: yamlconfigreader
        name: Not a secret

alert
```

Secrets will be stored in the same location as secrets.yml

#### Building & Deploying Pipelines
Building and deploying your pipelines should follow at least a dev/prod flow. That means, you will need an orchestration configuration for each of two different environements, two environments and deployment endpoints for dev and prod, respectively. And this even goes for locations where data is stored - preferably in different cloud accounts.

We currently using this approach here at Tellius. In our projects we create a pipelines in a monorepo - with customer or domain level separation. This allows us to keep similar code all in one place. And the pipelines are reusable - the same conventional structure will exist in all places. When working on one pipeline we will
1. Create the new pipeline code
2. Create a new driver
3. Create a new entry in the entrypoint file
4. Create a new test (we have an additional directory for tests)
5. We will test locally if possible to identify any issues before committing code if possible.
6. We will commit and push code to development branch
7. Dev CI flow will execute
8. Docker Image will be created
9. Argo CronWorkflow will be pushed to S3
10. (Manually right now) Argo will manually be updated with the latest version of the manifest.
11. Argo will be triggered (manually) - maybe a few times - on a dev Argo deployment
12. We check the logs to see if anything went wrong - eventhough local may have worked - remote may not have.
13. If successful and ready to push to production go to 14, else iterate and improve (same if failure)
14. Merge code to main branch
15. CI/CD flow will execute again
16. 10-12 will repeat.

The CI/CD flow is approximately this below at minimum

![Basic Pipeline](images/build_flow.png)













<!--
### Declarative API

Before we start, let's make it clear, the Declarative API is more advanced in usage than the Pragmatic API, which we describe below. However, it is much cleaner and is what should be used in most production situations. The Pragmatic API is best suited for development and testing of new pipelines and new Pipes.

The declarative API works by specifying the
1. A collection of Alert Managers
2. A Collection of Pipelines

```yaml
version: v1

alert_managers:
  - name: Email Alert Manager
    type: gmailemailalertmanager
    config:
      email_addresses:
        - alert_email@some_email.something
      mode: mfa
      secrets:
        type: yamlconfigreader
        name: Gmail Secrets

pipelines:
  - name: Device Inventory
    pipes:
      - name: Query Inventory
        type: QueryDI
        config:
          secrets:
            type: yamlconfigreader
            name: Inventory Secrets

      - name: Add Date From Current Time
        type: appenddatecolumn
        config:
          parents:
            - Query Inventory

      - name: Write to Disk
        type: writelocalfile
        config:
          parents:
            - Add Data From Current Time
          directory: output_data

  - name: Time Difference
    pipes:
      - name: Query Time Difference
        type: QueryTD
        config:
          secrets:
            type: yamlconfigreader
            name: Time Difference Secrets

      - name: Add Date From Current Time
        type: appenddatecolumn
        config:
          parents:
            - Query Time Difference
```

All parts of the declarative API require that a field of `name` be present. The name field provides a unique identifier for the

The first part, that alert_manager section is required when you need to setup or configure alerting for pipelines. This is used in the event that there are issues with a pipeline and an alert is required.

Each AlertManager has a type. This is the name of the class and can be any mix of upper and lowercase.

There will also be a configuration. The configuration (`config`) section will be the values required to construct the class. When the class requires secrets there will be a special section called _secret_. The secrets section requires specifying a type. The type refers to the class type that will be used to `read` the secrets into memory. The `name` in the secrets section corresponds to the secret as named in the `secrets.yml`.

```yaml
alert_managers:
  - name: Email Alert Manager
    type: gmailemailalertmanager
    config:
      email_addresses:
        - john.aven@tellius.com
      mode: mfa
      secrets:
        type: yamlconfigreader
        name: Gmail Secrets
 ```

The pipelines section describes a collection of various different pipelines that will get scheduled and executed. The pipelines have a `name` and `pipes` fields. The pipes field is a collection of different Pipes that will be executed in order of dependency. Each Pipe will have a `name`, `type` and `config` just as the AlertManager. A config within a pipe will have an additional field `parents` that will list, by names, the Pipes in the current pipeline, which must be executed beforehand.

```yaml

pipelines:
  - name: Pipeline 1
    pipes:
      - name: Pipe One
        type: pipelineTypeOne
        config: SOME_CONFIGURATION_DICTIONARY
      - name: Pipe Two
        type: pipelineTypeTow
        config:
          some_parameter: some_value
          parents:
            - Pipe One
``` -->
<!--
### Pragmatic API

The Pragmatic API is capable of everything that the Declarative API is. However, it is generally easier for a beginner to write a pipeline pragmatically. An example, and simple, pipeline is seen below

```python

# Set up the pipes (define the pipes)
read_secrets = {}
read_configuration = {
  'parameter': 'value'
  'secrets': pipe_secrets
}
read_pipe = SomePipe(**read_configuration)

transform_configuration = {}
transform_pipe = TransformPipe(**transform_configuration)

write_configuration = {}
write['secrets'] = {}
write_pipe = WritePipe(**write_configuration)

# Create pragmatic pipe

read = read_pipe.run()
transform = transform_pipe.run(parent=read)
write = write_pipe.run(parent=transform)

```

In the above the notation **some_dictionary is python shorthand for passing a bunch of named keyword arguments.

This approach is pretty simple. It is allows one to interactively build a pipeline and test it out. This is especially useful locally.

## Orchestration of Pipeline Execution

Orchestrating pipelines is the act of executing the pipeline manually or through the use of an orchestration engine.

### Local Execution

Locally executing a pipeline should only be done during testing. The execution should happen from the root of your project. And assuming the suggested project structure you would called
```bash
cd your_project
python -m pipelines.pipeline_drivers.your_pipeline
```

### Cron Workflows

## Extending the Library

tdm is designed to be extended both in the library and externally within your own pipeline's codebase. We will cover here how to extend the library locally within your pipelines and how to update / modify deployments to support your new code.

### Creating New Transformation, Readers, and Writers

The library comes with a number of base classes, all of which can be explored in the libraries' documentation - included in the codebase for ease of access.

To create a new Pipe that has a type of Read, Write or Transform you will need to create a new class that inherits from these classes and implements the _run(...) method

```python
from tellius_data_manager.pipes.transformers.transformer_pipe import Transform


class NewTransform(Transform):
    def _run(self, local_arguments: some_type = None, **kwargs):
# Do Something Here
```

Make sure to include explicitly any variables that



### Including New Code in Your Pipeline

### Updating Local Deployments

### Updating Docker Deployments

### Building New Connectors

### Creating Custom Transformations

## Configuring Your Pipeline

The configuration, in the current version of tdm is describe below

```yaml
version: v1

pipelines:
  - name:
    pipes:
      - name: Read S3

```

Features to Come:

* Auto Argo Creation
* Kubernetes Secrets
* AWS Stored Secrets

## Software Design Considerations

Software is designed using SOLID OOP design principles, and any extension to it must follow this design. Any extension
beyond what is currently present must be discussed - especially if it changes or breaks current design abstractions.

In terms of design patterns the solution relies on a combination of the
* Strategy Pattern
* Polymorphic Factory Pattern
* Builder Pattern -->
