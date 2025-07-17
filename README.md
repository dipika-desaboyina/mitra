# mITRa

# Section 1 - Project Description

## 1.1 Project

**mITRa** is an emotionally intelligent AI assistant designed to help
Indian taxpayers navigate the complexities of e-filing with empathy,
retrieval-based reasoning, and conversational support.

## 1.2 Description

Tax return filing is an emotionally overwhelming process for the average
Indian around this time of the year. It is not easy to find answers on
search engines alone because most answers are filled with jargon terms,
acronyms, and taxation concepts that are not intuitive for a person with
no background knowledge in the field, which in turn leads to going down
rabbit holes of trying to find and understand information that is
directly applicable to their specific use case. This is where mITRa
comes in - mITRa is a chatbot that is powered by retrieval based system
that pulls information from an exhaustive set of Income Tax
documentation in one place and answers all of the users' queries and
concerns in an emotionally intelligent way, attuned to the tone and
needs of the user.

## 1.3 Revision History

  --------------------------------------------------------------------------
  **Date**            **Comment**                                        **Author**
  ------------ ------------------------------------------------ ------------
  2025-07-16          Design Document V1 drafted                         Dipika Desaboyina
                                                              

  2025-07-17          User & query modelling, document_scraper.py        Dipika Desaboyina                                    

                                                                

                                                                

                                                                
  --------------------------------------------------------------------------

**Contents**

> [[Section 1 - Project
> Description]{.underline}](#section-1---project-description)
>
> [[1.1 Project]{.underline}](#project)
>
> [[1.2 Description]{.underline}](#description)
>
> [[1.3 Revision History]{.underline}](#revision-history)
>
> [[Section 2 - Overview]{.underline}](#section-2---overview)
>
> [[2.1 Purpose]{.underline}](#purpose)
>
> [[2.2 Scope]{.underline}](#scope)
>
> [[2.3 Requirements]{.underline}](#requirements)
>
> [[Section 3 - System
> Architecture]{.underline}](#section-3---system-architecture)
>
> [[Section 4 - Data
> Dictionary]{.underline}](#section-4---data-dictionary)
>
> [[Section 5 - Software Domain
> Design]{.underline}](#section-5---software-domain-design)
>
> [[5.1 Software Application Domain
> Chart]{.underline}](#software-application-domain-chart)
>
> [[5.2 Software Application
> Domain]{.underline}](#software-application-domain)
>
> [[5.2.1 Domain X]{.underline}](#domain-x)
>
> [[5.2.1.1 Component Y of Domain
> X]{.underline}](#component-y-of-domain-x)
>
> [[5.2.1.1.1 Task Z of Component Y1 of Domain
> X]{.underline}](#task-z-of-component-y1-of-domain-x)
>
> [[Section 6 -- Data Design]{.underline}](#section-6-data-design)
>
> [[6.1 Persistent/Static Data]{.underline}](#persistentstatic-data)
>
> [[6.1.1 Dataset]{.underline}](#dataset)
>
> [[6.1.2 Static Data]{.underline}](#static-data)
>
> [[6.1.3 Persisted data]{.underline}](#persisted-data)
>
> [[6.2 Transient/Dynamic Data]{.underline}](#transientdynamic-data)
>
> [[6.3 External Interface Data]{.underline}](#external-interface-data)
>
> [[6.4 Transformation of Data]{.underline}](#transformation-of-data)
>
> [[Section 7 - User Interface
> Design]{.underline}](#section-7---user-interface-design)
>
> [[7.1 User Interface Design
> Overview]{.underline}](#user-interface-design-overview)
>
> [[7.2 User Interface Navigation
> Flow]{.underline}](#user-interface-navigation-flow)
>
> [[7.3 Use Cases / User Function
> Description]{.underline}](#use-cases-user-function-description)
>
> [[Section 8 - Extra Design Features / Outstanding
> Issues]{.underline}](#section-8---extra-design-features-outstanding-issues)
>
> [[Section 9 -- References]{.underline}](#section-9-references)

# Section 2 - Overview

## 2.1 Purpose

This project is a Retrieval-Augmented Generation (RAG) system designed
to provide emotionally intelligent support for users struggling with the
Indian Income Tax Portal
([[https://www.incometax.gov.in/iec/foportal/]{.underline}](https://www.incometax.gov.in/iec/foportal/)).
It answers questions like:

"Which ITR form should I use?"

"Why is my refund delayed?"

"How do I file taxes as a freelancer?"

"What is Form 26AS and where do I find it?"

Unlike generic chatbots, this system is capable of detecting user
sentiment (e.g., frustration, confusion) and adjusting its tone to
provide a more empathetic, human-like interaction.

## 2.2 Scope

### 2.2.1 In Scope

#### 2.2.1.1. Core Functionality

Building a retrieval-augmented generation (RAG) system that can:

-   Answer user queries about tax filing, PAN/Aadhaar linking, refunds,
    > ITR forms, deadlines, etc.

-   Retrieve answers from a curated corpus of government documents,
    > FAQs, and tax guides.

-   Generate responses that feel empathetic and emotionally appropriate,
    > not robotic.

#### 2.2.1.2. Backend System

Implementation using:

-   LlamaIndex for ingestion, chunking, and document retrieval.

-   LangChain to chain the retrieval and generation steps.

-   FastAPI as the backend web server to create the webhook.

-   Weaviate for vector database indexing.

-   Mistral 7B via Ollama as the foundational model.

-   DialogFlow CX to handle the NLU and user interaction.

-   Streamlit for hosting the demo.

#### 2.2.1.3. LLM & Sentiment Integration

-   Local or cloud-free deployment of an open-source LLM (e.g., Mistral
    > 7B via Ollama) for answer generation.

-   Sentiment detection using lightweight models (e.g.,
    > twitter-roberta-base-sentiment) to:

    -   Analyze the user's emotional tone (e.g., frustration,
        > confusion).

    -   Adjust the assistant's tone of voice accordingly (e.g., calm,
        > supportive, instructive).

#### 2.2.1.4. Knowledge Base Construction

##### Phase 1 : 

Scraping and preprocessing of:

-   Income Tax Portal

-   High-ranking blog content - restricted the scope to ClearTax for now

Scraping and preprocessing using requests and BeautifulSoup. The outputs
at the end of Phase 1 are Markdown files that preserve the structure of
the original webpage, including the handy screenshots provided for
guidance which can be retrieved for the user based on their search
query.

##### Phase 2 : 

-   Chunking, cleaning, and indexing for semantic search using FAISS or
    > Chroma.

#### 2.2.1.5. Multi-Persona Support

Designing workflows for different user types based on real world
scenarios :

1.  Salaried employees

2.  Freelancers/self-employed

3.  Pensioners

4.  NRIs

5.  First-time filers

6.  Unemployed users

7.  Users with no income

8.  Users with income below taxable limit

#### 2.2.1.6. Lightweight UI or CLI Interface

-   A simple interface for testing the assistant - Streamlit

-   Demonstrates emotionally-aware, context-relevant dialogue without
    > requiring frontend development.

#### 2.2.1.7. Local or Free-Tier Deployment

-   Ability to run locally on CPU via Ollama or deploy on HuggingFace
    > Spaces without incurring costs.

-   No use of paid LLMs (like GPT-4) or proprietary APIs.

### 2.2.2 Out of Scope 

#### 2.2.2.1. Real-time Integration with Income Tax Portal

The assistant will not file taxes, submit forms, or interact with the
income tax website on behalf of the user.

#### 2.2.2.2. Personal Data Handling

Users will not be asked to submit their PAN, Aadhaar, Form 16, or any
personally identifiable information (PII). This is a general help
assistant, not a tax filing tool.

#### 2.2.2.3. Fine-tuning or Training a Custom LLM

The project will use pre-trained models (like Mistral or MiniLM) and not
train a new language model from scratch.

#### 2.2.2.4. Mobile App or Full Web App Frontend

No dedicated mobile or web UI beyond a simple test interface (e.g.,
Streamlit or Telegram).

#### 2.2.2.5. Multiple Language Support

This version is limited to English only. Regional languages can be
considered as a future extension.

## 

## 2.3 Requirements

### 2.3.1 Functional Requirements

-   The system must accept natural language questions related to income
    > tax filing in India.

-   The system must retrieve relevant information from a local vector
    > index built from official documents and guides.

-   The system must use a lightweight LLM to generate a helpful answer
    > from retrieved context.

-   The system must detect user sentiment (e.g., frustration, confusion)
    > from input text.

-   The system must modify the tone and style of its response based on
    > the detected sentiment.

-   The system must support common user personas: salaried employee,
    > freelancer, pensioner, NRI.

-   The backend must be exposed via an API (e.g., using FastAPI) for
    > testing and UI integration.

-   The assistant must run fully on local CPU or free cloud (e.g.,
    > HuggingFace Spaces).

### 2.3.2 Non-Functional Requirements

-   The system should respond to user queries within 10 seconds on CPU.

-   The system should support up to 50 concurrent users without crashing
    > (with acceptable latency).

-   All personal data must remain local and never be stored or logged.

-   The system must use only open-source or free-tier tools and models.

-   The system should be easily portable and run on minimal local
    > hardware (e.g., 8-core CPU, 16GB RAM).

# Section 3 - System Architecture

Describe/include a figure of the overall system architecture (and where
this module fits in)

# Section 4 - Data Dictionary

Brief description of each element in this module or a link to an actual
data dictionary

(template of a database table description)

  -----------------------------------------------------------------------
  **Table**
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  ------------------------------------------------------------------------
  **Field**    **Notes**                                   **Type**
  ------------ ------------------------------------------- ---------------
  DOCNAME      Name of the url from which the doc has been VARCHAR
               scraped                                     

  ID           Unique identifier of each chunk             UUID

  CHUNK        Text chunk, including image urls            VARCHAR

  IMAGE_SRC    Url from the chunk                          VARCHAR
  ------------------------------------------------------------------------

# Section 5 - Software Domain Design

## 5.1 Software Application Domain Chart

Describe / chart each major software application domain and the
relationships between objects (UML, etc)

## 5.2 Software Application Domain

A Comprehensive high level description of each domain (package/object
wherever it is better to start) within the scope of this module (or
within the greater scope of the project if applicable)

### 5.2.1 Domain X

> A high level description of the family of components within this
> domain and their relationship. Include database domain, stored
> procedures, triggers, packages, objects, functions, etc.

#### 5.2.1.1 Component Y of Domain X

> Define Component Y, describe data flow/control at component level

##### 5.2.1.1.1 Task Z of Component Y1 of Domain X

> Define Task Z, describe data flow/control at task level

# Section 6 -- Data Design

Describe the data contained in databases and other shared structures
between domains or within the scope of the overall project architecture

## 6.1 Persistent/Static Data

Describe/illustrate the logical data model or entity relationship
diagrams for the persistent data (or static data if static)

### 6.1.1 Dataset

> Describe persisted object/dataset and its relationships to other
> entities/datasets

### 6.1.2 Static Data

> Describe static data

### 6.1.3 Persisted data

> Describe persisted data

## 6.2 Transient/Dynamic Data

Describe any transient data, include any necessary subsections

## 6.3 External Interface Data

Any external interfaces' data goes here (this is for the data, section 8
is for the interface itself)

## 6.4 Transformation of Data

Describe any data transformation that goes on between design elements

# Section 7 - User Interface Design

## 7.1 User Interface Design Overview

Pictures, high level requirements, mockups, etc.

## 7.2 User Interface Navigation Flow

Diagram the flow from one screen to the next

## 7.3 Use Cases / User Function Description

Describe screen usage / function using use cases, or on a per function
basis

# Section 8 - Extra Design Features / Outstanding Issues

Does not fit anywhere else above, but should be mentioned \-- goes here

# Section 9 -- References 

Any documents which would be useful to understand this design document
or which were used in drawing up this design.
