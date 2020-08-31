# Contributing Guidelines for eLife Sprint Participants

## Welcome!
The project leads are Philippe Rocca-Serra (@proccaserra) & Lilly Winfree (@lwinfree). 
Phil will be available during 2nd, 3rd & 4th sessions on both days, and Lilly will be available during the 3rd, 4th & 5th sessons on both days.

## Project Intro
Scientific articles make extensive use of tables to present information such as: lists of reagents, lists of tools, lists of experimental results, and analytical results.
However, these table's structures are often ad-hoc, making reuse and/or information extraction labor intensive. Our solution to this problem is to use 
[Frictionless datapackages](https://specs.frictionlessdata.io/data-package/)to make sure table headers and structures are being described in a machine readable form.
We have previously generated [templates of datapackages for reporting statistical results](https://gitlab.com/datascriptor/datascriptor-fldatapackages),
and we propose to create more tabular templates informed by the analysis of existing tables and identification of patterns in those.
To start, we will analyse eLife Tables (using this dataset) to identify key patterns with text mining. We will then build datapackage templates (and test these templates with researchers and publishers).
Next, we plan to add new functionality to the DataScriptor app to allow for uploads of these new datapackages. The Datascriptor app helps write reproducible manuscripts. 
The ultimate/long term goal would be to generate text for a manuscript based on these newly generated datapackage templates that have been informed by real eLife article data.


## Project Goals / Tasks
We are using [issues](https://github.com/ISA-tools/frictionless-collab/issues) to list the project goals/tasks and are organizing these goals on a [project board](https://github.com/ISA-tools/frictionless-collab/projects/1).
Each issue has a label for things like what kind of help is needed to work on that goal.

Check out the project's canvas for a visual overview of the project: https://docs.google.com/presentation/d/1nxjUH-A9M0-mDtr3k5hSdnemmPPzYaRiX45ZZ-LJmKs/

At the beginning of each session, we will try to come together & plan out tasks for that session.
At the end of each session, we will do a recap of what was achieved during the session.
If you miss these recaps, reach out to either Phil or Lilly on Slack to get caught up!

## Contributing roles
Why should you work on our team? We are passionate about making research articles more reproducible, easier to understand, and easier to write!
You will learn about these ideas, have a chance to talk about your ideas, and also learn about the open source [Frictionless Data project](https://frictionlessdata.io/) and [Datascriptor project](https://gitlab.com/datascriptor).
If that sounds fun, come join us! Specifically, we are looking for help from the following contributors:
- You know JavaScript or Python to help generate Frictionless datapackages and work with the existing datascriptor app to add new upload functionality.
- You are familiar with text mining/NER to identify key patterns in data reporting from eLife publication data. 
- You are a researcher, editor, or other publication experts to help us evaluate and test our datapackage profiles.
We have tried to create enough goals to get started, but are eager to have all contributors help drive the goals of this project! Bring your ideas :-) 

## Slack
We are using our Slack channel #frictionless-datascriptor to communicate throughout the Sprint.

## Code of Conduct
During the Sprint, this project adheres to the [eLife Sprint Code of Conduct](https://sprint.elifesciences.org/code-of-conduct/).
After the Sprint, please refer to the [Frictionless Data Code of Conduct](https://frictionlessdata.io/code-of-conduct/).
(The eLife Sprint CoC has time limits attached to it, which is why we need two CoCs).
