### Laws, sections and articles

TABLE laws:
    '''
        Table to host all laws of a specific country. In this table only the main data will appear
        
        1, 'Costituzione', 1948, 0
        2, 'Codice Civile', 19??, 0
        3, 'Codice Penale', 19??, 0
    '''
    id                  > INT # Autoincremental ID of the law
    name                > TEXT required=True # Name of the law
    became              > DATE # Date when became a law

TABLE sections:
    '''
        Table to host all laws sections.

        1, 1, 0, 'Principi fondamentali', 1
        2, 1, 0, 'Parte prima', 1
        3, 1, 2, 'Titolo I', 1
        4, 1, 2, 'Titolo II', 2
    '''
    id                  > INT # Autoincremental ID of the section
    law_id              > FK(laws) # Foreign Key pointing to the law which the section is part of
    parent_id           > FK(sections) default=0 # Section that contain this section (if none, 0 will appear)
    name                > VARCHAR(50) required=True # Name of the section
    description         > VARCHAR(50) # Formal description of the section
    order               > INT # Order to be able to sort in a selection

TABLE articles:
    '''
        Table to host all laws articles.

        1, 1, "L'Italia è una Repubblica...", 1, 1
    '''
    id                  > INT # Autoincremental ID of the article
    number              > INT required=True # number of the article in the code
    text                > TEXT required=True # full original text of the article
    law_id              > FK(laws) # Foreign Key pointing to the law which the article is part of
    section_id          > FK(sections) # Foreign Key pointing to the section which the article is part of

### Resources

TABLE resources:
    '''
        Table to host all resources on articles.

        1, 1, 'Some text', 'http://example.com/page', 1, 1
    '''
    id                  > INT # Autoincremental ID of the resource
    category_id         > FK(resource_categories) # Foreign Key pointing to the right resource_category
    text                > TEXT required=True # Text of the contribution, in case of a web-resource an extract or a short introduction
    uri                 > VARCHAR(255) # URI if web-resourse, else None
    source_id           > FK(sources) # Foreign Key pointing to the source
    
TABLE resource_categories:
    '''
        Table to host all categories which identify the kind of resource
    
        1, 'Esegesi'
        2, 'Storia'
        3, 'Link'
        4, 'Dottrina'
        5, 'Giurisprudenza'
        6, 'Normativa'
        7, 'Attualita'
        8, 'Dati'
    '''
    id                  > INT # Autoincremental ID of the resource category
    name                > VARCHAR(100) required=True # Name of the resource category

TABLE resource_fields:
    '''
        Table to host optional free-caption fields.

        1, 1, 'Reviewed by', 'Name Surname' 
    '''
    id                  > INT # Autoincremental ID of the resource_field
    resource_id         > FK(resources) # Foreign Key pointing to his resource 
    key                 > VARCHAR(50) # Name of the field
    value               > TEXT # Value of the field

### Sources

TABLE sources:          # Fonti delle Rirorse 
    id                  > INT 
    type_id             > FK(source_types)
    name                > VARCHAR(50) required=True # Reference array ['Giudice', 'Avvocato', 'Accademico', 'Governo', 'Parlamento'
                                      #'Organo Giurisdizionale', 'TAR', 'Corte Costituzionale', 'Presidente della Repubblica',
                                      #'Commentatore', 'Costituizionalista', 'Giornalista', 'Redattore OPEN-IUS']
                                      
TABLE source_type:      # Reference array: ['Legge dello Stato', 'Opinione', 'Dichiarazione',
                        #                     'Sentenza', 'Regolamento']
    id                  > INT
    name                > VARCHAR(50) required=True
    
TABLE source_fields:    # ?
    id                  > INT
    source_id           > FK(sources)
    key                 > VARCHAR(50)
    value               > TEXT

### Authors

TABLE authors:          # Author can be a person or an institution (oppure facciamo scrivere il firmatario?
                        # Nel caso di Source=Governo Author=il/i Ministro/i per esempio)
    id                  > INT
    title_id            > FK(titles)
    name                > VARCHAR(50) required=True
    surname             > VARCHAR(50)
    
TABLE author_titles:
    id                  > INT
    name                > VARCHAR(50) required=True #['Governo', 'Parlamento', 'Prof.', 'Dott.', 'Avv.', 'Sig.', 'Sig.ra']

TABLE author_fields:
    id                  > INT
    author_id           > FK(authors)
    key                 > VARCHAR(50)
    value               > TEXT

TABLE author_resource:
    author_id           > FK(authors)
    resource_id         > FK(resources)

### Topics

TABLE topics:
    id                   > INT
    name                 > VARCHAR(50) required=True

TABLE topic_fields:
    id                  > INT
    topic_id            > FK(topics)
    key                 > VARCHAR(50)
    value               > TEXT

TABLE author_topic:
    author_id           > FK(authors)
    topic_id            > FK(topics)

TABLE resource_topic:
    resource_id         > FK(resources)
    topic_id            > FK(topics)

TABLE article_topic:
    article_id          > FK(articles)
    topic_id            > FK(topics)

TABLE law_topic:
    law_id              > FK(laws)
    topic_id            > FK(topics)

#Serve una tabella users per autenticazione?
    
'''
TABLE Dati:
  #Possibile implementazione futura
    id                   > INT(12)
    formato              > VARCHAR(20) choices?=['pdf', 'json', 'csv', 'xcl'] 
    contenuto            > BLOB
'''
