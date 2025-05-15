
## Description


## Requirements
You need to have Bazel (https://bazel.build/) to build this project.
Check https://docs.bazel.build/versions/4.1.0/install.html for the installation.
As an alternative, if you already have Visual Studio Code and Docker installed you can use the devcontainer provided in the project to run a linux container with Bazel included. 

## Build 
To build the executable:
```Bash
bazel build ...
```

## Run
To run the generated executable:
```Bash
./bazel-bin/src/project1
``` 

## Tests
To run the tests:
```Bash
bazel test --test_output=all ...
```