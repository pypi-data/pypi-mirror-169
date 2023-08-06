# Panther
<hr/>

## Requirements
<div class="termy">

```console
Python 3.10+
```
</div>

<hr/>

## Installation

- ### Create Virtual Environment

  * <a href="https://">Linux </a>
  * <a href="https://">Windows </a>
  * <a href="https://">Mac </a>

- ### Install Panther 
    <div class="termy">

    ```console
    $ pip install panter
    ```
    </div>
<hr/>

## Usage
- #### Create Project
    <div class="termy">
    
    ```console
    $ panther create <project_name>
    ```
    </div>
- #### Run Project
    <div class="termy">
    
    ```console
    $ panther run 
    ```
    </div>

## TODO:

#### Base 
- [x] Start with Uvicorn 
- [x] Fix URL Routing 
- [x] Read Configs 
- [x] Handle Exceptions 
- [x] Add Custom Logger 
- [x] Request Class 
- [x] Response Class 
- [x] Validate Input 
- [x] Custom Output Model 
- [x] Log Queries
- [x] Add Package Requirements
- [x] Custom Logging
- [ ] Handle Form-Data
- [ ] Handle Cookie
- [ ] Handle File 
- [ ] Handle WS 
- [ ] Handle GraphQL
- [ ] Add py.typed 
- [ ] Refactor app __call__ 

#### Database:
- [x] Structure Of DB Connection
- [x] TinyDB Connection
- [x] MongoDB Connection
- [x] Create Custom BaseModel For All Type Of Databases
- [ ] Set TinyDB As Default

#### Simple Queries
- [x] Get One 
- [x] List  
- [x] Create 
- [x] Delete 
- [x] Update
- [ ] Get or Raise
- [ ] Get or Create
- [ ] List with Pagination
- [ ] Other Queries

#### Middleware
- [x] Add Middlewares To Structure
- [x] Create BaseMiddleware
- [x] Pass Custom Parameters To Middlewares
- [ ] Import Custom Middlewares Of User

#### Authentication 
- [ ] Choose Type of Authentication 
- [ ] JWT 
- [ ] Token Storage 
- [ ] Cookie 
- [ ] Query Param
- [ ] Store JWT After Logout In Redis

#### Cache
- [x] Add Redis To Structure

#### Throttling
- [ ] Monitor Requests 
- [ ] Ban User 
- [ ] User Redis For Block His JWT

#### Migration 
- [x] Add Alembic To Structure
- [ ] Set Custom Name For Migrations 
- [ ] Merge Migrations 

#### TUI (for Linux)
- [ ] Create Project with Options
- [ ] Monitor Requests  
- [ ] Monitor Query Performance (Time)
- [x] Monitor Response Time
- [ ] Monitor Fastest & Slowest API
    
#### CLI (for Windows)
- [x] Create Project 
- [x] Run Project 

#### Documentation 
- [ ] Read The Doc or MkDoc 
- [ ] Framework Performance Ranking 

#### Tests 
- [ ] Add Test To Package