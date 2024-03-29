[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10761502.svg)](https://doi.org/10.5281/zenodo.10761502) [![Documentation Status](https://readthedocs.org/projects/text-analysis/badge/?version=latest)](https://text-analysis.readthedocs.io/en/latest/?badge=latest)

# Text Analysis with Grobid

## Description
This project uses **Grobid**, a machine learning software, to extract structured metadata and content from documents in PDF format. The extracted information includes a word cloud with the keywords of the abstracts of the all documents, a bar chart showing the number of figures and the URLs that appear in each PDF document.

*Note: There are already 10 PDFs in the repository. If you want to process your own PDFs, please save them in the "papers" folder.*

## Documentation
You can find the documentation [here](https://text-analysis.readthedocs.io/en/latest/)

## Requirements
To run this program you will need:
* [Docker](https://docs.docker.com/engine/install/) which is a software that provides a convenient way to package, distribute and run applications as containers, ensuring consistency across different environments.
* [Grobid](https://github.com/kermitt2/grobid) which is a machine learning-based toolkit for extracting information from documents in PDF format.


## Installation instructions
**Step 1:** Clone the repository from GitHub to your local machine:

```
git clone https://github.com/yiminzhou7/Text-Analysis.git
```

**Step 2:** Start the docker server.

**Step 3:** Install Grobid

```
docker pull lfoppiano/grobid:0.7.2
```


## Execution instructions

### Conda
**Step 1:** Start the Docker server.

**Step 2:** Run Grobid on **localhost:8070**:

```
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

You can check if Grobid is running properly by openning a web browser and visit the following URL: [http://localhost:8070](http://localhost:8070).

**Step 3:** Open a new command line and create a blank virtual environment with [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) with a name in python 3.10

```
conda create -n text_analysis python=3.10
```

**Step 4:** Activate the environment.

```
conda activate text_analysis
```

**Step 5:** Go to the main directory ("Text-Analysis") and install the dependencies from `requirements.txt` file:

```
pip install -r requirements.txt
```

**Step 6:** Before running the main program, it is recommended to run the `testing.py` file found in the "**tests**" folder. For this purpose, stay in the main directory ("Text-Analysis") and execute

```
python tests/testing.py
```
    
**Step 7:** After passing the tests, stay in the main directory and execute the **main** program

```
python main.py
```

Once executed, the program will save the results in the "**results**" folder:
- A figure of wordcloud saved as "wordcloud.png".
- A histogram saved as "figures.png".
- URLs of each paper saved as "links.txt".

**Step 8:** Once the results have been obtained, stop the container where it is running Grobid.

To find out the CONTAINER_ID, execute:

```
docker container ps
```

Then, stop the container

```
docker container stop CONTAINER_ID
```


### Docker compose
**Step 1:** Start the Docker server.

**Step 2:** Stay in the main directory ("Text-Analysis") and execute (*Note: make sure there are no programs using port 8070 because that's where Grobid will run*): 

```
docker-compose up
```

In this case, docker-compose will run the tests ("tests/testing.py") before running the main program ("main.py").

If all tests are passed, then the main program will be executed, otherwise it stops.
    
Once executed, the program will save the results in the "**results**" folder:
- A figure of wordcloud saved as "wordcloud.png".
- A histogram saved as "figures.png".
- URLs of each paper saved as "links.txt".

**Step 4:** Once the results have been obtained, execute

```
docker-compose down
```


## Running examples
The main program has been run with 10 PDFs (stored in the **papers** folder). 

The wordcloud results of the abstracts, histogram of number of figures and the URLs found in each paper are shown below.
<figure>
  <img src="docs/wordcloud.png" alt="Wordcloud" style="width:450px">
  <figcaption><i>Figure 1. Wordcloud generated from the abstracts text.</i></figcaption>
</figure>


<figure>
  <img src="docs/figures.png" alt="Histogram" style="width:470px">
  <figcaption><i>Figure 2. Histogram of number of figures per paper.</i></figcaption>
</figure>


<figure>
  <img src="docs/links.png" alt="Histogram" style="width:470px">
  <figcaption><i>Figure 3. URLs of each paper.</i></figcaption>
</figure>




## Preferred citation
Yimin Zhou.

## Where to get help
You can write to yimin.zhou@alumnos.upm.es about any help you may need.
