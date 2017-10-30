![](https://travis-ci.org/andykuszyk/jenkins-data-science-summary.svg?branch=master)

# jenkins-data-science-summary
A python command line tool that can generate a summary report compatible XML file that summarizes data science jobs in Jenkins. See the Jenkins plugin here:

https://wiki.jenkins.io/display/JENKINS/Summary+Display+Plugin

## Installation
```
pip install jdss
```

## Usage
### Single build results (e.g. training a model)
Build a report that shows some metrics and some images on multiple tabs:
```
jdss job --tab metrics.json --tab *.png --names Metrics Images --output ./
```
This will generate a `summary.xml` file in the current directory, with two tabs.

### Multiple build results (e.g. summarising multiple models)
Summaries multiple jobs in a table:
```
jdss jobs --url http://jenkins/my-job/ --history 10 --artifact metrics.json
```

With multiple artifacts:
```
jdss jobs --url http://jenkins/my-job/ --history 10 --artifact metrics1.json metrics2.json
```

With job parameters
```
jdss jobs --url http://jenkins/my-job/ --history 10 --artifact metrics.json --parameters parameter1 parameter2
```

With Jenkins basic authentication:
```
jdss jobs --url http://jenkins/my-job/ --history 10 --artifact metrics.json --user user.name --password p4ssword1
```

## Releasing
```
./release.sh [current-version] [new-version]
```
